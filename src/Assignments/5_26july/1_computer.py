# class prices:
#     def __init__(self,name,price) -> None:
#         self.name=name
#         self.price=price
class person:
    pass
class vendor(person):
        pass
class customers(person):
        pass
    
class computer:
    invoice=" "
    def __init__(self,name,hddsize,keyboardsize,monitorsize,mousekeys,os,vendor,price) -> None:
        self.name=name
        self.harddisk=hddsize
        self.keyboard=keyboardsize
        self.monitor=monitorsize
        self.mouse=mousekeys
        self.os=os
        self.vendor=vendor
        self.price=price

    def additem(self):
        invoice+=self.name+" "
    def getBill()->str:
        return str
    
        
    
class laptop(computer):
    def __init__(self, hddsize, keyboardsize, monitorsize, mousekeys,os,vendor,price,batterysize,charginewattage) -> None:
        super().__init__(hddsize, keyboardsize, monitorsize, mousekeys,os,vendor,price,)
        battery=batterysize
        power=charginewattage
        
class tab(computer):
    def __init__(self, hddsize, monitorsize) -> None:
        super.hddsize=hddsize
        super.monitorsize=monitorsize
        
        
        

if __name__ == '__main__':
    pass