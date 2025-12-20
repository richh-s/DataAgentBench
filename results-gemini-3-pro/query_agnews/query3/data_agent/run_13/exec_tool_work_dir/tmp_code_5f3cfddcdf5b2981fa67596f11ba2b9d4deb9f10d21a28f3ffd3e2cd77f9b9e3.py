code = """import json
import collections

# Load metadata
with open(locals()['var_function-call-13931165385016182989'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-13152675576488987514'], 'r') as f:
    articles_list = json.load(f)

# Create a lookup for articles
articles_map = {int(a['article_id']): a for a in articles_list if 'article_id' in a}

# Define keywords
business_keywords = {
    "business", "economy", "market", "stock", "trade", "finance", "financial", "invest", "investor", 
    "bank", "banking", "money", "profit", "revenue", "corporate", "company", "merger", "acquisition", 
    "deal", "shares", "prices", "oil", "gas", "energy", "industry", "manufacturing", "retail", "sales", 
    "tax", "rate", "fed", "central bank", "inflation", "dollar", "euro", "currency", "wall street", 
    "nasdaq", "dow jones", "employment", "jobs", "deficit", "budget", "debt", "gdp", "recession", 
    "growth", "bonds", "treasury", "ipo", "earnings", "quarterly", "dividend", "shareholder", "ceo", "cfo",
    "imf", "wto", "opec", "commidity", "futures", "sector", "venture"
}

tech_keywords = {
    "technology", "tech", "science", "computer", "software", "hardware", "internet", "web", "online", 
    "net", "mobile", "phone", "wireless", "network", "google", "microsoft", "apple", "intel", "ibm", 
    "nasa", "space", "astronomy", "biology", "physics", "research", "study", "launch", "satellite", 
    "orbit", "moon", "mars", "virus", "security", "hacker", "cyber", "chip", "processor", "gadget", 
    "device", "innovation", "digital", "broadband", "server", "data", "algorithm", "robot", "ai", 
    "artificial intelligence", "biotech", "genome", "lab", "patent", "linux", "windows", "browser"
}

sports_keywords = {
    "sport", "game", "match", "team", "player", "coach", "score", "win", "lose", "draw", "goal", 
    "touchdown", "basket", "ball", "league", "cup", "championship", "tournament", "olympic", "medal", 
    "athlete", "football", "soccer", "baseball", "basketball", "hockey", "tennis", "golf", "racing", 
    "driver", "formula one", "f1", "nascar", "cricket", "rugby", "stadium", "club", "season", "playoff", 
    "quarterback", "pitcher", "batter", "striker", "goalkeeper", "referee", "umpire", "nfl", "nba", 
    "mlb", "nhl", "fifa", "uefa"
}

world_keywords = {
    "world", "government", "president", "minister", "prime minister", "parliament", "congress", "senate", 
    "law", "police", "army", "military", "war", "conflict", "peace", "treaty", "election", "vote", 
    "poll", "country", "nation", "international", "un", "united nations", "eu", "european union", 
    "iraq", "iran", "afghanistan", "china", "russia", "us", "usa", "uk", "france", "germany", "bomb", 
    "attack", "kill", "dead", "blast", "disaster", "quake", "storm", "flood", "politics", "party", 
    "democrat", "republican", "diplomat", "official", "security", "terror", "troops", "strike", "protest",
    "israel", "palestinian", "baghdad", "korea", "nuclear"
}

def classify(text):
    text = text.lower()
    scores = {
        "business": 0,
        "tech": 0,
        "sports": 0,
        "world": 0
    }
    words = text.split()
    for w in words:
        # Avoid escaping issues by just stripping common punctuation
        w = w.strip(".,?!:;\"'")
        if w in business_keywords: scores["business"] += 1
        if w in tech_keywords: scores["tech"] += 1
        if w in sports_keywords: scores["sports"] += 1
        if w in world_keywords: scores["world"] += 1
    
    # Priority handling
    if scores["business"] == 0 and scores["tech"] == 0 and scores["sports"] == 0 and scores["world"] == 0:
        return "unknown"
    
    return max(scores, key=scores.get)

# Process
year_counts = collections.defaultdict(int)
missing_articles = 0
processed_count = 0
business_count = 0

for m in metadata_list:
    aid = int(m['article_id'])
    pub_date = m['publication_date'] # YYYY-MM-DD
    year = int(pub_date[:4])
    
    if 2010 <= year <= 2020:
        if aid in articles_map:
            art = articles_map[aid]
            content = (art.get('title', '') + " " + art.get('description', ''))
            cat = classify(content)
            if cat == 'business':
                year_counts[year] += 1
                business_count += 1
            processed_count += 1
        else:
            missing_articles += 1

# Calculate average
years = range(2010, 2021) # 2010 to 2020 inclusive
total_business = sum(year_counts[y] for y in years)
average = total_business / len(years)

result = {
    "year_counts": year_counts,
    "missing": missing_articles,
    "processed": processed_count,
    "total_business": total_business,
    "average": average
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-13931165385016182989': 'file_storage/function-call-13931165385016182989.json', 'var_function-call-3866583078313724775': 'file_storage/function-call-3866583078313724775.json', 'var_function-call-4925085607958011088': [{'_id': '6944cc47e14c7aa41c39dfa0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cc47e14c7aa41c39dfa1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cc47e14c7aa41c39dfa2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cc47e14c7aa41c39dfa3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cc47e14c7aa41c39dfa4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13638747952208399334': {'count': 14860, 'min_id': 3, 'max_id': 127583}, 'var_function-call-17502236686681799269': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13152675576488987514': 'file_storage/function-call-13152675576488987514.json'}

exec(code, env_args)
