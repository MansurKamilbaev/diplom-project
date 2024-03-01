from pydantic import BaseModel


class AddProductValidator(BaseModel):
    product_name: str
    product_description: str
    product_price: float
    product_quantity: int


class EditProductValidator(BaseModel):
    product_id: int
    edit_data: str
    new_data: str


class CommentProductValidator(BaseModel):
    product_id: int
    assessment: int
    comment: str
