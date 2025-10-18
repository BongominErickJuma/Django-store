from store.signals import order_created
from django.dispatch import receiver


@receiver(order_created)
def OnOrderCreated(sender, **kwargs):
    order = kwargs.get("order")
    print(f"Order created with ID: {order.id} for Customer ID: {order.customer.id}")
