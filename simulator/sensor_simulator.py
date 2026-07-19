import random
import time

print("MotorSense AI Simulator Started...\n")

while True:

    status = random.choice(["Healthy", "Warning", "Critical"])

    if status == "Healthy":
        temperature = random.uniform(35, 45)
        current = random.uniform(2.8, 3.5)
        vibration = random.uniform(0.10, 0.30)

    elif status == "Warning":
        temperature = random.uniform(46, 60)
        current = random.uniform(3.6, 4.5)
        vibration = random.uniform(0.31, 0.80)

    else:
        temperature = random.uniform(61, 80)
        current = random.uniform(4.6, 6.0)
        vibration = random.uniform(0.81, 1.50)

    print("--------------------------------")
    print(f"Status      : {status}")
    print(f"Temperature : {temperature:.2f} °C")
    print(f"Current     : {current:.2f} A")
    print(f"Vibration   : {vibration:.2f} g")

    time.sleep(2)