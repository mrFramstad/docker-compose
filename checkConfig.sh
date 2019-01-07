docker run -it --rm -v /home/stoffer/smartHome/docker-compose/Home-AssistantConfig:/config -v /etc/letsencrypt:/etc/letsencrypt -e "TZ=Europe/Oslo" homeassistant/home-assistant python -m homeassistant --config /config --script check_config

