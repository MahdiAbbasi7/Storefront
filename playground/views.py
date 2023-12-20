from django.core.cache import cache
from django.http import BadHeaderError
from django.shortcuts import render
from django.core.mail import mail_admins, send_mail , EmailMessage
from templated_mail.mail import BaseEmailMessage
from playground.tasks import notify_customers
import requests


def say_hello(request):
    # notify_customers.delay('hellooo')
    key = 'httpbin_result'
    if cache.get(key) is None:
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        cache.set(key, data)
    # try:
    #     message = BaseEmailMessage(https://meet.google.com/yom-fkbp-cji
    #         template_name = 'emails/first.html',
    #         context = {'name': 'Mahdi'}
    #     )
    #     message.send(['alihdada@test.com'])
        
    #     # mail_admins('subject', 'message', html_message='message')
    # except BadHeaderError:
    #     raise BadHeaderError('This is bad method!')
    return render(request, 'hello.html', {'name': cache.get(key)})