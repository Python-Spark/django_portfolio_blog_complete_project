from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse

from .models import Contact

class ContactUs(SuccessMessageMixin, CreateView):
    template_name = 'contactus/contact.html'
    model = Contact
    fields = ['name', 'email', 'suggestion']
    success_message = "your message from %(email)s sent successfully!"

    def get_success_url(self):
        return reverse('contact-us')
