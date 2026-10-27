from django.shortcuts import render
import re

# Create your views here.
def login_view(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")

        user_pattern = r'^[A-Za-z0-9_]{4,15}$'
        pass_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&*!]).{8,}$'

        if not re.fullmatch(user_pattern, username):
            message = "Invalid username!"

        elif not re.fullmatch(pass_pattern, password):
            message = "Invalid password!"

        else:
            message = "Input validation successful!"

    return render(request, "login.html", {"message": message})