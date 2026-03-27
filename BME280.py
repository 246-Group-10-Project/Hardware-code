import time
import board
import busio
import adafruit_bme280

# Create I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create sensor object
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# Optional: set sea level pressure (adjust for your location)
bme280.sea_level_pressure = 1013.25

while True:
    temperature = bme280.temperature
    humidity = bme280.humidity
    pressure = bme280.pressure
    altitude = bme280.altitude

    print("Temperature: {:.2f} °C".format(temperature))
    print("Humidity: {:.2f} %".format(humidity))
    print("Pressure: {:.2f} hPa".format(pressure))
    print("Altitude: {:.2f} m".format(altitude))
    print("-" * 30)

    time.sleep(2)