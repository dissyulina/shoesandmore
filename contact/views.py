from django.shortcuts import render


def contact(request):
    """ Contact Us Page """
    
    return render(request, 'contact/contact.html')
