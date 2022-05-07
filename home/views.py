from django.shortcuts import render

from home.forms import FeedBackForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone


def home_view(request):
    return render(request, "home.html", {})


def about_view(request):
    return render(request, "about.html", {})


def contacts_view(request):
    form = FeedBackForm()
    if request.method == "POST":
        form = FeedBackForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except IntegrityError:
                messages.add_message(
                    request, messages.ERROR, "Ваш прошлый запрос еще не обработан")
                messages.add_message(
                    request, messages.ERROR, "Попробуйте позже")

            return redirect(reverse("contacts_page"))

    context = {
        "feedback_form": form,
        "address": "200 N. Spring Street Los Angeles CA 90012 United States",
        "phone": "+1(800) 000-00-00",
        "email": "support@blog.com"
    }
    return render(request, 'contacts.html', context)
