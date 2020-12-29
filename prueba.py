import random

def testicket ():
    
    tickets = [('Los Angeles',    'New York City', 21), 
                        ('Duluth',         'Houston',        8), 
                        ('Sault St Marie', 'Nashville',      8), 
                        ('New York',       'Atlanta',        6), 
                        ('Portland',       'Nashville',     17), 
                        ('Vancouver',      'Montreal',      20), 
                        ('Duluth',         'El Paso',       10), 
                        ('Toronto',        'Miami',         10)]
    len(tickets)
    max_value=len(tickets)-1
    random_number=random.randrange(0,max_value,1)
    return(tickets[random_number])
lista_tickets=[0,1,2]
for tickets in lista_tickets:
    print(testicket())
