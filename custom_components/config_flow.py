from homeassistant import config_entries
from homeassistant.core import callback
from . import DOMAIN

class DSTStatusConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for DST Status."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="DST Status", data={})

        return self.async_show_form(step_id="user")
