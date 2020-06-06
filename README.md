# pl2303
Simple PL2303 125khz rfid reader/writer based on the work of [Fredrik Nordin](https://github.com/freedick/pl2303_rfid)

# Installation
```
sudo apt install -y python-pip
pip install pyserial
```

Please also add the following line to your `/etc/udev/rules.d/99-card-reader.rules`:
```
SUBSYSTEM=="tty", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", SYMLINK+="ttyQCardReader%n"
```


