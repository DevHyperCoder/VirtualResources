from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required(login_url='/signin')
def profile(request):
    user_id = request.GET.get('id')
    user = None
    try:
        user = UserProfile.objects.get(id=user_id)
    except UserProfile.DoesNotExist:
        print(f"Could not find user with id = {user_id}")

    return render(request, "profile.html", {'user': user})
