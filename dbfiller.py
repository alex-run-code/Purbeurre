import mysql.connector
import openfoodfacts
import config


mydb = mysql.connector.connect(
  host=config.DB_HOST,
  user=config.DB_USER,
  passwd=config.DB_PASSWD
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
        if not food['product_name_fr'].strip():
            continue
        product_name_fr = food['product_name_fr']
        nova_group = food['nova_group']
        url = food['url']
        stores_tags = food['stores_tags']
        #adding store in stores
        for store in stores_tags:
            add_store_sql = "INSERT IGNORE INTO stores (stores_name) values (%s)"
            val_store_sql = [(store,)]
            mycursor.executemany(add_store_sql, val_store_sql)
            mydb.commit()
        #adding food in foods
        sql = "SELECT id FROM categories WHERE category_name = %s"
        val = [(category,)]
        mycursor.executemany(sql, val)
        category_id = mycursor.fetchall()
        category_id = category_id[0][0]
        add_food_sql = "INSERT IGNORE INTO foods (product_name, nova_group, category_id, off_url) VALUES (%s, %s, %s, %s)"
        val_food_sql = [(product_name_fr, nova_group, category_id, url)]
        mycursor.executemany(add_food_sql, val_food_sql)
        mydb.commit()
        #adding foods id and stores id in foods stores
        for store in stores_tags:
            sql = ' SELECT id FROM foods WHERE product_name = %s '
            val = [(product_name_fr,)]
            mycursor.executemany(sql, val)
            foods_id = mycursor.fetchall()
            foods_id = int(foods_id[0][0])
            sql = ' SELECT id FROM stores WHERE stores_name = %s '
            val = [store]
            mycursor.execute(sql, val)
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




#fill_categories()
fill_foods()