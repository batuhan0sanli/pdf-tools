# --------------- IMPORT ---------------
# --------------------------------------
from pyfiglet import Figlet
import os

# --------------- FIGLET ---------------
def figlet():
    os.system("clear")
    f = Figlet(font='slant')
    print(f.renderText('PDF Tools'))
    return None

# --------------- EXIT ---------------
def quit():
    figlet()
    print("")
    print("Teşekkürler..")
    exit()