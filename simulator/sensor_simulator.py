import csv
import random
import time
from datetime import datetime

filename = "../dataset/motor_data.csv"

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Timestamp",
        "Temperature",
        "Current",
        "Vibration",
        "Status"
    ])

    print("Generating dataset...\n")

    for i in range(100):

        status = random.choice(["Healthy", "Warning", "Critical"])

        if status == "Healthy":
            temperature = round(random.uniform(35,45),2)
            current = round(random.uniform(2.8,3.5),2)
            vibration = round(random.uniform(0.10,0.30),2)

        elif status == "Warning":
            temperature = round(random.uniform(46,60),2)
            current = round(random.uniform(3.6,4.5),2)
            vibration = round(random.uniform(0.31,0.80),2)

        else:
            temperature = round(random.uniform(61,80),2)
            current = round(random.uniform(4.6,6.0),2)
            vibration = round(random.uniform(0.81,1.50),2)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow([
            timestamp,
            temperature,
            current,
            vibration,
            status
        ])

print("Dataset Generated Successfully!")