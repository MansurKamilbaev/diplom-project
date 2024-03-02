from fastapi import FastAPI
from users.user_api import user_router
from products.products_api import product_router
from starlette.staticfiles import StaticFiles
from usercart.user_cart_api import cart_router


from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Пятёрочка", docs_url='/')

app.mount(path='/gallery', app=StaticFiles(directory='media'))

app.include_router(user_router)
app.include_router(product_router)
app.include_router(cart_router)

