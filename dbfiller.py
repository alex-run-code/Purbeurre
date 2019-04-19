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
                'url' in food, 
                ]
        if not all(rules):
            continue
        if len(food['product_name_fr']) == 0:
            continue
        Product_name_fr = str(food['product_name_fr'])
        nova_group = str(food['nova_group'])
        countries_tags = str(food['countries_tags'])
        stores_tags = str(food['stores_tags'])
        url = str(food['url'])
        add_food_sql = "INSERT INTO foods (Product_name, nova_group, category_name, countries_tags, stores_tags, off_url) VALUES (%s, %s, %s, %s, %s, %s)"
        val_food_sql = [(Product_name_fr, nova_group, category, countries_tags, stores_tags, url)]
        mycursor.executemany(add_food_sql, val_food_sql)
        mydb.commit()
        print("added successfully")

# This function add a category in the database
def add_category_in_db(category):
    add_category_sql = 'INSERT INTO categories (category_name) VALUES (%s)'
    val_cat_sql = [(category,)]
    mycursor.executemany(add_category_sql, val_cat_sql)
    mydb.commit()

# Add a category in the table 'categories'
def fill_categories():
    add_category_in_db('snacks')
    add_category_in_db('boissons')
    add_category_in_db('desserts')
    add_category_in_db('viandes')
    add_category_in_db('charcuteries')

# Add all the foods from selected categories in the table 'foods'
def fill_foods():
    add_food_in_db('snacks')
    add_food_in_db('boissons')
    add_food_in_db('desserts')
    add_food_in_db('viandes')
    add_food_in_db('charcuteries')

fill_foods()




