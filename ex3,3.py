#câu 1 Grid 2x2 
def ve_dong_ngang():
    print("+ - - - - + - - - - +")

def ve_dong_doc():
    print("|         |         |")

def grid_2x2():
    for i in range(2):
        ve_dong_ngang()
        for j in range(4):
            ve_dong_doc()
    ve_dong_ngang()

# chạy
grid_2x2()
# câu 2 Grid 4x4 
def ve_dong_ngang_4():
    print("+ - - - - + - - - - + - - - - + - - - - +")

def ve_dong_doc_4():
    print("|         |         |         |         |")

def grid_4x4():
    for i in range(4):
        ve_dong_ngang_4()
        for j in range(4):
            ve_dong_doc_4()
    ve_dong_ngang_4()

# chạy
grid_4x4()