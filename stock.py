stocks = {
    "APPL": 180,
    "TSLA": 250,
    "GOOG":150
    }

stock = input("enter stock name:").upper()
qty = int(input("enter qunatity: "))

if stock in stocks:
    total = stocks[stock] * qty
    print("total investment = ",total)
    file=open("portfolio.txt","w")
    file.write("stock name:" +stock +"\n")
    file.write("quantity:" +str(qty) + "\n")
    file.write("price: " + str(stocks[stock]) + "\n")
    file.write("total investment: " + str(total))
    file.close()

    print("data save in portfolio.txt")

else:
    print("stock not found")


               