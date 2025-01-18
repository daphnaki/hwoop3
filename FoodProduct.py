from datetime import datetime, timedelta
from enum import Enum


class ProductCategory(Enum):
    DAIRY = "Dairy"
    MEAT = "Meat"
    PARVE = "Parve"

class FoodProduct:
    def __init__(self,name: str, price: float, category: ProductCategory, production_date: datetime,expiration_date: datetime):
        self.__name: str = name
        self.__price : float = price
        self.__category: ProductCategory = category
        self.__production_date: datetime = production_date
        self.__expiration_date: datetime = expiration_date

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        if isinstance(new_name,str):
            if new_name.isalpha():
                if len(new_name) >=3 and not repeated_chars(new_name):
                    self.__name = new_name
                else:
                    raise ValueError(f"{new_name} is not valid")
            else:
                raise TypeError(f"name must be letters. cannot be numbers")
        else:
            raise TypeError("Name must be a string.")


    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,new_price):
        if isinstance(new_price,float):
            if 0.1 <= new_price <= 100:
                self.__price = new_price
            else:
                raise ValueError ('Price must be between 0.1 and 100')
        else:
            raise TypeError("Price must be Float type")

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self,new_category):
        if not isinstance(new_category,ProductCategory):
            raise TypeError ("Category must be ProductCategory object")

    @property
    def production_date(self):
        return self.__production_date

    @production_date.setter
    def production_date(self,new_production_date):
        if isinstance(new_production_date,datetime):
            if new_production_date < datetime.now():
                self.__production_date = new_production_date
            else:
                raise ValueError("Production Date must in the past")
        else:
            raise TypeError("Production date must be a datetime object")

    @property
    def expiration_date(self):
        return self.__expiration_date
    @expiration_date.setter
    def expiration_date(self,new_expiration_date):
        if isinstance(new_expiration_date,datetime):
            one_week_ahead = datetime.now() + timedelta(days=7)
            if new_expiration_date >= one_week_ahead:
                self.__expiration_date = new_expiration_date
            else:
                raise ValueError("Expiration date must be at least a week into the future.")
        else:
            raise TypeError("Expiration date must be a datetime object.")

    @property
    def remaining(self):
        return (self.expiration_date - datetime.now()).days


    def __add__(self, other:int):
        return self.price + other


    def __sub__(self, other:int):
        return self.price - other


    def __mul__(self, other:int):
        return self.price * other


    def __eq__(self, other):
        if isinstance(other,int):
            return self.price == other
        if isinstance(other,FoodProduct):
           return self.price == other.price


    def __ne__(self,other):
        return not self == other


    def __gt__(self,other):
        if isinstance(other,int):
            return self.price > other
        if isinstance(other,FoodProduct):
           return self.price > other.price


    def __lt__(self, other):
        return not self > other


    def __len__(self):
        return (self.production_date - datetime.now()).days


    def __hash__(self):
        return hash(self.price)


    def __str__(self):
        return (f'name={self.__name}, price={self.__price}, category={self.__category}, production date = {self.__production_date}'
                f'expire date = {self.__expiration_date}, remaining_days: {self.remaining}')


    def __repr__(self):
        return f"FoodProduct({self.__name},{self.__price},{self.__category},{self.__production_date},{self.__expiration_date},{self.remaining})"

def repeated_chars(string):

    if len(string) <=1:
        return False
    if string[0] == string[1]:
        return True
    return repeated_chars(string[1:])

