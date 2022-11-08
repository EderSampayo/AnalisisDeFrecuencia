#!/bin/bash
hoy=$(date +%F)
ayer=$(date -d "yesterday" +%F)

mkdir /var/tmp/Backups2/$hoy

rsync -av --link-dest=/var/tmp/Backups/$ayer /home/$(whoami)/Escritorio/Seguridad/ /var/tmp/Backups2/$hoy
