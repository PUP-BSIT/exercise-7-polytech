def get_order_details():
    # TODO(Keith): Gather product name, price, and quantity in a list. 
    details = []
    while True:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        order = {
            'product_name': product_name,
            'price': price,
            'quantity': quantity,
            'total': price * quantity
        }
        details.append(order)
   
        add_more = input("Add another item? (y/n): ")
        if add_more.lower() != 'y':
            break
    return details

def get_customer_info():
    # TODO(Annie): Collect name and check if senior citizen.
    name = input("Enter your name: ")
    is_senior = input("Are you a senior citizen? (y/n): ").strip().lower()

    customer_info = {
        "name": name,
        "is_senior": is_senior in ['yes', 'y']
    }

    if customer_info["is_senior"]:
        customer_info["senior_id"] = input("Enter senior ID: ")

    return customer_info 

def calculate_total(details, is_senior):
    # TODO(Zyra): Compute total and apply senior discount.
    grand_total = sum(order['total'] for order in details)
    return grand_total * 0.9 if is_senior else grand_total


# TODO: Display items, customer name, senior ID (if any), and total amount.  
# Assigned to: Mikee  

# TODO: Integrate and execute all functions in the main program.  
# Assigned to: Kalelle  

def main():
    order_list = get_order_details()
    customer_info = get_customer_info()

if __name__ == "__main__":
    main()
