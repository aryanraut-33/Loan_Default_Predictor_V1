# Loan Default Prediction Project

> **Goal:** To predict if a certain loan application will default using a dataset from The Lending Club, a peer-to-peer lending platform.

## Dataset Overview

- **Source:** The Lending Club (P2P lending platform)
- **Size:** 2.2 million rows with over 150 features
- **Type:** Industry-grade financial dataset

## Project Steps

### 1. Data Preprocessing & Feature Selection

- Reduced dataset from 151 to 24 features based on domain understanding
- Eliminated features causing data leakage (post-loan period information)
- Applied financial domain knowledge to identify relevant metrics
- Handled missing data through dropping and median imputation techniques

### 2. Feature Engineering

Created new meaningful features to improve model performance:

- **credit_history_length:** Days between issue date and earliest credit line
- **is_joint_application:** Binary flag for joint applications
- **loan_to_income_ratio:** Loan amount divided by annual income
- **calculated_installment:** Theoretical monthly payment
- **installment_to_income_ratio:** Monthly payment as fraction of income
- **open_to_total_acc_ratio:** Open vs total credit lines ratio
- **total_utilization:** Current balance vs credit limit
- **revolving_balance_fraction:** Revolving balance proportion
- **has_mortgage:** Binary flag for mortgage accounts
- **dti_x_delinq:** DTI ratio × delinquencies interaction
- **fico_x_int_rate:** FICO score × interest rate interaction

### 3. Exploratory Data Analysis (EDA)

- Loan amount distribution analysis
- Default rate by loan grade
- Default rate by home ownership status
- FICO score vs DTI score relationships
- State-wise default rate visualization using choropleth maps

### 4. Model Training & Evaluation

- Train/dev/test split based on application year (time-based splitting)
- Standard scaling for numerical features
- One-hot encoding for categorical variables
- Baseline model: Logistic Regression
- **Results:** AUC score of 0.72 (above average performance)

## Key Learnings

- Gained experience handling large-scale datasets (2.2M+ rows)
- Developed skills in data preprocessing and feature engineering
- Acquired domain knowledge in financial metrics (DTI, FICO, interest rates)
- Learned to identify and prevent data leakage in time-series problems
- Demonstrated that proper preprocessing can significantly improve model performance

## Learning Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/) - For data manipulation and analysis
- [TensorFlow Documentation](https://www.tensorflow.org/guide) - For machine learning frameworks

---

**Note:** This project focused primarily on data preprocessing and feature engineering rather than complex ML algorithms, demonstrating that quality data preparation is often more impactful than sophisticated models.
