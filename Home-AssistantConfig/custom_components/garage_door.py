import homeassistant.loader as loader

# The domain of your component. Should be equal to the name of your component.
DOMAIN = 'garage_door'

# List of component names (string) your component depends upon.
DEPENDENCIES = ['mqtt']
 
CONF_STATUS_TOPIC = 'status_topic'
CONF_TRIGGER_TOPIC = 'trigger_topic'
DEFAULT_STATUS_TOPIC = '/connectedGarageDoor/status'

def setup(hass, config):
    #Set up the Hello MQTT component.
    mqtt = hass.components.mqtt
    status_topic = config[DOMAIN].get(CONF_STATUS_TOPIC, DEFAULT_STATUS_TOPIC)
    entity_id = 'garage_door.last_message'

    # Listener to be called when we receive a message.
    def message_received(topic, payload, qos):
        #Handle new MQTT messages.
        hass.states.set(entity_id, payload)

    # Subscribe our listener to a topic.
    mqtt.subscribe(status_topic, message_received)

    # Set the initial state.
    hass.states.set(entity_id, 'Ukjent status')  

    # Return boolean to indicate that initialization was successfully.
    return True