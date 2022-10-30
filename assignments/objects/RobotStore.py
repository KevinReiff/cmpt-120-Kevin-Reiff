from math import prod
from Product import Product

p1 = Product("Ultrasonic range finder", 2.50, 4)
p2 = Product("Servo motor", 14.99, 10)
p3 = Product("Servo controller",44.95, 5 )
p4 = Product("Microcontroller Board", 34.95, 7)
p5 = Product("Laser range finder", 149.99, 2)
p6 = Product("Lithium polymer battery", 8.99, 8)

products = [p1, p2, p3, p4, p5, p6]

def print_stock():
    print("\nAvailable Products")
    print("------------------")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            print(f"{str(i)}) {products[i].name}, ${products[i].price}, {products[i].quantity} in stock")
    print()

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        userinput = input("Enter product ID and quantity you wish to buy: ")
        if "exit" == str(userinput):
            print("Exiting...")
            break

        vals = userinput.split(" ")
        prod_id = int(vals[0])
        count = int(vals[1])

        product = products[prod_id]

        print(f"name={product.name} quantity={product.quantity} price={product.price}")
        if product.inStock(count):
            if cash >= product.getTotalCost():
                price = product.price * count
                cash -= price
                product.remove(count)
                print("You purchased", count, product.name + ".")
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")
        else:
            print("Sorry, we are sold out of", product.name)

main()
