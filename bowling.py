class scoreSheet:
    def __init__(self,numbers):
        self.numbers = numbers
        self.strikee = 'X'
        self.sparee = '/'
        self.null = '-'
        self.strike_counter = []
        self.spare_counter = []
        self.normall = []
        # self.position_count = []


    
    def strike(self):
        while range(len(self.numbers)):
            for i in self.numbers:
                actual_position = self.numbers.index(i)
                next_position = self.numbers[actual_position+1]
                second_next_position = self.numbers[actual_position+2]

                if (self.numbers[actual_position] == self.strikee) and (second_next_position == self.sparee):
                    
                    self.strike_counter.append(20)
                    self.strike_counter.append(0) # X AND /
                    self.numbers.remove(self.numbers[actual_position])
                    # self.position_count.append(actual_position)
                
                elif i != self.strikee  and next_position == self.sparee: # menor a 10 y spare
                    self.spare()


                elif self.numbers[actual_position] < 10 and self.numbers[next_position] != self.sparee: #menor que 10 y no es /
                    ii.normal                   
                
                elif self.numbers[actual_position] == self.strikee and self.numbers[next_position] < 10 and self.numbers[second_next_position] != self.sparee:
                    self.strike_counter.append(10)
                    self.strike_counter.append(self.numbers[next_position])#posicio 1 strike 2 menor que 10  y 3 no /

                else:
                    if i == self.strikee: #ELSE
                        int(next_position)
                        self.strike_counter.append(10 + self.numbers[next_position]) 
                        # self.strike_counter.append()
                        # self.strike_counter.append(self.numbers[second_next_position])
            break



    def spare(self):
        while range(len(self.numbers)):
            for i in  self.numbers:
                actual_position = self.numbers.index(i)
                next_position = self.numbers[actual_position+1]
                if self.numbers[actual_position] == 'X':
                    self.strike()
                elif self.numbers[actual_position] != 10  and self.numbers[actual_position+1] == self.sparee: #<10 AND /
                    self.numbers
                    self.strike_counter.append(0)
                    self.strike_counter.append(10)
                elif self.numbers[actual_position]:
                    return None




    def normal(self):
        for i in self.numbers:
            while range(len(self.numbers)):
                actual_position = (self.numbers.index(i))
                next_position = (self.numbers[actual_position+1])
                if self.numbers[actual_position] != 10 and self.numbers[next_position] !=  self.sparee:
                    self.normall.append(actual_position + next_position)



    def score(self):
        return sum(self.strike_counter + self.spare_counter +  self.normall)
