class Phone:
    def turn_on(self):
        print("Phone booting up...")

class Camera:
    def turn_on(self):
        print("Camera warming up...")

class SmartDevice(Phone, Camera):
    pass

sd = SmartDevice()
sd.turn_on()  # Phone booting up...

print(SmartDevice.__mro__)
