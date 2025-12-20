code = """import json
import collections

# Load metadata (from file)
meta_var = locals()['var_function-call-11571275440922023109']
if isinstance(meta_var, str) and (meta_var.endswith('.json') or '/' in meta_var):
    with open(meta_var, 'r') as f:
        meta_list = json.load(f)
else:
    meta_list = meta_var

# Load articles (check if file or object)
articles_var = locals()['var_function-call-11051996893389232622']
if isinstance(articles_var, str) and (articles_var.endswith('.json') or '/' in articles_var):
    # It might be a file path if the system decided it was large but didn't print the standard message?
    # Or if I misread. Let's try to open if it looks like a path, else assume it's data.
    # However, if it's just a short string result, open might fail.
    # Safe check: try-except or check type.
    try:
        with open(articles_var, 'r') as f:
            articles_list = json.load(f)
    except:
        articles_list = articles_var # Assume it's the data
else:
    articles_list = articles_var

# Map article_id to region for 2015 articles
id_to_region = {}
for m in meta_list:
    aid = str(m['article_id'])
    id_to_region[aid] = m['region']

# Keywords (Same as before)
keywords = {
    "Sports": ["sport", "game", "match", "cup", "league", "team", "player", "coach", "score", "win", "won", "loss", "lost", "olympic", "nfl", "nba", "mlb", "nhl", "soccer", "football", "baseball", "basketball", "tennis", "golf", "racing", "medal", "champion", "tournament", "stadium", "athens", "sox", "yankees"],
    "Business": ["business", "market", "stock", "trade", "economy", "fiscal", "fed", "bank", "profit", "earnings", "dollar", "euro", "yen", "oil", "price", "corp", "inc", "ltd", "company", "merger", "deal", "ceo", "invest", "dow", "nasdaq", "wall st", "revenue", "financial"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "space", "nasa", "biotech", "study", "research", "cancer", "virus", "health", "mobile", "phone", "chip", "server", "data", "biology", "physics", "astronomy"],
    "World": ["world", "international", "war", "peace", "military", "army", "troop", "president", "minister", "government", "parliament", "senate", "election", "vote", "un", "united nations", "eu", "european union", "treaty", "nuclear", "bomb", "attack", "terror", "isis", "al qaeda", "syria", "iraq", "iran", "china", "russia", "korea", "afghanistan", "israel", "palestine", "ukraine", "protest", "crisis", "refugee", "diplomat", "foreign", "blast", "killed", "kill", "police", "security", "gaza", "baghdad", "cairo", "premier", "official", "strike"]
}

region_counts = collections.defaultdict(int)

# To debug, let's track which categories are found
debug_info = {"total_articles_2015": len(id_to_region), "processed": 0, "classified_world": 0}

for art in articles_list:
    # Ensure article is a dict (just in case)
    if not isinstance(art, dict): continue
    
    aid = str(art.get('article_id'))
    if aid in id_to_region:
        debug_info["processed"] += 1
        title = art.get('title', '')
        desc = art.get('description', '')
        # Handle None
        if title is None: title = ""
        if desc is None: desc = ""
        
        text = (title + " " + desc).lower()
        
        scores = {cat: 0 for cat in keywords}
        for cat, kws in keywords.items():
            for kw in kws:
                if kw in text:
                    scores[cat] += 1
        
        if max(scores.values()) > 0:
            best_cat = max(scores, key=scores.get)
            if best_cat == "World":
                region_counts[id_to_region[aid]] += 1
                debug_info["classified_world"] += 1

print("__RESULT__:")
print(json.dumps({"region_counts": region_counts, "debug": debug_info}))"""

env_args = {'var_function-call-11571275440922023109': 'file_storage/function-call-11571275440922023109.json', 'var_function-call-3574930073058179550': {'count': 6696, 'ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_function-call-11051996893389232622': [{'_id': '69451246c36b2bdffa0eca9e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451246c36b2bdffa0eca9f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451246c36b2bdffa0ecaa0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451246c36b2bdffa0ecaa1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451246c36b2bdffa0ecaa2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
