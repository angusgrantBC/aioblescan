# aioblescan

aioblescan is a Python 3/asyncio library to listen for BLE advertized packets.

[![PyPI version fury.io](https://badge.fury.io/py/aioblescan.svg)](https://pypi.python.org/pypi/aioblescan)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-licen)
[![GITHUB-BADGE](https://github.com/frawau/aioblescan/workflows/black/badge.svg)](https://github.com/psf/black)

# Installation

We are on PyPi so

     pip3 install aioblescan
or

     python3 -m pip install aioblescan



# How to use

Essentially, you create a function to process the incoming
information and you attach it to the `BTScanRequester`. You then create a Bluetooth
connection, you issue the scan command and wait for incoming packets and process them.

You can use Eddystone or RuuviWeather to retrieve specific information


The easiest way is to look at the `__main__.py` file.

You can run the module with

    python3 -m aioblescan

Add `-h` for help.

To see the RuuviTag weather information try:

    python3 -m aioblescan -r

You will get

    Weather info {'rssi': -64, 'pressure': 100300, 'temperature': 24, 'mac address': 'fb:86:84:dd:aa:bb', 'tx_power': -7, 'humidity': 36.0}
    Weather info {'rssi': -62, 'pressure': 100300, 'temperature': 24, 'mac address': 'fb:86:84:dd:aa:bb', 'tx_power': -7, 'humidity': 36.0}

To check Eddystone beacon

    python3 -m aioblescan -e

You get

    Google Beacon {'tx_power': -7, 'url': 'https://ruu.vi/#BEgYAMR8n', 'mac address': 'fb:86:84:dd:aa:bb', 'rssi': -52}
    Google Beacon {'tx_power': -7, 'url': 'https://ruu.vi/#BEgYAMR8n', 'mac address': 'fb:86:84:dd:aa:bb', 'rssi': -53}

To check ATC_MiThermometer with [custom firmware](https://github.com/atc1441/ATC_MiThermometer) beacon

    python3 -m aioblescan -A

You get

    Temperature info {'mac address': 'a4:c1:38:40:52:38', 'temperature': 2.8, 'humidity': 62, 'battery': 72, 'battery_volts': 2.863, 'counter': 103, 'rssi': -76}
    Temperature info {'mac address': 'a4:c1:38:40:52:38', 'temperature': 2.8, 'humidity': 62, 'battery': 72, 'battery_volts': 2.863, 'counter': 103, 'rssi': -77}

To check Tilt hydrometer beacon

    python3 -m aioblescan -T

You get

    {"uuid": "a495bb50c5b14b44b5121370f02d74de", "tiltColour": "Orange", "tempF": 69, "tempC": 20.6, "gravity": 1027, "rssi": -83, "mac": "c7:8c:35:08:85:dd"}

For a generic advertise packet scanning

    python3 -m aioblescan

You get

    HCI Event:
        code:
            3e
        length:
            19
        LE Meta:
            code:
                02
            Adv Report:
                num reports:
                    1
                ev type:
                    generic adv
                addr type:
                    public
                peer:
                    54:6c:0e:aa:bb:cc
                length:
                    7
                flags:
                    Simul LE - BR/EDR (Host): False
                    Simul LE - BR/EDR (Control.): False
                    BR/EDR Not Supported: False
                    LE General Disc.: True
                    LE Limited Disc.: False
                Incomplete uuids:
                        ff:30
                rssi:
                    -67
    HCI Event:
        code:
            3e
        length:
            43
        LE Meta:
            code:
                02
            Adv Report:
                num reports:
                    1
                ev type:
                    no connection adv
                addr type:
                    random
                peer:
                    fb:86:84:dd:aa:bb
                length:
                    31
                flags:
                    Simul LE - BR/EDR (Host): False
                    Simul LE - BR/EDR (Control.): False
                    BR/EDR Not Supported: False
                    LE General Disc.: True
                    LE Limited Disc.: True
                Complete uuids:
                        fe:aa
                Advertised Data:
                    Service Data uuid:
                        fe:aa
                    Adv Payload:
                        10:f9:03:72:75:75:2e:76:69:2f:23:42:45:77:59:41:4d:52:38:6e
                rssi:
                    -59

Here the first packet is from a Wynd device, the second from a Ruuvi Tag


aioblescan can also send EddyStone advertising. Try the -a flag when running the module.


# FAQ

Why not use scapy?

    Scapy is great and you can do

        import scapy.all as sa
        test=sa.BluetoothHCISocket(0)
        command=sa.HCI_Cmd_LE_Set_Scan_Enable(enable=1,filter_dups=0)
        chdr=sa.HCI_Command_Hdr(len=len(command))
        hdr=sa.HCI_Hdr(type=1)
        test.send(hdr / chdr / command)

    to get things going. But... the great thing with Scapy is that there is so
    many versions to choose from.... and not all have all the same functions ... and
    installation can be haphazard, with some version not installing at all. Also
    scapy inludes a lot of other protocols and could be an overkill... lastly it
    is never too late to learn...

What can you track?

    aioblescan will try to parse all the incoming advertised information. You can see
    the raw data when it does not know what to do. With Eddystone beacon you can see the
    URL, Telemetry and UID
