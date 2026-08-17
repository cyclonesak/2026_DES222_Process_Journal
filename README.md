## [DES222 Process Journal](https://cyclonesak.github.io/2026_DES222_Process_Journal/)

[Markdown Cheet-sheet](MD_cheat-sheet.md) or [GFM guide](https://github.github.com/gfm/)

**Development of a responsive technology prototype - an application or device that responds to the situation/context it is in. This could be:**
- a mobile application (or web interface viewed on a phone) that taps into the sensors of the mobile device, such as location or orientation
- a standalone custom hardware device that uses environmental sensors, or biometric sensors
- a hybrid of the two, with some hardware communicating with a web interface or application on a computer or phone

#### **Week 8 - give a brief (3 - 5 minute) presentation covering**
- project concept, and how it relates to responsive design.
- one or more possible realisations of the concept
- discussion of existing related projects
any progress so far (can be quite brief, just what they are)

**The material you present in your Oral Presentation should be reflected in your process journal (see below) at the time of the presentation.**

The role of a process journal is to have a place where you can record your process and understanding of your work primarily for your own benefit.

At the end of the semester, you should be able to follow your thoughts and actions on a week-to-week basis and be able to re-create anything you have made, even a significant time later (such a year from now).

---
# My Project
TBC...

When I go kitesurfing, it can get a bit cold out in the wind. I usually have my phone with me - it tracks my location and measures jump height using the accerometer [Surfr App](https://www.thesurfr.app/). What if I create a sensor to measure my core temperature under my wetsuit that will send an alarm to my phone if it drops below a certain value... it emits a buzzer noise. I could also add a sensor for UV light for sunburn risk - measure the light over a certain time period - if brighter than x - remind user to reapply sunscreen.

OR.. I could do it the other way around - is it too hot, too bright? Build a Green / Yellow / Red LED 

#### Hardware:
- ESP32
- Temperature + humidity sensor (DHT22, DHT11, or BME280)
- 1 RGB LED or 3 single LEDs
- USB power bank
- Breadboard, jumper wires
- A clip, lanyard, or belt-pouch so it can be worn on a bag or waist
- small vibration motor

A sewn or velcro pouch, a lunch-box enclosure with a bag clip. The object should be worn.
ESP32 creates its own Wi‑Fi access point and serves a tiny webpage. Phone joins that network and opens the device address. No cloud, no Holfuy, no CORS, no app store.

Firmware reads sensors every second, computes a simple heat index, maps values to Settle / Glance / Shelter.

#### Software: 
ESP32 exposes /sensors as JSON and / as the interface.

The page restyles itself from the live mode. This is dynamic configuration, not a static dashboard with a colour chip.

Reuse Task 1 phone / tablet / desktop layouts, light and dark. Force high contrast even if the OS theme is dark if Surfr is running or brightness is >x or some other trigger.

**The Plan:**
 - for the pitch: Show a breadboard that already switches LED colour, plus phone mockups or a half-working page.
 
 **Three-minute video storyboard:**
 1. Clip onto a bag. Walk outside.
 2. Close-up of LED shifting as glare and heat rise.
 3. Phone in the sun: type gets huge, charts disappear, word becomes "SEEK SHADE" reapply sunscreen or whatever.
 4. Step under a tree or indoors: UI settles, LED calms.
 5. One sentence on why the device stopped asking for attention.
 6. Shoot it in one afternoon in a backyard

 If I have no light sensor, use the phone’s ambient-light or time-of-day as the second channel, and keep the ESP32 for on-body temperature.

 modes GO / PAUSE / Pack-down, and treat glare + heat + “can I use my phone with sandy hands”