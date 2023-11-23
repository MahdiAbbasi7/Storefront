from django.db import models
from django.core.validators import MinValueValidator

class Promotions(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class  Collection(models.Model):
    title = models.CharField(max_length=255)
    features_product = models.ForeignKey(
        'Product',on_delete=models.SET_NULL, null= True, related_name='+')
    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']
        # you can handle this in admin file.

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    #9999.99
    price = models.DecimalField(
        max_digits=6, 
        decimal_places=2, 
        validators= [MinValueValidator(1, message='Price is not in range.')])
    
    inventory_type = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    # for one to mant relationships we use ForeignKey.
    collections = models.ForeignKey(Collection, on_delete=models.PROTECT,related_name='products')
    promothions = models.ManyToManyField(Promotions, blank=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['title']


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    class Meta:
        ordering = ['first_name', 'last_name']


class Order(models.Model):
    PENDING = 'P'
    COMPLETE = 'C'
    FAILED = 'F'

    PAYMENT_CHOICES = [
        (PENDING, 'P'),
        (COMPLETE, 'C'),
        (FAILED, 'F'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_CHOICES, default=PENDING)
    customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

class OrderItem(models.Model):
    # for reverse relationship this name is conventions orderitem_set.(related_name)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    zip = models.PositiveIntegerField(null=True, blank=True)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    data = models.DateField(auto_now_add=True)

