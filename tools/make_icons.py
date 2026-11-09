# -*- coding: utf-8 -*-
"""Generate the launcher icons from the Thinker emblem in quizara_logo.png.

Usage (from the project root):
    python tools/make_icons.py

Writes the adaptive icon (Android 8+), legacy square/round icons (Android 6-7) into
app/src/main/res, and the 512x512 Play Store icon into store/play_icon_512.png.
Requires: pip install pillow
"""
import os

from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, 'app', 'src', 'main', 'res')
SOURCE = os.path.join(RES, 'drawable-nodpi', 'quizara_logo.png')

# The emblem (statue, circle, question marks) without the QUIZAPA lettering below it.
EMBLEM_BOX = (300, 115, 985, 766)
BACKGROUND = (11, 15, 20)            # the logo's own navy, also @color/ic_launcher_background
DENSITIES = {'mdpi': 1, 'hdpi': 1.5, 'xhdpi': 2, 'xxhdpi': 3, 'xxxhdpi': 4}

# Adaptive icons are 108dp; launchers only promise to keep the central 66dp circle.
ADAPTIVE_DP = 108
ADAPTIVE_EMBLEM_DP = 70
# Legacy icons are 48dp and shown as-is, so the emblem can be larger.
LEGACY_DP = 48
LEGACY_EMBLEM_RATIO = 0.86


def emblem(size):
    img = Image.open(SOURCE).convert('RGB').crop(EMBLEM_BOX)
    img.thumbnail((size, size), Image.LANCZOS)
    return img


def centered(canvas, img):
    canvas.paste(img, ((canvas.width - img.width) // 2, (canvas.height - img.height) // 2))
    return canvas


def mask(size, round_icon):
    scale = 4  # draw large then shrink, for smooth edges
    m = Image.new('L', (size * scale, size * scale), 0)
    d = ImageDraw.Draw(m)
    box = (0, 0, size * scale - 1, size * scale - 1)
    if round_icon:
        d.ellipse(box, fill=255)
    else:
        d.rounded_rectangle(box, radius=int(size * scale * 0.18), fill=255)
    return m.resize((size, size), Image.LANCZOS)


def save(img, *parts):
    path = os.path.join(*parts)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, optimize=True)
    return path


def main():
    for name, factor in DENSITIES.items():
        folder = os.path.join(RES, 'mipmap-' + name)

        # Adaptive foreground: the emblem on transparency; the navy comes from the background layer.
        size = round(ADAPTIVE_DP * factor)
        fg = centered(Image.new('RGBA', (size, size), (0, 0, 0, 0)),
                      emblem(round(ADAPTIVE_EMBLEM_DP * factor)).convert('RGBA'))
        save(fg, folder, 'ic_launcher_foreground.png')

        # Legacy icons for launchers without adaptive icon support.
        size = round(LEGACY_DP * factor)
        art = centered(Image.new('RGB', (size, size), BACKGROUND), emblem(round(size * LEGACY_EMBLEM_RATIO)))
        for file, round_icon in (('ic_launcher.png', False), ('ic_launcher_round.png', True)):
            icon = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            icon.paste(art, (0, 0), mask(size, round_icon))
            save(icon, folder, file)

    adaptive = ('<?xml version="1.0" encoding="utf-8"?>\n'
                '<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n'
                '    <background android:drawable="@color/ic_launcher_background" />\n'
                '    <foreground android:drawable="@mipmap/ic_launcher_foreground" />\n'
                '</adaptive-icon>\n')
    for file in ('ic_launcher.xml', 'ic_launcher_round.xml'):
        path = os.path.join(RES, 'mipmap-anydpi-v26', file)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(adaptive)

    with open(os.path.join(RES, 'values', 'ic_launcher_background.xml'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n'
                '    <color name="ic_launcher_background">#%02X%02X%02X</color>\n</resources>\n' % BACKGROUND)

    # Play Store listing icon: full square, Play applies its own rounding.
    play = centered(Image.new('RGB', (512, 512), BACKGROUND), emblem(round(512 * LEGACY_EMBLEM_RATIO)))
    print('wrote', save(play, ROOT, 'store', 'play_icon_512.png'))
    print('wrote mipmaps for', ', '.join(DENSITIES))


if __name__ == '__main__':
    main()
