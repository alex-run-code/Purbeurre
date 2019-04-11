import mysql.connector
import openfoodfacts

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="210991"
)

mycursor = mydb.cursor(buffered=True)
mycursor.execute("USE PurBeurredb")

#This function download some data from OFF's db to our mysql db (PurBeurreDb)
def add_food_in_db(category):
    products = openfoodfacts.products.get_by_facets({
    'category': category,
    'language': 'france'
    })
    list_of_food = []
    for food in products:
        rules = ['product_name_fr' in food,
                'nova_group' in food,
                'countries_tags' in food,
                'stores_tags' in food,
                'nutriments' in food and 'energy' in food['nutriments'] #disable this line for "boissons"
                ]
        if all(rules):
            if len(food['product_name_fr']) != 0:
                Product_name_fr = str(food['product_name_fr'])
                nova_group = str(food['nova_group'])
                countries_tags = str(food['countries_tags'])
                stores_tags = str(food['stores_tags'])
                energy = food['nutriments']['energy'] # put energy = 0 for boissons, else, put energy = food['nutriments']['energy']
                # ! THE NEXT LINE MUST BE MODIFIED FOR EACH DIFFERENT TABLE: viandes, snacks, boissons, etc... !
                # change [table] in "INSERT INTO [table]"
                mysql = "INSERT INTO desserts (Product_name, nova_group, countries_tags, stores_tags, energy) VALUES (%s, %s, %s, %s, %s)"
                values = [(Product_name_fr, nova_group, countries_tags, stores_tags, energy)]
                mycursor.executemany(mysql, values)
                mydb.commit()
                print("added successfully")

#change the name of the category here
add_food_in_db('desserts')

