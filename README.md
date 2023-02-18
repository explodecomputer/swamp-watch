# Swamp-watch

Creating a time lapse of the Brooks Dye Works swamp.

- Take 2 scenes per day (deep sleep in between) - https://blog.balena.io/enabling-deep-sleep-for-your-raspberry-pi-project/ and https://github.com/raspberrypi/picamera2
- Pan to take 3 pictures each scene - https://github.com/arducam/pca9685
- Stitch the three pictures - https://github.com/brianpinto91/image-stitching
- Upload to google photos or somewhere similar - https://www.projectpro.io/recipes/upload-files-to-google-drive-using-python


## Raspberry Pi equipment

- RPi camera module v3
- RPi 2b
- wifi dongle BCM43143
- arducam pan tilt platform sku: B0283

## Installation

```
virtualenv swampwatch
source swampwatch/bin/activate
pip install -r requirements.txt --extra-index-url https://test.pypi.org/simple/
```








---

## Pi Setup Notes





### Getting camera to work

two different libraries - raspistill and libcamera

libcamera-hello was telling me that the legacy app was being used. Use `sudo raspi-config` to turn off legacy interface

After that it was saying some libraries were missing. Run

```
sudo apt update
sudo apt upgrade
```

Updated libcamera and after that

```
libcamera-still -o test.jpg
```

works.

### Getting wifi dongle to work

Use `wpa_cli` and then `scan` and `scan_results` to find which networks it can see. This dongle can only see littleboxes2.4, works using 

```
sudo nano /etc/network/interfaces
```

```
auto lo
iface lo inet loopback
iface eth0 inet manual

auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
```

and

```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

```
network={
ssid="NAME"
psk="PWD"
proto=RSN
key_mgmt=WPA-PSK
pairwise=CCMP TKIP
group=CCMP TKIP
id_str=”Name of WiFi Network”
}
```

### Getting pan tilt to work

Use this example code: https://github.com/arducam/pca9685

First need to enable I2C module 

```
sudo raspi-config
```

interfaces -> I2C enable

Then install python library

```
sudo apt-get install libcap2-dev
sudo pip3 install adafruit-circuitpython-servokit
```
