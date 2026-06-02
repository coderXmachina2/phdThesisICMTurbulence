from PIL import Image
import os

images = {"bulletCluster.jpg": "bulletCluster_sq.jpg",
	  "Macsj0717.jpg":     "Macsj0717_sq.jpg",
          "elgordoCluster.jpg":"elgordoCluster_sq.jpg",
          "musketball.jpg":    "musketBall_sq.jpg",}

TARGET = 1000

for src, dst in images.items():
    img = Image.open(src)
    w, h = img.size
    # Centre crop to square
    side = min(w, h)
    left  = (w - side) // 2
    top   = (h - side) // 2
    img   = img.crop((left, top, left + side, top + side))
    img   = img.resize((TARGET, TARGET), Image.LANCZOS)
    img.save(dst, quality=95)
    print(f"{src} → {dst}")
