# 12 · TumGard × H. pylori: animated ad storyboard

*hugg · Meta video ads · Built 27 Oct 2026 · Status: ready for keyframe generation · Updated: TumGard is a black lehyam*
*Format: claymation mechanism ad (reference: Flakes anti-dandruff ad). Script: "Bacteria gaya, nuksaan wahi raha".*

24 shots, about 55 seconds, 9:16. Each shot has: the captions it covers, the colour stage, the cast references to upload, a keyframe prompt, and the camera move for image-to-video.

---

## 0. Finish the cast sheet first (still to generate)

S03–S09 and S14–S17 depend on these. Use the Rohan turnaround (R-B) as a style reference for each.

**#4a · Lining, damaged (L-D)** · new image · 9:16
```
Macro miniature-set landscape inside a human stomach, built entirely from clay, matching the clay texture and finish of the reference image. Soft rolling folds of pink stomach lining like gentle dunes stretching to the horizon. The surface is pocked with raw red craters (#C23B2E) of different sizes, their edges inflamed and swollen. A shiny clear-gel protective layer covers the folds but is torn and patchy, missing over the craters. Three bright orange droplets (#F07A1A) fall from above; where one lands in a crater, a tiny wisp of steam rises. No characters, no creatures. Mood: slightly dim, uncomfortable, a little unsettling, but not gory. Keep the middle third of the frame simple and uncluttered. Camera: low angle, macro lens, shallow depth of field, horizon soft and blurred. Vertical 9:16. Style: handcrafted stop-motion claymation look, visible plasticine texture and tool marks, tactile miniature-set realism. No outlines, no flat vector, no glossy CGI plastic. No text.
```
Pick the **simplest, clearest composition**, not the prettiest. It has to survive two rounds of edits.

**#4b · Lining, healing (L-H)** · edit of L-D
```
Edit this image. Keep the exact same camera angle, same ridges, same horizon, same crater positions and sizes. Do not move or reshape anything. Remove the falling droplets and the steam.

A thick, glossy, velvety black lehyam (a soft herbal paste, like a smooth balm, not runny liquid, not tar, not oil) has been gently laid into the craters on the left half of the frame and into half of the central crater. It sits as smooth rounded black pools with a soft satin sheen, lit by a warm amber-gold glow (#E0A030) along its edges and highlights, as if it is quietly working.

Around the edges of each black pool, the black is soaking in and revealing fresh, healthy pink lining (#E8A3A0) underneath, and the clear gel layer is knitting back together over it. The craters on the right half are still raw red and uncovered.

Overall lighting slightly warmer than before. Calm and soothing, not dirty, not sticky, not ominous. Same claymation style. No text.
```

**#4c · Lining, healthy (L-OK)** · edit of L-H
```
Edit this image. Keep the exact same camera angle, same ridges, same horizon. Do not move or reshape anything. The black lehyam has fully soaked in and is completely gone; no black remains anywhere. Every crater is now healed into smooth, healthy pink lining (#E8A3A0), with only faint soft marks where the craters were. An intact, continuous glossy clear-gel layer covers the whole surface. A faint warm amber-gold glow (#E0A030) lingers in the light. Warm, calm, healthy. Same claymation style. No text.
```
**Check:** lay L-D, L-H and L-OK side by side. The folds, horizon and crater positions must match. If one drifted, re-run that edit from the previous state; don't chain off a drifted image.

**#5 · Prop sheet (P)** · new image · 16:9
```
Prop sheet of small clay objects on a plain light-grey studio background, matching the clay texture and finish of the reference image: two antibiotic capsules in clinical white and pale blue (#DDEBF5), an empty foil blister strip, three orange acid droplets (#F07A1A), a small pile of black kalonji seeds, two pieces of licorice root, a steel spoon holding half a spoonful of thick, glossy black lehyam paste with a soft satin sheen. Each object isolated with space around it. Soft even studio lighting. No text.
```

**#6 · TumGard jar (J)** · upload the real product photo
```
Recreate the attached product as a clay miniature in the same claymation style as the second reference image: same shape, same proportions, same colours and label layout, with visible plasticine texture. Place it on a simple warm stone pedestal with soft amber-gold lighting (#E0A030). Plain softly blurred background. Do not invent any text.
```
Use it for shape and lighting only. The real label is comped in the edit.

