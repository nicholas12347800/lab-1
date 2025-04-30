# 8.1 CHECK PROTECTION

# Get dollar amount from user
amount = float(input("Enter the dollar amount: "))

# Format the amount with 2 decimal places
formatted_amount = f"{amount:,.2f}"

# Pad with leading asterisks to make total length 10 characters
check_protected = f"{formatted_amount:*>10}"

# Print the result
print(check_protected)
