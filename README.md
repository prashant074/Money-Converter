# Currency Converter Script

This Python script demonstrates a simple **currency conversion tool** using predefined exchange rates. The program allows users to input an amount and convert it between supported currencies: `GBP`, `USD`, `EUR`, `BRL`, `JPY`, and `TRY`.

## Key Features
1. **Exchange Rates**:  
   Predefined static exchange rates for quick reference.
2. **Functions**:
   - `get_exchange_rate`: Retrieves the conversion rate between two currencies.
   - `convert_currency`: Converts a given amount from one currency to another using the exchange rate.
3. **User Input**:  
   Prompts users to enter:
   - Amount to convert.
   - Source currency (`from_currency`).
   - Target currency (`to_currency`).
4. **Error Handling**:  
   Handles invalid currencies or unavailable exchange rates.

## How to Use
1. Run the script.
2. Follow the prompts to enter:
   - Amount to convert.
   - Source and target currencies.
3. The script calculates and displays the converted amount.

---

### Example
**Input**:
```
Enter the amount to convert: 100  
Enter the source currency (GBP, USD, EUR, BRL, JPY, TRY): USD  
Enter the target currency (GBP, USD, EUR, BRL, JPY, TRY): EUR  
```

**Output**:
```
100.0 USD is equivalent to 85.00 EUR.
```
