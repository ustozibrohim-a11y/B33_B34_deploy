import src.core.models as models


def generate_order_text(billing, order, items) -> str:
    text = (f"<b>Yangi Buyurtma</b> #{order.pk}\n\n"

            f"<b>Buyurtmachi</b>: \n"
            f"<b>FIO</b>: {billing.f_name}\n"
            f"<b>Phone</b>: {billing.phone}\n"
            f"<b>ExPhone</b>: {billing.ex_phone}\n"
            f"<b>Address</b>: {billing.address}\n\n"

            f"<b>Buyurtma</b>\n"
            f"<b>Umumiy Narx</b>: {order.total_price}\n\n"

            f"<b>Maxsulotlar</b>")
    for i in items:
        text += f"\n{i.product.name} {i.quantity}x{i.price}$ {i.total_sum}"

    text += f"\n<a href='http://127.0.0.1:8000/admin/core/order/{order.pk}/change/'>Admin Panelda Korish </a>"
    return text
