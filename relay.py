# to start program automatically after turning on controller file must have name "main.py"
from machine import Pin
import time
import utime
import _thread

# a program used to turn on the diode after pressing the button on GPIO1 or GPIO2 and connected to the device for a specific time

# GPIO pin 16
led = Pin(16, Pin.OUT)
button = Pin(0, Pin.IN, Pin.PULL_UP)
button2 = Pin(1, Pin.IN, Pin.PULL_UP)
last_time = 0
enabledTime = 5 # time in seconds

led.value(1)
ledState = led.value()

def setLed():
    global led
    global ledState
    ledState = not ledState
    print('zmiana led na ' + str(ledState))
    led.toggle()

def disableLed():
    global ledState
    global led
    global enabledTime
    while True:
        if not ledState:
            for i in range(enabledTime * 10):
                time.sleep(0.1)
                if ledState:
                    break
            if not ledState:
                ledState = True
                led.value(1)
        time.sleep(0.1)

# a method launched after clicking a button, records the time of the last click so that it is known when a new event occurred
def my_handler(button):
    global last_time
    new_time = utime.ticks_ms()
    if (new_time - last_time) > 200:
        setLed()
        last_time = new_time

# starting listening on button 1 for state changes 0->1 and 1->0
def startButton1():
    button.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = my_handler)

# starting listening on button 2 for state changes 0->1 and 1->0
def startButton2():
    button2.irq(trigger = Pin.IRQ_FALLING | Pin.IRQ_RISING, handler = my_handler)

# starting a new thread listening for the LED to turn on and off
_thread.start_new_thread(disableLed, ())
startButton1()
startButton2()

# the main thread of the program, it may get boring ;)
while True:
    time.sleep(10)
