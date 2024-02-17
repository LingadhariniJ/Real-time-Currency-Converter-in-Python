import asyncio
from forex_python_async.converter import CurrencyRates

async def currency_converter(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        # Fetch real-time exchange rates asynchronously
        exchange_rate = await c.get_rate(from_currency, to_currency)

        # Perform currency conversion
        converted_amount = round(amount * exchange_rate, 2)

        # Display the result
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")

    except Exception as e:
        print(f"Error: {e}")

async def main():
    # Accept user input
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency code (e.g., USD): ").upper()
    to_currency = input("Enter the target currency code (e.g., EUR): ").upper()

    # Call the asynchronous currency converter function
    await currency_converter(amount, from_currency, to_currency)

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
