class book:
    def __init__(self, pgs):
        self.pages = pgs
        
        
b1 = book(102)
b2 = book(120)
b3 = book(302)
b4 = book(502)


total = b1.pages + b2.pages + b3.pages + b4.pages

print(total)