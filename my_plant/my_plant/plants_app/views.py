from django.shortcuts import render, redirect

from my_plant.auth_app.models import Profile
from my_plant.plants_app.forms import PlantForm, DeletePlantForm, EditPlantForm
from my_plant.plants_app.models import Plant


def catalogue_page(request):
    plants = Plant.objects.all()
    context = {
        'profile': Profile.objects.first(),
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)


def create_plant_page(request):
    form = PlantForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('catalogue')

    context = {
        'profile': Profile.objects.first(),
        'form': form,
    }

    return render(request, 'create-plant.html', context)


def plant_details_page(request, pk):
    plant = Plant.objects.get(id=pk)
    context = {
        'profile': Profile.objects.first(),
        'plant': plant,
    }

    return render(request, 'plant-details.html', context)


def edit_plant_page(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = EditPlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'edit-plant.html', context)


def delete_plant_page(request, pk):
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeletePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DeletePlantForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
    }
    return render(request, 'delete-plant.html', context)
