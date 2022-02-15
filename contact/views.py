from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Defining a new custome message level
SUCCESS_NO_BAG = 50


def contact(request):
    """ Contact Us Page """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
             messages.add_message(request, SUCCESS_NO_BAG, 'Contact Form submitted. Thank you!')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, 'contact/contact.html', context)


def faq(request):
    """ FAQ Page """
    return render(request, 'contact/faq.html')

