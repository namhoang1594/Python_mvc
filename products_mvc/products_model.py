import products_db


class ProductsModel(object):
    #Phương thức khởi tạo
    def __init__(self, database_server, username, password, database):
        self.connection, self.metadata, self.engine = products_db.ket_noi_den_csdl(database_server,
                                                                                 username,
                                                                                 password,
                                                                                 database)

    #Phương thức lấy dữ liệu
    def get_all_products(self):
        results = products_db.lay_tat_ca_du_lieu_bang_products(self.connection,
                                                           self.metadata,
                                                           self.engine)
        return results

    #Phương thức insert
    def them_products(self, productsname, productsprice, productsnumber, productsdescription):
        resultID = products_db.them_products(self.connection,
                                       self.metadata,
                                       self.engine,
                                        productsname,
                                        productsprice,
                                        productsnumber,
                                        productsdescription)
        return resultID

    #Phương thức update
    def update_products(self, productsname, productsprice, productsnumber, productsdescription, productsid):
        resultID = products_db.update_products(self.connection,
                                             self.metadata,
                                             self.engine,
                                             productsname,
                                             productsprice,
                                             productsnumber,
                                             productsdescription,
                                             productsid)
        return resultID

    #Phương thức delete
    def delete_products(self, productsid):
        resultID = products_db.delete_products(self.connection,
                                               self.metadata,
                                               self.engine,
                                               productsid)
        return resultID