code = """import json
import collections

# Load metadata (ID -> Region) for 2015
# The file path is in 'var_function-call-5438198083873646081'
meta_path = locals()['var_function-call-5438198083873646081']
with open(meta_path, 'r') as f:
    metadata_list = json.load(f)

# Create a dictionary for quick lookup: article_id -> region
# Ensure article_id is string to match articles DB result
meta_dict = {str(item['article_id']): item['region'] for item in metadata_list}

# Load articles
# The file path is in 'var_function-call-5122843298511226853'
articles_path = locals()['var_function-call-5122843298511226853']
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# Keywords (Heuristic)
world_keywords = {
    "world", "international", "un", "united nations", "war", "peace", "military", "army", "troops", 
    "president", "minister", "parliament", "government", "diplomat", "treaty", "nuclear", "bomb", "blast",
    "attack", "crisis", "refugee", "migrant", "syria", "iraq", "afghanistan", "iran", "korea", "china", 
    "russia", "ukraine", "eu", "europe", "nato", "israel", "palestine", "isis", "islamic state", "terror", 
    "boko haram", "al qaeda", "police", "crash", "disaster", "storm", "quake", "vote", "election", 
    "leader", "protest", "court", "law", "official", "state", "country", "security", "force", "fight", "kill"
}
sports_keywords = {
    "sport", "game", "match", "cup", "league", "team", "score", "win", "lose", "player", "coach", 
    "football", "soccer", "basketball", "baseball", "hockey", "tennis", "golf", "olympic", "championship", 
    "tournament", "medal", "athlete", "race", "f1", "nfl", "nba", "mlb", "nhl", "fifa", "club", "squad"
}
business_keywords = {
    "business", "company", "stock", "market", "share", "price", "economy", "economic", "trade", "profit", 
    "loss", "bank", "finance", "investment", "dollar", "euro", "yen", "oil", "gas", "energy", "corp", 
    "inc", "ltd", "deal", "merger", "acquisition", "revenue", "sales", "ceo", "cfo", "investor", "wall street"
}
scitech_keywords = {
    "science", "technology", "computer", "internet", "web", "software", "hardware", "phone", "mobile", 
    "app", "google", "microsoft", "apple", "ibm", "intel", "space", "nasa", "astronomy", "biology", 
    "genetics", "medical", "study", "research", "virus", "disease", "health", "cancer", "drug", "patient", 
    "browser", "server", "chip", "wireless", "network", "online", "digital"
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Simple tokenization by removing punctuation is better, but simple split is fast
    import re
    tokens = set(re.findall(r'\w+', text))
    
    scores = {
        "World": len(tokens.intersection(world_keywords)),
        "Sports": len(tokens.intersection(sports_keywords)),
        "Business": len(tokens.intersection(business_keywords)),
        "Sci/Tech": len(tokens.intersection(scitech_keywords))
    }
    
    # If all 0, default to World? Or Unknown? 
    # In AG News, usually World is the 'catch-all' for political/general news.
    if max(scores.values()) == 0:
        return "World" # Default
    
    return max(scores, key=scores.get)

# Process
world_articles_regions = []
count_classified = 0
count_world = 0

for article in articles_list:
    aid = str(article['article_id'])
    if aid in meta_dict:
        # It's a 2015 article
        cat = classify(article.get('title', ''), article.get('description', ''))
        count_classified += 1
        if cat == "World":
            world_articles_regions.append(meta_dict[aid])
            count_world += 1

# Count by region
region_counts = collections.Counter(world_articles_regions)
most_common = region_counts.most_common(1)

print(f"Classified {count_classified} articles.")
print(f"Found {count_world} World articles.")
print(f"Region counts: {region_counts}")

print("__RESULT__:")
print(json.dumps(most_common))"""

env_args = {'var_function-call-5438198083873646081': 'file_storage/function-call-5438198083873646081.json', 'var_function-call-663649913820504999': 'file_storage/function-call-663649913820504999.json', 'var_function-call-17511441074562581401': 'file_storage/function-call-17511441074562581401.json', 'var_function-call-1490848209420094816': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17174248310466427660': [{'_id': '69451ba04596b9c169c8dcc5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69451ba04596b9c169c8dcc6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69451ba04596b9c169c8dcc7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69451ba04596b9c169c8dcc8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69451ba04596b9c169c8dcc9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-12965496480603250842': 'file_storage/function-call-12965496480603250842.json', 'var_function-call-5122843298511226853': 'file_storage/function-call-5122843298511226853.json'}

exec(code, env_args)
