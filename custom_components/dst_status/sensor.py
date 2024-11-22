from datetime import datetime
from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "dst_status"

SENSORS = {
    "date": "%B %d, %Y",
    "date_numbers": "%x",
    "time": "%-I:%M %p",
    "date_time": "%B %d, %Y - %-I:%M %p",
    "week_day_long": "%A",
    "week_day_short": "%a",
    "week_and_date": "%a, %B %d, %Y",
}


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up DST Status sensors."""
    sensors = [DateTimeSensor(name, fmt) for name, fmt in SENSORS.items()]
    async_add_entities(sensors, update_before_add=True)


class DateTimeSensor(SensorEntity):
    """Representation of a DateTime sensor."""

    def __init__(self, name, fmt):
        self._name = name.replace("_", " ").title()
        self._fmt = fmt
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        """Update the sensor state."""
        self._state = datetime.now().strftime(self._fmt)
