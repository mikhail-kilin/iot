import RPi.GPIO as IO
import time

status = 0
red = 40
green = 38
blue = 36

button = 8

IO.cleanup()
IO.setmode (IO.BOARD)
IO.setup(red,IO.OUT)
IO.setup(green,IO.OUT)
IO.setup(blue,IO.OUT)
IO.setup(button,IO.IN) 

while True:
	IO.output(red,IO.LOW)
	IO.output(green,IO.LOW)
	IO.output(blue,IO.LOW)
	if status == 0:
		IO.output(red,IO.HIGH)
	if status == 1:
		IO.output(blue,IO.HIGH)
	if status == 2:
		IO.output(green,IO.HIGH)
	if IO.input(button) == False:
		status = (status + 1) % 3
	time.sleep(0.1)
