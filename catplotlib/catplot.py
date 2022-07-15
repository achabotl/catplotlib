"""Top-level package for catplotlib."""

import matplotlib.pyplot as plt
import requests

from io import BytesIO
from urllib.parse import quote


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
