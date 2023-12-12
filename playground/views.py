from django.http import BadHeaderError
from django.shortcuts import render
from django.core.mail import mail_admins, send_mail , EmailMessage
from templated_mail.mail import BaseEmailMessage


def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name = 'emails/first.html',
            context = {'name': 'Mahdi'}
        )
        message.send(['alihdada@test.com'])
        
        # mail_admins('subject', 'message', html_message='message')
    except BadHeaderError:
        raise BadHeaderError('This is bad method!')
    return render(request, 'hello.html', {'name': 'Mahdi'})

# def debug(request):
#     # None : if we use first()
#     # Boolean : if we use exists()
#     query_set = Product.objects.filter(price__range=(200, 300))
#     # Limit : 0, 1, 2, 3, 4
#     product = Product.objects.all()[:5]
#     # Limit : 5, 6, 7, 8, 9
#     product = Product.objects.all()[5:10]

#     # query for get all products that are ordered and order by title.
#     query_set = Product.objects.filter(
#         id__in = OrderItem.objects.values_list('product_id').distinct()).order_by('title')
    
#     # selected_related uses for one to one and foreignkeys.
#     # prefetch_related uses for many to many and reverse foreignkeys.
#     # Get the last 5 orders with their customer and itmes (inc product)
#     query_set = Order.objects.select_related('customer').order_by('-placed_at')[:5]

#     return render(request, 'sqll.html', {'products': list(query_set)})