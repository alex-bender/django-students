from main import settings


def my_cont_processor(request):
    return { 'settings' : settings, }