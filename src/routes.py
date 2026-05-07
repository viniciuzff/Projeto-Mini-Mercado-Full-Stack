from Application.Controllers.user_controller import UserController
from Application.Controllers.auth_controller import AuthController
from Application.Controllers.product_controller import ProductController
from flask import jsonify, make_response
from middlewares.auth_middleware import token_required


def init_routes(app):

    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({"mensagem": "API - OK"}), 200)

    # --- Sellers ---
    @app.route('/api/sellers', methods=['POST'])
    def register_user():
        return UserController.register_user()

    @app.route('/api/sellers/activate', methods=['POST'])
    def verify():
        return AuthController.verify()

    # --- Auth ---
    @app.route('/api/auth/login', methods=['POST'])
    def login():
        return AuthController.login()

    # --- Me ---
    @app.route('/me', methods=['GET'])
    @token_required
    def get_me(current_user):
        return UserController.get_me(current_user)

    # --- Produtos ---
    @app.route('/api/products', methods=['POST'])
    @token_required
    def create_product(current_user):
        return ProductController.create_product(current_user)

    @app.route('/api/products', methods=['GET'])
    @token_required
    def list_products(current_user):
        return ProductController.list_products(current_user)

    @app.route('/api/products/<int:product_id>', methods=['GET'])
    @token_required
    def get_product(current_user, product_id):
        return ProductController.get_product(current_user, product_id)

    @app.route('/api/products/<int:product_id>', methods=['PUT'])
    @token_required
    def update_product(current_user, product_id):
        return ProductController.update_product(current_user, product_id)

    @app.route('/api/products/<int:product_id>/inactivate', methods=['PATCH'])
    @token_required
    def inactivate_product(current_user, product_id):
        return ProductController.inactivate_product(current_user, product_id)