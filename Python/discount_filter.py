# discount_filter.py

def is_in_discount_or_premium(direction, swing_high, swing_low, price):
    midpoint = (swing_high + swing_low) / 2

    if direction == "BUY":
        return price < midpoint

    if direction == "SELL":
        return price > midpoint

    return False
