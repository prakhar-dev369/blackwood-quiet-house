# Blackwood: The Quiet House

An original first-person 3D horror escape level for phones and desktop browsers.

Find three tools. Stay quiet. Hide before the Keeper sees you.

- Four furnished rooms and a haunted gallery
- Noise-sensitive enemy with patrol, investigation and chase
- Wardrobe, bed and locker hiding
- Fuse, cutters and key to unlock the exit
- Optional mirror route with three hidden sigils
- Three nights and three endings
- Procedural animation, textures, lighting and synthesized sound
- Touch joystick + look controls; WASD + mouse on desktop
- Explorer, Standard and Nightmare modes

This is **Chapter 01**, one complete short level, not a full multi-level commercial game.

## Play

Open this repository's GitHub Pages site in a recent Chrome, Safari, Firefox or Edge browser with WebGL support. Headphones recommended. On phones, landscape gives a wider view.

Desktop: WASD move, mouse look, Shift run, C crouch, E use/hide, M map, Escape pause. Arrow left/right can also turn. On phones, use the left joystick, drag the right side to look, and tap USE near objects.

## Build and source

`index.html` is a self-contained, gzip-packed build of the clean static release. It has no remote asset requests or backend. Packing keeps delivery small; the unpacked source is not obfuscated or encrypted.

Run `python3 unpack_source.py` to recover `source/index.html`, `source/game.js`, `source/three.min.js` and the Three.js license. Serve that folder with `python3 -m http.server 8000 --directory source` to work on future levels.

All room models, textures, sound and animation are original procedural work. Three.js 0.160.1 is bundled under its included MIT license. No copied Granny assets, character models, levels, music or game code are used. No additional open-source license is assigned to the original game code or art.

There are no ads, analytics or accounts in the game. Ending collection is saved only in this browser; closing the page resets the current run.
