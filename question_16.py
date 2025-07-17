def winner(move_a,move_b):
    move_a = move_a.lower()
    move_b = move_b.lower()

    if move_a == move_b:
        return "DRAW"
    elif (move_a == "stone" and move_b == "scissor") or (move_a == "scissor" and move_b == "paper") or (move_a == "paper" and move_b == "stone"):
        return "Player A wins"
    else:
        return "Player B wins"

def play():
    score_a =0
    score_b =0
    round= 1
    while score_a < 5 and score_b < 5:
        input_a =input("Player A: ").strip()
        input_b =input("Player B: ").strip()
        result=winner(input_a,input_b)
        print("Result:", result)

        if result == "Player A wins":
            score_a += 1
        elif result == "Player B wins":
            score_b += 1

        round += 1
    print("\nGame Over")
    if score_a == 5:
        print("Player A is the winner!")
    else:
        print("Player B is the winner!")
play()