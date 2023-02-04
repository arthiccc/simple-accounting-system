def account_input():
    transactions = []
    while True:
        print("Enter 'done' to exit")
        transaction = input("Enter a transaction: ")
        if transaction == "done":
            break
        transactions.append(transaction)
    return transactions

transactions = account_input()

print("Transactions: ")
for transaction in transactions:
    print("-", transaction)
