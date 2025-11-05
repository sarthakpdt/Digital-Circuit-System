import time
import random

# Mock sensor data generation function
def generate_sensor_data():
    temperature = random.uniform(18, 30)  # Random temperature between 18°C and 30°C
    humidity = random.uniform(40, 60)     # Random humidity between 40% and 60%
    dust_concentration = random.uniform(0, 100)  # Random dust concentration in micrograms per cubic meter
    return temperature, humidity, dust_concentration

# Function to simulate sending sensor data over a wireless network
def send_data_over_network(data):
    # Code to send data over the network would go here
    print("Sending data over the network:", data)

# Function to check air quality and trigger alerts if necessary
def check_air_quality(temperature, humidity, dust_concentration, temp_threshold, hum_threshold, dust_threshold):
    if temperature > temp_threshold:
        print("Alert: High temperature detected! Temperature:", temperature, "°C")
    if humidity > hum_threshold:
        print("Alert: High humidity detected! Humidity:", humidity, "%")
    if dust_concentration > dust_threshold:
        print("Alert: High dust concentration detected! Dust Concentration:", dust_concentration, "micrograms per cubic meter")

# Main function to continuously collect and send sensor data
def main():
    try:
        # Ask the user for threshold values
        temp_threshold = float(input("Enter the temperature threshold (in °C): "))
        hum_threshold = float(input("Enter the humidity threshold (in %): "))
        dust_threshold = float(input("Enter the dust concentration threshold (in micrograms per cubic meter): "))

        print("\nThreshold values entered by the user:")
        print("Temperature threshold:", temp_threshold, "°C")
        print("Humidity threshold:", hum_threshold, "%")
        print("Dust concentration threshold:", dust_threshold, "micrograms per cubic meter")

        interval = int(input("\nEnter the time interval (in seconds) between each data collection and transmission: "))

        while True:
            # Generate sensor data
            temperature, humidity, dust_concentration = generate_sensor_data()

            # Construct data packet
            data_packet = {
                "temperature": temperature,
                "humidity": humidity,
                "dust_concentration": dust_concentration
            }

            # Send data over the network
            send_data_over_network(data_packet)

            # Check air quality and trigger alerts if necessary
            check_air_quality(temperature, humidity, dust_concentration, temp_threshold, hum_threshold, dust_threshold)

            # Wait for the specified time interval before collecting the next set of data
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Program terminated by user")

if __name__ == "__main__":
    main()
