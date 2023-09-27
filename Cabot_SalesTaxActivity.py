while True:
    print("Sales Tax")
    price = eval(input("Enter purchase amount: "))
    tax = price * 0.06
    sale = "{:.2f}".format(tax)
    print("Sales Tax of", price, "is:", sale)
    discount = float(price) - float(sale)
    new = "{:.2f}".format(discount)
    print("The discounted price is now", new)
    print("----------------------------------")
