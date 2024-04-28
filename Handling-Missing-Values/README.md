# Handling Missing Values 💼

## Complete Case Analysis 📊
- [Handling Missing Data](https://github.com/Sami606713/100_Days_Of_Machine_Learning/blob/main/Handling-Missing-Values/CompleteCaseAnalysis(CCA).ipynb)

Complete Case Analysis (CCA) involves removing all rows that contain missing values from a dataset.

- In Complete Case Analysis, we can remove all rows that contain missing values.

- CCA is applicable when we are confident that missing data is completely at random (MCAR).

- Generally, we can remove values if they are missing less than 5%. ✅

## Remember Before Applying CCA 🧠

Before removing and after removing, the distribution of data should be the same or almost the same.

## Handling Numeric Data 📊
- [Handling Numeric Data](https://github.com/Sami606713/100_Days_Of_Machine_Learning/blob/main/Handling-Missing-Values/Handling_Missing_Values(num-data).ipynb)

# Simple Imputer

## Introduction

The Simple Imputer is a technique used to handle missing data by filling in the missing values with specific statistics. It is particularly useful when working with datasets that have missing values in some of their features.

## Strategies

The Simple Imputer provides several strategies to fill in the missing values:

1. **Mean**: This strategy computes the mean of the non-missing values in the feature and replaces the missing values with this mean. It is suitable for features with a normally distributed data.
   
2. **Median**: This strategy computes the median of the non-missing values in the feature and replaces the missing values with this median. It is suitable for features with skewed data distributions.

3. **Arbitrary Values**: Apart from mean and median, you can also choose to fill missing values with arbitrary values, such as zero, a specific constant, or any other value deemed appropriate for the dataset.

## Usage

To use the Simple Imputer, follow these steps:

1. Initialize the Simple Imputer object with the desired strategy.
2. Fit the imputer to your training data using the `fit` method.
3. Transform your training data using the `transform` method to fill in the missing values based on the strategy learned from the training data.
4. Optionally, you can also use the `fit_transform` method to perform both fitting and transforming in a single step.
5. For test or validation data, use the `transform` method to fill in missing values based on the learned strategy from the training data.


## Handling Numeric Data 📊
- [Random Value Imputition](https://github.com/Sami606713/100_Days_Of_Machine_Learning/blob/main/Handling-Missing-Values/RandomValueImputition.ipynb)


# Iterative Imputer
- [Iterative Imputer](https://github.com/Sami606713/100_Days_Of_Machine_Learning/blob/main/Handling-Missing-Values/missing-indicator.ipynb)
  
## Overview
Iterative Imputer is a technique used to fill missing values in a dataset by considering multiple columns simultaneously. It falls under the category of multiclass imputation methods.

## Working
1. **Initial Imputation:** Missing values are filled initially using a simple method such as mean imputation.
2. **Conversion to Missing Values:** The filled values are then converted back to missing values.
3. **Model Building:** A predictive model is built to estimate the missing values. Here, the column with missing data serves as the target variable, while the other columns act as features.
4. **Iteration:** The difference between predicted values and the mean value of the entire column is calculated. The process of prediction and difference calculation continues iteratively until the difference becomes negligible (close to zero).

## Advantage
- **Accuracy:** It is considered one of the most accurate methods for imputation.

## Disadvantage
- **Computational Cost:** It can be computationally expensive and slow, especially for large datasets.

