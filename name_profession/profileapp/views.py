from django.shortcuts import render


def show_profile(request):
    context = {
        'name': 'Mrunal Gaikwad',
        'profession': 'Web Developer'
    }
    return render(request, 'profileapp/profile.html', context)
