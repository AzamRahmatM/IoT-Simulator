import random
import time
import tkinter as tk
from tkinter import ttk


# Part 1: IoT Device Emulation

class SmartLight:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.brightness = 0

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def set_brightness(self, brightness):
        self.brightness = brightness


class Thermostat:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.temperature = 20  # Default temperature

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def set_temperature(self, temperature):
        self.temperature = temperature


class SecurityCamera:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False
        self.security_status = "Disarmed"

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False

    def arm(self):
        self.security_status = "Armed"

    def disarm(self):
        self.security_status = "Disarmed"


# Part 2: Central Automation System

class AutomationSystem:
    def __init__(self):
        self.devices = []

    def discover_device(self, device):
        self.devices.append(device)

    def execute_automation_tasks(self):
        for device in self.devices:
            if isinstance(device, SmartLight) and random.choice([True, False]):
                device.set_brightness(random.randint(0, 100))
            elif isinstance(device, Thermostat) and random.choice([True, False]):
                device.set_temperature(random.randint(18, 25))
            elif isinstance(device, SecurityCamera) and random.choice([True, False]):
                if device.status:
                    device.security_status = "Detected Motion"


def simulate_automation_system():
    automation_system = AutomationSystem()

    light1 = SmartLight("L1")
    thermostat1 = Thermostat("T1")
    camera1 = SecurityCamera("C1")

    automation_system.discover_device(light1)
    automation_system.discover_device(thermostat1)
    automation_system.discover_device(camera1)

    for _ in range(10):  # Simulate 10 iterations
        automation_system.execute_automation_tasks()
        time.sleep(2)  # Simulate some time passing


# Part 3: Monitoring Dashboard

class MonitoringDashboard:
    def __init__(self, automation_system):
        self.automation_system = automation_system

        # Creating the main window
        self.root = tk.Tk()
        self.root.title("Smart Home Monitoring Dashboard")

        # Creating and placing widgets
        self.create_widgets()

    def create_widgets(self):
        # Creating a label to display device status
        self.status_label = ttk.Label(self.root, text="Device Status:")
        self.status_label.grid(row=0, column=0, padx=10, pady=10)

        # Creating a text widget to display device information
        self.status_text = tk.Text(self.root, height=10, width=50)
        self.status_text.grid(row=1, column=0, padx=10, pady=10)

        # Creating a button to simulate user interaction
        self.interact_button = ttk.Button(self.root, text="Interact with Devices", command=self.interact)
        self.interact_button.grid(row=2, column=0, padx=10, pady=10)

        # Updating device status on the GUI
        self.update_device_status()

    def update_device_status(self):
        # Clearing previous content
        self.status_text.delete(1.0, tk.END)

        # Updating with current device status
        for device in self.automation_system.devices:
            self.status_text.insert(tk.END, f"{device.device_id}: {device.status}\n")

        # Scheduling the method to run periodically (every 2000 milliseconds)
        self.root.after(2000, self.update_device_status)

    def interact(self):
        # Simulate user interaction (toggle device status)
        for device in self.automation_system.devices:
            if isinstance(device, SmartLight):
                if device.status:
                    device.turn_off()
                else:
                    device.turn_on()
            elif isinstance(device, Thermostat):
                if device.status:
                    device.turn_off()
                else:
                    device.turn_on()
            elif isinstance(device, SecurityCamera):
                if device.status:
                    device.turn_off()
                else:
                    device.turn_on()


if __name__ == "__main__":

    automation_system = AutomationSystem()

    light1 = SmartLight("L1")
    thermostat1 = Thermostat("T1")
    camera1 = SecurityCamera("C1")

    automation_system.discover_device(light1)
    automation_system.discover_device(thermostat1)
    automation_system.discover_device(camera1)

    simulate_automation_system()

    monitoring_dashboard = MonitoringDashboard(automation_system)

    # Running the Tkinter main loop
    monitoring_dashboard.root.mainloop()
