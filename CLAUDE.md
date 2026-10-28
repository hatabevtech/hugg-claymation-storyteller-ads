# hugg animated ads: production desk

This repo is where the keyframes for hugg's claymation mechanism ads get generated. The thinking (script, storyboard, reviews) lives in the claude.ai project "Objective: Launch Better Ads"; this repo is production.

Current ad: **TumGard × H. pylori**. Read `storyboard.md` before doing anything.

## Files
- `storyboard.md`: the shot list. Section 2 is the reference key, section 3 the style anchor and colour stages, section 4 the shots (S01–S24), section 6 the checks.
- `cast/`: the locked cast sheet, named by reference code (`R-B.png`, `R-F.png`, `R-A.png`, `HP.png`, `HP-S.png`, `L-D.png`, `L-H.png`, `L-OK.png`, `P.png`, `J.png`, `NUT.png`). **Never regenerate these.** They are approved.
- `gen.py`: calls the Gemini image API. `python3 gen.py models` lists image models; `python3 gen.py run ...` generates options. See its docstring.
- `prompts/`: save each shot's final prompt as `prompts/Sxx.txt` before generating, so every frame is reproducible.
- `motion/MOTION.md`: Google Flow motion prompts (Frames to Video), one per clip.
- `frames/`: options as `Sxx_a.png` … `Sxx_d.png`; the approved pick copied to `frames/final/Sxx.png`.

## The API
- The Gemini key is attached by the environment's network proxy (header `x-goog-api-key`). Don't look for a key, don't ask for one, never print headers.
- Start with `python3 gen.py models` and use the best current image model (pass `--model`). Test with one tiny request before a batch.

## How to work
1. **Work in batches by beat** and stop after each for the user's approval:
   S01–S02 · S03–S09 · S10–S13 · S14–S17 · S18–S23. (S08 is `cast/L-D.png` as-is; S15 is the L-D → L-H → L-OK video sequence, so there's nothing to generate; S24 is built in the edit.)
2. For each shot: write the prompt to `prompts/Sxx.txt` (replace `[STYLE ANCHOR]` with the text from storyboard §3), attach the listed refs, generate 2 options (re-roll only if both fail a check).
3. **"Edit of Sxx" means edit**: pass the approved `frames/final/Sxx.png` as the FIRST `--ref`, then the cast refs. Never regenerate a shot that's meant to continue another.
4. **Look at every option yourself** (open the PNGs) and recommend one per shot, with one line on why. Reject and re-roll anything that fails a check below rather than presenting it.
5. Show the user the options and your pick. On approval, copy picks to `frames/final/` and commit with a short message per batch.

## Creative direction (from the user, after cut v1)
The mechanism visuals must be **visceral and emotional, not just clear**: the viewer should *feel* it. Stylised, never realistic or gory.
- **Damage:** make the hurt felt: angry, inflamed, throbbing red; the lining flinching; acid that stings.
- **The product applied:** the hero moment. Show how the lehyam looks and feels as it touches the lining: thick, velvety, glossy black settling like a soothing balm, the amber glow spreading warmth, the red calming to pink, the lining visibly relaxing. Linger on texture and relief.
- Prioritise more shots and closer angles of application (spoon, the lehyam's texture, it meeting the lining) when generating the next round.

## Checks (reject on any)
- **Rohan:** same face, deep brown skin tone, full black moustache, matching the cast sheets. Before = grey-blue shirt; after = off-white shirt, warm light. Skin tone drifts lighter in edits; watch it.
- **H. pylori:** straight twisted fusilli body in every frame, never coiled, never worm- or slug-like. Mustard-olive, angry V brows, jagged teeth.
- **Lining:** S03–S09 read as the same place as `cast/L-*`: same ridges, crater positions.
- **Colours mean one thing:** grey-blue = before only; white-blue = antibiotic only; glossy black lehyam with amber glow = TumGard only (it must never look like oil, tar or dirt); warm golden = after.
- **Claim safety:** TumGard never appears in a frame with a bacterium.
- **Composition:** one clear subject, calm uncluttered middle third (captions go there), background blurred.
- **No text** anywhere in a frame: no letters, labels or garbled writing.
- Indian cast always. Secondary people soft-focus at the frame edges.

## Don't
- Don't name animation studios or films in prompts; it drags in their characters.
- Don't change the script, captions or claims. Raise issues with the user instead.
- Don't overwrite anything in `cast/`.
