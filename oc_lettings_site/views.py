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
    logger.info("Rendering index.html")
    return render(request, "index.html")


def error_404_view(request, exception):
    message = f"404 error: Page not found | Path: {request.path}"
    logger.error(message)
    sentry_sdk.capture_message(message, level="error")
    return render(request, "404.html", status=404)


def error_500_view(request):
    logger.error("500 error: Internal server error | Path: %s", request.path)
    return render(request, "500.html", status=500)
