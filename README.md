# 3r-m2

_Shiny Applcation_ in python.

## Goal

<div style="text-align: justify">

Develop an application to simulate a portfolio value attrition over time depending on several customers caracteristics:

- .. (IN PROGRESS),

## Documentation

We have a `shiny` application that we call with:

```shell
shiny run --reload app.py
```

The purpose of the application is to offer the user a way to see the portfolio value evolution in direct according to customers caracteristics, revenue, cost and discount rate.

The user can, if he wishes, look at the train database containing all the customers caracteristics including lifetime and churn by scrolling the application.

The application steps are:

- To run a model based on Weibull or Log-Normal or Log-Logistic law:
     - This model predict the customer survival function into the portfolio.
- Restore the portfolio value attrition over time in an interactive figure:
     - Two traces because of two portfolio value functions (Jain and Singh in 2002 and Gupta and Lehman in 2004).

### Example:

```shell
shiny run --reload app.py
```

![..](..)

</div>