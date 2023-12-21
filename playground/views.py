from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import BadHeaderError
from django.shortcuts import render
from django.core.mail import mail_admins, send_mail , EmailMessage
from django.utils.decorators import method_decorator
from rest_framework.views import APIView
from templated_mail.mail import BaseEmailMessage
from playground.tasks import notify_customers
import requests
import logging

logger = logging.getLogger(__name__)


class HelloView(APIView):
    # @method_decorator(cache_page(5 * 60))
    def get(self, request):
    # notify_customers.delay('hellooo')
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Recived the response')
            data = response.json()
        except:
            logger.critical('httpbin is offline')
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