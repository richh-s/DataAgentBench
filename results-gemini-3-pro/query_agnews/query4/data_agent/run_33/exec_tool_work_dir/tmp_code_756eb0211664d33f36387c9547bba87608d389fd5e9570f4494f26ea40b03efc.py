code = """import json
import collections

# Load data
with open(locals()['var_function-call-11571275440922023109'], 'r') as f:
    meta_list = json.load(f)

with open(locals()['var_function-call-11051996893389232622'], 'r') as f:
    articles_list = json.load(f)

# Map article_id to region for 2015 articles
# Handle potential type mismatch (str vs int). Convert everything to str for matching.
id_to_region = {}
for m in meta_list:
    aid = str(m['article_id'])
    id_to_region[aid] = m['region']

# Keywords
keywords = {
    "Sports": ["sport", "game", "match", "cup", "league", "team", "player", "coach", "score", "win", "won", "loss", "lost", "olympic", "nfl", "nba", "mlb", "nhl", "soccer", "football", "baseball", "basketball", "tennis", "golf", "racing", "medal", "champion", "tournament", "stadium", "athens", "sox", "yankees"],
    "Business": ["business", "market", "stock", "trade", "economy", "fiscal", "fed", "bank", "profit", "earnings", "dollar", "euro", "yen", "oil", "price", "corp", "inc", "ltd", "company", "merger", "deal", "ceo", "invest", "dow", "nasdaq", "wall st", "revenue"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "space", "nasa", "biotech", "study", "research", "cancer", "virus", "health", "mobile", "phone", "chip", "server", "data", "biology", "physics", "astronomy"],
    "World": ["world", "international", "war", "peace", "military", "army", "troop", "president", "minister", "government", "parliament", "senate", "election", "vote", "un", "united nations", "eu", "european union", "treaty", "nuclear", "bomb", "attack", "terror", "isis", "al qaeda", "syria", "iraq", "iran", "china", "russia", "korea", "afghanistan", "israel", "palestine", "ukraine", "protest", "crisis", "refugee", "diplomat", "foreign", "blast", "killed", "kill", "police", "security", "gaza", "baghdad", "cairo"]
}

# Counters
region_counts = collections.defaultdict(int)

debug_log = []

for art in articles_list:
    aid = str(art['article_id'])
    if aid in id_to_region:
        # It's a 2015 article
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        
        scores = {cat: 0 for cat in keywords}
        for cat, kws in keywords.items():
            for kw in kws:
                # Simple containment check
                if kw in text:
                    scores[cat] += 1
        
        # Determine category
        # If max score is 0, we can't classify (or maybe default to something? likely won't happen often)
        # Tie breaking: Just pick one (maybe based on priority or first found).
        if max(scores.values()) > 0:
            best_cat = max(scores, key=scores.get)
            
            if best_cat == "World":
                region_counts[id_to_region[aid]] += 1
                if len(debug_log) < 5:
                    debug_log.append({"title": art['title'], "region": id_to_region[aid], "scores": scores})

print("__RESULT__:")
print(json.dumps({"region_counts": region_counts, "debug": debug_log}))"""

env_args = {'var_function-call-11571275440922023109': 'file_storage/function-call-11571275440922023109.json', 'var_function-call-3574930073058179550': {'count': 6696, 'ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_function-call-11051996893389232622': [{'_id': '69451246c36b2bdffa0eca9e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451246c36b2bdffa0eca9f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451246c36b2bdffa0ecaa0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451246c36b2bdffa0ecaa1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451246c36b2bdffa0ecaa2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
