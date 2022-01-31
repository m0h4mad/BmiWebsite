from jdatetime import date


GENDERS = ['male', 'female']
UNDERWEIGHT = 'underweight'
NORMALWEIGHT = 'normalweight'
OVERWEIGHT = 'overweight'
OBESE = 'obese'


class Bmi:
    def __init__(self, age, weight, height, gender):
        '''
            Standard BMI Calculation For Any Age And Gender

            # Arguments:
                - age (`int`) : Age
                - weight (`int`) : Weight as KG
                - height (`int`) : Height as CM
                - Gender (`str`) : Gender (must be 'male' or 'female')
            
            # Example:
                >>> b = Bmi(3, 8, 60, 'female')
                >>> b.calculate()
                {'bmi': 22.2, 'weight': 'obese'}
        '''

        self.age = age
        self.weight = weight
        self.height = height / 100
        self.gender = gender
        self.bmi = self.weight / (self.height ** 2)
    
    # Boys 2 to 5 years old
    def b2_5(self):
        if self.bmi < 14:
            return UNDERWEIGHT
        
        elif self.bmi < 16.5:
            return NORMALWEIGHT
        
        elif self.bmi < 18:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    # Girls 2 to 5 years old
    def g2_5(self):
        if self.bmi < 14:
            return UNDERWEIGHT
        
        elif self.bmi < 17:
            return NORMALWEIGHT
        
        elif self.bmi < 18.5:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    def b5_10(self):
        if self.bmi < 14:
            return UNDERWEIGHT
        
        elif self.bmi < 17:
            return NORMALWEIGHT
        
        elif self.bmi < 19:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    def b10_19(self):
        if self.bmi < 17:
            return UNDERWEIGHT
        
        elif self.bmi < 22.5:
            return NORMALWEIGHT
        
        elif self.bmi < 26:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    def g5_10(self):
        if self.bmi < 14:
            return UNDERWEIGHT
        
        elif self.bmi < 17:
            return NORMALWEIGHT
        
        elif self.bmi < 20:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    def g10_19(self):
        if self.bmi < 17.5:
            return UNDERWEIGHT
        
        elif self.bmi < 23.5:
            return NORMALWEIGHT
        
        elif self.bmi < 27:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    def cal_adult(self):
        if self.bmi < 18.5:
            return UNDERWEIGHT
        
        elif self.bmi < 24.5:
            return NORMALWEIGHT
        
        elif self.bmi < 29.9:
            return OVERWEIGHT
        
        else:
            return OBESE
    
    def cal_kid(self):
        if self.gender == GENDERS[0]:
            if self.age in range(2, 5):
                return self.b2_5()
            
            elif self.age in range(5, 10):
                return self.b5_10()
            
            else:
                return self.b10_19()
        
        else:
            if self.age in range(2, 5):
                return self.g2_5()
            
            elif self.age in range(5, 10):
                return self.g5_10()
            
            elif self.age in range(10, 19):
                return self.g10_19()
    
    def calculate(self):
        result = {'bmi': round(self.bmi, 1)}

        if self.age < 19:
            result.update({'weight': self.cal_kid()})
        
        else:
            result.update({'weight': self.cal_adult()})
        
        return result


def calculate_age(year, month, day):
    birth_date = date(year, month, day)
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


if __name__ == '__main__':
    b = Bmi(3, 8, 60, 'female')
    print(b.calculate())

    print(calculate_age(1385, 10, 11))
