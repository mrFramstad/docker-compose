docker run -it --rm -v /Users/fichfram/docker-compose/Home-AssistantConfig:/config -e "TZ=Europe/Oslo" homeassistant/home-assistant python -m homeassistant --config /config --script check_config

