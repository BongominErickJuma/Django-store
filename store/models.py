from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount_applied = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    # Circular relationship
    featured_product = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True, related_name='+')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ["title"]
    

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="_")
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    Promotions = models.ManyToManyField(Promotion)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["title"]


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(null=True)
    membership = models.TextField(max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        ordering = ["first_name", "last_name"]
    


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()


class Order(models.Model):
    
    PAYMENT_PENDING = 'P'
    PAYMENT_COMPLETE = 'C'
    PAYMENT_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_COMPLETE, 'Complete'),
        (PAYMENT_PENDING, 'Pending'),
        (PAYMENT_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.TextField(max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="orderItems")
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)



class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

