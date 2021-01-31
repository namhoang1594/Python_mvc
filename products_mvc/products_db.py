import sqlalchemy as db

def ket_noi_den_csdl(database_server, username, password, database):
    connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData()
    return connection, metadata, engine

#Xây dựng hàm lấy tất cả dữ liệu của bảng Products
def lay_tat_ca_du_lieu_bang_products(connection, metadata, engine):
    # Lấy đối tượng product từ bảng products trong csdl
    products = db.Table('products', metadata, autoload=True, autoload_with=engine)

    # Lấy tất cả dữ liệu của bảng products - tương đương câu lênh SELECT * FROM products
    query = db.select([products])

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    return ResultSet

#Hàm insert - tra ve id vua duoc tao
def them_person(connection, metadata, engine,
                productsname, productsprice, productsnumber, productsdescription):
    # Lấy đối tượng products từ bảng products trong csdl
    products = db.Table('products', metadata, autoload=True, autoload_with=engine)
    # Chèn 1 dòng vào bảng products
    query = db.insert(products).values(productsname = productsname, productsprice = productsprice, productsnumber = productsnumber, productsdescription = productsdescription)
    ResultProxy = connection.execute(query)
    # Trả về giá trị id vừa được sinh
    return ResultProxy.inserted_primary_key
#Hàm update
def update_products(connection, metadata, engine,
                productsname, productsprice, productsnumber, productsdescription, productsid):
    products = db.Table('products', metadata, autoload=True, autoload_with=engine)
    query_update = db.update(products).values(productsname = productsname, productsprice = productsprice,
                                              productsnumber = productsnumber, productsdescription = productsdescription).where(products.columns.productsid == productsid)
    ResultProxy = connection.execute(query_update)
    return ResultProxy

#Hàm delete
def update_products(connection, metadata, engine,
                    productsid):
    products = db.Table('products', metadata, autoload=True, autoload_with=engine)
    query_delete = db.delete(products).where(products.columns,productsid == productsid)
    ResultProxy = connection.execute(query_delete)
    return ResultProxy