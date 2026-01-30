# trend_d1.py

def detect_d1_trend(swings):
    """
    swings = list of dicts:
    [
      {"high": 2050, "low": 2020},
      ...
    ]
    """

    if len(swings) < 3:
        return "NO_TREND"

    h1 = swings[-1]["high"]
    h2 = swings[-2]["high"]

    l1 = swings[-1]["low"]
    l2 = swings[-2]["low"]

    if h1 > h2 and l1 > l2:
        return "BUY"

    if h1 < h2 and l1 < l2:
        return "SELL"

    return "NO_TREND"
