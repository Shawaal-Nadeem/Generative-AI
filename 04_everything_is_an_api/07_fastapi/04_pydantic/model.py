from pydantic import BaseModel

class Creature(BaseModel):
    name: str
    description: str
    image: str
    location: str
    price: int
    

# obj = Creature(name="Squirrel", description="A small squirrel", image="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", location="Squirrel Hill", price=10)
# print(obj.name)