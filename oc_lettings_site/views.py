from django.shortcuts import render
import logging
import sentry_sdk

logger = logging.getLogger(__name__)


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie
# quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla
# eget feugiat sagittis, sem mi convallis eros. Vitae dapibus nisi lorem
# dapibus sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis
# quis. Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae erat ac
# orci placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim
# cursus in. Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    Render the homepage.

    Logs the rendering of the index page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered index.html page.
    """
    logger.info("Rendering index.html")
    return render(request, "index.html")


def error_404_view(request, exception):
    """
    Handle 404 errors (Page Not Found).

    Logs the 404 error and sends the message to Sentry.

    Args:
        request (HttpRequest): The HTTP request object.
        exception (Exception): The exception that triggered the 404.

    Returns:
        HttpResponse: The rendered 404.html page with a 404 status code.
    """
    message = f"404 error: Page not found | Path: {request.path}"
    logger.error(message)
    sentry_sdk.capture_message(message, level="error")
    return render(request, "404.html", status=404)


def error_500_view(request):
    logger.error("500 error handled by custom view | Path: %s", request.path)
    return render(request, "500.html", status=500)
