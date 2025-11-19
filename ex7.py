import pandas as pd

def process_purchase_file(filename):

    # Read the file into a DataFrame
    df = pd.read_csv(filename, header=None, names=["Item", "Price", "Quantity", "Free"])

    # Calculate amount per item
    df["Amount"] = df["Price"] * df["Quantity"]

    # Total number of purchased items
    total_items = df["Quantity"].sum()

    # Total free items
    total_free = df["Free"].sum()

    # Total amount before discount
    amount_to_pay = df["Amount"].sum()

    # Discount based on price of free items
    df["Discount"] = df["Free"] * df["Price"]
    discount = df["Discount"].sum()

    # Final payable amount
    final_amount = amount_to_pay - discount

    # Output
    print(f"\nResults from file: {filename}")
    print(f"No of items purchased: {total_items}")
    print(f"No of free items: {total_free}")
    print(f"Amount to pay: {amount_to_pay}")
    print(f"Discount given: {discount}")
    print(f"Final amount paid: {final_amount}")


# Test on the two files
process_purchase_file("purchase-1.txt")
process_purchase_file("purchase-2.txt")
