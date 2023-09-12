# 3r-m2

```bash
.
├── contractual
│   ├── core
│   │   └── graphic.py
│   │   └── portfolio.py
│   ├── data
│   │   └── __init__.py
│   │   └── data.py
│   │   └── df.csv
│   │   └── dfbis.csv
│   │   └── saved_model.sav
│   └── tools
│       └── graphic_tools.py
│       └── help.py
│       └── portfolio_tools.py
└── no-contractual
└── requirements.txt
```

_Poetry project_.

```diff
+ WORK IS DONE.

Every subtabs and every tabs work well.

! COMMENT IN PROGRESS...

Code needs to be commented.
```


_Shiny Applcation_ in python.

## Goal

<div style="text-align: justify">

Develop an [application](https://alexisvte.shinyapps.io/contractual-portfolio-value-app/?_ga=2.149677491.462710402.1681053594-1612834766.1681053594) to simulate a portfolio value attrition over time depending on several customers caracteristics:

- personal (customer),
- economical (contract),
- technical (depending on contract).

## Documentation

We have a `shiny` application that we call by typing:

```shell
shiny run --reload app.py
```

The purpose of the application is to offer the user a way to see the portfolio value evolution in direct according to customers caracteristics, revenue, cost and discount rate.

The user can, if he wishes, look at the train database containing all the customers caracteristics including lifetime and churn by scrolling the application.

The application steps are:

- To run a model based on Weibull or Log-Normal or Log-Logistic law:
     - This model predict the customer survival function into the portfolio.
- Restore the portfolio value attrition over time in an interactive figure:
     - Two traces because of two portfolio value functions based on:
          - Jain and Singh of 2002,
          - Gupta and Lehman of 2004.

### Result:

![Shiny for python application.](https://user-images.githubusercontent.com/82931295/230781253-2577d6d5-fef8-4205-a9b8-9590b02ccde3.png)

</div>
