from typing import List


def maxProfit(prices: List[int]) -> int:
    """Finds the best time to buy and sell stock

    Parameters
    ----------
    prices : List[int]
        Prices of stock by day

    Returns
    -------
    int
        The maximum profit that can be achieved

    """
    return sum([max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices))])
