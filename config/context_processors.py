from menu.models import MenuItem


def menu(request):
    return {"menu": MenuItem.objects.all()}
