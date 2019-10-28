from datetime import datetime as dt
from dateutil.relativedelta import relativedelta

class Customer:
    student_name = 'Todd Landry Jr'
    
    def __init__(self, cust_id, first, last, dob, city, state, cust_zip):
        self.cust_id = cust_id
        self.first = first
        self.last = last
        self.dob = dob
        self.city = city
        self.state = state
        self.cust_zip = cust_zip
        
    def full_name(self):
        return self.first + ' ' + self.last
    
    def age(self):
        dob_format = dt.strptime(self.dob, '%Y-%m-%d')
        today = dt.today()
        age = relativedelta(today, dob_format)
        return age.years
    
    def adult(self):
        age = self.age()
        if age >= 18:
            return True
        else: 
            return False
        
    def to_json(self):
        cust_attributes = {
                           'id':self.cust_id, 
                           'first_name':self.first, 
                           'last_name':self.last, 
                           'dob':self.dob, 
                           'city':self.city, 
                           'state':self.state, 
                           'zip':self.cust_zip, 
                           'age':self.age(), 
                           'full_name':self.full_name(), 
                           'adult':self.adult()
                          }
        return cust_attributes
        