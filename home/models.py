from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField()
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Cost: {self.cost}, Description: {self.description[:50]}, Image: {self.image}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=(('registered', 'Registered'), ('in_queue', 'In Queue'), ('collected', 'Collected')))
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name}"