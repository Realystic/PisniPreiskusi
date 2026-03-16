import sys
import os

#Pot do glavne mape projekta
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from upravljanje_pisnih_preiskusov import glavni_meni

if __name__ == "__main__":
    glavni_meni()