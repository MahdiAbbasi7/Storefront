from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import BadHeaderError
from django.shortcuts import render
from django.core.mail import mail_admins, send_mail , EmailMessage
from templated_mail.mail import BaseEmailMessage
from playground.tasks import notify_customers
import requests

@cache_page(5 * 60)
def say_hello(request):
    # notify_customers.delay('hellooo')
    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
    return render(request, 'hello.html', {'name': data})
    # try:
    #     message = BaseEmailMessage(https://meet.google.com/yom-fkbp-cji
    #         template_name = 'emails/first.html',
    #         context = {'name': 'Mahdi'}
    #     )
    #     message.send(['alihdada@test.com'])
        
    #     # mail_admins('subject', 'message', html_message='message')
    # except BadHeaderError:
    #     raise BadHeaderError('This is bad method!')