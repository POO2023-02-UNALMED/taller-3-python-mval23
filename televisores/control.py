class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self):
        self._tv.turnOn()

    def turnOff(self):
        self._tv.turnOff()

    def canalUp(self):
        self._tv.canalUp()

    def canalDown(self):
        self._tv.canalDown()

    def volumenUp(self):
        self._tv.volumenUp()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def enlazar(self, tv):
        self._tv = tv
        self._tv.setControl(self)

    def setTV(self, tv):
        self._tv = tv

    def getTV(self):
        return self._tv
