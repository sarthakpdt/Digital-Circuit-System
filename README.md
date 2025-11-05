# Indoor Air Quality Monitoring System using Wireless Sensor Network

This project focuses on monitoring indoor air quality using wireless sensor technology.  
The system continuously measures **Temperature**, **Humidity**, and **Dust Concentration** and sends the data wirelessly to a monitoring unit. If any reading exceeds the safe limit, the system generates alerts to ensure timely safety actions.

---

## 📌 Project Objective
To design and implement a digital indoor air monitoring system that:
- Collects environmental data using sensors
- Transmits data wirelessly through a sensor network
- Checks air quality in real-time
- Alerts the user when air quality becomes unsafe

---

## 🏛 System Overview

Most people spend the majority of their time indoors. Pollutants like dust, smoke, and chemicals can affect breathing and cause long-term health issues.  
This monitoring system helps detect harmful indoor air conditions early by using:

- **Wireless Sensors** to collect real-time environmental data  
- **Microcontroller Unit (MCU)** for processing  
- **Wireless Transceiver Module** for data transmission  
- **Monitoring Interface / Console Output** for user visibility  

If thresholds are crossed, the system **alerts the user instantly**.

---

## 🧠 Key Features

| Feature | Description |
|--------|-------------|
| Real-time Monitoring | Continuously measures temperature, humidity, and dust concentration |
| Wireless Data Transfer | Sensor data is transmitted over a wireless transceiver |
| Threshold Alerts | Alerts user when values exceed the safe range |
| Custom Threshold Input | Users can set their own safe value limits |
| Adjustable Time Interval | Data refresh interval is user-defined |

---

## 🛠 Hardware Components Used
- Wireless Transceiver Module (nRF24L01 or equivalent)
- Microcontroller (C8051 / STM32 Cortex-M3)
- Temperature and Humidity Sensor
- Dust / Air Quality Sensor
- Power Supply Module (Battery/Adaptor)
- Buzzer or Alarm Module (optional)

---

## 💻 Software Used
| Software | Purpose |
|---------|---------|
| Python | Data Simulation, Processing & Alerting |
| MySQL (Optional) | Data Logging and Storage |
| HTML/CSS/JS (Optional) | Web-Based Monitoring Dashboard |

---
## ✅ Results

The Indoor Air Quality Monitoring System successfully measured and analyzed real-time environmental parameters including temperature, humidity, and dust concentration. When the sensor readings crossed the predefined threshold values, the system generated instant alerts, enabling timely intervention to maintain a healthy indoor atmosphere.

The wireless data transmission worked efficiently, showing continuous live readings at the user-defined time intervals. The alert mechanism accurately identified abnormal environmental conditions such as:

- High Temperature
- High Humidity Levels
- Increased Dust/Particulate Concentration (Poor Air Quality)

This demonstrated that the system can actively monitor indoor spaces such as homes, classrooms, offices, and laboratories, and notify occupants of potential air quality risks. The prototype can be further extended to control ventilation systems or trigger automated responses such as activating air purifiers or sending SMS and mobile notifications.

Overall, the project proved to be:
- **Reliable** in real-time monitoring  
- **Accurate** in environmental sensing  
- **Scalable** for smart-home / IoT integration  
- **Effective** in improving indoor safety and health conditions

