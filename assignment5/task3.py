#Task 3: Game Scoreboard

players = []
for i in range(5):
    print(f"Enter scores for Player {i+1} (4 rounds):")
    scores = list(map(int, input().split()))
    players.append(scores)

total_scores = [sum(scores) for scores in players]
average_scores = [sum(scores) / 4 for scores in players]

print("\nScoreboard:")
for i, scores in enumerate(players, 1):
    print(f"Player {i}: Scores = {scores}, Total = {total_scores[i-1]}, Average = {average_scores[i-1]:.2f}")

print("\nRound Summary:")
for round_num, scores in enumerate(zip(*players), 1):
    print(f"Round {round_num}: Highest = {max(scores)}, Lowest = {min(scores)}")

rankings = sorted(enumerate(total_scores, 1), key=lambda x: x[1], reverse=True)
print("\nRankings:")
for rank, (player, score) in enumerate(rankings, 1):
    print(f"{rank}. Player {player} with {score} points")
