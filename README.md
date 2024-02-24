# Pico relay

The program is used to turn on the light, e.g. in a corridor, where it is required to turn it off automatically after a certain time

# Wiring diagram
![switch_schema](https://github.com/krupakrzysztof/PicoSwitch/assets/87368964/1e63da84-fe58-40ab-8cb5-99ab94190783)

Pins 1-3 and 2-38 are used to connect buttons.
Pin 40 outputs voltage to the relay, 23 is relay ground, and 21 (GPIO 16) is used to change its state.
