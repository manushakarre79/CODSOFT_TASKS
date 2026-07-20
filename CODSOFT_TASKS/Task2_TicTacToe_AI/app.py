from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

board = [" " for _ in range(9)]


def check_winner(b, player):
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for w in wins:
        if b[w[0]] == b[w[1]] == b[w[2]] == player:
            return True
    return False


def minimax(b, is_max):
    if check_winner(b,"O"):
        return 1

    if check_winner(b,"X"):
        return -1

    if " " not in b:
        return 0


    if is_max:
        best = -math.inf

        for i in range(9):
            if b[i]==" ":
                b[i]="O"
                score=minimax(b,False)
                b[i]=" "
                best=max(best,score)

        return best

    else:
        best=math.inf

        for i in range(9):
            if b[i]==" ":
                b[i]="X"
                score=minimax(b,True)
                b[i]=" "
                best=min(best,score)

        return best



def best_move():

    score=-math.inf
    move=0

    for i in range(9):

        if board[i]==" ":

            board[i]="O"

            value=minimax(board,False)

            board[i]=" "

            if value>score:
                score=value
                move=i

    return move



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/move", methods=["POST"])
def player_move():

    data=request.json
    player=int(data["position"])


    if board[player]!=" ":
        return jsonify({"error":"Invalid move"})


    board[player]="X"


    if check_winner(board,"X"):
        return jsonify({"board":board,"result":"You Win!"})


    if " " not in board:
        return jsonify({"board":board,"result":"Draw"})


    ai=best_move()

    board[ai]="O"


    if check_winner(board,"O"):
        return jsonify({"board":board,"result":"AI Wins!"})


    return jsonify({"board":board,"result":""})



@app.route("/reset")
def reset():

    global board

    board=[" " for _ in range(9)]

    return jsonify({"status":"reset"})



if __name__=="__main__":
    app.run(debug=True)