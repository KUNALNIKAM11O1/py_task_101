# 1.What will be the output of the following code?

# ```
# classProduct:
# def__init__(self,name,price):
# self.name=name
# self.price=price

# p1=Product("Laptop",50000)
# print(p1.name)

# Ans a) Error

### Q2

#Which keyword is used to define a class in Python?

# Ans c) Self

### Q3

#What is `self` in Python classes?

# Ans c) Reference to current object

# ### Q4

# Which function is automatically called when an object of a class is created?

# Ans d) __init__()

# ### Q5

# Which feature is used for pattern matching in Python 3.10+?

# Ans c) match case

# Section B

### Q6

# Write a **function** that calculates the **final price of a product including GST**.

# GST Rules:

# Electronics → 18%

# Clothing → 5%

# Books → 0%

def calculate_price(price,category):
    
    if category == "electronics":
        gst = 0.18
    elif category == "clothing":
        gst = 0.5
    elif category == "books":
        gst = 0
    else:
        gst = 0
    
    fin_price = price + (price * gst)
    return fin_price

print(calculate_price(1000,"electronics"))

### Q7

# Write a Python program using **match-case** to display menu options.

# ```
# 1 → View Products
# 2 → Add to Cart
# 3 → Checkout
# 4 → Exit

choice = int(input("Enter choice: "))

match choice:
    case 1:
        print("Viewing products...")
    case 2:
        print("Product added to cart")
    case 3:
        print("Proceeding to checkout")
    case 4:
        print("Exiting program")
    case _:
        print("Invalid choice")



### Q8

# Write a function that **counts total items in a shopping cart**.

# Example:

cart= ["Laptop","Mouse","Keyboard"]

def count(cart):
    return len(cart)

total = count(cart)

print("Total items in cart are :",total)

# E-commerce System

class Product:
    def __init__(self,product_id,name,price,category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

    def display_product(self):
        print("Product ID",self.product_id)
        print("Name :",self.name)
        print("Price :",self.price)
        print("Category :",self.category)
        print()

class Cart:
    def __init__(self):
        self.prodcuts = []

    def add_products(self,product):
        self.prodcuts.append(product)
        print(product.name,"added to the cart")

    def view_cart(self):
        if not self.prodcuts:
            print("The cart is empty")
        else:
            print("Items in Cart :")
            for p in self.prodcuts:
                print(p.name)


def cal_fin_price(price,category):
    if category == "electronics":
        gst = 0.18
    elif category == "clothing":
        gst = 0.5
    elif category == "books":
        gst = 0
    else:
        gst = 0

    fin_price = price + price * gst
    return fin_price

def cal_total_cart(cart):
    total_num = 0
    for product in cart.products:
        total_num = cal_fin_price(product.price, product.category)

    print("Total Value of Cart :",total_num)


products = [
    Product(101, "Laptop", 50000, "Electronics"),
    Product(102, "Mobile", 20000, "Electronics"),
    Product(103, "Shirt", 1500, "Clothing"),
    Product(104, "Book", 500, "Books")
]

cart = Cart()


while True:

    print("\n1 View Products")
    print("2 Add Product to Cart")
    print("3 View Cart")
    print("4 Calculate Cart Total")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    match choice:

        case 1:
            print("\nAvailable Products")
            for p in products:
                print(p.product_id, p.name, p.price)

        case 2:
            pid = int(input("Enter Product ID: "))
            found = False

            for p in products:
                if p.product_id == pid:
                    cart.add_products(p)
                    found = True
                    break

            if not found:
                print("Product not found")

        case 3:
            cart.view_cart()

        case 4:
            cal_total_cart(cart)

        case 5:
            print("Exiting program")
            break

        case _:
            print("Invalid choice")