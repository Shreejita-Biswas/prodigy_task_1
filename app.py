import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# --- 1. Load Data ---
df = pd.read_csv('train.csv')

# --- 2. Preprocess & Feature Engineer ---
# Create a 'TotalBath' feature
df['TotalBath'] = df['FullBath'] + (0.5 * df['HalfBath'])

# Select features (X) and target (y)
features = ['GrLivArea', 'BedroomAbvGr', 'TotalBath']
target = 'SalePrice'
X = df[features]
y = df[target]

# --- 3. Split Data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- 4. Train Model ---
model = LinearRegression()
model.fit(X_train, y_train)

print("Model training complete!")
print(f"Intercept: {model.intercept_:.2f}")
print(f"Coefficients: {model.coef_}")


# --- 5. Evaluate Model ---
y_pred = model.predict(X_test)

# Calculate metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Absolute Error (MAE): ${mae:,.2f}")
print(f"R-squared (R2): {r2:.2f}")

# --- 6. Visualize Results ---
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.7)
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', lw=2)
plt.xlabel("Actual Prices", fontsize=12)
plt.ylabel("Predicted Prices", fontsize=12)
plt.title("Actual vs. Predicted House Prices", fontsize=14)
plt.grid(True)
plt.show()
