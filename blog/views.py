from django.shortcuts import render

# Create your views here.


def get_base(request):
    """Renders base page."""
    return render(request, 'blog/base.html')
