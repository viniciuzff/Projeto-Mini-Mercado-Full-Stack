from Infrastructure.Model.product import Product
from config.data_base import db


class ProductService:

    @staticmethod
    def create_product(seller_id, data):
        name = data.get("name")
        price = data.get("price")
        quantity = data.get("quantity")
        image_url = data.get("image_url", None)

        if not name or price is None or quantity is None:
            raise Exception("Campos obrigatórios: name, price, quantity")

        product = Product(
            seller_id=seller_id,
            name=name,
            price=price,
            quantity=quantity,
            image_url=image_url,
            status=True
        )

        db.session.add(product)
        db.session.commit()

        return product

    @staticmethod
    def list_products(seller_id):
        return Product.query.filter_by(seller_id=seller_id).all()

    @staticmethod
    def get_product(seller_id, product_id):
        product = Product.query.filter_by(id=product_id, seller_id=seller_id).first()

        if not product:
            raise Exception("Produto não encontrado")

        return product

    @staticmethod
    def update_product(seller_id, product_id, data):
        product = Product.query.filter_by(id=product_id, seller_id=seller_id).first()

        if not product:
            raise Exception("Produto não encontrado")

        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)
        product.quantity = data.get("quantity", product.quantity)
        product.image_url = data.get("image_url", product.image_url)

        db.session.commit()

        return product

    @staticmethod
    def inactivate_product(seller_id, product_id):
        product = Product.query.filter_by(id=product_id, seller_id=seller_id).first()

        if not product:
            raise Exception("Produto não encontrado")

        product.status = False
        db.session.commit()

        return product