#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
# This file deals with the Tilt formatted message
from struct import unpack
import struct
import json
import aioblescan as aios
#Tilt format based on iBeacon format and filter includes Apple iBeacon identifier portion (4c000215) as well as Tilt specific uuid preamble (a495)
#TILT = '4c000215a495'
TILT = '0215a495'


class Tilt(object):
    """
    Class defining the content of a Tilt advertisement
    """

    def decode(self, packet):
        data = {}
        raw_data = packet.retrieve('Manufacturer Specific Data')

        if raw_data:
            val = raw_data[0].payload
            manufacturerID = val[0].val
            payload = val[1].val.hex()
            mfg_id = payload[0:8]
            rssi = packet.retrieve('rssi')
            mac = packet.retrieve("peer")
            if mfg_id == TILT:
               colourCode = payload[10:12]

               tiltColour = ""
               if colourCode == "10":
                       tiltColour = "Red"
               elif colourCode == "20":
                       tiltColour = "Green"
               elif colourCode == "30":
                       tiltColour = "Black"
               elif colourCode == "40":
                       tiltColour = "Purple"
               elif colourCode == "50":
                       tiltColour = "Orange"
               elif colourCode == "60":
                       tiltColour = "Blue"
               elif colourCode == "70":
                       tiltColour = "Yellow"
               elif colourCode == "80":
                       tiltColour = "Pink"

               tempF = int(payload[36:40], 16) #temperature in degrees F
               tempC = round(((tempF - 32) * 5/9), 1)
               gravity = int(payload[40:44], 16) #temperature in degrees F

               data['uuid'] = payload[4:36]
               data['tiltColour'] = tiltColour
               data['tempF'] = tempF
               data['tempC'] = tempC
               data['gravity'] = gravity
               data['rssi'] = rssi[-1].val
               data['mac'] = mac[-1].val
               return json.dumps(data)
