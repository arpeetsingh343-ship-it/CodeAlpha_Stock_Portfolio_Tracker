stock_prices = {
    "AAPL" : 180,
    "TSLA" : 250,
    "GOOGL" : 140,
    "AMZN" : 175
}

def main():
    print("--- STOCK Portfolio Tracker ---")

    # 1. User inputs
    stock_name = input("Enter stock name (e.g., AAPL): ").upper()

    if stock_name in stock_prices:
        try:
            quantity = int(input(f"Enter quantity of {stock_name} shares: "))

            # 2. Basic Arithmetic
            price = stock_prices[stock_name]
            total_value = price * quantity

            # 3. Display Results
            result_msg = f"Total Investment for {quantity} shares of{stock_name}: ${total_value}"
            print(f"\n{result_msg}")

            #4. File Handling
            with open("portfolio_summary.txt" , "w") as file:
                file.write(result_msg)
            print("Summary saved to portfolio_summary.txt")

        except ValueError:
            print("Invalid input. Please enter a number for quantity.")

    else:
        print("Stock symbol not found in our database.")

if __name__ == "__main__":
    main()                        