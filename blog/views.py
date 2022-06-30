from django.shortcuts import render

# Create your views here.


def home(request):
    """Renders home page."""
    page_title = "Recent Posts"
    return render(request, "blog/index.html", {"page_title": page_title})


def about(request):
    """Renders about page."""
    page_title = "About"
    return render(request, "blog/about.html", {"page_title": page_title})


def contact(request):
    """Renders contact page."""
    page_title = "Contact"
    return render(request, "blog/contact.html", {"page_title": page_title})
