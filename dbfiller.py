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
                'url' in food, 
                'stores_tags' in food,
                ]
        if not all(rules):
            continue
        if len(food['product_name_fr']) == 0:
            continue
        product_name_fr = str(food['product_name_fr'])
        nova_group = str(food['nova_group'])
        url = str(food['url'])
        stores_tags = food['stores_tags']
        #adding store in stores
        for store in stores_tags:
            add_store_sql = "INSERT IGNORE INTO stores (stores_name) values (%s)"
            val_store_sql = [(store,)]
            mycursor.executemany(add_store_sql, val_store_sql)
            mydb.commit()
        #adding food in foods
        mycursor.execute("SELECT id FROM categories WHERE category_name = '" + category + "'")
        category_id = mycursor.fetchall()
        category_id = category_id[0][0]
        add_food_sql = "INSERT IGNORE INTO foods (product_name, nova_group, category_id, off_url) VALUES (%s, %s, %s, %s)"
        val_food_sql = [(product_name_fr, nova_group, category_id, url)]
        mycursor.executemany(add_food_sql, val_food_sql)
        mydb.commit()
        #adding foods id and stores id in foods stores
        for store in stores_tags:
            mycursor.execute('SELECT id FROM foods WHERE product_name = "' + product_name_fr + '"')
            foods_id = mycursor.fetchall()
            foods_id = int(foods_id[0][0])
            mycursor.execute("SELECT id FROM stores WHERE stores_name = '" + store + "'")
            stores_id = mycursor.fetchall()
            stores_id = int(stores_id[0][0])
            add_foods_id_sql = "INSERT INTO foods_stores (foods_id, stores_id) VALUES (%s, %s)"
            val_foods_id_sql = [(foods_id, stores_id)]
            mycursor.executemany(add_foods_id_sql, val_foods_id_sql)
            mydb.commit()
        print("added successfully")

# This function add a category in the database
def add_category_in_db(category):
    add_category_sql = 'INSERT IGNORE INTO categories (category_name) VALUES (%s)'
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




fill_categories()
fill_foods()

