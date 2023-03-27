# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.shortcuts import redirect, render
#
# from furniture.forms import CreateUserForm
#
#
# def register(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         test_username = request.POST.get('username')
#         test_email = request.POST.get('email')
#         user_objects = User.objects.filter(username=test_username)
#         user_objects1 = User.objects.filter(email=test_email.lower())
#         if len(user_objects) == 0:
#             if len(user_objects1) == 0:
#                 form = CreateUserForm(request.POST)
#                 if form.is_valid():
#                     form.save()
#                     user = form.cleaned_data.get('username')
#                     messages.success(request, 'Account Was Created ' + user + ' ..!')
#                     return redirect('login')
#                 else:
#                     context = {'form': form, 'invalid': 'text-danger', 'tex': "User name was already exist!"}
#                     return render(request, 'signup.html', context)
#             else:
#                 context = {'form': form, 'invalid': 'text-danger', 'tex': "Email name was already exist!"}
#                 return render(request, 'signup.html', context)
#         else:
#             context = {'form': form, 'invalid': 'text-danger', 'tex': "User name was already exist!"}
#             return render(request, 'signup.html', context)
#     else:
#         context = {'form': form}
#         return render(request, 'signup.html', context)
