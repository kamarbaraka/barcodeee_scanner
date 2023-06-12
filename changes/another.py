class employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+last+'@company'
    
    def full(self):
        return(self.email)
emplo = employee('evans', 'murunga', 20000)

print(employee.full(emplo))


        
