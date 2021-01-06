import random
#https://github.com/CodeProgress/TicketToRide/blob/master/TTRCards.py
class Player:
    def __init__(self, color):
        self.color=color
        self.ticket=[]
    
    def get_ticket_random (self,numbers_of_tickets):
        cantidad_de_tickets_actuales=len(self.ticket)
        total_tickets=cantidad_de_tickets_actuales+numbers_of_tickets

        while cantidad_de_tickets_actuales<total_tickets:
            iteraciones+=1
            tickets = [('Madrid',    'Lisboa', 3), 
                                ('Madrid',         'Barcelona',        2), 
                                ('Pamplona', 'París',      4), 
                                ('Lisboa',       'Cadiz',        6)]
            len(tickets)
            max_value=len(tickets)-1
            random_number=random.randrange(0,max_value,1)
            random_ticket=tickets[random_number]
            if random_ticket not in self.ticket:
                self.ticket.append(random_ticket)
        return "i am happy"
        
def multiplicacion (number)


# lista_tickets=[0,1,2]
# player_tickets=[]
# numero_de_tickets=3
# while len(player_tickets)<numero_de_tickets:
#     random_ticket=get_ticket_random()
#     if  random_ticket not in player_tickets:
#         player_tickets.append(random_ticket)
# print(player_tickets)

azul=Player(color='azul')
print(azul.color)
azul.get_ticket_random(2)
print(azul)