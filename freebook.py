#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
Simple web client, using URLLIB2
Created on 10/14/2014

@author: carlesm
'''

import urllib2
import bs4


class Client(object):

    """Web Client, for https://www.packtpub.com/packt/offers/free-learning
    """

    def __init__(self):
        super(Client, self).__init__()

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
        Parses an html page searching for the agenda
        """
        soup = bs4.BeautifulSoup(html, "lxml")
        title_of_book = soup.find("div", "dotd-title")

        title = title_of_book.text

        return title.strip()


        #
        # novetats_llista = []
        # for novetat in novetats:
        #     datahtml = novetat.find("span", "data")
        #     data = datahtml.text
        #     item = novetat.find("a")
        #     text = item.text
        #     url = item["href"]
        #     # print data, ",", text, ",", url
        #     novetat_tupla = (data, text, url)
        #     novetats_llista.append(novetat_tupla)
        #return novetats_llista

    def print_data(self, data):
        """
        Prints data retrieved
        """
        for datum in data:
            print ",".join(datum)

    def run(self):
        """
        Retrieves list of announces from www.udl.cat and print
        it
        """

        html = self.get_web_page("https://www.packtpub.com/packt/offers/free-learning")
        name_of_book = self.parse_web_page(html)
        return name_of_book
        #self.print_data(novetats)


if __name__ == "__main__":

    client = Client()

    book = client.run()
    print book

    #bot = telepot.Bot('532729363:AAEhg8JpTrqn9wD8VFnOzTbkj8Q9uGz-JBI')

    #bot.sendMessage(469707767, book)
    #bot.sendPhoto(469707767, 'https://78.media.tumblr.com/60c60b4ab0dfa7de63249f26353dc5a0/tumblr_nuvue1qcrU1rhvcavo1_400.gif')
    #print bot.getMe()


    #response = bot.getUpdates()
    #print(response)
    #i = 0
    #bot.sendMessage(471124140, book)
    #bot.sendMessage(469707767, book)
    #bot.sendMessage(386740481, book)
    #bot.sendMessage(11513281, book)

    #    i+=1
