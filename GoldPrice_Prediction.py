# Sample data (Replace this with your own dataset or data handling)
# Let's assume you have lists representing features and gold prices
# Example data for features and corresponding gold prices
features = [[1.2], [2.4], [3.6], [4.8], [5.0]]  # Example feature: weight of gold
gold_prices = [150, 220, 300, 380, 400]  # Corresponding gold prices

# Simple linear regression function
def simple_linear_regression(features, target):
    n = len(features)
    sum_x = sum(features)
    sum_y = sum(target)
    sum_xy = sum([x * y for x, y in zip(features, target)])
    sum_x_sq = sum([x ** 2 for x in features])

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_sq - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

# Calculate slope and intercept using simple linear regression
slope, intercept = simple_linear_regression([f[0] for f in features], gold_prices)

# Function to predict gold price
def predict_price(weight):
    return slope * weight + intercept

# Example prediction for a weight of 6.2
predicted_price = predict_price(6.2)
print(f"Predicted gold price for a weight of 6.2: {predicted_price}")
