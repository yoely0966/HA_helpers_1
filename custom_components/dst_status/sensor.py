from datetime import datetime
import pytz
from homeassistant.components.sensor import SensorEntity

DEFAULT_NAME = "DST Status"

def is_dst():
    now = datetime.now()
    timezone = pytz.timezone("America/New_York")  # Replace with your desired timezone
    return bool(timezone.localize(now).dst())

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([DSTSensor()])

class DSTSensor(SensorEntity):
    def __init__(self):
        self._state = None
        self._name = DEFAULT_NAME

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        self._state = "Yes" if is_dst() else "No"
