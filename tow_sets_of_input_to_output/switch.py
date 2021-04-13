import machine
import utime

#DIFINE FISRT SIX-SET OF INPUT WITH PULL_UP CONFIGURATION
#WHAT IS PULL-UP :- https://eepower.com/resistor-guide/resistor-applications/pull-up-resistor-pull-down-resistor/#
#WE USE GPIO 0,1,2,3,4,5 FOR FIRST SET OF INPUT
A0 = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)
A1 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
A2 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)
A3 = machine.Pin(3, machine.Pin.IN, machine.Pin.PULL_UP)
A4 = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)
A5 = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_UP)

#DIFINE SECOND SIX-SET OF INPUT WITH PULL_UP CONFIGURATION
#WE USE GPIO 6,7,8,9,10,11 FOR SECOND SET OF INPUT
B0 = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
B1 = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)
B2 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_UP)
B3 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_UP)
B4 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_UP)
B5 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_UP)

#DIFINE SIX-SET OF OUTPUT
#WE USE GPIO 16,17,18,19,20,21 FOR OUTPUT
C0 = machine.Pin(16,machine.Pin.OUT)
C1 = machine.Pin(17,machine.Pin.OUT)
C2 = machine.Pin(18,machine.Pin.OUT)
C3 = machine.Pin(19,machine.Pin.OUT)
C4 = machine.Pin(20,machine.Pin.OUT)
C5 = machine.Pin(21,machine.Pin.OUT)

#DIFINE SELECT PIN
#SELECT PIN IS PULL_UP WITH R1.
SEL = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

#CREAT WHILE LOOP WITH CONDITION TRUE WHITCH MEAN IT WILL LOOP AGAIN 
#AND AGAIN UNTILL CONDITION IS FALSE
while True:
	#NOW WE CREAT AND IF LOOP THAT CHECK THE VALUE OF SELECT PIN AND TOGGLE BETWEEN 
	#THE TOW SET OF SIX INPUT WE MADE. 
	if SEL.value:
		C0.value = A0.value
		C1.value = A1.value
		C2.value = A2.value
		C3.value = A3.value
		C4.value = A4.value
		C5.value = A5.value
	else:
		C0.value = A0.value
		C1.value = A1.value
		C2.value = A2.value
		C3.value = A3.value
		C4.value = A4.value
		C5.value = A5.value
	#WE ADD 0.02SEC OF DELAY
	utime.sleep(0.02)
