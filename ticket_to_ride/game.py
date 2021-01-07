from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from ast import literal_eval as make_tuple

from ticket_to_ride.auth import login_required
from ticket_to_ride.db import get_db
import logging
import random

bp = Blueprint("game", __name__)


@bp.route("/partida<int:id>/jugador<int:player>/", methods=("GET", "POST"))
@login_required

def player_ticket_menu(id,player):
    """Show all the tickets, most recent first."""
    
    # tickets_player=get_tickets_players(id,player)
    
    db = get_db()
    tickets_player = db.execute(
        "SELECT p.id, origen, destino,puntos, created,game_id, author_id, username"
        " FROM player_tickets p JOIN user u ON p.author_id = u.id"
        " WHERE p.game_id = ? AND p.player_id= ?"
        " ORDER BY created DESC",
        (id,player)
    ).fetchall()
    keys=tickets_player[0].keys()
    return render_template("game/tickets_jugador.html", tickets_player=tickets_player,id=id,player=player)

def get_tickets_players(id,player)  :

    tickets_player=(
            get_db()
            .execute(
                "SELECT p.id, origen, destino,puntos, created,game_id, author_id, username"
                " FROM player_tickets p JOIN user u ON p.author_id = u.id"
                " WHERE p.id = ? AND p.player_id= ?" ,
                (id,player),
            )
            .fetchone()
    )
    
    # if tickets_player is None:
    #         abort(404, f"Post id {id} or player {player} doesn't exist.")
    
    return tickets_player


    
    
            
@bp.route("/partida<int:id>/jugador<int:player>/create", methods=("GET", "POST"))
@login_required

def create(id,player):
    """Create a new ticket for the current user."""
    def get_ticket_random (numbers_of_tickets,tickets=[]):
        cantidad_de_tickets_actuales=len(tickets)
        total_tickets_al_finalizar=cantidad_de_tickets_actuales+numbers_of_tickets

        while cantidad_de_tickets_actuales<total_tickets_al_finalizar:
            all_tickets = [('Madrid',    'Lisboa', 3), 
                                ('Madrid',         'Barcelona',        2), 
                                ('Pamplona', 'París',      4), 
                                ('Lisboa',       'Cadiz',        6)]
           
            max_value=len(all_tickets)
            random_number=random.randrange(0,max_value,1)
            random_ticket=all_tickets[random_number]
            if random_ticket not in tickets:
                tickets.append(random_ticket)
                cantidad_de_tickets_actuales=len(tickets)
        return tickets
    
    tickets_player=get_tickets_players(id,player)
    tickets=[]
    if len(tickets)==0:
        tickets=(get_ticket_random(4))
    else:
        tickets=(get_ticket_random(1,tickets))
            

    return render_template("game/create_ticket.html", id=id,player=player,tickets=tickets)

@bp.route("/partida<int:id>/jugador<int:player>/save", methods=("GET", "POST"))
@login_required
def save_tickets(id,player):
    def save_ticket(game_id,player_id,ticket):
             
        origen,destino,puntos=make_tuple(ticket)
      
        db=get_db()
        db.execute(
                    "INSERT INTO player_tickets ( game_id,player_id, author_id,origen,destino,puntos) VALUES (?, ?,?, ?,?,?)",
                    (game_id, player_id,g.user["id"], origen,destino,puntos),
                )
        db.commit()
     
    if request.method == 'POST':
        
        if request.form['submit_button'] == 'Yeca':
            tickets = request.form.getlist('tickets')
            for ticket in tickets:
                
                save_ticket(id,player,ticket)
    
    return redirect(url_for("game.player_ticket_menu",id=id,player=player))
