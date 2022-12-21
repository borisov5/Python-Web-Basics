from django.shortcuts import render, redirect

from my_plant.auth_app.forms import EditProfileForm, ProfileForm
from my_plant.auth_app.models import Profile
from my_plant.plants_app.models import Plant


def create_profile_page(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {
        'form': form
    }

    return render(request, 'create-profile.html', context)


def profile_details_page(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }

    return render(request, 'profile-details.html', context)



def edit_profile_page(request):
    profile = Profile.objects.first()

    if request.method == 'GET':
        context = {
            'form': EditProfileForm(initial=profile.__dict__)
        }
        return render(request, 'edit-profile.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')
        else:
            context = {
                'profile': Profile.objects.first(),
                'form': form,
            }
            return render(request, 'edit-profile.html', context)


def delete_profile_page(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == 'POST':
        profile.delete()
        plants.delete()

        return redirect('home')

    context = {
        'profile': Profile.objects.first(),
    }

    return render(request, 'delete-profile.html', context)
