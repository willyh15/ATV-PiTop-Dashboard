import RPi.GPIO as GPIO
import time

# Define GPIO pins
START_PIN = 18  # Pin to control the starter solenoid

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(START_PIN, GPIO.OUT)

def crank_engine():
    GPIO.output(START_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(START_PIN, GPIO.LOW)

if __name__ == '__main__':
    crank_engine()
    GPIO.cleanup()
