import random
from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db
from src.Infrastructure.http.whats_app import WhatsApp


class UserService:

    @staticmethod
    def create_user(name, cnpj, email, phone, password):

        code = str(random.randint(1000,9999))

        user = User(
            name=name,
            cnpj=cnpj,
            email=email,
            phone=phone,
            password=password,
            status=False,
            verification_code=code
        )

        db.session.add(user)
        db.session.commit()

        WhatsApp.whats_app(code)

        return UserDomain(user.id, user.name, user.email, user.password)