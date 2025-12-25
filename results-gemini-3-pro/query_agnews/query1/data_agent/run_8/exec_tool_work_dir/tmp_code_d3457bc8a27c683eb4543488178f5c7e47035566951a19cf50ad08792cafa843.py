code = """import json
import re

with open(locals()['var_function-call-8284316981365420739'], 'r') as f:
    articles = json.load(f)

# Expanded Keywords
sp = set([
    "sport", "sports", "football", "basketball", "baseball", "soccer", "tennis", "golf", "hockey", 
    "olympic", "olympics", "medal", "tournament", "championship", "league", "cup", "athlete", 
    "player", "coach", "team", "match", "score", "game", "playoff", "finals", "nfl", "nba", "mlb", 
    "nhl", "fifa", "uefa", "quarterback", "touchdown", "goal", "red sox", "yankees", "lakers", 
    "bulls", "celtics", "knicks", "pistons", "pacers", "spurs", "heat", "suns", "dodgers", "giants", 
    "mets", "phillies", "braves", "marlins", "cardinals", "astros", "rangers", "patriots", "eagles", 
    "steelers", "colts", "vikings", "packers", "falcons", "panthers", "jaguars", "broncos", "chiefs", 
    "raiders", "chargers", "cowboys", "redskins", "real madrid", "barcelona", "manchester", 
    "arsenal", "chelsea", "liverpool", "milan", "juventus", "bayern", "athens", "swimming", 
    "gymnastics", "marathon", "sprint", "driver", "nascar", "f1", "rugby", "cricket", "boxing", 
    "wrestling", "davis cup", "ryder cup", "pga", "lpga", "wta", "atp", "grand slam", "wimbledon",
    "us open", "french open", "australian open"
])

biz = set([
    "stock", "stocks", "market", "markets", "price", "prices", "company", "companies", "corp", 
    "inc", "ltd", "profit", "profits", "revenue", "revenues", "earnings", "sale", "sales", 
    "investment", "investor", "share", "shares", "economy", "economic", "trade", "trading", 
    "dollar", "euro", "yen", "currency", "bank", "banks", "banking", "fed", "federal reserve", 
    "inflation", "rate", "rates", "job", "jobs", "unemployment", "manager", "ceo", "cfo", 
    "wall st", "wall street", "nasdaq", "dow", "jones", "oil", "gas", "energy", "crude", "barrel", 
    "merger", "acquisition", "deal", "ipo", "finance", "financial", "retail", "retailer"
])

tech = set([
    "software", "internet", "computer", "computers", "microsoft", "google", "apple", "linux", 
    "windows", "virus", "worm", "spam", "security", "hacker", "space", "nasa", "science", 
    "scientific", "research", "researcher", "study", "cell", "phone", "mobile", "wireless", 
    "technology", "tech", "web", "online", "digital", "chip", "processor", "intel", "amd", 
    "ibm", "server", "network", "broadband", "satellite", "robot", "gadget", "device"
])

world = set([
    "iraq", "iraqi", "baghdad", "president", "bush", "kerry", "election", "elections", "vote", 
    "voters", "voting", "campaign", "war", "peace", "government", "minister", "official", 
    "officials", "un", "united nations", "eu", "european union", "police", "court", "judge", 
    "military", "army", "troops", "soldier", "soldiers", "bomb", "blast", "explosion", "attack", 
    "attacks", "kill", "killed", "politics", "political", "politician", "congress", "senate", 
    "senator", "representative", "democrat", "republican", "law", "bill", "palestine", "palestinian", 
    "israel", "israeli", "gaza", "sharon", "arafat", "iran", "nuclear", "weapon", "terror", 
    "terrorism", "terrorist", "al qaeda", "bin laden", "sudan", "darfur", "russia", "putin"
])

def classify(text):
    words = re.findall(r'\w+', text.lower())
    scores = {"S": 0, "B": 0, "T": 0, "W": 0}
    for w in words:
        if w in sp: scores["S"] += 1
        if w in biz: scores["B"] += 1
        if w in tech: scores["T"] += 1
        if w in world: scores["W"] += 1
    
    # Heuristics for ambiguity
    # If "senate" or "congress" or "bush" is present, heavily penalize Sports (unless it's Reggie Bush?)
    # But usually in 2004 (AG News dataset time), Bush is George W. Bush.
    if any(w in ["senate", "congress", "bush", "kerry", "iraq", "election"] for w in words):
        scores["S"] -= 5 # Penalty
        
    if max(scores.values()) == 0: return "U"
    return max(scores, key=scores.get)

articles.sort(key=lambda x: len(x['description']), reverse=True)

found = None
for art in articles:
    ft = art['title'] + " " + art['description']
    c = classify(ft)
    if c == "S":
        found = art
        break

print("__RESULT__:")
print(json.dumps(found))"""

env_args = {'var_function-call-5600887256776046897': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6243788860290969808': ['authors', 'article_metadata'], 'var_function-call-621124544545937450': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-14125888797793058960': [{'_id': '694468d48f62606ef06538a3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-371116049882488257': [{'author_id': '0', 'name': 'Felicia Miles'}, {'author_id': '1', 'name': 'Stacy Hunt'}, {'author_id': '2', 'name': 'Carol Reed'}, {'author_id': '3', 'name': 'Dr. Daniel Brown'}, {'author_id': '4', 'name': 'Andre Lam MD'}], 'var_function-call-16428439284826624530': [{'_id': '694468d48f62606ef06538a3', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694468d48f62606ef06538a4', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694468d48f62606ef06538a5', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694468d48f62606ef06538a6', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694468d48f62606ef06538a7', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7895339117705645390': {'count': 5, 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)']}, 'var_function-call-15665066354817605845': 'file_storage/function-call-15665066354817605845.json', 'var_function-call-4236206756542118061': {'count': 10000}, 'var_function-call-8284316981365420739': 'file_storage/function-call-8284316981365420739.json', 'var_function-call-1559858938885482885': {'_id': '694468d48f62606ef0664643', 'title': '2004 US Senate Outlook', 'description': "With all the hoopla over Bush and Kerry, some of you may not have been paying close attention to the other races going on in this loaded US political season. I've read a good dozen or so Senate outlooks, and my blurry eyes and spinning brain kept getting lost in all the numbers and losing track of who, ultimately, was likely to control the Senate on November third. So I made my very own Senate outlook to figure it out (or add further confusion, depending on what you think of my predictions). The bad news is, we probably won't know who controls the Senate on November third. The good news, if you're a Democrat (or a person who loves one), is that my best guess at this point is that when the dust settles, Democrats will probably be in control by the very slimmest possible margin. Shock! But everyone knows the Dems have no chance of taking either house of Congress. I think everyone hasn't been paying attention. Read on for my rundown."}}

exec(code, env_args)
