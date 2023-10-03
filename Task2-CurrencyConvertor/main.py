class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = {}

    def set_exchange_rate(self, from_currency, to_currency, rate):
        self.exchange_rates[(from_currency, to_currency)] = rate

    def convert_currency(self, amount, from_currency, to_currency):
        key = (from_currency, to_currency)
        if key in self.exchange_rates:
            converted_amount = amount * self.exchange_rates[key]
            return converted_amount, to_currency
        else:
            return None, None

def main():
    converter = CurrencyConverter()

    # Manually set exchange rates
    converter.set_exchange_rate('USD', 'EUR', 0.85)
    converter.set_exchange_rate('EUR', 'USD', 1.18)
    converter.set_exchange_rate('USD', 'GBP', 0.75)
    converter.set_exchange_rate('GBP', 'USD', 1.33)

    while True:
        try:
            amount = float(input("Enter the amount to convert: "))
            from_currency = input("Enter the currency to convert from: ").upper()
            to_currency = input("Enter the currency to convert to: ").upper()

            converted_amount, target_currency = converter.convert_currency(amount, from_currency, to_currency)

            if converted_amount is not None:
                print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {target_currency}")
            else:
                print("Invalid currency pair. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()
