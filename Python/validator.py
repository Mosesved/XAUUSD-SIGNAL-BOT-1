# validator.py

def validate_all(rules: dict):
    """
    rules = {
      "trend_ok": True,
      "zone_ok": True,
      "discount_ok": True,
      "session_ok": True,
      "choch_ok": True,
      "candle_ok": True,
      "rr_ok": True
    }
    """

    for name, passed in rules.items():
        if not passed:
            print(f"RULE FAILED: {name}")
            return False

    return True
