class Repulogep:
    def __init__(self,hely,tipus,maxseb):
        self.__hely=hely
        self.__tipus=tipus
        self.__maxseb=maxseb

    def set_hely(self,hely):
        self.__hely=hely

    def get_tipus(self):
        return self.__tipus

    def set_tipus(self, tipus):
        self.__tipus = tipus

    def get_tipus(self):
        return self.__tipus

    def set_maxseb(self, maxseb):
        self.__maxseb = maxseb

    def get_maxseb(self):
        return self.__maxseb

    def __str__(self):
        return str(self.__hely)+" "+self.__tipus+" "+str(self.__maxseb)

    def szamol(self,tavolsag):
        return self.__maxseb*tavolsag

    def __lt__(self, other):
        if isinstance(other,Repulogep):
            if self.__maxseb==other.__maxseb:
                return self.__tipus<other.__tipus
            else:
                return self.__maxseb<other.__maxseb

    def __eq__(self, other):
        if isinstance(other,Repulogep):
            if self.__tipus==other.__tipus and self.__hely==other.__hely:
                return True
            else:
                return False

    def __sub__(self, other):
        if isinstance(other, Repulogep):
            return self.__hely+other.__hely

    def __ge__(self, other):
        if isinstance(other, Repulogep):
            if self.__hely>=other.__hely:
                return True
            else:
                return False

class Repuloter():
    count=0
    lista=[]
    # def __init__(self,hely,tipus,maxseb):
    #     super().__init__(self,hely,tipus,maxseb)

    def get_lista(self):
        return self.lista

    def addRepulogep(self,file_name):
        try:
            be=open(file_name,"r")
            elso=int(be.readline())
            while self.count<=elso:
                for line in be:
                    line=line.strip()
                    li=line.split(";")
                    self.lista.append(Repulogep(int(li[0]),li[1],int(li[2])))
                    self.count+=1
                self.count+=1
                break
            # print(self.count)
            # print(elso)
            if self.count<=elso:
                return True
            else:
                return False

            be.close()
        except FileNotFoundError:
            print("Nincs fájl")




# #main
# ter=Repuloter()
# ter.addRepulogep("444.txt")
# listaa=ter.get_lista()
# # for i in listaa:
# #     print(i)
# tavolsag=int(input("Távolság: "))
# for i in listaa:
#     print("A(z) {} tipusú gép {} óra alatt érne a térhez.".format(i.get_tipus(),round(tavolsag/i.get_maxseb(),4)))





class Mozi:
    def __init__(self,cim,ev,rend,kolt,bev):
        self.__cim=cim
        self.__ev=ev
        self.__rend=rend
        self.__kolt=kolt
        self.__bev=bev

    def __str__(self):
        return self.__cim+" "+self.__ev+" "+self.__rend+" "+self.__kolt+" "+self.__bev



n=int(input("Szám: "))
count=0
lista=[]
while count<n:
    sor=input(": ")
    sor=sor.strip()
    li=sor.split(";")
    lista.append(Mozi(li[0],str(li[1]),li[2],li[3],li[4]))
    count+=1

for i in lista:
    print(i)