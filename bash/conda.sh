#!/bin/bash
#Turn on or Turn off Conda init

echo "¿Desea activar o desactivar Conda?"
read -p "(s/n): " orden

if [[ $orden = s ]]; then
	conda config --set auto_activate_base True
	echo "Activado"
elif [[ $orden = n ]]; then
	conda config --set auto_activate_base False
	echo "Desactivado"
else
	echo "ud no aprende, ¿verdad?"
fi
