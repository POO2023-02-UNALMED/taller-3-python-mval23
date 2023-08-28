class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.canal = 1
        self.precio = 500
        self.volumen = 1
        self.control = None
        TV.numTV += 1

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def getCanal(self):
        return self.canal

    def setCanal(self, canal):
        if(canal >= 1 and canal <= 120 and self.estado):
            self.canal = canal

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if(volumen >= 0 and volumen <= 7 and self.estado):
            self.volumen = volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls, numTV):
        cls.numTV = numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if(self.canal < 120 and self.estado):
            self.canal += 1

    def canalDown(self):
        if(self.canal > 1 and self.estado):
            self.canal -= 1

    def volumenUp(self):
        if(self.volumen < 7 and self.estado):
            self.volumen += 1

    def volumenDown(self):
        if(self.volumen > 0 and self.estado):
            self.volumen -= 1
