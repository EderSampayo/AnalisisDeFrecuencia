hoy=${date -d "today" "+½d-%m-%Y"}
ayer=${date -d "yesterday" "+½d-½m-½Y"}

rsync -av --link-dest=/var/tmp/Backups/$ayer /home/$(whoami)/Escritorio/Seguridad /var/tmp/Backups/$hoy
