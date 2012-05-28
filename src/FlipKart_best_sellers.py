'''
Created on May 9, 2012

@author: MUNEER
'''
from pprint import pprint
from BeautifulSoup import BeautifulSoup
import urllib2

'''
The hierarchy in best seller results is as follows:
Category:
--->Book
--->Author

--->Book
--->Author

--->Book
--->Author

Category:
--->Book
--->Author

--->Book
--->Author etc..

To parse we first search for the Category html divs and iterate over these categories.
Inside a particular Category, we iterate again searching for books and authors. We save the list in 
a dictionary with concerned Category as the key name.
'''

def get_best_seller_books():
    best_sellers = {}
    myhtml = urllib2.urlopen("http://www.flipkart.com/books/bestseller")
    #myhtml = open("flipkart_ref.html",'r')
    soup = BeautifulSoup(myhtml.read())
    myhtml.close()
    best_seller_categories = soup.findAll('div', attrs={'class':"line fk-litems-section "})
    for categories in best_seller_categories:
        category_div = categories.findAll('div', attrs={'class':"fk-landing-module-title"})
        category = category_div[0].h2.string
        best_sellers[category] = []
        best_seller_divs = categories.findAll('div', attrs={'class':"fk-product-thumb fkp-medium"}) 
        for items in best_seller_divs:
            book = items.findAll('a', attrs={'class':"title tpadding5 fk-anchor-link"})[0]['title']
            #author = items.span.string
            best_sellers[category].append(book)
    return best_sellers


def get_best_seller_mobiles():
    myhtml = urllib2.urlopen("http://www.flipkart.com/mobile/1/bestsellers")
    #myhtml = open("flipkart_mobiles.html",'r')
    soup = BeautifulSoup(myhtml.read())
    myhtml.close()
    best_selling_phones = []
    best_seller_categories = soup.findAll('h2', attrs={'class':"fk-srch-item-title fksd-bodytext"})
    for phones in best_seller_categories:
        phone_name = phones.a.string
        best_selling_phones.append(phone_name)
    return best_selling_phones
    
if __name__ == '__main__':
    pprint(get_best_seller_books())#use conventional print as below if unicode is an issue
    for items in get_best_seller_mobiles():
        print items
    
    
    
    
    
    
    
    
