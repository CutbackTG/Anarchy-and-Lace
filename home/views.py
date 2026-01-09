from django.contrib import messages
from django.shortcuts import render, redirect


def index(request):
    """Landing page."""
    return render(request, "home/index.html")


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
            return render(request, "home/contact.html")

        messages.success(request, "Message sent. We’ll get back to you soon ✨")
        return redirect("home:contact")

    return render(request, "home/contact.html")
