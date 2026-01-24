from __future__ import annotations

from decimal import Decimal

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from orders.models import Order


def _money(amount: int | None) -> Decimal:
    if amount is None:
        return Decimal("0.00")
    return (Decimal(amount) / Decimal("100")).quantize(Decimal("0.01"))


@csrf_exempt
def stripe_webhook(request):
    if not settings.STRIPE_WEBHOOK_SECRET:
        return HttpResponse("Missing STRIPE_WEBHOOK_SECRET", status=500)

    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE", "")

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError:
        return HttpResponse("Invalid payload", status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse("Invalid signature", status=400)

    event_type = event["type"]
    data = event["data"]["object"]

    if event_type == "checkout.session.completed":
        metadata = data.get("metadata") or {}
        order_id = metadata.get("order_id")

        if order_id:
            order = Order.objects.filter(id=order_id).first()
            if order and order.status != Order.Status.PAID:
                order.status = Order.Status.PAID

                order.stripe_checkout_session_id = data.get("id", "") or order.stripe_checkout_session_id
                order.stripe_payment_intent_id = data.get("payment_intent", "") or ""

                order.currency = (data.get("currency") or "gbp").upper()
                order.subtotal = _money(data.get("amount_subtotal"))
                order.total = _money(data.get("amount_total"))

                total_details = data.get("total_details") or {}
                order.shipping_cost = _money(total_details.get("amount_shipping"))

                shipping = data.get("shipping_details") or {}
                address = shipping.get("address") or {}

                order.shipping_name = shipping.get("name", "") or ""
                order.shipping_phone = shipping.get("phone", "") or ""

                order.shipping_line1 = address.get("line1", "") or ""
                order.shipping_line2 = address.get("line2", "") or ""
                order.shipping_city = address.get("city", "") or ""
                order.shipping_postcode = address.get("postal_code", "") or ""
                order.shipping_country = address.get("country", "") or ""

                customer_details = data.get("customer_details") or {}
                if not order.email and customer_details.get("email"):
                    order.email = customer_details["email"]

                order.save()

    return HttpResponse("OK", status=200)
