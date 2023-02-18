from picamera2 import Picamera2
import time
import adafruit_servokit

class ServoKit(object):
    default_angle = 90
    def __init__(self, num_ports):
        print("Initializing the servo...")
        self.kit = adafruit_servokit.ServoKit(channels=16)
        self.num_ports = num_ports
        self.resetAll()
        print("Initializing complete.")
    def setAngle(self, port, angle):
        if angle < 0:
            self.kit.servo[port].angle = 0
        elif angle > 180:
            self.kit.servo[port].angle = 180
        else:
            self.kit.servo[port].angle = angle
    def getAngle(self, port):
        return self.kit.servo[port].angle
    def reset(self, port):
        self.kit.servo[port].angle = self.default_angle
    def resetAll(self):
        for i in range(self.num_ports):
            self.kit.servo[i].angle = self.default_angle

def test():
    servoKit = ServoKit(4)
    print("Start test")
    for i in range(0,180, 5):
        servoKit.setAngle(0, i)
        servoKit.setAngle(2, i)
        time.sleep(.05)
    for i in range(180,0,-5):
        servoKit.setAngle(0, i)
        servoKit.setAngle(2, i)
        time.sleep(.05)
    for i in range(15,145, 5):
        servoKit.setAngle(1, i)
        servoKit.setAngle(3, i)
        time.sleep(.05)
    for i in range(145,15,-5):
        servoKit.setAngle(1, i)
        servoKit.setAngle(3, i)
        time.sleep(.05)    
    servoKit.resetAll()

picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)

picam2.start()

np_array = picam2.capture_array()
print(np_array)
picam2.capture_file("demo.jpg")
picam2.stop()

servoKit = ServoKit(2)
servoKit.setAngle(0, 90)
servoKit.setAngle(1, 90)


