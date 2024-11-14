""" Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. 
    The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
    If the discount is 20% or higher, apply the discount; otherwise, return the original price. """

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        applied_discount_amount = (price * discount_percent) / 100
        final_price = price - applied_discount_amount
        return final_price
    else:
        return price

""" Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. 
    Print the final price after applying the discount, or if no discount was applied, print the original price."""
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function created above -> calculate_discount(original_price, discount_percentage)
    final_price = calculate_discount(original_price, discount_percentage)

    # Output the price the user has to pay
    if final_price == original_price:
        print(f"No discount was applied. The price stayed at: {original_price}")
    else:
        print(f"The discount was applied. The final price is you'll pay is: {final_price}")
except ValueError: # An exception added in case the user inputs invalid values
    print("Please enter valid numbers for the price and discount percentage.")
