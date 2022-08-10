from config import app
from utils import init_db
from blueprints.user_bp.views import user_blueprint
from blueprints.order_bp.views import order_blueprint
from blueprints.offer_bp.views import offer_blueprint

app.register_blueprint(user_blueprint)
app.register_blueprint(order_blueprint)
app.register_blueprint(offer_blueprint)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
