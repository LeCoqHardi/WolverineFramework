#!/bin/bash

echo "What do you want to do ? 1 = Custom MAC Address // 2 = Random MAC Address"
read -p "WolverineFramework - Answer> " ReponseII
echo "What is the name of your network interface ?"
read -p "WolverineFramework - Network Interface> "NetworkInterface
if [ $ReponseII = 1	]
then
	echo "Type your MAC Address ? (??:??:??:??:??:??)"
	read -p "WolverineFramework - MAC Address> " MacAdress
	sudo ifconfig $NetworkInterface down
	sudo macchanger -m $MacAdress $NetworkInterface
	sudo ifconfig $NetworkInterface up
	sudo macchanger -s $NetworkInterface
elif [ $ReponseII = 2 ]
then
	sudo ifconfig $NetworkInterface down
	sudo macchanger -r $NetworkInterface
	sudo ifconfig $NetworkInterface up
	sudo macchanger -s $NetworkInterface
fi

