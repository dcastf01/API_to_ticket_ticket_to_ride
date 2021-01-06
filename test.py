import random

def get_ticket_random (numbers_of_tickets,tickets=[]):
        cantidad_de_tickets_actuales=len(tickets)
        total_tickets=cantidad_de_tickets_actuales+numbers_of_tickets

        while cantidad_de_tickets_actuales<total_tickets:
                all_tickets = [('Madrid',    'Lisboa', 3), 
                                        ('Madrid',         'Barcelona',        2), 
                                        ('Pamplona', 'París',      4), 
                                        ('Lisboa',       'Cadiz',        6)]
                len(all_tickets)
                max_value=len(all_tickets)-1
                random_number=random.randrange(0,max_value,1)
                random_ticket=all_tickets[random_number]
                if random_ticket not in tickets:
                        tickets.append(random_ticket)
                        cantidad_de_tickets_actuales=len(tickets)
                        
        return tickets
    
    
print(get_ticket_random(1))