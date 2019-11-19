from django.db import models

from shop.models import Product


class Order(models.Model):
    """
    Сохраняет информацию о покупателе, флаг paid - оплачен заказ или нет,
    метод для получения полной стоимости Товара
    """
    first_name = models.CharField(max_length=64, verbose_name='Имя покупателя')
    last_name = models.CharField(max_length=564, verbose_name='Фамилия покупателя')
    email = models.EmailField()
    address = models.CharField(max_length=256, verbose_name='Адрес покупателя')
    postal_code = models.CharField(max_length=64, verbose_name='Индекс')
    city = models.CharField(max_length=128, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    def __str__(self):
        return 'Заказ {}'.format(self.id)
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    Сохраняет Товар, количество и стоимость каждого эелемента Корзины
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Товар для заказа'
        verbose_name_plural = 'Товары для заказа'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity


