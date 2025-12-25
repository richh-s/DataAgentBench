code = """import json
import re
import os

# Load filtered metadata
meta_var = locals()['var_function-call-5517223453251049220']
if isinstance(meta_var, str) and os.path.exists(meta_var):
    with open(meta_var, 'r') as f:
        metadata_list = json.load(f)
else:
    metadata_list = meta_var

# Load articles
articles_var = locals()['var_function-call-16606308814807674915']
if isinstance(articles_var, str) and os.path.exists(articles_var):
    with open(articles_var, 'r') as f:
        articles_list = json.load(f)
else:
    articles_list = articles_var

# Create lookup for metadata
meta_dict = {}
for m in metadata_list:
    meta_dict[str(m['article_id'])] = m['publication_date']

# Define Keywords (using the expanded lists)
business_keywords = {"business", "economy", "economic", "market", "markets", "stock", "stocks", "wall street", "bond", "bonds", "invest", "investment", "investor", "investors", "hedge fund", "private equity", "finance", "financial", "bank", "banks", "banking", "money", "dollar", "euro", "yen", "currency", "trade", "trading", "commodity", "commodities", "oil", "gas", "crude", "energy", "price", "prices", "gold", "companies", "company", "firm", "firms", "corp", "corporate", "profit", "profits", "earnings", "loss", "losses", "revenue", "revenues", "sales", "retail", "deal", "deals", "merger", "acquisition", "buyout", "ipo", "regulator", "sec", "fed", "federal reserve", "rates", "inflation", "job", "jobs", "unemployment", "ceo", "cfo", "executive", "manager", "management", "share", "shares", "shareholder", "dividend", "bankrupt", "bankruptcy", "audit", "accounting", "debt", "loan", "credit", "mortgage", "imf", "wto", "treasury", "budget", "tax", "taxes", "telecom", "telecoms", "airline", "airlines", "automaker", "automakers", "manufacturer", "manufacturing", "industry", "industrial", "commercial", "commerce"}

tech_keywords = {"technology", "tech", "science", "scientific", "computer", "computers", "computing", "software", "hardware", "internet", "web", "website", "online", "digital", "cyber", "virus", "worm", "hacker", "security", "data", "database", "network", "wireless", "mobile", "phone", "cellphone", "smartphone", "smartphones", "tablet", "laptop", "pc", "chip", "processor", "server", "cloud", "google", "microsoft", "apple", "intel", "ibm", "yahoo", "amazon", "facebook", "twitter", "space", "nasa", "shuttle", "mission", "mars", "moon", "astronomy", "universe", "planet", "galaxy", "physics", "biology", "genetics", "genome", "stem cell", "cloning", "medical", "medicine", "drug", "health", "cancer", "disease", "research", "lab", "scientist", "scientists", "engineer", "engineers", "robot", "robotics", "gadget", "device", "screen", "display", "video game", "gaming", "console", "broadband", "isp", "search engine", "browser", "operating system", "linux", "windows", "mac", "ipod", "itunes"}

sports_keywords = {"sport", "sports", "game", "games", "match", "matches", "team", "teams", "player", "players", "coach", "manager", "athlete", "athletes", "score", "scores", "scoring", "goal", "goals", "touchdown", "run", "runs", "homerun", "win", "wins", "winner", "winning", "won", "lose", "loses", "loser", "losing", "lost", "draw", "tie", "defeat", "victory", "champion", "champions", "championship", "cup", "league", "season", "tournament", "playoff", "playoffs", "olympic", "olympics", "medal", "gold", "silver", "bronze", "football", "soccer", "baseball", "basketball", "tennis", "golf", "hockey", "cricket", "rugby", "racing", "f1", "formula 1", "nascar", "driver", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "club", "stadium", "field", "court", "pitch", "referee", "umpire", "final", "finals", "semi-final", "quarter-final", "round", "heat", "lap", "time", "record", "world record"}

world_keywords = {"world", "international", "nation", "nations", "national", "country", "countries", "state", "states", "government", "governments", "politics", "political", "politician", "party", "election", "elections", "vote", "voters", "voting", "poll", "polls", "campaign", "candidate", "president", "presidency", "presidential", "prime minister", "minister", "ministry", "official", "officials", "leader", "leaders", "parliament", "congress", "senate", "house", "legislation", "law", "court", "judge", "ruling", "supreme court", "war", "wars", "conflict", "fight", "fighting", "battle", "military", "army", "navy", "air force", "soldier", "soldiers", "troops", "police", "security", "attack", "attacks", "bomb", "bombing", "blast", "explosion", "kill", "kills", "killed", "killing", "death", "deaths", "dead", "wound", "wounded", "injure", "injured", "casualty", "casualties", "terrorism", "terrorist", "terror", "al qaeda", "iraq", "afghanistan", "iran", "syria", "israel", "palestinian", "gaza", "lebanon", "egypt", "libya", "russia", "china", "north korea", "nuclear", "weapon", "weapons", "arms", "sanction", "sanctions", "treaty", "agreement", "talks", "summit", "meeting", "diplomacy", "diplomat", "ambassador", "embassy", "un", "united nations", "nato", "eu", "european union", "protest", "protests", "protester", "demonstration", "rally", "riot", "violence", "crisis", "disaster", "earthquake", "tsunami", "flood", "hurricane", "typhoon", "storm", "famine", "refugee", "human rights", "aid"}

categories = {
    "Business": business_keywords,
    "Sci/Tech": tech_keywords,
    "Sports": sports_keywords,
    "World": world_keywords
}

def classify(title, desc):
    text = (str(title) + " " + str(desc)).lower()
    # Simple tokenizer
    tokens = set(re.findall(r'\b[a-z]+\b', text))
    
    scores = {}
    for cat, keywords in categories.items():
        scores[cat] = len(tokens.intersection(keywords))
    
    best_cat = max(scores, key=scores.get)
    # Check if all 0, maybe classify as World or unknown?
    if scores[best_cat] == 0:
        return "Unclassified"
    
    return best_cat

yearly_counts = {year: 0 for year in range(2010, 2021)}
processed_count = 0
business_count = 0

for art in articles_list:
    aid = str(art.get('article_id'))
    if aid in meta_dict:
        processed_count += 1
        pub_date = meta_dict[aid]
        try:
            year = int(pub_date.split('-')[0])
            if 2010 <= year <= 2020:
                cat = classify(art.get('title', ''), art.get('description', ''))
                if cat == "Business":
                    yearly_counts[year] += 1
                    business_count += 1
        except:
            pass

total_years = 11
average = sum(yearly_counts.values()) / total_years

print("__RESULT__:")
print(json.dumps({
    "processed_articles": processed_count,
    "total_business": business_count,
    "yearly_counts": yearly_counts,
    "average": average
}))"""

env_args = {'var_function-call-5517223453251049220': 'file_storage/function-call-5517223453251049220.json', 'var_function-call-10913154760749403926': 'file_storage/function-call-10913154760749403926.json', 'var_function-call-2633958125002449470': [{'_id': '6944cee63429fba040671429', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cee63429fba04067142a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cee63429fba04067142b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cee63429fba04067142c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cee63429fba04067142d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14966595658088174430': [{'_id': '6944cee63429fba040671429', 'article_id': '0'}], 'var_function-call-3456426640295154631': [{'_id': '6944cee63429fba040671429', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cee63429fba04067142a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cee63429fba04067142b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cee63429fba04067142c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cee63429fba04067142d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10445686298075355025': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'average': 0.0}, 'var_function-call-9853011394914001325': {'metadata_count': 14860, 'articles_fetched_count': 5, 'intersection_count': 1, 'sample_meta_id': '42080', 'sample_art_id': '0'}, 'var_function-call-3404000095356730995': 'file_storage/function-call-3404000095356730995.json', 'var_function-call-3792693235583259872': {'max_id': 127583, 'min_id': 3, 'count': 14860}, 'var_function-call-16606308814807674915': 'file_storage/function-call-16606308814807674915.json'}

exec(code, env_args)
