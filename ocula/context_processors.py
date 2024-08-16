from django.conf import settings


def general_environment(request):
    """Pass variables from settings to templates"""
    return {
        "debug": settings.DEBUG,
        "environment": settings.ENVIRONMENT,
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "app_host_url": settings.APP_HOST_URL,
        "build_time": settings.BUILD_TIME,
    }
