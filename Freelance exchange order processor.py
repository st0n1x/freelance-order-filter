import json
import csv

orders = []
def get_price(order):
    return order[1]

try:
    with open("history.json", "r") as f:
        seen = set(json.load(f))
except:
    seen = set()

while True:
    order = input("Enter a name, price, site and description separated by ';'(Q to quit): ")
    if order.lower() == "q":
        break
    else:
        parts = order.split(";")
        parts[1] = float(parts[1])
        orders.append(parts)

sorted_orders = sorted(orders, key=get_price, reverse=True)
final_result = []
price_filter = float(input("Enter a minimum price: "))
keys = input("Enter a keywords separated by ',': ")
keys = keys.split(",")
for order in sorted_orders:
    if order[1] >= price_filter:
            for key in keys:
                key = key.strip()
                if key in order[0].lower() or key in order[3].lower():
                    final_result.append(order)
                    break

new_orders = ["Name", "Price", "Site", "Description"]
for order in final_result:
    order_id = f"{order[0]}_{order[1]}_{order[2]}"
    if order_id not in seen:
        new_orders.append(order)
        seen.add(order_id)
file_path1 = "history.json"

with open(file_path1, "w") as f:
    json.dump(list(seen), f, indent=4)

file_path2 = "Orders.csv"

with open(file_path2, "w", newline="") as file:
    writer = csv.writer(file)
    for row in new_orders:
        writer.writerow(row)
    print("csv file was created")