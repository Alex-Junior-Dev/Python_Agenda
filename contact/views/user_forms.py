from django.shortcuts import render # type: ignore

from contact.forms import RegisterForm #type: ignore

def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm()

        if form.is_valid():
            form.save()

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )