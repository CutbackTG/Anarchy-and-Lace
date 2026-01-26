from django.contrib import messages
from django.shortcuts import redirect, render

from reviews.models import Review


def index(request):
    """Landing page."""
    featured_reviews = (
        Review.objects.filter(featured=True)
        .select_related("product", "user")
        .order_by("-created_at")[:3]
    )
    return render(request, "home/index.html", {
        "featured_reviews": featured_reviews,
        "active_menu_item": "home",
    })


def contact(request):
    """
    Simple contact form.
    For now: shows a success message. Later you can wire email/CRM.
    """
    if request.method == "POST":
        name = (request.POST.get("name") or "").strip()
        email = (request.POST.get("email") or "").strip()
        message = (request.POST.get("message") or "").strip()

        if not name or not email or not message:
            messages.error(request, "Please fill in your name, email, and message.")
            return render(request, "home/contact.html", {"active_menu_item": "contact"})

        messages.success(request, "Message sent. We’ll get back to you soon ✨")
        return redirect("home:contact")

    return render(request, "home/contact.html", {"active_menu_item": "contact"})


def kimono_history(request):
    """Magazine-style history page for kimono textiles."""
    return render(request, "home/kimono_history.html", {"active_menu_item": "kimono_history"})
