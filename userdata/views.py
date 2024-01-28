from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserDataModelForm
from .models import UserData


def user_form(request):
    if request.method == 'POST':
        form = UserDataModelForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect('view_data_page', instance_id=instance.pk)
    else:
        form = UserDataModelForm()

    return render(request, 'userdata/index.html', {'form': form})


def view_data_page(request, instance_id):
    instance = get_object_or_404(UserData, pk=instance_id)
    return render(request, 'userdata/view_data_page.html', {'instance': instance})
