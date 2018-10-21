#Moduł motor - obsługa napędów robota
import RPi.GPIO as GPIO
import time

#PINOUT
#Piny prędkości
left_speed_pin = 12
right_speed_pin = 13
#Piny kierunku
left_dir_1_pin = 19
left_dir_2_pin = 16
right_dir_1_pin = 26
right_dir_2_pin = 20

def init():
	#Funkcja inicjująca działanie pozostałych funkcji. Wymagana do uruchomienia!
	GPIO.setmode(GPIO.BCM) 
	GPIO.setwarnings(False)
	GPIO.setup(left_speed_pin, GPIO.OUT)
	GPIO.setup(right_speed_pin, GPIO.OUT)
	left_side = GPIO.PWM(left_speed_pin,100) #instancja PWM na pinie 12 z częstotliwością 100Hz
	right_side = GPIO.PWM(right_speed_pin,100)
	left_speed = 0 #predkosc lewej strony robota 
	right_speed = 0 #predkosc prawej strony robota
	left_side.start(left_speed) #start generowania pwm na silniki. Predkosc poczatkowa 0, oczekuje.
	right_speed.start(right_speed)
	
	GPIO.setup(left_dir_1_pin, GPIO.OUT) #piny kierunku jazdy LOW,LOW - stoi w miejscu, HIGH LOW do przodu, LOW HIGH do tyłu
	GPIO.setup(left_dir_2_pin, GPIO.OUT)
	GPIO.setup(right_dir_1_pin, GPIO.OUT)
	GPIO.setup(right_dir_2_pin, GPIO.OUT)
	
	nowSpeed = 0