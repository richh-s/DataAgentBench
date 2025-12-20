code = """import json
import collections

# Load Metadata
meta_path = locals()['var_function-call-8065168044607916997']
with open(meta_path, 'r') as f:
    metadata_list = json.load(f)

# Load Articles
articles_path = locals()['var_function-call-5534044041402657599']
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

article_map = {}
for art in articles_list:
    aid = str(art.get('article_id'))
    article_map[aid] = {
        'title': art.get('title', ''),
        'description': art.get('description', '')
    }

keywords = {
    'Sports': ["sport", "game", "match", "team", "player", "coach", "win", "victory", "defeat", "score", "season", "league", "cup", "championship", "tournament", "olympic", "medal", "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "athlete", "stadium", "club", "fifa", "uefa", "nfl", "nba", "racing", "driver"],
    'Business': ["business", "company", "corp", "market", "stock", "share", "economy", "economic", "dollar", "euro", "currency", "price", "profit", "revenue", "sale", "deal", "merger", "bank", "finance", "invest", "oil", "gas", "energy", "industry", "dow", "nasdaq", "wall street", "fed", "central bank", "rates", "inflation"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "software", "internet", "web", "digital", "data", "phone", "mobile", "space", "nasa", "biology", "physics", "research", "scientist", "microsoft", "google", "apple", "intel", "linux", "virus", "hacker", "robot", "online"],
    'World': ["world", "international", "government", "politics", "president", "minister", "leader", "official", "state", "country", "nation", "un", "united nations", "eu", "nato", "war", "peace", "military", "army", "troop", "soldier", "nuclear", "terror", "attack", "bomb", "blast", "kill", "rebel", "police", "election", "vote", "protest", "riot", "disaster", "earthquake", "tsunami", "flood", "hostage", "kidnap", "treaty", "diplomacy", "foreign", "iraq", "syria", "afghanistan", "iran", "palestine", "israel", "ukraine", "yemen", "libya", "isis", "islamic state", "refugee", "migrant", "crisis", "parliament", "senate"]
}

def classify(text):
    text = text.lower()
    scores = {k: 0 for k in keywords}
    for cat, words in keywords.items():
        for w in words:
            if w in text:
                scores[cat] += 1
    
    # Weights
    if "oil" in text and ("price" in text or "market" in text): scores['Business'] += 2
    if "iraq" in text or "syria" in text: scores['World'] += 2
    if "president" in text: scores['World'] += 1
    if "cup" in text and "world" in text: scores['Sports'] += 2 # World Cup
    if "championship" in text: scores['Sports'] += 1
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unclassified'
    return best_cat

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

env_args = {'var_function-call-4853062979931688291': ['authors', 'article_metadata'], 'var_function-call-4853062979931687004': ['articles'], 'var_function-call-8065168044607916997': 'file_storage/function-call-8065168044607916997.json', 'var_function-call-5431530743641856445': 6696, 'var_function-call-5110049920548127149': [{'_id': '694509f52dd2076557e496d0', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694509f52dd2076557e496d1', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694509f52dd2076557e496d2', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694509f52dd2076557e496d3', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694509f52dd2076557e496d4', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1075365744212528405': 5, 'var_function-call-5534044041402657599': 'file_storage/function-call-5534044041402657599.json', 'var_function-call-5091405437131664763': {'Asia': 73, 'North America': 88, 'South America': 81, 'Europe': 68, 'Africa': 90}}

exec(code, env_args)
