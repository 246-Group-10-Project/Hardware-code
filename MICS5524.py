import spidev
import time

# SPI setup
spi = spidev.SpiDev()
spi.open(0, 0)  # bus 0, device 0
spi.max_speed_hz = 1350000

def read_adc(channel):
    # MCP3008 protocol
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        raw_value = read_adc(0)  # read from channel 0
        
        # Convert to voltage (assuming 3.3V reference)
        voltage = raw_value * (3.3 / 1023.0)

        print(f"Raw: {raw_value} | Voltage: {voltage:.2f} V")

        time.sleep(1)

except KeyboardInterrupt:
    spi.close()