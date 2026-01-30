# candles.py

def is_bullish_engulfing(prev, curr):
    return curr["close"] > curr["open"] and curr["close"] > prev["open"]


def is_bearish_engulfing(prev, curr):
    return curr["close"] < curr["open"] and curr["close"] < prev["open"]


def is_pinbar(candle):
    body = abs(candle["close"] - candle["open"])
    wick = candle["high"] - candle["low"]
    return wick > body * 2


def is_strong_close(candle):
    return abs(candle["close"] - candle["open"]) > (candle["high"] - candle["low"]) * 0.6
