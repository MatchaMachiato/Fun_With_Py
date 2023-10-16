from lxml import html
import requests
import os
import aspose.words as aw

name = input("What do you want to name this file: ")
url = input("Gimme your link to your result file: ")
# "https://ieltsonlinetests.com/score/33644700"
newDir = os.path.join(os.path.abspath(os.path.curdir), name)
os.mkdir(newDir)


page = requests.get(url)
tree = html.fromstring(page.content)


global textToPrint
def createPassage(i):
    openWeb = f'//div[@id="set-container-{i}"]//div[@class="passage-content"]//p//text()'
    text = tree.xpath(openWeb)
    
    global name
    # print("----------------------------------------------------------------------------------------")
    openFile = f"Passage_{i}.txt"

    def stuff(openFile):
        global newDir
        f = open(os.path.join(newDir, openFile), "w", encoding="utf-8")
        for pas in text:
            f.write(pas + '\n')
        f.close()

    stuff(openFile)

    def stuff2(openFile, i):
        global newDir
        f = open(os.path.join(newDir, openFile), "r", encoding="utf-8")   
        doc = aw.Document()
        builder = aw.DocumentBuilder(doc)
        builder.write(f.read())
        doc.save(os.path.join(newDir, f"Passage_{i}.docx"))
        f.close()
    stuff2(openFile, i)
createPassage(1)
createPassage(2)
createPassage(3)
