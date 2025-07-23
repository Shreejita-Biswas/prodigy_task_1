# 🏠 House Price Prediction using Linear Regression

This project implements a linear regression model to predict house sale prices based on key features like living area, number of bedrooms, and bathrooms. The model is built using Python with the `pandas`, `scikit-learn`, and `matplotlib` libraries.

## 📜 Description

The goal of this project is to create a simple yet effective model for estimating house prices. The script performs the following steps:
1.  **Loads** the housing data from `train.csv`.
2.  **Preprocesses** the data by engineering a new feature, `TotalBath`, which combines full and half bathrooms.
3.  **Selects** a set of features (`GrLivArea`, `BedroomAbvGr`, `TotalBath`) and the target variable (`SalePrice`).
4.  **Splits** the data into training and testing sets to prepare for model evaluation.
5.  **Trains** a linear regression model on the training data.
6.  **Evaluates** the model's performance on the test data using Mean Absolute Error (MAE) and R-squared ($R^2$) metrics.
7.  **Visualizes** the results with a scatter plot comparing actual prices to the model's predictions.

---

## ⚙️ Technologies Used

* **Python 3**
* **Pandas:** For data manipulation and loading the dataset.
* **Scikit-learn:** For building and evaluating the linear regression model.
* **Matplotlib:** For visualizing the model's performance.

---

## 🚀 Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Shreejita-Biswas/prodigy_task_1.git](https://github.com/Shreejita-Biswas/prodigy_task_1.git)
    cd prodigy_task_1
    ```

2.  **Install the required libraries:**
    It's recommended to create a virtual environment first. Then, install the packages using pip.
    ```bash
    pip install pandas scikit-learn matplotlib
    ```

3.  **Dataset:**
    Make sure the `train.csv` file is in the root directory of the project.

---

## ▶️ How to Run

To run the script and see the output, execute the following command in your terminal:

```bash
python main.py
```
*(Assuming your script is named `main.py`)*

The script will:
1.  Print the model's intercept and coefficients after training.
2.  Print the **Mean Absolute Error (MAE)** and **R-squared ($R^2$)** score.
3.  Display a scatter plot showing the relationship between the actual and predicted house prices.

---

## 📊 Results

The model's performance is evaluated using two key metrics:
* **Mean Absolute Error (MAE):** This represents the average absolute difference between the actual and predicted prices. A lower value is better.
* **R-squared ($R^2$):** This metric indicates the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1, with a higher value indicating a better fit.

The output will also include a visualization:

https://github.com/Shreejita-Biswas/prodigy_task_1/blob/main/Output.png
*(You can replace this with a screenshot of your actual plot)*

This plot helps visually assess the model's accuracy. The closer the points are to the red dashed line, the more accurate the predictions.
