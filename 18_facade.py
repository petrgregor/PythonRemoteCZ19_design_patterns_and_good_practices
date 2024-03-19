class ProductAvailabilityService:
    def is_available(self, product_id):
        if product_id == 2:
            return True
        return False


class PaymentService:
    def pay(self, product_id, amount):
        print(f"Product {product_id} amount {amount} is paid")


class DeliveryService:
    def deliver_product(self, product_id, amount, recipient):
        print(f"Delivering product {product_id} amount {amount} to {recipient}")


class OrderFacade:
    def __init__(self, product_availability_service, payment_service, delivery_service):
        self._product_availability_service = product_availability_service
        self._payment_service = payment_service
        self._delivery_service = delivery_service

    def place_order(self, product_id, amount, recipient):
        if self._product_availability_service.is_available(product_id):
            self._payment_service.pay(product_id, amount)
            self._delivery_service.deliver_product(product_id, amount, recipient)
        else:
            print(f"Product {product_id} is not available.")


def main():
    product_availability_service = ProductAvailabilityService()
    payment_service = PaymentService()
    delivery_service = DeliveryService()

    order_facade = OrderFacade(product_availability_service, payment_service, delivery_service)

    order_facade.place_order(2, 5, "Office")
    order_facade.place_order(3, 4, "Home")


if __name__ == '__main__':
    main()
