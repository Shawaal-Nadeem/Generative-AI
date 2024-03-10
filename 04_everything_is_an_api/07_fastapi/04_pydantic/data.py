from model import Creature

list_of_objs = [
    Creature(
        name="Grizzly Bear",
        description="A large bear native to North America, known for its distinctive hump on its shoulders and long claws.",
        image="https://example.com/grizzly_bear.jpg",
        location="North America",
        price=5000
    ),
    Creature(
        name="Bald Eagle",
        description="A majestic bird of prey found in North America, recognized by its white head and tail feathers.",
        image="https://example.com/bald_eagle.jpg",
        location="North America",
        price=2500
    ),
    Creature(
        name="Kangaroo",
        description="A marsupial found mainly in Australia, known for its powerful hind legs and pouch for carrying young.",
        image="https://example.com/kangaroo.jpg",
        location="Australia",
        price=3000
    )
]

def get_all_creatures():
    return list_of_objs