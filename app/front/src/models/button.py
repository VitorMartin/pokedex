from app.front.src.models.i_dispositivo import I_Dispositivo

class Button(I_Dispositivo): 

    PINO_BTN = 20

    def __init__(self, resistor=gpio.PUD_DOWN, borda=gpio.RISING, pino=PINO_BTN):

        self._pino = pino
        self._setup = gpio.IN
        self._resistor = resistor
        self._borda = borda
        gpio.setup(self._pino, self._setup, pull_up_down=self._resistor)

    def getBorda(self):
        return self._borda
        pass
