"""
Views for the profiles application.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile
import logging

logger = logging.getLogger(__name__)


# Create your views here.
# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero
# pulvinar eget. Fusc faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum
# lacus d
def index(request):
    """
    Displays the list of all user profiles.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTML response containing all profiles.
    """
    logger.info("Rendering profiles index page")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed tincidunt,
# dolor id facilisis fringilla, eros leo tristique lacus,it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Displays the details of a single user profile.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username used to retrieve the corresponding profile.

    Returns:
        HttpResponse: The HTML response with profile details.
    """
    logger.info("Rendering profile page for user: %s", username)
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
