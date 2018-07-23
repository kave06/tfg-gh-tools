from ghTools.climate import Climate


class Dht_22():

    def __init__(self, id, ambient):
        self.id = id
        self.ambient = Climate()
