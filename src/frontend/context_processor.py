import src.core.models as models


def variables(request):
    context = {
        "category_list": models.Category.objects.all()
    }
    return context
