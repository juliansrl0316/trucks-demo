from bs4 import BeautifulSoup
import requests
import json

urls = ['http://gorilla.hellomoving.com/wc.dll?mpagent~viewassign~74B9C458DB60',
        'https://fox.hellomoving.com/wc.dll?mpagent~viewassign~F51CC96020AC',
        'https://puma.hellomoving.com//wc.dll?mpagent~viewassign~42CEE72757DE']


urlsdic = {
    "All State Moving and Storage": 'http://gorilla.hellomoving.com/wc.dll?mpagent~viewassign~74B9C458DB60',
    "New Leaf Moving Group": 'https://fox.hellomoving.com/wc.dll?mpagent~viewassign~F51CC96020AC',
    "Trinity Van Lines": 'https://puma.hellomoving.com//wc.dll?mpagent~viewassign~42CEE72757DE',
    "Safe Ship": 'https://gorilla.hellomoving.com//wc.dll?mpagent~viewassign~5E3FD536C2D6'
}

tableDic = dict()
tupleDic = dict()

def GetHtmlInfo():
    for url in urlsdic:  
    
        page_response = requests.get(urlsdic[url], timeout=5)
    
        page_content = BeautifulSoup(page_response.content, "html.parser")
    
        tableRows = page_content.find_all("tr")
      
        statsHtml = []
        count = 0
        tupleList = list()
    
        for row in tableRows[3:]:
            for element in row.find_all("font"):
                if count > 11:
                    statsHtml.clear()
                    count = 0
    
                statsHtml.insert(count, element.text)
                count += 1
    
            moveDate = statsHtml[2]
            
            tupleDic = {
                "Job No.": statsHtml[0],
                "Type": statsHtml[1].replace(" ", "").strip(),
                "Move Date": moveDate[:10]+" | "+moveDate[10:],
                "Time": statsHtml[3],
                "1st Available Delivery": statsHtml[4].replace(" ", "").strip(),
                "Moving From": statsHtml[5].replace(" ", "").strip()+" "+statsHtml[6],
                "Moving To": statsHtml[7].replace(" ", "").strip()+" "+statsHtml[8],
                "CF / Lbs": statsHtml[9].replace(" ", "").strip(),
                "Miles": statsHtml[10],
                "Estimate": statsHtml[11]
            }
            
            tupleList.append(tupleDic)
            
    
            
        tableDic[url] = tupleList
    return tableDic
        