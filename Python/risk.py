# risk.py
import config


def calculate_sl_tp(entry, atr_m15, direction):
    sl_distance = atr_m15 * config.ATR_SL_MULTIPLIER
    tp_distance = sl_distance * config.RR_MIN

    if direction == "BUY":
        sl = entry - sl_distance
        tp = entry + tp_distance
    else:
        sl = entry + sl_distance
        tp = entry - tp_distance

    return sl, tp
