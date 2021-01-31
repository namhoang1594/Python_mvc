
import products_db
import products_model, products_view, products_controller

def start():
    #Khởi tạo đối tượng model
    model = products_model.ProductsModel("localhost","root","123456789","spring_cg")
    #Khởi tạo đối tượng view
    view = products_view.ProductsView()
    #Khởi tạo controller
    controller = products_controller.ProductsController(model, view)
    item = menu()
    while item in ["1", "2", "3", "4"]:
        if item =="1":
            controller.show_all_products()
        elif item =="2":
            productsname = input("Nhập tên sản phẩm: ")
            productsprice = input("Nhập giá sản phẩm: ")
            productsnumber = input("Nhập số lượng: ")
            productsdescription = input("Nhập mô tả: ")
            controller.them_products(productsname, productsprice, productsnumber, productsdescription)
        elif item=="3":
            productsname = input("Nhập tên sản phẩm: ")
            productsprice = input("Nhập giá sản phẩm: ")
            productsnumber = input("Nhập số lượng: ")
            productsdescription = input("Nhập mô tả: ")
            productsid = input("Nhập id sản phẩm")
            controller.update_products(productsname, productsprice, productsnumber, productsdescription, productsid)
        elif item=="4":
            productsid = input("Nhập id sản phẩm")
            controller.delete_products(productsid)

        item = menu()
def menu():
    print("1: Hiển thị tất cả Sản Phẩm")
    print("2: Thêm mới Sản Phẩm")
    print("3: Cập nhật Sản Phẩm")
    print("4: Xóa Sản Phẩm")
    choice = input("Hãy lựa chọn tác vụ. Chọn sai sẽ thoát chương trình!")
    return choice

if __name__ == "__main__":
    start()