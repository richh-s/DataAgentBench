code = """import json
import collections

# Load Metadata
path_meta = locals()['var_function-call-4524539130792533253']
with open(path_meta, 'r') as f:
    meta_list = json.load(f)
meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Load Articles
path_articles = locals()['var_function-call-8766970931896504381']
with open(path_articles, 'r') as f:
    articles_list = json.load(f)

# Join
articles_2015 = []
for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_map:
        articles_2015.append({
            'article_id': aid,
            'title': art.get('title', ''),
            'description': art.get('description', ''),
            'region': meta_map[aid]
        })

# Classification
categories = {
    'Sports': ["sport", "soccer", "football", "baseball", "basketball", "tennis", "golf", "hockey", "olympics", "olympic", "tournament", "championship", "league", "team", "athlete", "coach", "game", "match", "score", "cup", "medal", "nfl", "nba", "mlb", "fifa"],
    'Business': ["business", "market", "economy", "financial", "stock", "share", "invest", "bank", "profit", "loss", "trade", "deal", "merger", "acquisition", "company", "corporation", "sales", "revenue", "oil", "price", "wall st", "nasdaq", "dow", "dollar", "currency", "ceo", "earnings", "imf", "fed", "deficit"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "iphone", "space", "nasa", "mars", "robot", "gadget", "device", "mobile", "wireless", "network", "silicon", "biology", "physics", "chemistry", "study", "research", "data", "cyber", "hacker", "virus"],
    'World': ["world", "international", "politics", "war", "conflict", "iraq", "iran", "syria", "afghanistan", "gaza", "israel", "palestine", "ukraine", "russia", "china", "eu", "european union", "un", "united nations", "government", "president", "prime minister", "minister", "official", "military", "army", "troop", "bomb", "attack", "blast", "kill", "death", "disaster", "storm", "hurricane", "earthquake", "tsunami", "treaty", "diplomacy", "election", "vote", "poll", "parliament", "foreign", "refugee", "crisis", "terrorism", "terror", "nuclear", "protest", "police", "court", "judge", "law"]
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # Heuristic for "World":
    # If "Business" and "World" both score, "Business" usually wins if terms like "oil", "price", "market" are present.
    # But "World" wins if "war", "attack", "president" (context dependent) are present.
    # Let's trust the score.
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    
    # Tie breaking
    # If tie between World and Business (e.g. oil price war), usually Business unless "war" or "politics".
    if scores['World'] == scores['Business'] and scores['World'] > 0:
        if any(w in text for w in ["war", "conflict", "attack", "kill", "military", "bomb"]):
            return "World"
        return "Business"
        
    return best_cat

world_counts = collections.defaultdict(int)
debug_list = []

for art in articles_2015:
    cat = classify(art['title'], art['description'])
    if cat == 'World':
        world_counts[art['region']] += 1
        if len(debug_list) < 5:
            debug_list.append(art)

if world_counts:
    top_region = max(world_counts, key=world_counts.get)
    count = world_counts[top_region]
else:
    top_region = "None"
    count = 0

print("__RESULT__:")
print(json.dumps({
    "top_region": top_region, 
    "count": count, 
    "all_counts": world_counts,
    "total_2015_classified_world": sum(world_counts.values()),
    "total_2015_articles": len(articles_2015),
    "sample_world_articles": [a['title'] for a in debug_list]
}))"""

env_args = {'var_function-call-4524539130792533253': 'file_storage/function-call-4524539130792533253.json', 'var_function-call-12841960327215520545': 'file_storage/function-call-12841960327215520545.json', 'var_function-call-17275925162365337320': [{'_id': '6944ea9ed4512ac83e64878c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ea9ed4512ac83e64878d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ea9ed4512ac83e64878e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ea9ed4512ac83e64878f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ea9ed4512ac83e648790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-845048519728556146': {'top_region': 'None', 'count': 0, 'all_counts': {}}, 'var_function-call-15108040845174692452': {'count_2015': 0, 'sample_titles': [], 'sample_descriptions': []}, 'var_function-call-16784580192302694402': {'len_articles': 5, 'first_ids': ['0', '1', '2', '3', '4']}, 'var_function-call-8766970931896504381': 'file_storage/function-call-8766970931896504381.json'}

exec(code, env_args)
