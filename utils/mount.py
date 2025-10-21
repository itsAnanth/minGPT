"""

    Not a part of the actual training code
    only to be used to mount drive to colab env
    used to store and retrieve training data shards

"""

import importlib.util


def mountDrive():
    if importlib.util.find_spec("google") is not None:

        from google.colab import drive
        drive.mount('/content/drive')

    else:
        print("Not google colab environment")