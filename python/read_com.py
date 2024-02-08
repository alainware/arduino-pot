import serial
import csv
import time

# Serial port cofiguration
# Adjust the port depending on the environment (Windows, Mac, Linux)
# Windows -> COM3, COM4, COM5, etc.
# macOS -> /dev/cu.usbmodem14101, /dev/cu.usbmodem14201, etc.
serial_port = serial.Serial('COM3', 9600)
results_csv = 'potentiometer_data.csv'

# Open CSV file as read mode
with open(results_csv, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write headers to CSV file
    csv_writer.writerow(['Time (ms)', 'Value'])

    # Read data from serial port and write to CSV file
    while True:
        try:
            # Read serial port line
            line = serial_port.readline().decode().strip()

            # Split the line into time and value
            time, value = line.split(',')

            # Write data to CSV file
            csv_writer.writerow([time, value])

            # Display data in the console
            print(f'Time: {time} ms, Value: {value}')
            time.sleep(1)
        except KeyboardInterrupt:
            print("Process interrupted.")
            break

# Close the serial port
serial_port.close()
