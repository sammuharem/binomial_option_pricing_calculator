# Binomial Option Pricing Calculator #
Option Pricing Calculator using the Binomial Pricing Method (No Libraries Required)

## Background ##
A derivative is a financial instrument that derives its value from the price of an underlying asset. An option gives the owner the ability to buy or sell the underlying asset at pre-determined price. An option that allows the holder to buy the asset at the pre-determined price (also known as the exercise or strike price) is called a call option. An option that lets the owner sell the underlying asset at the strike price is called a put option.
There are three key types of options, a European option allows the holder to exercise ('redeem') the option only at maturity of the option. An American option can be exercised any time before maturity. A Bermudan option is exercisable at pre-deteremined dates decided at the creation of the option.

The binomial pricing method is one of the three most common methods used to value options - the others being the Black-Scholes model and a Monte Carlo simulation.
The method predicts the price of the underlying asset at intervals (branches) between now and maturity of the option contract. This creates a tree showing the price movements of the asset, which can be used to find the fair value of the option.
Unlike Black-Scholes, the binomial method allows the intrinsic value of the option to be calculated prior to maturity, better representing the value of American and Bermudan options which have the option of early exercise.

## Pricing options using this method is done by: ##
  1. Determining the magnitude that stock prices will rise or fall between each branch.
  2. Calculating the probability that the stock price will move upwards or downward.
  3. Forming the binomial stock price tree with the specified number of branches.
  4. Calculate the payoff of the option at maturity.
  5. Working backwards, value the option by discounting the value of the option at the following nodes using. If the option is American or Bermudan and exercisible at that branch, then the value of the option if it was exercised is calculated, if it is greater than the discoutned value, it becomes the calculated value of the branch.
  6. The value derived at the top of the tree is the fair value of the option today.

## Features of the Script ##
* Does not require any libraries - it will work in base python3 and immune to changes in libraries
* Option type is specified as a parameter allowing easy implementations 
* Returns and displays the calculated stock tree 

The following assumptions are made by the model:
* No dividends are paid across the option's life 
* Risk-Free rate is constant across the option's life
* The price will move up or down each period

## Variables and Paramaters ##
The variables required are:
Name | Symbol | Description
| :--- | :--: | :----
Stock Price | s | The current price of the underlying asset (time 0)
Exercise Price | x | The strike price of the option contract
Time to Maturity | t | The time until maturity of the option contract (in years)
Risk-Free Rate | r | The current risk-free rate
Branches/Steps | b | The number of branches used to value the option  
Volatility | v | The volatility of the price movements in the underlying asset

Optional variables are:
Name | Symbol | Description
| :--- | :--: | :----
Option Nationality | nat | 'A' for American (default), 'B' for Bermudan, 'E' for European
Option Type | typ | 'C' for Call (default), 'P' for Put
Print Results |prnt| True to enable printing (default), False to disable
Exercisible Periods |exP | The branches that a Bermudan option can be exercised
