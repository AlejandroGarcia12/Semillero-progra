numeros={"1111011":9,"1111111":8,"1110000":7,"1011111":6,"1011011":5,"0010011":4,"1001111":3,"1101101":2,"0110000":1,"1111110":0}
numeros2={9:"1111011",8:"1111111",7:"1110000",6:"1011111",5:"1011011",4:"0010011",3:"1001111",2:"1101101",1:"0110000",0:"1111110"}
print("ingrese # de casos: ")
n_casos=int(input())
casos=[]

for i in range(n_casos):
    print("ingrese caso: ")
    c=input("")
    casos.append(c)
def traductor(casos):
    trad=[]
    for i in casos:
        n_leds=int(i[0])
        lector=2
        for j in range(n_leds):
            if i[lector:lector+7] in numeros.keys():
                trad.append(numeros[i[lector:lector+7]])
                lector=lector+8    
trad=[]
for i in casos:
    n_leds=int(i[0])
    lector=2
    for j in range(n_leds):
        if i[lector:lector+7] in numeros.keys():
            trad.append(numeros[i[lector:lector+7]])
            lector=lector+8


for i in casos:
    n_leds=int(i[0])
    lector=2
    newleds=[]
    for h in range(2):
        newled=""
        change=False
        for j in i[lector:lector+7]:
            if j=="1" or change==True:
                newled=newled+j
            elif j=="0" or change==False:
                j="1"
                newled=newled+j
                change=True
        for i in numeros.keys():
            if i==newled:
                newleds.append(newled)
                lector=lector+8
                print(newleds)
            

        
    
                
                
                
                
 
        
        

            
    
    


    