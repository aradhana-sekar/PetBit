from adafruit_circuitplayground import cp
import time
steps = 0
dailytarget = 10000
dayssinceepoch = int(time.time()/86400)
display = True
light = True
while True:
    if cp.switch == True:
        display = False
    else:
        display = True
    if cp.touch_A1:
        dailytarget = 5000
    if cp.touch_A2:
        dailytarget = 10000
    if cp.touch_A3:
        dailytarget = 15000
    if cp.touch_A4:
        dailytarget = 20000
    if cp.touch_A5:
        dailytarget = 25000
    if cp.touch_A6:
        dailytarget = 30000
    if cp.shake(10):
        steps = steps + 1
    values = [(0,0,0)]*10
    stepprogressled = steps % 10
    if steps < dailytarget:
        for i in range (0, steps*10/dailytarget):
            values[i] = (30, 0, 0)
    values[stepprogressled] = (0, 0, 30)
    if cp.light < 6 and light == True:
        for i in range(0, 10):
            values[i] = (1, 1, 1)
    if cp.button_a:
        if light == True:
            light = False
        else:
            light = True
    if display == False:
        values = [(0,0,0)]*10
    currentdayssinceepoch = int(time.time()/86400)
    if currentdayssinceepoch > dayssinceepoch:
        steps = 0
        dayssinceepoch = currentdayssinceepoch
    if steps == dailytarget:
        cp.start_tone(1000)
        time.sleep(0.5)
        cp.stop_tone()
    if steps >= dailytarget:
        for i in range (0, 10):
            values[i] = (0, 15, 0)
        stepprogressled = steps % 10
        values[stepprogressled] = (0, 255, 0)
    for i in range (0, 10):
        cp.pixels[i] = values[i]