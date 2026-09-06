## [DES222 Process Journal](https://cyclonesak.github.io/2026_DES222_Process_Journal/)

[Markdown Cheat-sheet](MD_cheat-sheet.md) or [GFM guide](https://github.github.com/gfm/)

**Development of a responsive technology prototype - an application or device that responds to the situation/context it is in. This could be:**
- a mobile application (or web interface viewed on a phone) that taps into the sensors of the mobile device, such as location or orientation
- a standalone custom hardware device that uses environmental sensors, or biometric sensors
- a hybrid of the two, with some hardware communicating with a web interface or application on a computer or phone

#### **Week 8 - give a brief (3 - 5 minute) presentation covering**
- project concept, and how it relates to responsive design.
- one or more possible realisations of the concept
- discussion of existing related projects
- any progress so far (can be quite brief, just what they are)

**The material you present in your Oral Presentation should be reflected in your process journal (see below) at the time of the presentation.**

The role of a process journal is to have a place where you can record your process and understanding of your work primarily for your own benefit.

At the end of the semester, you should be able to follow your thoughts and actions on a week-to-week basis and be able to re-create anything you have made, even a significant time later (such a year from now).

---
# My Project

When I go kitesurfing, it can get a bit cold out in the wind. I usually have my phone with me - it tracks my location and measures jump height using the accelerometer [Surfr App](https://www.thesurfr.app/). What if I create a sensor to measure my core temperature under my wetsuit that will send an alarm to my phone if it drops below a certain value... it emits a buzzer noise. I could also add a sensor for UV light for sunburn risk - measure the light over a certain time period - if brighter than x - remind user to reapply sunscreen.

OR… I could do it the other way around — is it too hot, too bright? Build a Blue / Green / Yellow / Red LED indicator.

Importantly, the scenario does not just apply to kitesurfers. The concept can be expanded to any outdoor activity with exposure to temperature and UV extremes.

The [Surfr App](https://www.thesurfr.app/) I currently use (or a [WOO Sports](https://www.woosports.com/en/products/woo-kiteboard-sensor-package-4-0-65240-7200) package) does not support these features. Garmin/Suunto watch sun/heat features don’t either. L’Oréal My Skin Track UV (a wearable UV badge — directly related to UV 1/2 but provides no real‑time feedback to the wearer) and the Shade UV sensor by Shade (much better than I could make, but an app‑based clinical tool rather than a feedback mechanism for the wearer) also do not directly correlate.

CORE 2 Thermal Sensor — measures core body temperature and skin temperature and calculates a real‑time Heat Strain Index for endurance athletes, streaming to a phone or watch via BLE and ANT+. This is the closest analogue to the “temperature‑under‑the‑wetsuit” idea I originally floated. Reviewing it changed my thinking: real core‑temperature measurement is hard and requires a paired heart‑rate monitor to be accurate. That pushed me away from claiming “core temperature” and towards ambient heat + UV + on‑body microclimate (two DS18B20 waterproof digital temperature sensors, one under the wetsuit and one over it, measuring variation changes over time).

There are similar DIY projects:
- [EnviroGo](https://www.cnx-software.com/2026/01/20/envirogo-esp32-s3-wearable-environmental-monitor-features-7-sensors/)  
- [ElectronicWings](https://www.electronicwings.com/users/vairamanielectro/projects/5825/context-aware-environmental-parameter-monitoring-node-using-esp32-c6)

I want to differentiate my project by including a responsive phone app that responds to the environmental feedback it recieves along the lines of [Sensing Ambient Light for User Experience-Oriented Color Scheme Adaptation on Smartphone Displays.](/SensingAmbientLightforUserExperience.pdf)

My project addresses the 'in session' safety question of 'am I freezing/cooking? Can I even read my phone screen right now with wet, sandy hands in direct glare?' Thats the gap - to deliver safety cues through a system that survives sun, water and sandy fingers.

A number of implementation pathways are being actively considered:
- Phone-only (no custom hardware). Use the phone's own ambient-light sensor, the device thermometer, and a weather-API UV index lookup. 
- Wearable sensor + native mobile app. ESP32 streams to a Flutter/React app. Most 'professional' feeling, but disproportionate amount of work to get app going.
- ✔ **🟩 Chosen.** Wearable sensor + ESP32 serving its own responsive web page. ESP32 hosts its own WiFi app and serves a single web page that the phone loads in a browser. This lets the responsive website work from Task 1 be used here: the page restyles itself (type size, contrast, layout, message wording) based on live sensor values. Two responsive channels — physical LED/Speaker/Vibration and adaptive UI — driven by the same data. No cloud, no CORS, no app store, testable in a backyard.
- On-body sensor with LED only, no phone at all. Simplest wearable, but throws away the entire responsive-web-UI.

#### Hardware:
- ESP32
- Temperature + humidity sensor (DHT22, DHT11, or BME280) DS18B20
- 1 RGB LED or 3 single LEDs (I have a variable colour LED or small screen)
- USB power bank
- Breadboard, jumper wires
- A clip, lanyard, or belt-pouch so it can be worn on a bag or waist
- small vibration motor and/or speaker

A sewn or velcro pouch, a lunch-box enclosure with a bag clip. The object should be worn.
ESP32 creates its own Wi‑Fi access point and serves a tiny webpage. Phone joins that network and opens the device address. No cloud, no Holfuy, no CORS, no app store.

Firmware reads sensors every second, computes a simple heat index, maps values to Settle / Glance / Shelter.

#### Software: 
ESP32 exposes /sensors as JSON and / as the interface.

The page restyles itself from the live mode. This is dynamic configuration, not a static dashboard with a colour chip.

Reuse Task 1 phone / tablet / desktop layouts, light and dark. Force high contrast even if the OS theme is dark if Surfr is running or brightness is >x or some other trigger.

**The Plan:**
- for the pitch: Show a breadboard that already switches LED colour, plus phone mockups or a half-working page.
 
 **Three-minute video story:**
 1. Clip onto a bag. Walk outside.
 2. Close-up of LED shifting as glare and heat rise.
 3. Phone in the sun: type gets huge, charts disappear, word becomes "SEEK SHADE" reapply sunscreen or whatever.
 4. Step under a tree or indoors: UI settles, LED calms.

 If I have no light sensor functional, use the phone’s ambient-light or time-of-day search on weather API UV index as the second channel, and keep the ESP32 for on-body temperature.

 modes GO / PAUSE / Pack-down, and treat glare + heat + “can I use my device without sandy, wet hands?”