from typing import Optional

class Item:
    def __init__(self,
                 description: str,
                 price: int,
                 image_url: str,
                 brand_name: Optional[str] = None,
                 shipping_price: Optional[str] = None) -> None:
        
        self.description = description
        self.price = price
        self.image_url = image_url
        self.brand_name = brand_name
        self.shipping_price = shipping_price
    
    def __str__(self) -> str:
        return (f"Item(desc: {self.description}, price: {self.price}, "
                f"brand: {self.brand_name}, shipping: {self.shipping_price}, "
                f"url: {self.image_url})")
