class ProductRecord(object):

    def __init__(self, prodNum, desc, quantity, price): #initialise instances
        self._prodNum = prodNum
        self._desc = desc
        self._quantity = quantity
        self._price = price

    def __str__(self):
        return 'ProductRecord: {} {} {} {}'.format(self._prodNum, self._desc, self._quantity, self._price)

    def __eq__(self, pr):
        return self._prodNum == pr._prodNum and self._price == pr._price
