# main.py

from validator import validate_all

def generate_signal(rules, signal_data):
    if not validate_all(rules):
        return "NO SIGNAL"

    return f"""
XAUUSD {signal_data['direction']}
TF: M15
Entry: {signal_data['entry']}
Stop Loss: {signal_data['sl']}
Take Profit: {signal_data['tp']}
Reason: Zone + CHoCH + Candle
"""


# EXAMPLE (MANUAL INPUT FOR NOW)
rules = {
    "trend_ok": True,
    "zone_ok": True,
    "discount_ok": True,
    "session_ok": True,
    "choch_ok": True,
    "candle_ok": True,
    "rr_ok": True
}

signal_data = {
    "direction": "BUY",
    "entry": 2034.50,
    "sl": 2030.00,
    "tp": 2043.50
}

print(generate_signal(rules, signal_data))
