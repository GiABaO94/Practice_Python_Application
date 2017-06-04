#Practice Class
class Line(object):
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 + (y2-y1)**2 )**0.5

    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return float((y2-y1))/(x2-x1)

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)
print(li.distance())
print(li.slope())


#Practice Inheritance
class Animal(object):
    spec = "Animal"
    def __init__(self):
        self.type = 'Dog'
    def Activity_01(self):
        return 'Depend on the animal'
    def Activity_02(self):
        return 'This is an animal (Activity 2)'

class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name = name
    def Activity_01(self):
        return "Gau gau"

dog = Dog(name = 'Husky')
print(dog.type)
print(dog.name)
print(dog.Activity_01())
print(dog.Activity_02())

#Practice Special Method

class Book(object):
    Product = "Designed by BaoVHG"
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    #Method to print
    def __str__(self):
        return 'Title: %s ----- Author: %s ----- No.of.Pages: %s \n%s' % (self.title, self.author, self.pages, self.Product)

    #Method to calc lengh
    def __len__(self):
        return self.pages

    #Method to delete
    def __del__(self):
        print('The book is deleted')

book = Book('Neu gap nguoi ay cho toi gui loi chao','Ichikawa',345)
print(book)
print(len(book))
del book
print(book)