import json
import os
import sys
from converter.registry import CurrencyRegistry
from converter.converter import CurrencyConverter
from converter.currency import CurrencyError

CURRENCY_FILE = "currencies.json"

def load_currencies():
    if not os.path.exists(CURRENCY_FILE):
        with open(CURRENCY_FILE, "w") as f:
            json.dump({"USD": 1.0}, f)
    with open(CURRENCY_FILE, "r") as f:
        return json.load(f)

def save_currencies(data):
    with open(CURRENCY_FILE, "w") as f:
        json.dump(data, f, indent=4)

def show_menu():
    print("\n==== Currency Converter ====")
    print("1. Convert currency")
    print("2. Update exchange rate")
    print("3. List available currencies")
    print("4. Exit")
    print("============================")

def select_currency(registry):
    currencies = list(registry._currencies.keys())
    if not currencies:
        print("No currencies available.")
        return None

    print("\nSelect currency (or type 'x' to cancel):")
    for idx, code in enumerate(currencies):
        print(f"  {idx + 1}. {code}")

    choice = input("Enter number: ")
    if choice.lower() == 'x':
        return None
    try:
        choice = int(choice)
        if 1 <= choice <= len(currencies):
            return currencies[choice - 1]
        else:
            print("Invalid selection.")
            return None
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

def main():
    currency_data = load_currencies()
    registry = CurrencyRegistry()
    converter = CurrencyConverter(registry)

    for code, rate in currency_data.items():
        registry.add_currency(code, rate)

    while True:
        show_menu()
        choice = input("Enter choice (or 'x' to exit): ")
        if choice.lower() == 'x' or choice == "4":
            print("Goodbye!")
            break

        if choice == "1":
            try:
                amount_input = input("Amount to convert (or 'x' to cancel): ")
                if amount_input.lower() == 'x':
                    continue
                amount = float(amount_input)

                from_code = select_currency(registry)
                if from_code is None:
                    continue
                to_code = select_currency(registry)
                if to_code is None:
                    continue

                result = converter.convert(amount, from_code, to_code)
                print(f"{amount} {from_code} = {result} {to_code}")
            except CurrencyError as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid amount. Must be a number.")

        elif choice == "2":
            code = select_currency(registry)
            if code is None:
                continue
            new_rate_input = input(f"Enter new exchange rate for {code} to USD (or 'x' to cancel): ")
            if new_rate_input.lower() == 'x':
                continue
            try:
                new_rate = float(new_rate_input)
                registry.update_currency(code, new_rate)
                currency_data[code] = new_rate
                save_currencies(currency_data)
                print(f"{code} updated to rate {new_rate}")
            except ValueError:
                print("Invalid input. Must be a number.")

        elif choice == "3":
            print("\nAvailable currencies:")
            for code in registry._currencies:
                rate = registry.get_currency(code).rate_to_usd
                print(f"  {code}: 1 {code} = {rate} USD")

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
