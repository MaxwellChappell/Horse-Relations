from geneology import relation, sort_dict

kentucky_derby = [
    "/hit+show3",
    "/verifying",
    "/two+phils",
    "/confidence+game2",
    "/tapit+trice",
    "/kingsbarns5",
    "/reincarnate3",
    "/mage6",
    "/skinner7",
    "/practical+move",
    "/disarm7",
    "/jaces+road",
    "/sun+thunder2",
    "/angel+of+empire",
    "/forte21",
    "/raise+cain",
    "/derma+sotogake",
    "/rocket+can",
    "/lord+miles",
    "/continuar",
]

entirety = {}

for horse in kentucky_derby:
    info = relation(horse)
    for ancestor in info:
        if ancestor in entirety:
            entirety[ancestor] += info[ancestor]
        else:
            entirety[ancestor] = info[ancestor]

entirety = sort_dict(entirety)

for horse in entirety:
    print(horse, entirety[horse]/20)
    