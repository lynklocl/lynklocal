from django.shortcuts import render, get_object_or_404
from .models import LynkLocal, Contact_Form_Submission
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def home(request):
    lynk_local = get_object_or_404(LynkLocal, pk=1)
    return render(request, 'index.html', {'lynk_local': lynk_local})


def contact_form_submission(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        form_purpose = request.POST.get('form_purpose')
        user_type = request.POST.get('user_type')
        free_quote = request.POST.get('free_quote')

        contact_form = Contact_Form_Submission(
            name = name,
            email = email,
            phone_number = phone_number,
            message = message,
            user_type = user_type,
            form_purpose = form_purpose,
            free_quote = free_quote,
        )
       
        contact_form.save()
        
        lynk_local = get_object_or_404(LynkLocal, pk=1)

        email_subject = 'Contact Form Submission'
        email_body = render_to_string('email_template.html', {
            'name': name,
            'email': email,
            'phone_number': phone_number,
            'message': message,
            'lynk_local_phone_number' : lynk_local.phone_number,
            'form_purpose': form_purpose,
            'user_type': user_type,
            'free_quote': free_quote,
        })

        # Send the email
        msg = EmailMessage(email_subject, email_body, to=[email, 'lynkslocal@gmail.com'])
        msg.content_subtype = 'html'
        msg.send()

        return render(request, 'index.html', {'lynk_local': lynk_local})





