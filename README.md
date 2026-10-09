# Neon Cyberpunk HyperOS Theme — Starter

A neon blue/purple theme project for Xiaomi / Redmi / POCO devices.

## Important compatibility note
This repository is a **starter/source project**, not a Xiaomi-certified theme. `build_mtz.py` creates a ZIP-based `.mtz` prototype with wallpapers and metadata. HyperOS versions and Themes app builds can require specific internal component paths or authorized theme packages, so successful packaging does **not** guarantee that every component will apply on POCO M6 5G / HyperOS 2.0.208.0.

## Repository structure
```text
Neon-Cyberpunk-HyperOS/
├── README.md
├── description.xml
├── requirements.txt
├── build_mtz.py
├── assets/
│   ├── home.svg
│   ├── lockscreen.svg
│   └── icon-concept.svg
├── theme/
│   └── README.md
└── .github/
    └── workflows/
        └── build.yml
```

## Build on GitHub
1. Create a public repository named `Neon-Cyberpunk-HyperOS`.
2. Upload all files and folders from this project.
3. Open **Actions** and enable workflows if GitHub asks.
4. Open **Actions → Build Neon Cyberpunk MTZ → Run workflow** (or push a commit).
5. When the workflow completes, open the run and download the `neon-cyberpunk-mtz-prototype` artifact.
6. Test only with a compatible Xiaomi theme workflow. If the Themes app rejects it, use Xiaomi Theme Editor / a compatible MTZ tool to import the assets and build a device-compatible theme.

## Local build
```bash
python -m pip install -r requirements.txt
python build_mtz.py
```
Output: `dist/NeonCyberpunk.mtz`

## What's included
- `assets/home.svg`: home wallpaper source artwork
- `assets/lockscreen.svg`: lock-screen wallpaper source artwork
- `assets/icon-concept.svg`: visual icon concept only; not a full app-icon replacement pack
- `description.xml`: theme metadata
- `build_mtz.py`: renders SVG wallpaper artwork to PNG and packages a prototype MTZ

## Customize
Edit the SVG files in `assets/`. The design canvas is 1080 × 2400 pixels.
Use only artwork, fonts, and icons you own or have permission to use.

## Disclaimer
Independent community project; not affiliated with or endorsed by Xiaomi. Xiaomi and HyperOS are trademarks of their respective owners.
