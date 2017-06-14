# telegram-bot-ssh
Bot de Telegram para levantar y detener el servicio sshd en sistemas con Systemd

Para instalarlo:
	1 - Clonar el repositorio
	2 - Ejecutar el instalador Install.sh
	3 - Modificar el fichero bot.py añadiendo el token de tu bot
	4 - En bot.py introducir el id de chat del que se va a poder recibir 
		ordenes o borrar esa condicion del if

Como funciones extra toma la lectura de la temperatura devuelta por el comando
sensors, y muestra el estado del servicio SSH. Se podría ampliar para ejecutar
cualquier script de administración o similar.
