"""Top-level package for catplotlib."""
import random
import sys
from io import BytesIO
from urllib.parse import quote

import matplotlib
import matplotlib.pyplot as plt
import requests

CATS = ["🐱", "😹", "😻", "🙀", "😿", "😽", "😸", "😺", "😾", "😼"]
DEFAULT_BACKEND = matplotlib.get_backend()
URL = "https://cataas.com/cat"


class CatError(OSError):
    pass


def plot(says=None):
    url = URL

    if says is not None:
        url = f"{url}/says/{quote(says)}"

    try:
        r = requests.get(url)
    except requests.RequestException as e:
        raise CatError(f"Cat-astrophe!") from e

    if not r.status_code == 200:
        raise CatError(
            f"Cat-astrophe! That didn't work because '{r.reason}'",
        )

    data = BytesIO(r.content)
    img = plt.imread(data, format="jpg")

    return plt.imshow(img)


def catterplot(n=10):
    cats = CATS

    x = [random.random() * 10 for _ in range(n)]
    y = [random.random() * 10 for _ in range(n)]
    markers = random.choices(cats, k=n)
    scatter = plt.scatter(x, y, color="white")

    matplotlib.use("module://mplcairo.macosx")
    print(f"Backend is now {matplotlib.get_backend()}")

    prop = matplotlib.font_manager.FontProperties(
        fname="/System/Library/Fonts/Apple Color Emoji.ttc"
    )
    for x0, y0, cat in zip(x, y, markers):
        plt.annotate(
            cat, (x0, y0), ha="center", va="bottom", fontsize=30, fontproperties=prop
        )

    plt.title("Catterplot")
    plt.xlabel("x-catxis")
    plt.ylabel("y-catxis")
    plt.xlim(min(x) - 3, max(x) + 3)
    plt.ylim(min(y) - 3, max(y) + 3)

    return scatter
