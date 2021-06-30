import requests
from bs4 import BeautifulSoup
import sqlite3
import time
from urllib.parse import urljoin



class spider:
    def __init__(self):
        self.con=sqlite3.connect('project.sqlite')
        self.cur=self.con.cursor()
        self.cur.execute('drop table if exists All_links ')
        self.cur.execute('drop table if exists Visited_links ')


    def page_data(self, url):
        self.url=url
        try:
            with requests.get(self.url) as self.url_request:
                self.url_data = self.url_request.text
                self.url_request.close()
            return self.url_data
        except:
            print(f'we were unable to visit {self.url}')

    def find_links(self,base_url, html_data):
        self.links = []
        soup = BeautifulSoup(html_data, 'html.parser')
        anchor_tags = soup.find_all('a')
        for a in anchor_tags:
            self.l2v = a.get('href')
            if  self.l2v:
                self.l2v = self.complete_link(base_url, self.l2v)
                my_link = self.base_link(base_url, self.l2v)
                self.links.append(my_link)
            else:
                continue
        return self.links


    def complete_link(self,base, l2v):
        self.l2v=l2v
        if 'https' in self.l2v:
            return self.l2v
        else:
            return urljoin(base,self.l2v)


    def base_link(self,base_url, l2v):
        self.l2v=l2v
        if base_url not in self.l2v:
            return
        else:
            return self.l2v


    def insert_to_db(self,links):
        # self.con = sqlite3.self.connect('project.sqlite')
        # self.cur = self.con.cursor()
        # self.cur.execute('Drop table if exists All_links')
        # self.cur.execute('Drop table if exists Visited_Links')
        self.cur.execute('Create table IF NOT EXISTS Visited_Links(v_Links TEXT)')
        self.cur.execute('CREATE TABLE IF NOT EXISTS All_links(Links TEXT) ')
        for self.l2v in links:
            if self.l2v is None:
                pass
            else:
                self.cur.execute('SELECT Links from All_links where links=?', (self.l2v,))
                data = self.cur.fetchall()
                if not data:
                    self.cur.execute('INSERT INTO All_links(Links) values(?)', (self.l2v,))
                else:
                    print(f'{self.l2v} is already in database')
        self.con.commit()

    def sel(self):
        # self.con = sqlite3.connect('project.sqlite')
        # self.cur = self.con.cursor()
        self.cur.execute('select Links from All_links')
        return self.cur.fetchone()

    def new_link_to_visit(self):

        # self.con = sqlite3.self.connect('project.sqlite')
        # self.cur = self.con.cursor()
        # self.cur.execute('select Links from All_links')
        # self.l2v = self.cur.fetchone()
        self.l2v=self.sel()
        self.che=self.check_in_vlink(self.l2v[0])
        while self.che:
            self.l2v = self.sel()
            self.che = self.check_in_vlink(self.l2v[0])
        self.cur.execute('select v_Links from Visited_Links where v_Links=?', (self.l2v[0],))
        data = self.cur.fetchall()
        if not data:
            self.cur.execute('insert into Visited_Links(v_Links) values(?)', (self.l2v[0],))
            print(f'{self.l2v[0]} is visited now')
            self.cur.execute('delete from All_links where Links=?', (self.l2v[0],))
        self.con.commit()
        print('new_link_to_visit run')
        print(f'new self.l2v is {self.l2v}')
        return self.l2v[0]

    def check_in_vlink(self,elink):
        links=[]
        # self.con=sqlite3.connect('project.sqlite')
        # self.cur=self.con.cursor()
        self.cur.execute('select v_Links from Visited_Links')
        all_v_links=self.cur.fetchall()
        for link in all_v_links:
            links.append(link[0])
        if elink in links:
            self.cur.execute('Delete FROM All_Links Where Links=?',(elink,))
            self.con.commit()
            return True
        else:
            return False

    def if_page(self,url):
        self.url=url
        self.cur.execute('Create table IF NOT EXISTS All_pages(pages TEXT)')
        if self.url.endswith('htm') or self.url.endswith('html'):
            self.cur.execute('insert into All_pages(pages) Values(?)',(self.url,))
        else:
            pass


url = 'https://www.facebook.com/'
base_url = 'https://www.facebook.com/'

myspider=spider()
while True:
    myspider.if_page(url)
    data=myspider.page_data(url)
    links=myspider.find_links(base_url,data)
    myspider.insert_to_db(links)
    url=myspider.new_link_to_visit()
    time.sleep(2)


print(links)