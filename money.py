# Sample exchange rates for demonstration purposes
EXCHANGE_RATES = {
    'GBP': {'USD': 1.37, 'EUR': 1.16, 'BRL': 7.03, 'JPY': 151.25, 'TRY': 26.81},
    'USD': {'GBP': 0.73, 'EUR': 0.85, 'BRL': 5.13, 'JPY': 110.57, 'TRY': 19.53},
    'EUR': {'GBP': 0.86, 'USD': 1.18, 'BRL': 6.02, 'JPY': 129.41, 'TRY': 23.03},
    'BRL': {'GBP': 0.14, 'USD': 0.19, 'EUR': 0.17, 'JPY': 21.07, 'TRY': 3.83},
    'JPY': {'GBP': 0.0066, 'USD': 0.0090, 'EUR': 0.0077, 'BRL': 0.047, 'TRY': 0.18},
    'TRY': {'GBP': 0.037, 'USD': 0.051, 'EUR': 0.043, 'BRL': 0.26, 'JPY': 5.49},
}

def get_exchange_rate(from_currency, to_currency):
    """Fetch the exchange rate from one currency to another."""
    if from_currency in EXCHANGE_RATES and to_currency in EXCHANGE_RATES[from_currency]:
        return EXCHANGE_RATES[from_currency][to_currency]
    else:
        raise ValueError(f"Exchange rate from {from_currency} to {to_currency} not available.")

def convert_currency(amount, from_currency, to_currency):
    """Convert the amount from one currency to another."""
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def main():
    """Main function to run the currency converter."""
    print("Welcome to the Currency Conversion Tool!")
    
    # Input from the user
    try:
        amount = float(input("Enter the amount to convert: "))
        from_currency = input("Enter the source currency (GBP, USD, EUR, BRL, JPY, TRY): ").upper()
        to_currency = input("Enter the target currency (GBP, USD, EUR, BRL, JPY, TRY): ").upper()
        
        # Currency conversion
        result = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equivalent to {result:.2f} {to_currency}.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
