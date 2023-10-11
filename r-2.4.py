class Flower:
    """A flower class."""

    def __init__(self, name:str, num_petals:int, price:float):
        """Create a new flower instance

        name        the name of the flower
        num_petals  the number of petals the flower has
        price       the price of the flower  (type: float)
        """
        self._name = name
        self._num_petals = num_petals
        self._price = float(price)
    
    def get_name(self):
        """Return name of the flower"""
        return self._name
    
    def get_petal_count(self):
        """Return the number of petals"""
        return self._num_petals
    
    def get_price(self):
        """Return price of the flower."""
        return self._price
    
    def set_name(self, new_name):
        """Set flower name to new_name"""
        self._name = new_name
    
    def set_petal_count(self, val):
        """Set number of petals to val"""
        self._num_petals = val
    
    def set_price(self, px):
        """Set price of the flower to px"""
        self._price = px
    

if __name__ == '__main__':
    rose = Flower('Rose', 20, 150)
    print('Name:', rose.get_name())
    print('Petals:', rose.get_petal_count())
    print('Price:', rose.get_price())
    print()
    rose.set_name('Sunflower')
    rose.set_petal_count(23)
    rose.set_price(90)
    print('Name:', rose.get_name())
    print('Petals:', rose.get_petal_count())
    print('Price:', rose.get_price())
    