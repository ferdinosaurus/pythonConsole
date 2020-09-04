def printNewLine():
    for x in range(25):
        print()

def insertBookByTxt():
    f = open("ListBook.txt", "r")
    test = f.read().splitlines()
    return test

def printBookList(bookList):
    for book in bookList:
        print(book)

def printMenu():
    print("===========")
    print("1.Add")
    print("2.Update")
    print("3.Delete")
    print("4.Exit")

def add():
    print("input book : ")
    book = str(input())
    bookList.append(book)

def update():
    print("old book name : ")
    oldBookName = str(input())
    indexBook = checkBookIndex(oldBookName)
    if(indexBook!=-1):
        print("new book name : ")
        bookName = str(input())
        bookList[indexBook] = bookName
    else:
        print("not found or Bugs")
        input()
    
def checkBookIndex(book):
    index = -1
    for i in range(0,len(bookList)):
        if(book==bookList[i]):
            index = i
        break
    return index

def delete():
    print("input book name: ")
    book = str(input())
    bookList.remove(book)

#init
bookList = insertBookByTxt()
menu=0

#menu exit
while menu!=4:
    printNewLine()
    printBookList(bookList)
    printMenu()
    print("Choose Menu : ")
    menu = int(input())

    if(menu==1):
        add()
    elif (menu==2):
        update()
    elif (menu==3):
        delete()
    
    
    