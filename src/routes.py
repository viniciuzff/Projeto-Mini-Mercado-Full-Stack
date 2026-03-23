from Application.Controllers.user_controller import UserController
from Application.Controllers.auth_controller import AuthController
from flask import jsonify, make_response

def init_routes(app):    

    @app.route('/api', methods=['GET'])
    def health():
        return make_response(jsonify({
            "mensagem": "API - OK; Docker - Up",
        }), 200)
    
    @app.route('/user', methods=['POST'])
    def register_user():
        return UserController.register_user()
    
  
    app.add_url_rule(
        "/user/<int:user_id>",
        view_func=UserController.update_user,
        methods=["PUT"]
    )

  
    @app.route("/login", methods=["POST"])
    def login():
        return AuthController.login()
    
    @app.route("/verify", methods=["POST"])
    def verify():
        return AuthController.verify()