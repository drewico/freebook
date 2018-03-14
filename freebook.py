#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple free books advisor, using URLLIB2 and BeautifulSoup
Created on 03/10/2018

@author: luisrosales
'''
import urllib2
import bs4

class Book(object):

    """Scrapy free book, for https://www.packtpub.com/packt/offers/free-learning
    """

    def __init__(self):
        super(Book, self).__init__()

    def get_web_page(self, url):
        """
        Retrieves an HTML URL returns, HTML
        """
        f = urllib2.urlopen(url)
        html = f.read()
        f.close()
        return html

    def parse_web_page(self, html):
        """
        Parses an html page searching for free book
        """
        soup = bs4.BeautifulSoup(html, "lxml")
        info = soup.find("div", "dotd-main-book")

        title = info.find("div", "dotd-title")
        details = info.find("div", "")
        more_details = info.find("ul", "")

        if details is None or title is None:
            return "There are not free books for today :("
        if more_details is None:
            return "\nTitle: " + title.text.strip() + "\n\nDescription: " + details.text.strip()
        else:
            return "\nTitle: " + title.text.strip() + "\n\nDescription: " + details.text.strip() + "\n" + more_details.text.strip()

    def run(self):
        """
        Retrieves the necessary data to get the free book today
        """
        html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning")
        book = self.parse_web_page(html)
        return book


if __name__ == "__main__":

    obtain_book = Book()
    book = obtain_book.run()
    print "\nFREE BOOK FOR TODAY\n" + book
