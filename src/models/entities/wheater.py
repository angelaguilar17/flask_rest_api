class Wheater():

    def __init__(self, id, ciudad=None, hora=None, clima=None) -> None:
        self.id = id
        self.ciudad = ciudad
        self.hora = hora
        self.clima = clima

    def to_JSON(self):
        return {
            'id' : self.id,
            'ciudad' : self.ciudad,
            'hora' : self.hora,
            'clima' : self.clima
        }