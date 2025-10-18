from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from uuid import uuid4


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount_applied = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    # Circular relationship
    featured_product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, related_name="+"
    )

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
    MEMBERSHIP_BRONZE = "B"
    MEMBERSHIP_SILVER = "S"
    MEMBERSHIP_GOLD = "G"

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, "Bronze"),
        (MEMBERSHIP_SILVER, "Silver"),
        (MEMBERSHIP_GOLD, "Gold"),
    ]

    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(null=True)
    membership = models.TextField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ["user__first_name", "user__last_name"]
        permissions = [("view_history", "can view history")]


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        unique_together = [["cart", "product"]]


class Order(models.Model):

    PAYMENT_PENDING = "P"
    PAYMENT_COMPLETE = "C"
    PAYMENT_FAILED = "F"

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_COMPLETE, "Complete"),
        (PAYMENT_PENDING, "Pending"),
        (PAYMENT_FAILED, "Failed"),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.TextField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_PENDING
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    class Meta:
        permissions = [("cancel_order", "Can cancel Order")]


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="orderItems"
    )
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
