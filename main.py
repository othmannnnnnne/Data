from Scrapers import LeMatin, Bladi, LaVieEco, LeSiteInfo, BourseNews, Medias24, h24info, LaQuotidienne, libelles, BO

from enum import Enum




class Mois(Enum):
    janvier = 1
    février = 2
    mars = 3
    avril = 4
    mai = 5
    juin = 6
    juillet = 7
    août = 8
    septembre = 9
    octobre = 10
    novembre = 11
    décembre = 12
dates1=[]
def ArrangeLeMatin(i,n):
    LeMatin.scroll(i,n)
    k=0
    for u in LeMatin.dates:
        for i in range(1, 13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name, str(Mois(i).value))
                LeMatin.dates[k]=date
                k=k+1
    for i in range(0, len(LeMatin.dates)):
        if (len(LeMatin.dates[i]) == 17):
            dates1.append(LeMatin.dates[i][:3] + '0' + LeMatin.dates[i][3:])
        else:
            dates1.append(LeMatin.dates[i])
#ArrangeLeMatin(3,4)

dates2=[]
def ArrangeBladi(i,n):
    Bladi.scroll(i,n)
    k=0
    for u in Bladi.dates:
        for i in range(1,13):
            if (Mois(i).name in u):
                date = u.replace(Mois(i).name,str(Mois(i).value))
                Bladi.dates[k]=date
                k=k+1
    for i in range(0,len(Bladi.dates)):
        if(len(Bladi.dates[i]==9)):
            dates2.append(Bladi.dates[:3]+'0'+Bladi.dates[3:])
        else:
            dates2.append(Bladi.dates[i])

#ArrangeBladi(1,5)
dates3=[]
def ArrangelaVieEco(n):
    LaVieEco.scroll(n)
dates4=[]
def ArrangeLeSiteInfo(i,n):
    LeSiteInfo.scroll(i,n)
dates5=[]
def ArrangeLaQuotidienne(i,n):
    LaQuotidienne.scroll(i,n)
dates6=[]
def ArrangeBourseNews(i,n):
    BourseNews.scroll(i,n)
dates7=[]
def Arrangemedias24(i,n):
    Medias24.scroll(i,n)
dates8=[]
def Arrangeh24info(i,n):
    h24info.scroll(i,n)