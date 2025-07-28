# Stock Prices
stock_prices={ 
                "AAPL":180, 
              "TSLA":250,
              "GOOG":2700, 
              "MSFT":330
              }


#To hold portfolio
portfolio={}


# User input
print("Enter stock name and quantity( type done to finish): ")

while True:
    stock=input("stock name:").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not found in price list")
        continue
    quantity=int(input("Quantity:"))
    portfolio[stock]=quantity


# Calculation
total=0
for stock,quantity in portfolio.items():
    price=stock_prices[stock]
    investment=price*quantity
    print(f"\n{stock}: {quantity} shares × ${price} = ${investment}")
    total+=investment
    
print(f"\nTotal investment: {total}")


# Optional : Save to File 
save = input("Do you want to save this to a file? (yes/no):").lower()
if save == "yes":
    with open("Portfolio1.txt","w")as file:
        for stock,quantity in portfolio.items():
            price=stock_prices[stock]
            investment=price*quantity
            file.write(f"\n{stock}: {quantity} Shares x ${price} = ${investment}")
        file.write(f"\nTotal investment:{total}")
    print("\nFile is successfuly saved as Portfolio.txt")