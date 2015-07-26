#Code B Algorithmic Stock Trading Hackathon

###trader.py
`trader.py` is the main trader file. The general algorithm works as follows:

Step 1:
Exploration phase. The goal here is to empirically measure the dividend rate, because actually estimating it was complicated. To measure this, buy one share of one stock, and hold for 5 seconds. Observe the difference in cash, all due to dividends. Repeat for each stock.

Step 2:
Compare the dividend rate with a threshold value, and determine if the market has high or low dividend ratio parameters. If high, go to Step 3, else go to Step 4.

Step 3:
Select the n stocks which give the highest dividends (n was hardcoded to 4). Buy as many as possible of one stock, and cycle through them all. The goal here is to capitalize on the dividends.

Step 4:
This a low dividend scenario, so the goal is to apply classic stock trading strategies, which is to buy low and sell high. Details are known only by Jun (noonelah).

###sampler.py
`sampler.py` contains some functions that were used to collect data in a csv format for analysis in a spreadsheet.

###helper.py
`helper.py` contains helper functions as well as some API abstractions.

###clientpy2.py
`clientpy2.py` was the base file provided to us. It was modified to allow for multiple commands per requests, instead of creating and terminating a TCP connection for each command. Note that a maximum of three connections were allowed per simulation, and the connection has to be terminated by the client.

###ai.py
`ai.py` was a last-minute (last 3.5 hours) attempt at using an AI approach to the problem, after observing that our solution didn't perform too well compared to others. Input parameters were essentially thrown at perceptrons to see if they would stick. There is one perceptron per stock. A binary course of action is determined for each stock (buy as many as possible or sell as many as possible.) Since there are t stocks, there are t perceptrons and t decisions made. One stock is chosen at random and the decision is applied.

While computing the next set of actions (takes a second or so), the "success" of the last decision is measured. As a primitive measurement of success, the amount of dividends earned in the last period (~4 secs) was used. Whether a decision was successful is determined by comparing the dividends earned to a threshold. The perceptron weights are trained according to an update function and the success/failure value.

There are many issues with this model. Many details of the algorithm were hacked on the spot instead of being planned ahead. One such example is the random selection of a stock. Additionally, I suspect that a single perceptron is insufficient to model the performance of a stock. A more complex neural network would be preferred.
