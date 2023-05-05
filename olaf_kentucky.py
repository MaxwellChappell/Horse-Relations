from geneology import relation, sort_dict
from kentucky_derby import kentucky_horses

olaf = relation("/at+the+station2")
scores = {}
for horse in kentucky_horses:
    score = 0
    info = relation(horse)
    print(horse)
    for ancestor in info:
        if ancestor in olaf:
            print(ancestor, info[ancestor], olaf[ancestor])
            score += min(info[ancestor], olaf[ancestor])
    scores[horse] = score

leaderboard = sort_dict(scores)

for i, place in enumerate(leaderboard):
    print(f"{i + 1}: {place}, {leaderboard[place]}")
