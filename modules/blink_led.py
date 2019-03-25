from gpiozero import MCP3008, PWMLED

pot = MCP3008(0)
pot2 = MCP3008(1)
led = PWMLED(21)

while True:
    print(pot.value, pot2.value)
    led.blink(on_time=pot.value, off_time=pot2.value, n=1, background=False)
