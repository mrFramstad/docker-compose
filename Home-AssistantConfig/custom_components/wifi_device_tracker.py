import homeassistant.loader as loader

# The domain of your component. Should be equal to the name of your component.
DOMAIN = 'wifi_device_tracker'

def setup(hass, config):
    
    # Service to publish a message on MQTT.
    def set_connected(call):
        hass.states.set(call.data.get('entity_id'), 'home')  

    # Service to publish a message on MQTT.
    def set_disconnected(call):
        hass.states.set(call.data.get('entity_id'), 'away')  

    # Register our service with Home Assistant.
    hass.services.register(DOMAIN, 'device_connected', set_connected)
    hass.services.register(DOMAIN, 'device_disconnected', set_disconnected)

    # Return boolean to indicate that initialization was successfully.
    return True