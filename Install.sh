gcc -o start start.c
gcc -o stop stop.c
sudo chmod +x start
sudo chmod +x stop
sudo chown root start
sudo chown root stop
sudo chmod +s start
sudo chmod +s stop
