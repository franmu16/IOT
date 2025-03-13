class Book:
    title=""
    author = ""
    num = 0
    
    def info(self):
        #print("Author: %s, Title: %s, Pages: %d" %(self.title,self.author,self.num))
        print('Author: {0}, Title:{1}, Pages:{2}'.format(self.author,self.title,self.num))
    
    def __init__ (self,title="",author="",num=0):
        self.title = title
        self.author = author
        self.num = num
    
b1 = Book("Alessandro Manzoni","Promessi Sposi",500)
b1.info()
b2 = Book()
b2.info()