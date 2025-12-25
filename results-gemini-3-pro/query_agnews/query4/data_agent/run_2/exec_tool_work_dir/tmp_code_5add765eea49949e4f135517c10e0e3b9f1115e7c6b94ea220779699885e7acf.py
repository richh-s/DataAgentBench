code = """import json
import collections

# Load Metadata (2015 articles)
path_meta = locals()['var_function-call-4524539130792533253'] # actually I should use the one I loaded before? 
# Wait, I loaded it in the previous execute_python step but didn't save it to a file, only printed. 
# But the file `var_function-call-4524539130792533253` still exists in storage.
# However, I also generated a filtered list of IDs in `var_function-call-12841960327215520545`. 
# But that file only has IDs, not regions.
# So I should reload the original metadata file `var_function-call-4524539130792533253`.

with open(path_meta, 'r') as f:
    meta_list = json.load(f)

# Create a mapping article_id -> region
# Ensure article_id is string
meta_map = {str(item['article_id']): item['region'] for item in meta_list}

# Load Articles (All)
path_articles = locals()['var_function-call-17275925162365337320']
# The previous query_db might have returned a list directly if small, or a file path.
# The system message said "The result is stored under key: ...". So it is a file path?
# Or is it a variable containing the list?
# If it's a file path, it's a string. If it's the list, it's a list.
# I'll check type.

try:
    with open(path_articles, 'r') as f:
        articles_list = json.load(f)
except (TypeError, FileNotFoundError):
    # It might be the list directly if the tool behaves that way (though instructions say large results are files)
    articles_list = path_articles 

# Filter articles to only those in 2015
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

# Classification Logic
categories = {
    'Sports': ["sport", "soccer", "football", "baseball", "basketball", "tennis", "golf", "hockey", "olympics", "olympic", "tournament", "championship", "league", "team", "athlete", "coach", "game", "match", "score", "cup", "medal", "nfl", "nba", "mlb", "fifa"],
    'Business': ["business", "market", "economy", "financial", "stock", "share", "invest", "bank", "profit", "loss", "trade", "deal", "merger", "acquisition", "company", "corporation", "sales", "revenue", "oil", "price", "wall st", "nasdaq", "dow", "dollar", "currency", "ceo", "earnings"],
    'Sci/Tech': ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "google", "microsoft", "apple", "iphone", "space", "nasa", "mars", "robot", "gadget", "device", "mobile", "wireless", "network", "silicon", "biology", "physics", "chemistry", "study", "research", "data", "cyber"],
    'World': ["world", "international", "politics", "war", "conflict", "iraq", "iran", "syria", "afghanistan", "gaza", "israel", "palestine", "ukraine", "russia", "china", "eu", "european union", "un", "united nations", "government", "president", "prime minister", "minister", "official", "military", "army", "troop", "bomb", "attack", "blast", "kill", "death", "disaster", "storm", "hurricane", "earthquake", "tsunami", "treaty", "diplomacy", "election", "vote", "poll", "parliament", "foreign", "refugee", "crisis"]
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    
    # If no keywords match, it's hard. But let's assume coverage is decent.
    # Return category with max score.
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return "Unknown"
    return best_cat

world_counts = collections.defaultdict(int)

for art in articles_2015:
    cat = classify(art['title'], art['description'])
    if cat == 'World':
        world_counts[art['region']] += 1

# Find region with max articles
if world_counts:
    top_region = max(world_counts, key=world_counts.get)
    count = world_counts[top_region]
else:
    top_region = "None"
    count = 0

print("__RESULT__:")
print(json.dumps({"top_region": top_region, "count": count, "all_counts": world_counts}))"""

env_args = {'var_function-call-4524539130792533253': 'file_storage/function-call-4524539130792533253.json', 'var_function-call-12841960327215520545': 'file_storage/function-call-12841960327215520545.json', 'var_function-call-17275925162365337320': [{'_id': '6944ea9ed4512ac83e64878c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ea9ed4512ac83e64878d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ea9ed4512ac83e64878e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ea9ed4512ac83e64878f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ea9ed4512ac83e648790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