---

## 1. How to run this

1. **Upload the listed references** with every prompt. They are what keeps Rohan and the villain consistent.
2. **"Edit of Sxx"** means: upload that shot's chosen keyframe and edit it. Don't generate it fresh. This is how the composition holds between shots that continue each other.
3. **Paste the style anchor** (§3) at the end of every prompt where it says `[STYLE ANCHOR]`.
4. **No text in any image.** Captions, the end card and the real TumGard label are all added in the edit, not generated (the Typographer lens in doc 11 blocks generated type).
5. **Pick for clarity, not beauty.** One subject, a calm middle third (the captions sit there), and a background that blurs away.
6. **Secondary people** (family, the nutritionist) stay soft-focus or partly out of frame, so they don't need their own cast sheets. The one exception is the nutritionist in S22. See §5.

---

## 2. Reference key

| Code | Asset |
|---|---|
| **R-B** | Rohan, before: moustache turnaround, grey-blue shirt |
| **R-F** | Rohan, face sheet: image 3, bottom row |
| **R-A** | Rohan, after: off-white shirt, warm light, image 1 |
| **HP** | H. pylori hero: the fusilli villain |
| **HP-S** | H. pylori pose sheet: image 1 |
| **L-D** | Stomach lining, damaged (#4a) |
| **L-H** | Stomach lining, healing (#4b) |
| **L-OK** | Stomach lining, healthy (#4c) |
| **P** | Prop sheet (#5): capsules, blister strip, acid drops, kalonji, licorice, spoon |
| **J** | TumGard jar: the real pack shot (clay version for shape only) |

---

## 3. Style anchor (paste wherever `[STYLE ANCHOR]` appears)

```
Style: handcrafted stop-motion claymation look, matching the clay texture and finish of the reference images. Visible plasticine texture, subtle fingerprints and tool marks, soft rounded forms, slightly exaggerated proportions. Shot with a real macro lens: shallow depth of field, soft bokeh, tactile miniature-set realism. Composition: one clear subject, uncluttered, background simple and softly blurred, the middle third of the frame calm. Vertical 9:16. No outlines, no flat vector, no glossy CGI plastic. No text, no letters, no labels.
```

### Colour stages (declared meanings, doc 11 Lens 2)

| Stage | Palette | Hex |
|---|---|---|
| **Before** | Cool grey-blue, desaturated | #6B7A8A |
| **Villain** | Mustard-olive bacteria on pink lining | #A89A3C / #E8A3A0 |
| **Antibiotic** | Clinical white-blue | #DDEBF5 |
| **Damage** | Raw red craters, orange acid | #C23B2E / #F07A1A |
| **TumGard** | Glossy black lehyam, always lit with a warm amber-gold glow (the glow carries the "warm = TumGard" meaning; the black is the real product) | #141414 + #E0A030 |
| **After** | Warm golden sunlight | #F5C77A |

---

## 4. The shots

### Beat 1 · Hook (Before)

**S01** · *Antibiotic ka course / poora kiya.* · Before
Refs: R-B, R-F, P
```
Rohan, the clay man from the reference images, sits on the edge of a simple bed in a sparse bedroom at night. Same face, deep brown skin, full black moustache, grey-blue shirt. He holds an empty foil antibiotic blister strip in one hand and presses the other hand flat on his upper stomach, below the ribs. Tired, uncomfortable expression, brows pulled up and together. Cool grey-blue lighting from a window, the room minimal and softly blurred. Medium shot, Rohan centred. [STYLE ANCHOR]
```
Camera: slow push-in.

**S02** · *Toh jalan / abhi bhi kyu?* · Before
Refs: edit of S01, R-F
```
Edit this image. Same scene, same lighting, same Rohan. Reframe as a tight close-up on his face and shoulders. Stronger pain: brows pulled up tightly together, eyes slightly squeezed, mouth tight under the moustache, his hand pressed below his ribs just visible at the bottom of the frame. No text.
```
Camera: hold, slight push. This is the thumb-stop frame; the face must read at 25% size.

### Beat 2 · Catch: into the stomach (Villain)

**S03** · *Kyunki H. pylori* · Villain
Refs: L-OK, HP-S
```
Edit this image. Same landscape, same camera angle, same folds. Add a group of six of the mustard-olive fusilli-shaped villains from the second reference, with the same body, tails and face design, crawling over the glossy gel layer toward the camera, smug and scheming. The lining is still healthy pink. Slightly dimmer, more ominous lighting. No text.
```
Camera: fast dive in from above, landing low among the villains. (A whoosh through Rohan's shirt into this frame is the cut.)

**S04** · *saalon tak / aapki lining / khaata raha.* · Villain → Damage
Refs: L-D, HP-S
```
Edit this image. Same landscape, same camera angle, same crater positions. Add five of the fusilli-shaped villains from the second reference: two burrowing head-first through the torn gel layer, one chomping into the edge of a red crater with its mouth wide open, two grinning beside it. Same body shape, colour and face design as the reference. No text.
```
Camera: slow lateral dolly across the landscape.

**S05** · *(same captions continue)* · Villain
Refs: edit of S04, HP
```
Edit this image. Same scene. Move in to a close-up of one villain sitting on the rim of a red crater, eyes half-closed, letting out a contented burp with a tiny bubble. Background blurred. No text.
```
Camera: static, small bounce on the burp. (The comic beat.)

### Beat 3 · The antibiotic does its job (Antibiotic)

**S06** · *Antibiotic ne / bacteria hata diya.* · Antibiotic
Refs: edit of S04, P
```
Edit this image. Same landscape, same villains. Two clay antibiotic capsules in white and pale blue (#DDEBF5) drop from above and land among the villains, cracking open and releasing a clean white-blue wave of liquid. The villains look up, startled. Cool, clean, clinical light from the capsules. No text.
```
Camera: tilt down with the falling capsules.

**S07** · *Sahi kiya.* · Antibiotic
Refs: edit of S06, HP-S
```
Edit this image. Same landscape. The white-blue wave now sweeps across the whole frame from left to right. The villains are panicking, eyes wide, mouths open, tumbling and being washed out of frame in splashing water, exactly like the panicked pose in the reference. Same body shape and face design. No text.
```
Camera: whip-pan with the wave. This should feel like a win: the medicine is good.

### Beat 4 · The turn: the damage stays (Damage)

**S08** · *Par jo lining / usne khaayi, / woh wahi rahi.* · Damage
Refs: L-D
Use **L-D as-is** (#4a). No generation needed: an empty, quiet, cratered landscape with the gel layer torn.
Camera: slow pull-back and rise. The quiet after the wave. Hold it.

**S09** · *Isiliye / course ke baad bhi* · Damage
Refs: edit of L-D
```
Edit this image. Same landscape. Close-up on one raw red crater. A single bright orange droplet (#F07A1A) lands in it and sizzles, a small wisp of steam rising, the crater edges flinching. Background blurred. No text.
```
Camera: static macro, droplet falls into frame.

**S10** · *jalan.* · Before
Refs: R-B, R-F
```
Rohan, the clay man from the reference images, sits alone at a small dining table at night with a plate of plain food barely touched. Same face, deep brown skin, full black moustache, grey-blue shirt. One hand pressed on his upper stomach below the ribs, wincing, brows pulled up and together. Cool grey-blue light, the room softly blurred. Medium shot, the table and Rohan centred, the frame composed so the same table and angle can be reused later. [STYLE ANCHOR]
```
Camera: static. **This composition comes back in S23**, so keep the chosen frame.

### Beat 5 · Persona: frustration montage (Before)

**S11** · *Do course. / Teen test.* · Before
Refs: R-B, P
```
Rohan, the clay man from the reference images, stands at a kitchen counter, full body, in his grey-blue shirt. On the counter: a few foil blister strips, two small antacid bottles, and two plain paper envelopes of test reports. He looks down at them, tired. Cool grey-blue light, the kitchen minimal and softly blurred. No text on any object. [STYLE ANCHOR]
```
Camera: static, slight push.

**S12** · *Phir bhi / wahi pet.* · Before
Refs: edit of S11
```
Edit this image. Same Rohan, same counter, same camera. The pile has grown a lot: many more blister strips, antacid bottles, report envelopes, and three bowls of plain khichdi stacked around him, spilling over the counter edge. His shoulders drop, his expression defeated. No text on any object. No text.
```
Camera: same frame, and the cut between S11 and S12 is a jump cut (the pile "grows"). Optionally a third jump with an even bigger pile.

### Beat 6 · Dream outcome (After, brief)

**S13** · *Socho: / course khatam, / aur pet bhi shaant.* · After
Refs: R-A
```
Rohan, the clay man from the reference image, same face, same deep brown skin tone as the reference, full black moustache, off-white shirt, laughing at a warm family dinner table with a full plate of spicy food in front of him. Two or three family members at the edges of the frame, softly out of focus. Warm golden evening light (#F5C77A). Medium close-up on Rohan. [STYLE ANCHOR]
```
Camera: gentle drift. A short flash (about 1.5 s), then a hard cut back.

### Beat 7 · Mechanism: TumGard arrives (TumGard)

**S14** · *Usi lining pe / TumGard / kaam karta hai.* · TumGard
Refs: J, P
```
The product from the reference image, recreated as a clay miniature with the same shape, proportions and colours, standing on a simple warm stone pedestal. In front of it, a steel spoon holds half a spoonful of thick, glossy black lehyam with a satin sheen. Black kalonji seeds and two pieces of licorice root tumble through the air around it in slow motion. Warm amber-gold light (#E0A030) from behind, soft glow. Product centred, background soft amber blur. No text, no label text. [STYLE ANCHOR]
```
Camera: slow orbit. **Comp the real label/pack shot in the edit** (Lens 6 blocks a generated label).

**S15** · *Kalonji / aur licorice / lining ko / support karte hain.* · TumGard
Refs: L-D → L-H → L-OK
TumGard is a black lehyam: in motion it should settle into each crater like a soft balm and soak in, revealing pink, never spread like oil or tar.
**Use the three lining states as a start/middle/end sequence** for image-to-video: L-D as the start frame, L-H as the middle, L-OK as the end. If your video tool takes only start and end frames, run two clips (L-D → L-H, then L-H → L-OK) and cut them together.
Camera: locked, or a very slow drift. The change has to be gradual (red → pink, gel knitting closed), never instant magic.

**S16** · *(same captions, tail)* · TumGard
Refs: edit of L-OK
```
Edit this image. Same landscape, same camera. Close-up on the healed surface: one orange acid droplet lands on the intact glossy gel layer and beads off harmlessly, rolling away. Calm, warm light. No text.
```
Camera: static macro. The payoff of S09: same droplet, opposite result.

**S17** · *Doctor ki dawa / apna kaam kare, / TumGard apna.* · Antibiotic + TumGard
Refs: P, J
```
Two objects side by side on a simple surface, given equal weight, like partners: on the left, a clay foil antibiotic blister strip with white-and-pale-blue capsules, lit cool clinical white-blue; on the right, the clay TumGard jar from the reference with a spoon of glossy black lehyam in front, lit warm amber-gold. A soft split in the light down the middle. No text, no label text. [STYLE ANCHOR]
```
Camera: slow push-in. Comp the real label.

### Beat 8 · Effort (After)

**S18** · *Chai band nahi. / Bas aadha chammach / lunch ke baad,* · After
Refs: R-A
```
Rohan, the clay man from the reference image, same face, same deep brown skin tone as the reference, full black moustache, off-white shirt with an office ID lanyard, sits at an office desk at lunchtime. He holds a small glass of chai in one hand and lifts a steel spoon holding half a spoonful of glossy black lehyam to his mouth with the other, relaxed and smiling. Laptop and the office softly blurred behind him. Warm daylight. [STYLE ANCHOR]
```
Camera: static, small push.

**S19** · *aadha dinner ke baad. / 60 din.* · After
Refs: R-A
```
Rohan, the clay man from the reference image, same face, same deep brown skin tone as the reference, full black moustache, off-white shirt, at home in the evening after dinner, eating half a spoonful of glossy black lehyam off a steel spoon, an empty dinner plate on the table. Calm, content. Warm lamplight, home softly blurred. [STYLE ANCHOR]
```
Camera: static.

### Beat 9 · Time (After)

**S20** · *Log report karte hain: / pehle hafte mein / khane ke baad wali / jalan kam.* · After
Refs: edit of S19, R-A
```
Edit this image. Same Rohan, same table. He has finished a full meal and leans back in his chair, both hands resting on the table, relaxed and comfortable, a small satisfied smile. No hand on his stomach. No text.
```
Camera: slow pull-back. The hands on the table are the proof.

### Beat 10 · Risk (After)

**S21** · *Aur aap / akele shuru nahi karoge. / Founder ka seedha email,* · After
Refs: R-A
```
Over-the-shoulder close-up of Rohan, the clay man from the reference image, same face and off-white shirt, holding a clay smartphone. The screen shows a simple glowing envelope icon. He is smiling a little, surprised. Warm light, background softly blurred. No readable text anywhere. [STYLE ANCHOR]
```
Camera: static. **Comp the real founder email** on the phone screen in the edit.

**S22** · *phir asli nutritionist ka call. / Bot nahi.* · After
Refs: R-A, NUT (see §5)
```
Rohan, the clay man from the first reference, same face and off-white shirt, sits on his sofa holding a phone in a video call. On the phone screen, the clay nutritionist from the second reference smiles and talks. Rohan nods along, listening. Warm home light, background softly blurred. No text. [STYLE ANCHOR]
```
Camera: slow push toward the phone.

### Beat 11 · Close (After)

**S23** · *Course khatam, / aur pet bhi shaant.* · After
Refs: edit of S10, R-A
```
Edit this image. Same dining table, same camera angle, same framing. Transform it: warm golden evening light (#F5C77A) instead of cool grey-blue. Rohan now looks like the after reference: off-white shirt, same face, same deep brown skin tone, full black moustache, upright and happy, reaching for a second helping of spicy food from a full table. Two family members at the edges of the frame, softly out of focus, laughing. No text.
```
Camera: the same static frame as S10. The callback works because nothing moves except the light and the man.

**S24** · *Buy 2 Get 1, / saath mein free diet plan. / Aaj.* · End card
**Built in the edit, not generated.** Flat brand-colour background, the real TumGard pack shot, three benefit lines ticking in one at a time (Flakes-style). Benefit lines and the offer go to the writer and the regulatory pass.

---

## 5. One new cast item: the nutritionist (S22)

Run before S22. Same rules as Rohan: describe her first, plain background.
```
An Indian woman in her early 30s, made of clay. A warm, friendly, professional nutritionist. Medium brown skin, black hair tied back neatly, small simple earrings, kind expressive eyes, a gentle smile. Wearing a plain teal kurta with a small white collar. Head-and-shoulders, front view, on a plain light-grey studio background, nothing else in the frame. Slightly stylised stop-motion proportions matching the reference. [STYLE ANCHOR]
```

---

## 6. Before animating: checks

- **Same man:** lay all the Rohan shots side by side. Skin tone and moustache drift first (it happened on the R-A edit).
- **Same villain:** the body is a straight twisted spiral in every shot, never coiled.
- **Same landscape:** S03–S09 and S15–S16 read as one place. Compare crater positions.
- **Colour meanings hold:** grey-blue only before, black lehyam with an amber glow only for TumGard (black lehyam must never look like oil, tar or dirt), white-blue only the antibiotic.
- **TumGard never touches a bacterium.** It appears only after the villains are gone (claim safety; doc 06 TG3).
- Then run the Vox panel (doc 11), Phone Test first.

## 7. Open items

1. Real TumGard pack shot and label file for S14, S17 and S24.
2. The real founder email screenshot for S21.
3. The video tool, which sets the format of the motion prompts and whether S15 can take three frames.
4. Claim checks carried over from the script: "Chai band nahi" (doc 06 §11, item 2), and the wording "Kalonji aur licorice lining ko support karte hain".
