code = """import json
import collections
import re

# Load Metadata
meta_path = locals()['var_function-call-8065168044607916997']
with open(meta_path, 'r') as f:
    metadata_list = json.load(f)

# Load Articles
articles_path = locals()['var_function-call-5534044041402657599']
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# Build Article Map
article_map = {}
for art in articles_list:
    aid = str(art.get('article_id'))
    article_map[aid] = {
        'title': art.get('title', ''),
        'description': art.get('description', '')
    }

# Classification Keywords
keywords = {
    'Sports': ["sport", "game", "match", "team", "player", "coach", "win", "victory", "defeat", "score", "season", "league", "cup", "championship", "tournament", "olympic", "medal", "gold", "silver", "bronze", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "athlete", "stadium", "club", "nfl", "nba", "mlb", "nhl", "fifa", "uefa"],
    'Business': ["business", "company", "corp", "inc", "market", "stock", "share", "trade", "economy", "economic", "dollar", "euro", "yen", "currency", "price", "cost", "profit", "loss", "revenue", "sale", "buy", "sell", "deal", "merger", "acquisition", "bank", "finance", "financial", "invest", "investment", "investor", "ceo", "cfo", "manager", "oil", "gas", "energy", "crude", "barrel", "industry", "manufacturing", "retail", "consumer", "dow", "nasdaq", "wall street"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "network", "digital", "data", "phone", "mobile", "wireless", "satellite", "space", "nasa", "astronomy", "biology", "chemistry", "physics", "research", "study", "scientist", "discovery", "invention", "device", "gadget", "microsoft", "google", "apple", "intel", "ibm", "linux", "windows", "virus", "hacker", "browser", "server"],
    'World': ["world", "international", "government", "politics", "political", "president", "minister", "leader", "official", "state", "country", "nation", "un", "united nations", "eu", "european union", "nato", "war", "peace", "conflict", "military", "army", "troop", "soldier", "weapon", "nuclear", "terror", "terrorist", "attack", "bomb", "blast", "kill", "death", "injure", "casualty", "rebel", "insurgent", "police", "court", "trial", "judge", "law", "election", "vote", "campaign", "party", "protest", "riot", "demonstration", "disaster", "earthquake", "flood", "storm", "hurricane", "crash", "accident", "hostage", "kidnap", "treaty", "agreement", "sanction", "diplomacy", "foreign", "iraq", "iran", "afghanistan", "palestine", "israel", "syria", "russia", "china", "korea", "sudan", "africa", "asia", "europe", "latin america", "baghdad", "kabul", "tehran", "jerusalem", "gaza"]
}

def classify(text):
    text = text.lower()
    scores = {k: 0 for k in keywords}
    for cat, words in keywords.items():
        for w in words:
            # Simple substring match or word boundary match?
            # Word boundary is better to avoid "win" in "winner" (okay) or "window" (bad).
            # But regex might be slow for many calls.
            # Let's try simple tokenization.
            if w in text:
                scores[cat] += 1
    
    # Heuristics for ties or specific terms
    if "oil" in text and "price" in text: scores['Business'] += 2
    if "iraq" in text: scores['World'] += 2
    if "president" in text: scores['World'] += 1
    if "game" in text: scores['Sports'] += 1
    
    # Get max score
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unclassified'
    return best_cat

# Count World articles per region
region_counts = collections.defaultdict(int)

for item in metadata_list:
    aid = str(item['article_id'])
    region = item['region']
    
    if aid in article_map:
        content = article_map[aid]['title'] + " " + article_map[aid]['description']
        category = classify(content)
        if category == 'World':
            region_counts[region] += 1

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-4853062979931688291': ['authors', 'article_metadata'], 'var_function-call-4853062979931687004': ['articles'], 'var_function-call-8065168044607916997': 'file_storage/function-call-8065168044607916997.json', 'var_function-call-5431530743641856445': 6696, 'var_function-call-5110049920548127149': [{'_id': '694509f52dd2076557e496d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694509f52dd2076557e496d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694509f52dd2076557e496d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694509f52dd2076557e496d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694509f52dd2076557e496d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1075365744212528405': 5, 'var_function-call-5534044041402657599': 'file_storage/function-call-5534044041402657599.json'}

exec(code, env_args)
