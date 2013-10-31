Arduino-logging
===============
Logging library for Arudino

Usage
-----
```
#include <Logging.h>

#define LOGLEVEL LOG_LEVEL_DEBUG


void setup() {
    Log.Init(LOGLEVEL, 9600L);
}

void loop() {
    Log.Info("My favorite output stuff in future :-)"CR);
    //...
    Log.Info("End of cycle "CR);
}
```

Read your logs using the receiver included! Install it using
```
# cd receiver
# python setup.py install
```
and then
```
arduino_logging /dev/tty.usbmodem1411 9600
```

License
-------
This software is released under MIT License. 
Copyright (c) 2011 - 2013 Bernd Klein <berndklein@gmx.de>
Copyright (c) 2013 Andrea Stagi <stagi.andrea@gmail.com>