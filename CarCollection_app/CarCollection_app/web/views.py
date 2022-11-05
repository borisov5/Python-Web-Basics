from django.shortcuts import render, redirect

from CarCollection_app.web.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm,\
    CreateCarForm, EditCarForm, DeleteCarForm


from CarCollection_app.web.models import Profile, Car


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    cars = Car.objects.all()

    context = {
        'profile': profile,
        'cars': cars,
    }
    return render(request, 'index.html', context)


def show_catalogue(request):
    cars = Car.objects.all()

    len_cars = len(cars)

    context = {
        'cars': cars,
        'len_cars': len_cars,
    }
    return render(request, 'catalogue.html', context)


def show_profile(request):
    profile = get_profile()

    cars = Car.objects.all()
    budget = sum(c.price for c in cars)

    context = {
        'profile': profile,
        'budget': budget,
    }
    return render(request, 'profile-details.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'profile-create.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)


def create_car(request):
    if request.method == 'POST':
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateCarForm()

    context = {
        'form': form,
    }

    return render(request, 'car-create.html', context)


def edit_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'form': form,
        'car': car,
    }
    return render(request, 'car-delete.html', context)


def car_details(request, pk):
    car = Car.objects.get(pk=pk)

    context = {
        'car': car,
    }
    return render(request, 'car-details.html', context)


