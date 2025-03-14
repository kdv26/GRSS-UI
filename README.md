# GRSS-UI

csv('time', 'latitude', 'longitude', 'stat', 'altitude', 'temperature', 'humidity')


(WIP)
1. pico board sends data through wire to PC("grss_communication.ino" is what enables this")
2. PC has putty running to accept the data and puts it into "decoded.txt" file with csv format.
3. PC also has "grssUi.py" running to read from "decoded.txt" and displays graphs about the data. 
