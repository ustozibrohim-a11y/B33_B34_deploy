import telebot
from django.conf import settings

import src.core.models as models
import src.frontend.utils as util

token = settings.TOKEN
group_id = settings.GROUP_ID
bot = telebot.TeleBot(token)


class OrderAddService:

    @classmethod
    def add_order(cls, user, cart, items, billing):
        order = models.Order.objects.create(owner=user, billing=billing, total_price=cart.total_price)
        order_items = []
        for i in items:
            order_items.append(
                models.OrderItem(order=order,
                                 product=i.product,
                                 price=i.price, quantity=i.quantity, total_sum=i.total_sum)
            )
        models.OrderItem.objects.bulk_create(order_items)
        cart.is_active = False
        cart.save()
        text = util.generate_order_text(billing, order, items)
        bot.send_message(group_id, text=text, parse_mode="HTML")
