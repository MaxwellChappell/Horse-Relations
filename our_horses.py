from geneology import relation, sort_dict
from itertools import combinations

horses = ["/at+the+station2", "/grand+fappy", "/starship+brooklyn", "/surprenant2", "/lovable+louis", "/cap+trick", "/bones+baxter","/penalty+shot3", "/saylers+creek2","/shake+thechampagne","/yankee+scholar", "/ten+guitars","/piney+north"]
nice_names = {
    "/at+the+station2": "Olaf", 
    "/grand+fappy":"Cosmo", 
    "/starship+brooklyn": "Brooklyn", 
    "/surprenant2": "Oliver", 
    "/lovable+louis":"Louie", 
    "/cap+trick": "Cap Trick", 
    "/bones+baxter": "Archie",
    "/penalty+shot3": "Jet", 
    "/saylers+creek2": "Sayler",
    "/shake+thechampagne":"Cleo",
    "/yankee+scholar": "Yankee Scholar",
    "/ten+guitars": "Ten",
    "/piney+north":"Jones"
}

genes = {}
for horse in horses:
    genes[horse] = relation(horse)

all_pairs = list(combinations(horses, 2))
results = {}
singular_results = {
    "/at+the+station2": {}, 
    "/grand+fappy":{}, 
    "/starship+brooklyn": {}, 
    "/surprenant2": {}, 
    "/lovable+louis": {}, 
    "/cap+trick": {}, 
    "/bones+baxter": {},
    "/penalty+shot3": {}, 
    "/saylers+creek2": {},
    "/shake+thechampagne":{},
    "/yankee+scholar": {},
    "/ten+guitars": {},
    "/piney+north":{}
}
for combo in all_pairs:
    horse1 = genes[combo[0]]
    horse2 = genes[combo[1]]
    score = 0
    nice_pair = f"{nice_names[combo[0]]}, {nice_names[combo[1]]}"
    print(nice_pair)
    for ancestor in horse1:
        if ancestor in horse2:
            print(ancestor, horse1[ancestor], horse2[ancestor])
            score += min(horse1[ancestor], horse2[ancestor])
    singular_results[combo[0]][combo[1]] = score
    singular_results[combo[1]][combo[0]] = score
    results[nice_pair] = score

for horse in horses:
    leaderboard = sort_dict(singular_results[horse])
    print(nice_names[horse])
    for i, place in enumerate(leaderboard):
        print(f"{i + 1}: {nice_names[place]}, {leaderboard[place]}")
    print()

full_leaderboard = sort_dict(results)
for i, place in enumerate(full_leaderboard):
     print(f"{i + 1}: {place}, {full_leaderboard[place]}")
