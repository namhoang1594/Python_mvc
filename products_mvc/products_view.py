
import products_db

class ProductsView(object):

    #Hàm hiển thị tất cả dữ liệu về products
    def display_all_products(self, items):
        print("Dữ liệu về các products thu được như sau:")
        for item in items:
            print("ID: {}, Tên sản phẩm: {}, Giá: {}, Số lượng: {}, Mô tả: {}".format(item.productsid, item.productsname, item.productsprice, item.productsnumber, item.productsdescription))
        print("-----Kết thúc hiển thị dữ liệu------")

    #Hàm thông báo kết quả insert
    def ket_qua_insert(self, resultID):
        id = resultID[0]
        if id > 0:
            print("Insert thanh cong")
        else:
            print("Fail")