# 9. Optimal Strategy for Elevating Status from Regular User to VIP-9 on Binance for Algorithmic Trading Company

## Table of Contents  
1. Project Overview
2. Problem Statement
3. Brief Data Information
4. Project Workflow Stages
5. Results  
6. Conclusions

### Project Overview    
  
The essence of the case is to develop an optimal strategy for elevating status from a regular user to VIP-9 on Binance for an algorithmic trading company, focusing on Spot trading.

### Problem Statement    
Initially, we attempt to extract information from the Binance website regarding VIP statuses, calculate the optimal growth path, considering fees among other factors.

### Brief Data Information
Data on VIP statuses is obtained from the official Binance website: https://www.binance.com/en/fee/trading

### Project Workflow Stages  

1. Data extraction from the URL
2. Data transformation
3. Search for the optimal combination to raise Maker's status  
    3.1. Pool of status combinations  
    3.2. Maximum volume  
    3.3. Calculation mechanics
4. Calculation of the optimal strategy for elevating Taker's status

### Results:  

We found that using only the Maker strategy, the optimal status escalation sequence will be: 0, 1, 3, 5, 7, 9. The minimum fee paid to the exchange will be $163,060,000, which is 2.18% of the total invested amount. After reaching status 9, the fee will already be minimal, and the average rate will decrease. Certainly, the fee calculation is simplified and does not consider other factors such as trading volume, transaction frequency, and market dynamics. We also do not include the expected return from the asset and the fact that the longer we go to status 9, the more alternative investments we will lose. However, this approach allowed us to mathematically calculate the most profitable way to increase the level for the Maker strategy.

For Taker, the optimal strategy would be to skip 1 level, i.e., 0, 3, 5, 7, 9 (probably because VIP-0 and VIP-1 have the same commission rate for Taker). The total commission paid to the exchange will be 3.39%, which is generally expected to be higher than for Maker because Taker operations reduce liquidity. Similarly, this function can be used for USD or futures.

### Conclusions:  
We have developed a universal algorithm for elevating VIP status from a regular user to VIP-9 with minimal losses in fees. We have also confirmed that this scheme will differ for different strategies and commissions. In the future, using the same function, more complex strategies can be calculated, such as different combinations of Maker-Taker, or using commissions for other markets. The task will be to correctly calculate the expected return and adjust the rates column for calculations.