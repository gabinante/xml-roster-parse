try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import itertools
#Create an array to store members of each rank
frtrialmembers=[]
srtrialmembers=[]
trtrialmembers=[]
frmembers=[]
srmembers=[]
trmembers=[]
elders=[]
councilmembers=[]
guildmaster=[]



#Map the members to the correct array according to their rank
with open('roster.xml', 'r') as f:
    tree = ET.ElementTree()
    tree.parse(f)
    root = tree.getroot()
    for child in root:
        print child.tag, child.attrib
    for m in root.iter("member"):
        rank = m.find('rank')
        name = m.find('name')
        print name.text, rank.text
        rankfloat = float(rank.text)
        print "detected %s with rank %i" % (name.text, rankfloat)
        if rankfloat in [1]:
            frtrialmembers.append(name.text)
        elif rankfloat in [2]:
            srtrialmembers.append(name.text)
        elif rankfloat in [3]:
            trtrialmembers.append(name.text)
        elif rankfloat in [4]:
            frmembers.append(name.text)
        elif rankfloat in [5]:
            srmembers.append(name.text)
        elif rankfloat in [6]:
            trmembers.append(name.text)
        elif rankfloat in [7]:
            elders.append(name.text)
        elif rankfloat in [8]:
            councilmembers.append(name.text)
        elif rankfloat in [9]:
            guildmaster.append(name.text)
        else:
            print "error -- rank above 9 or not detected. Please create correct mapping."

'''
Now we write the html file. This is going to be specific to your website - I'm using a bunch of CSS here that won't work for you.
Once it's written we can jam it into a div on an html page by using javascript, php, or bash:
'''
with open("autoroster.html", 'w') as autoroster:
            autoroster.write("<h1>Members</h1>\n")
            autoroster.write("<div class=\"row\">\n")
            autoroster.write("<div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Packleader</h6>\n")
with open("autoroster.html", 'a') as autoroster:
    print guildmaster
    for each in guildmaster:
        autoroster.write(each.title())
        autoroster.write("<br>\n")
        if len(councilmembers) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Council Members</h6>\n")
            for each in councilmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
        if len(elders) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Elders</h6>\n")
            for each in elders:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
        if len(trmembers) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Third Rank Members</h6>\n")
            for each in trmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
        if len(srmembers) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Second Rank Members</h6>\n")
            for each in srmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
        autoroster.write("</div></div>\n")
        if len(frmembers) > 0:
            autoroster.write("<h6>First Rank Members</h6>\n")
            autoroster.write("<div class=\"row\">\n")
            autoroster.write("<div class=\"col-sm-1\">\n")
            x = 0
            for each in frmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
                x = x+1
                if x % 11 == 0:
                    autoroster.write("</div><div class=\"col-sm-1\">\n")
        autoroster.write("</div><div class=\"row\">\n")
        if len(trtrialmembers) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Third rank initiates</h6>\n")
            for each in trtrialmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
        if len(srtrialmembers) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>Second rank initiates</h6>\n")
            for each in srtrialmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
        if len(frtrialmembers) > 0:
            autoroster.write("</div><div class=\"col-lg-3\">\n")
            autoroster.write("<h6>First rank initiates</h6>\n")
            for each in frtrialmembers:
                autoroster.write(each.title())
                autoroster.write("<br>\n")
    autoroster.write("</div>\n")
    autoroster.write("</p>\n")
