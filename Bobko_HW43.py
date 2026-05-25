# task 1 - Добавление товаров
# task 2 - Увеличение цен

from pymongo import MongoClient
from pymongo.errors import PyMongoError

try:
    client = MongoClient(
        "mongodb://ich_editor:verystrongpassword@mongo.itcareerhub.de/"
        "?readPreference=primary&ssl=false&authMechanism=DEFAULT&authSource=ich_edit"
    )

    db = client["ich_edit"]
    products = db["products_121225ptm_PolinaBobko"]

    products.delete_many({})
    print("Collection cleared.")

    new_items = [
        {"name": "Pen", "price": 1.50, "stock": 3},
        {"name": "Notebook", "price": 4, "stock": 2},
        {"name": "Backpack", "price": 25, "stock": 1}
    ]

    res = products.insert_many(new_items)
    print(f"{len(res.inserted_ids)} products inserted.")

    updated_items = products.update_many(
        {},
        [{
            "$set": {
                "price": {
                    "$round": [
                        {"$multiply": ["$price", 1.2]},
                        2
                    ]
                }
            }
        }]
    )

    print(f"Prices updated for {updated_items.modified_count} products")

    print("Updated products:")
    for doc in products.find():
        print(f"- {doc['name']} — ${doc['price']:.2f}")

except PyMongoError as e:
    print(f"MongoDB error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")

finally:
    client.close()