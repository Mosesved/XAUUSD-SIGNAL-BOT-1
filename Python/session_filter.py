# session_filter.py
from datetime import datetime
import config


def is_valid_session():
    hour = datetime.now().hour

    in_london = config.LONDON_START <= hour <= config.LONDON_END
    in_ny = config.NY_START <= hour <= config.NY_END

    return in_london or in_ny
