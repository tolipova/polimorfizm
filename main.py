class Texnika:
    def __init__(self,brand,model,type):
        self.brand = brand
        self.model = model
        self.type = type
    def info(self)  :
        print(self.brand,self.model,self.type)

class Notebooks(Texnika):
    def __init__(self,brand,model,type,vedio_card,ram,display):
        super().__init__(brand,model,type)
        self.vedio_card = vedio_card
        self.ram = ram
        self.display = display

    def more_info(self):
        print(self.brand,self.model,self.type,self.vedio_card,self.ram,self.display)


class Televisions(Texnika):
    def __init__(self, brand, model, type,size,display):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display
    def more_info(self):
        print(self.brand,self.model,self.type,self.size,self.display)



class Smartphones(Texnika):
    def __init__(self, brand, model, type,size,sim_count):
        super().__init__(brand, model, type)
        self.size = size
        self.sim_count = sim_count
    def more_info(self):
        print(self.brand,self.model,self.type,self.size,self.sim_count)


s1 = Texnika('Apple','14pro max','smartphone')
s1.info()

s2 = Notebooks('macbook','new_mac','notebook','124px','34px','none')
s2.more_info()

