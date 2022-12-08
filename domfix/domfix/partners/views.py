from django.shortcuts import render


def show_partners(request):
    return render(request, 'partners/partners-page.html')


def add_partner(request):
    return render(request, 'partners/partner-add-page.html')


def delete_partner(request):
    return render(request, 'partners/partner-delete-page.html')


def edit_partner(request):
    return render(request, 'partners/partner-edit-page.html')
