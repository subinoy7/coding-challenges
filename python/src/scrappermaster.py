import sys
import urllib.request as urllib2
import re
import queue
import threading
from threading import Thread
import datetime

class Manager(threading.Thread):
    def __init__(self,q,URLDump):
        Thread.__init__(self)
        self.q = q
        self.URLDump=URLDump

    def run(self):
        while self.q.empty()==False:
            self.startScrapping(self.q.get(),self.q,self.URLDump)
            self.q.task_done()
        
    def startScrapping(self,endPoint,q,URLDump) :
        try:
            print('-- Straring scrapping of : ' + endPoint)
            user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
            customRequest = urllib2.Request(endPoint, headers={'User-agent':user_agent})
            rootSiteHandler = urllib2.urlopen(customRequest)
            rootSiteContent = rootSiteHandler.read()

            with open(endPoint.split('/')[-1], 'wb') as out_file:
                out_file.write(rootSiteContent)

            #print(rootSiteContent)

            rootSiteContent = str(rootSiteContent,'utf-8')

            listUrls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',rootSiteContent)
            #print(listUrls)

            self.addInQueue(listUrls,q,URLDump)

        except Exception as excp:
            print("Unexpected error:", excp)

    def addInQueue(self,listUrls,q,URLDump):
        for iter in listUrls:
            if URLDump.__contains__(iter):
                URLDump[iter]=URLDump[iter]+1
            else:
                URLDump[iter]=1
                q.put(iter)

def invokeScrapping(endPoint):
    q = queue.Queue()
    URLDump = {}
    baseUrl =''
    if endPoint:
        baseUrl = 'https://medium.com'
    q.put(baseUrl)
    print("Starting scrapping for the website:: " + baseUrl)
    for x in range(5):
        inst = Manager(q,URLDump)
        inst.daemon = True
        inst.start()

    q.join()
