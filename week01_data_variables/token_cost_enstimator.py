print("=== AI Token Cost Estimator ===")
tokens = int(input("How many tokens? "))
price_per_1000 = float(input("Price per 1000 tokens (in rupees)? "))
cost = (tokens / 1000) * price_per_1000
print(f"Estimated cost: ₹{cost:.2f}")