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

# TODO: Collect customer details and check if they are a senior citizen.  
# Assigned to: Annie  

# TODO: Compute total cost of items, applying senior citizen discount if needed.  
# Assigned to: Zyra  

# TODO: Display items, customer name, senior ID (if any), and total amount.  
# Assigned to: Mikee  

# TODO: Integrate and execute all functions in the main program.  
# Assigned to: Kalelle  