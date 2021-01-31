
import products_db

class ProductsController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng products
    def show_all_products(self):
        items = self.model.get_all_products()
        self.view.display_all_products(items)

    #Phương thức insert
    def them_products(self, productsname, productsprice, productsnumber, productsdescription ):
        resultID = self.model.them_products(productsname, productsprice, productsnumber, productsdescription)
        self.view.ket_qua_insert(resultID)

    #Phương thức update
    def update_products(self, productsname, productsprice, productsnumber, productsdescription, productsid):
        self.model.update_products(productsname, productsprice, productsnumber, productsdescription, productsid)
        self.view.ket_qua_update()

    #Phương thức delete
    def delete_products(self, productsid):
        self.model.delete_products(productsid)
        self.view.ket_qua_delete()