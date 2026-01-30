from lib.check_discount import get_payment_status, total_aft_discont

# enter discount price here
discount = 20

# list data customer and their total price
customers = [
    {
        "name": "Luna",
        "total_price": 40
    },
    {
        "name": "Budi",
        "total_price": 100
    },
    {
        "name": "Jenny",
        "total_price": 20
    },
] 

# print format layout
print("="*60)
print("Discount Case")
print("="*60)

# looping to handle all result
for item in customers:
    count = total_aft_discont(item.get("total_price"), discount)
    customer_name = item.get("name") # to get data from array can use item.get("param_name")
    customer_price = item["total_price"] # to get data from array can use item["param_name"]
    result_discount = get_payment_status(count, discount)
    print(f"{customer_name}'s total purchase is ${customer_price}, {result_discount}")

# print format layout
print("="*60)