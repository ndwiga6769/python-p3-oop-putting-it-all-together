#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self.pages = page_count
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")  
kigogo = Book("Kigogo",30)
    
print(kigogo.title)
print(kigogo.pages)
        