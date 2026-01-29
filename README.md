# Finnian's Macropad

This macropad will be a multi-layer hotkey machine. I have coded it so that one key switches between the different modes, with an LED indicating what mode its in. I plan on having presets for editing, sim racing, and a "general use" one, but I can always go back into the KMK firmware and add more features if I like.

### Challenges
I haven't done that much design work myself, so this was full of new experiences for me. I have used onshape for 3d cad work before, so it was fun learning how to use fusion (they were pretty similar, at least for what I was doing). 
I also enjoyed learning how to use the KiCAD software. I've used Rapidharness before for electrical work, but it was so cool and different designing a PCB. One of the biggest challenges was the coding, as I've only used Java for my compsci class, and figuring out how to use Github (it required a lot of youtube tutorials and headscratching). Overall, I persisted through and I gained a lot of valuable skills and had a good time!

### Bill Of Materials
- 4x M3x16mm Bolt
- 4x M3 Heatset
- 4x Cherry MX Switches
-4x Blank DSA Keycaps
- 2x SK6812 MINI Leds
- 1x XIAO RP2040
- 1x case (3d-printed top and bottom plate)
 



### Designs
Schematic            |  PCB         |   Case
:-------------------------:|:-------------------------:|:-------------------------:|
<img src="Macropad%20Images/MacropadPCBsch.png" width="400">  | <img src="Macropad%20Images/MacropadPCB.png" width="400">  | <img src="Macropad%20Images/MacropadCAD.png" width="400">  

### Firmware Overview
For this project, I decided to use KMK firmware as I thought it would be the most flexible for my needs. I have coded it to have three different "layers" of keys that I can switch between for different purposes. In the future, I want to explore how I can change the output of a key based on the time it was pressed. This could multiply the amount of possible hotkeys on my board.

