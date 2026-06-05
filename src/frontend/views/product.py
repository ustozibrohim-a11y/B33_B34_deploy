from django.shortcuts import render, redirect, get_object_or_404

import src.core.models as models


def home(request):
    object_list = models.Product.objects.all().order_by("-id")
    context = {
        "object_list": object_list,
    }
    return render(request, "home.html", context)


def product_filter_by_category(request, category_id):
    object_list = models.Product.objects.filter(category_id=category_id)
    context = {
        "object_list": object_list
    }
    return render(request, "home.html", context)


def product_searched_list(request):
    search = request.GET.get('search')
    object_list = models.Product.objects.all().order_by("-id")
    if search:
        object_list = object_list.filter(name__icontains=search)
    context = {
        "object_list": object_list
    }
    return render(request, "home.html", context)


from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def write_comments(request, product_id):
    user = request.user
    comment = request.POST.get("comment")
    product = get_object_or_404(models.Product, pk=product_id)
    models.Comment.objects.create(user=user, product=product, comment=comment)
    return redirect("home")
