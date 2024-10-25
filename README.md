# IoT Simulator Project

A Python-based IoT device simulation and automation system with a real-time monitoring dashboard. This project emulates smart home devices like **Smart Lights**, **Thermostats**, and **Security Cameras**, offering basic automation tasks and a Tkinter-based dashboard for live monitoring and interaction.

## Features

- **IoT Device Emulation**: 
  - Simulates **Smart Lights**, **Thermostats**, and **Security Cameras** with real-life functionalities (on/off, brightness, temperature, etc.).
  
- **Automation System**:
  - Automatically controls devices based on random conditions.
  - Executes periodic automation tasks (e.g., setting thermostat temperature, toggling light brightness).
  
- **Real-Time Monitoring Dashboard**:
  - A **Tkinter-based GUI** that allows users to monitor the status of each device in real-time.
  - Interactive buttons let users toggle device statuses (turn devices on/off).
  
- **Device Discovery**:
  - The central automation system discovers and controls new devices dynamically.
  
## Structure

The project is split into three main parts:

1. **IoT Device Emulation**:
    - **SmartLight**: Simulates a smart light with on/off status and brightness control.
    - **Thermostat**: Simulates a thermostat with temperature settings.
    - **SecurityCamera**: Simulates a security camera with an armed/disarmed state and motion detection.
    
2. **Automation System**:
    - Centralized automation system that controls all discovered devices.
    - Randomly simulates automation tasks such as adjusting brightness, temperature, or detecting motion.
    
3. **Monitoring Dashboard**:
    - A graphical interface (using **Tkinter**) that displays the current status of devices and allows user interaction.
    - Real-time updates to device statuses (e.g., toggling lights, adjusting temperatures, arming cameras).

## How to Use

1. **Running the Simulation**:
    - The project emulates a smart home with devices such as **lights**, **thermostats**, and **security cameras**.
    - To simulate automation tasks, run the program, and it will automatically control devices.

2. **Interacting with Devices**:
    - You can interact with devices through the **Tkinter-based dashboard**.
    - Buttons are provided to toggle device statuses manually (turn lights on/off, adjust thermostat, etc.).

### Key Features
- **Simulated Automation**: Every few seconds, random tasks are executed on the devices.
- **Monitoring Dashboard**: Displays the current status of each device and allows manual user interaction.
  
## Example Devices

- **SmartLight**: 
    - `turn_on()`: Turns the light on.
    - `turn_off()`: Turns the light off.
    - `set_brightness(brightness)`: Adjusts the light brightness.
  
- **Thermostat**: 
    - `turn_on()`: Turns the thermostat on.
    - `turn_off()`: Turns the thermostat off.
    - `set_temperature(temp)`: Sets the room temperature.
  
- **Security Camera**:
    - `turn_on()`: Arms the camera.
    - `turn_off()`: Disarms the camera.
    - `arm()`/`disarm()`: Changes the camera security status.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YourUsername/IoT-Simulator.git
    cd IoT-Simulator
    ```

2. Install necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the IoT simulation and monitoring dashboard:
    ```bash
    python main.py
    ```

## Technologies Used

- **Python 3.x**
- **Tkinter** (for GUI Dashboard)
- **Random & Time** libraries (for automation tasks)

## Future Improvements

- Add more types of IoT devices (e.g., **Smart Thermostats**, **Door Locks**).
- Enhance the automation system by incorporating **machine learning** for smarter automation.
- Extend the dashboard with more user-friendly features like **drag-and-drop** device management or **customizable automation rules**.

