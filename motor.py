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
	global initialized
	if initialized:
		return

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

	initialized = True

def direction(lewa_kierunek, prawa_kierunek):
	#Kierunek: 1 - do przodu, 0 - do tyłu
	if lewa_kierunek == 1:
		GPIO.output(left_dir_1_pin, GPIO.HIGH)
		GPIO.output(left_dir_1_pin, GPIO.LOW)
	if lewa_kierunek == 0:
		GPIO.output(left_dir_1_pin, GPIO.LOW)
		GPIO.output(left_dir_2_pin, GPIO.HIGH)
	if prawa_kierunek == 1:
		GPIO.output(right_dir_1_pin, GPIO.HIGH)
		GPIO.output(right_dir_2_pin, GPIO.LOW)
	if prawa_kierunek == 0:
		GPIO.output(right_dir_1_pin, GPIO.LOW)
		GPIO.output(right_dir_2_pin, GPIO.HIGH)
		
	
def drive(predkosc, kierunek):
	#predkosc zakres: 0-100. Kierunek: 1 - do przodu, 0 - do tyłu
	#ustawienie odpowiednich kierunków
	if kierunek == 1:
		direction(1, 1)
	if kierunek == 0:
		direction(0, 0)
	#wysterowanie prędkosc - z narastaniem
	speed_change = predkosc - nowSpeed
	speed_change_step = 1 #dodatki skok prędkosci jesli robot przyśpiesza
	if speed_change < 0:
		#Przy rozpędzaniu robota ta różnica jest dodatnia, ale przy hamowaniu już jest ujemna, więc dla pętli trzeba ją zrobić na plus. To samo ze skokiem prędkości
		speed_change = speed_change * (-1)
		speed_change_step = -1
	for x in range(x, speed_change, 1):
		nowSpeed = nowSpeed + speed_change_step #obliczenie aktualnej prędkości
		left_side.ChangeDutyCycle(nowSpeed)
		right_side.ChangeDutyCycle(nowSpeed)
		time.sleep(.2) #delay między następnym skokiem prędkośći 2 ms.
		#witam
		
		
