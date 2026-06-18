
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0

n = int(input("Enter number of stocks: "))

for i in range(n):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock}: ${investment}")
    else:
        print("Stock not found!")

print("\nTotal Investment Value: $", total_investment)


file = open("portfolio.txt", "w") 
file.write(f"Total Investment Value: ${total_investment}")

print("Result  in portfolio.txt")
