# h1_zones.py

def is_impulsive(candle_range, atr_h1):
    return candle_range >= 1.5 * atr_h1


def build_zone(origin_candle):
    return {
        "zone_high": origin_candle["high"],
        "zone_low": origin_candle["low"]
    }
