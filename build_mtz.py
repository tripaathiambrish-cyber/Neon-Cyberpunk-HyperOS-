from pathlib import Path
import shutil
import zipfile
import cairosvg
from PIL import Image

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
STAGE = DIST / "mtz-root"

def render_svg(source: Path, target: Path):
    target.parent.mkdir(parents=True, exist_ok=True)
    cairosvg.svg2png(url=str(source), write_to=str(target), output_width=1080, output_height=2400)

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    (STAGE / "wallpaper").mkdir(parents=True)
    (STAGE / "lockscreen").mkdir(parents=True)

    render_svg(ROOT / "assets" / "home.svg", STAGE / "wallpaper" / "home.png")
    render_svg(ROOT / "assets" / "lockscreen.svg", STAGE / "lockscreen" / "lockscreen.png")

    # Convert to JPEG previews for easier inspection.
    for src, dest in [
        (STAGE / "wallpaper" / "home.png", DIST / "home-preview.jpg"),
        (STAGE / "lockscreen" / "lockscreen.png", DIST / "lockscreen-preview.jpg"),
    ]:
        dest.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(src).convert("RGB") as im:
            im.save(dest, quality=92, optimize=True)

    shutil.copy2(ROOT / "description.xml", STAGE / "description.xml")
    output = DIST / "NeonCyberpunk.mtz"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in STAGE.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(STAGE).as_posix())

    print(f"Created prototype: {output}")
    print("NOTE: Xiaomi/HyperOS may require additional editor-exported component files/paths.")
    print("This package is a starter prototype, not a guarantee of successful installation.")

if __name__ == "__main__":
    main()
