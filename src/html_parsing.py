'''
Created on May 9, 2012

@author: MUNEER
'''
from pprint import pprint
from HTMLParser import HTMLParser
import urllib2
myhtml = urllib2.urlopen("http://www.flipkart.com/mobile/1/bestsellers")
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr
    def handle_endtag(self, tag):
        print "End tag  :", tag
    def handle_data(self, data):
        print "Data     :", data
my_parser = MyHTMLParser()
with open('flipkart_mobiles.html','w') as fl:
    fl.write(myhtml.read())
#print my_parser.feed(myhtml.read())
#pprint([x for x in dir(my_parser) if not x.startswith('_') ])
#print my_parser.get_starttag_text()
myhtml.close()
