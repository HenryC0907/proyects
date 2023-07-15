#!/bin/bash
#Turn on or turn off Bluetooth in case the interface don't work

echo "Bienvenido a Bluetooth. ¿Quiere encender o apagar?"
read -p "(s/n): " orden

if [[ $orden = s ]]; then
	/etc/init.d/bluetooth start
	echo "Bluetooth encendido"
elif [[ $orden = n ]]; then
	/etc/init.d/bluetooth stop
	echo "Bluetooth apagado"
else
	echo "¡No sea mk, escriba bien!"
fi
