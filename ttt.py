import random
domestic=["Barcelona","Bayern","Benfica","Chelsea","Juventus","Paris","PSV","Zenit"]
dic={"Arsenal":"ENG","Astana" :"KAZ","Atlético": "ESP","Barcelona" :"ESP","BATE" :"BLR", "Bayern ":"GER","Benfica ":"POR","Chelsea ":"ENG","CSKAMoskva" :"RUS", "DinamoZagreb": "CRO","DynamoKyiv":"UKR", "Galatasaray ":"TUR","Gent ":"BEL", "Juventus" :"ITA"," Leverkusen ":"GER","Lyon":"FRA","M.Tel-Aviv ":"ISR","Malmö ":"SWE","Man.City ":"ENG","Man.United ":"ENG"," Mönchengladbach ":"GER", "Olympicos ":"GRE", "Paris" :"FRA", "Porto" :"POR","PSV ":"NED","RealMadrid" :"ESP", "Roma": "ITA","Sevilla ":"ESP","ShakhtarDonetsk ":"UKR","Valencia" :"ESP", "Wolfsburg" :"GER", "Zenit": "RUS"}
print(len(dic.keys()))

groupa=[]
groupb=[]
groupc=[]
groupd=[]
groupe=[]
groupf=[]
groupg=[]
grouph=[]
groupa.append(domestic[0])
groupb.append(domestic[1])
groupc.append(domestic[2])
groupd.append(domestic[3])
groupe.append(domestic[4])
groupf.append(domestic[5])
groupg.append(domestic[6])
grouph.append(domestic[7])
visted={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
for i in dic.keys():
    
    if len(groupa)<4 :
       
            if dic[i] not in visted[1]:
                       groupa.append(i)
                       visted[1].append(dic[i])
    
            
    elif len(groupb)<4 :
       
            if dic[i] not in visted[2]:
                       groupb.append(i)
                       visted[2].append(dic[i])
    elif len(groupc)<4 :
       
            if dic[i] not in visted[3]:
                       groupc.append(i)
                       visted[3].append(dic[i])




    elif len(groupd)<4 :
       
            if dic[i] not in visted[4]:
                       groupd.append(i)
                       visted[4].append(dic[i])


    elif len(groupe)<4 :
       
            if dic[i] not in visted[5]:
                       groupe.append(i)
                       visted[5].append(dic[i])

    elif len(groupf)<4 :
       
            if dic[i] not in visted[6]:
                       groupf.append(i)
                       visted[6].append(dic[i])
    elif len(groupg)<4 :
       
            if dic[i] not in visted[7]:
                       groupg.append(i)
                       visted[7].append(dic[i])
    elif len(grouph)<4 :
       
            if dic[i] not in visted[8]:
                       grouph.append(i)
                       visted[8].append(dic[i])
print("GroupA:",groupa,end=" ")
print("\n")
print("GroupB:",groupb,end=" ")
print("\n")
print("GroupC:",groupc,end=" ")
print("\n")
print("GroupD:",groupd,end=" ")
print("\n")
print("GroupE:",groupe,end=" ")
print("\n")
print("GroupF:",groupf,end=" ")
print("\n")
print("GroupG:",groupg,end=" ")
print("\n")
print("GroupH:",grouph,end=" ")
