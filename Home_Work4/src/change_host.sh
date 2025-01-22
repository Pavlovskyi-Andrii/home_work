#!/bin/bash
echo "ubuntu22" | sudo tee /etc/hostname
sudo hostnamectl set-hostname ubuntu22
#отримати назу хоста
izmen_host_name=$(hostname)


echo "Hostname changed to ubuntu22 name: $izmen_host_name "




