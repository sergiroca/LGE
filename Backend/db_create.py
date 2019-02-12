from application import db
from application.models import Provider, Product, Customer, Stock, Order, User, ProdLote, Lote, StockLote, Price, FlaskForm, Category, SubCategory, Format, Origin, ProductComments, Offer, OfferClients, OfferProducts, CustomerGroup, Offerchild, OrderProducts, Order

db.create_all()

admin = User(username='Admin', email='admin@admin.com', password='sha256$RiJPq3hT$74f39e5334d7650bfb30e8294aac9b4275d304507e0e140abc2bec7c6ecebf50', user_role="ADMIN", is_active = True)
db.session.add(admin)
db.session.commit()

no_admin = User(username='no_admin', email='noadmin@admin.com', password='sha256$RiJPq3hT$74f39e5334d7650bfb30e8294aac9b4275d304507e0e140abc2bec7c6ecebf50', user_role="CUSTOMER", is_active = True)
db.session.add(no_admin)
db.session.commit()


print("DB created.")
