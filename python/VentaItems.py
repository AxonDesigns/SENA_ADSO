def input_int(msg, error_msg: str) -> int:
    while True:
        try:
            temp = int(input(str(msg)))
        except:
            print(error_msg)
        else:
            return temp

def input_int_range(msg, start: int, end: int, type_error_msg: str, range_error_msg: str) -> int:
    while True:
        temp = input_int(msg, type_error_msg)
        if temp >= start and temp <= end:
            return temp
        else:
            print(range_error_msg)

def main():
    item_count = input_int("Enter the amount of items to process: ", "ERROR: Enter a correct value")
    items = []

    for _ in range(item_count):
        name = input("Enter the product's name: ")
        id = input("Enter the product's identifier: ")
        amount = input_int("Enter item's purchased amount: ", "ERROR: Enter a correct value")
        unit_price = input_int("Enter item's unit price: ", "ERROR: Enter a correct value")
        iva_type = input_int_range("Enter IVA type:\n 1. Tax free\n 2. Goods\n 3. General\n> ", 1, 3, "ERROR: Enter a correct option", "ERROR: Enter a corrent value")
        iva_percentage = {1: 0.0, 2: 0.05, 3: 0.19}.get(iva_type, 0)
        subtotal = (unit_price * amount)

        items.append({"name": name, "id": id, "amount": amount, "unit_price": unit_price, "iva_type": iva_type, "iva_percentage": iva_percentage, "subtotal": subtotal})
    
    print("\n".join([(
            f'- {item["name"]} | [{item["id"]}]\n'.upper() +
            f'   Amount: {item["amount"]}\n' +
            f'   Unit Price: ${item["unit_price"]:,}\n'.replace(",", ".") +
            f'   IVA: {({1: "Tax Free 0%", 2: "Goods 5%", 3: "General 19%"}.get(item["iva_type"]))}\n' +
            f'   Subtotal price: ${item["subtotal"]:,}\n'.replace(",", ".") +
            f'   Total price: ${round(item["subtotal"] * (1 + item["iva_percentage"])):,}\n'.replace(",", ".")
            )for item in items]))

if __name__ == "__main__":
    main()