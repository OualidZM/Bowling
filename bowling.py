class Bowling:

    def __init__(self):
        self.is_strike = True
        self.is_spare = False


    def score(self,frame):
        score_counter = []
        strike_marke = 'X'

        while range(len(frame)):
            for pins_score in frame:
                
                if pins_score == strike_marke: #si es strike
                    poscion = frame.index(pins_score) #Posición donde se encuentra actualmente
                                                                                                    
                                                                                            #Si en la posición en donde se encuentra 
                                                                                            #equivale a un strike y las dos posiciones que vienen
                                                                                            #no son ni strike ni spare entonces se cumple el if

                    if frame[poscion] == 'X' and frame[poscion+1] != 'X' and frame[poscion+2] != '/':
                                                                                                        


                        try:                                                                #si se cumple el if, entonces se pondrá un 10 en el lugar de la 'X' y
                                                                                            #los dos próximos números que vienen se pasaran de string a int para luego sumar-los
                            position = frame[poscion] = 10
                            next_pin = int(frame[poscion+1])
                            next_pin_two = int(frame[poscion+2])
                            score_counter.append(position + next_pin + next_pin_two)

                            try:                                                            
                                if frame[poscion+2] != 'X' or '/':
                                    frame[poscion+2] = 0
                                    continue
                                else:
                                    if frame[poscion+2] == 'X' or '/':
                                        continue
                            except:
                                continue
                        except:                                                         #Si al encontrarse un strike(X) y dos números  más adelante vuelve a ser otro strike,
                                                                                        #esto tendrá que sumar, primero el primer strike encontrado +10, luego
                                                                                        #el número de al medio y finalmente el strike del final +10. 
                                                                                        #Si encuentra un spare(/) entonces sumara strike +10 y spare +10 y se parara
                            if frame[poscion+2] == 'X':
                                next_pin = int(frame[poscion+1])
                                next_pin_two = 10
                                score_counter.append(position + next_pin + next_pin_two)
                                continue
                            elif frame[poscion+2] == '/': # si hi ha strike seguit de /
                                position = poscion = 10
                                next_pin = 10
                                next_pin_two = 0
                                score_counter.append(poscion + next_pin_two)
                                continue

                    if pins_score == 'X':  
                                                                                        #si al encontrarse con un strike(X) y una posición más adelante
                                                                                        #encuentra otro strike(X) y vuelve a encontrarse un último strike dos 
                                                                                        # números más adelante(X), sumara 30(turkey)

                        poscion = frame.index(pins_score)
                        if frame[poscion] == 'X' and frame[poscion+1] == 'X' and frame[poscion+2] == 'X':
                            score_counter.append(30)
                            contador +=1
                            poscion += 1
                            continue
                                                                                        #si en la posición en que se encuentra hay un strike(X) y una posición
                                                                                        #más adelante otro strike(X) esto sumara 20


                        elif frame[poscion] == 'X' and frame[poscion+1] == 'X' and frame[poscion+2] != 'X':
                            position = poscion = 10 
                            next_pin = 10
                            next_pin_two = int(frame[poscion+3])
                            score_counter.append(position + next_pin + next_pin_two)
                            continue  

                                                                                        #si no ha sido spare y se ha puesto
                                                                                        #un 0 al siguiente números, entonces se ignora
                else:

                    
                    poscion = frame.index(pins_score)
                    if frame[poscion] == 0:
                        continue 

                                                                                        #si la posición no es 0
                                                                                        #y es menor que 10
                                                                                        #entonces se cumple el if.
                    if frame[poscion] != 0 and pins_score !=10:

                                                                                        #En el número que se encuentra,
                                                                                        #si el que viene hace que sea spare(/), se
                                                                                        # cumple el if

                        if frame[poscion + 1] == '/':
                                                                                        #se añadirá +10 al número actual,
                                                                                        #luego, donde se encuentra el símbolo de spare(/) se añadirá 0 y
                                                                                        #finalmente se pasara a int el número actual y  el número que esta
                                                                                        #a dos posiciones más adelante, y se sumaran

                            try:
                                position = frame[poscion] = 10
                                next_pin = frame[poscion+1] = 0
                                next_pin_two = int(frame[poscion+2])
                                score_counter.append(position + next_pin_two)
                            except:
                                if frame[poscion] == 0 and  frame[poscion+1] == '/':
                                        next_pin = 0
                                        next_pin_two = frame[poscion+2]
                                        score_counter.append(position + next_pin_two)
                                        continue

                                                                                        #si hay un número delante de un strike
                                                                                        #este lo añade y pasa al siguiente
                        elif frame[poscion] != 'X' and frame[poscion+1] == 'X':
                            
                            score_counter.append(int(frame[poscion]))
                            continue
                                                                                        #si no es ni spare(/) ni strike(X),
                                                                                        #al número donde se encuentra se añadirá y el siguiente
                                                                                        #se le pondrá un 0, porque la suma no llega a ser spare(/)
                        
                        elif frame[poscion + 1] != '/' or frame[poscion +1] != 'X':
                                score = int(pins_score)
                                score_counter.append(score)
                                first_position = frame[poscion+1] = 0 
                                score_counter.append(first_position)
                                continue
            break

        return sum(score_counter)
    

# if __name__ == "__main__":
#     bow = Bowling()
#     assert bow.score(['1','2','X','7','1','3','X','1','5','4','2','8','1','9','X','4','3','X','9','2']) == 118  
#     assert bow.score(['6','8','X','2','4','5','3','1','X','8','1','4','5','4','2','3','/','X','3','5']) == 88
#     assert bow.score(['5','4','X','8','X','1','X','3','X','5','4','7','8','9','1','X','3','7','6','8']) == 158
#     assert bow.score(['6','/','9','2','3','X','3','4','5','3','5','7','3','X','4','X','0','X','3','3']) == 135

