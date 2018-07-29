class Book(object):
    def __init__(self, title, author, pages):

        print "A book has been created"
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  #this is a special method
        return "title: %s, author: %s, pages: %s" %(self.title,self.author,self.pages)

    b = book('python', 'Diana', 100)
    print b
    Title: python, author: Diana, pages 100

#Another special methd, in conjuction with that length function
    def __len__(self):
        return self.pages 

        len(b)
        100 #results

#Another special mthd. Special methods are defined using underscores
     def __del__(self): #you can delete a record from memory
        print "A book is gone"

        b.title
        "python"

        del b
        A book is gone #prints that

        b.title #it's not defined, so that make sense
