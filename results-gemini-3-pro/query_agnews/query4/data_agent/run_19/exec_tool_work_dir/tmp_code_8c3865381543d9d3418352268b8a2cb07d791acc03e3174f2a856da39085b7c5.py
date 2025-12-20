code = """import json
import collections

# Load metadata
meta_path = locals()['var_function-call-2515222159544851485']
with open(meta_path, 'r') as f:
    metadata_list = json.load(f)

article_region = {item['article_id']: item['region'] for item in metadata_list}
target_ids = set(article_region.keys())

# Load articles
articles_path = locals()['var_function-call-899974702503546662']
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# Keywords (Refined)
categories = {
    "World": [
        "iraq", "iran", "president", "prime minister", "official", "military", "war", "bomb", "blast", "kill", 
        "un", "united nations", "parliament", "election", "vote", "security", "china", "russia", "israel", 
        "palestinian", "gaza", "darfur", "sudan", "syria", "lebanon", "afghanistan", "pakistan", "baghdad", 
        "tehran", "korea", "nuclear", "treaty", "talks", "diplomat", "court", "trial", "hurricane", "tsunami", 
        "terror", "rebel", "insurgent", "government", "senate", "congress", "bush", "putin", "blair", "sharon", 
        "arafat", "budget", "law", "politic", "party", "leader"
    ],
    "Sports": [
        "sport", "game", "cup", "team", "league", "match", "score", "win", "loss", "medal", "olympic", "player", 
        "coach", "champion", "nfl", "nba", "mlb", "nhl", "football", "soccer", "baseball", "basketball", "tennis", 
        "golf", "racing", "f1", "nascar", "stadium", "athlete", "sox", "yankee", "mets", "bulls", "lakers", 
        "tournament", "race", "rugby", "cricket"
    ],
    "Business": [
        "market", "stock", "share", "price", "profit", "earnings", "revenue", "dollar", "euro", "yen", "bank", 
        "fed", "economy", "trade", "sale", "oil", "gas", "company", "corp", "inc", "business", 'deal', 'merger', 
        'ceo', 'invest', 'fund', 'wall st', 'nasdaq', 'dow', 'gold', 'financial', 'inflation', 'rate', 'job'
    ],
    "Sci/Tech": [
        "google", "microsoft", "apple", "ibm", "intel", "software", "hardware", "internet", "web", "computer", 
        "phone", 'mobile', 'space', 'nasa', 'science', 'tech', 'technology', 'virus', 'chip', 'linux', 'windows', 
        'server', 'online', 'digital', 'wireless', 'broadband', 'satellite', 'orbit', 'robot', 'biotech', 'browser'
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
    if max(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

cat_counts = collections.defaultdict(int)
region_world_counts = collections.defaultdict(int)

# Inspect some classifications
samples = []

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in target_ids:
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = f"{title} {desc}"
        cat = classify(full_text)
        cat_counts[cat] += 1
        
        if cat == "World":
            region = article_region[aid]
            region_world_counts[region] += 1
            if len(samples) < 5:
                samples.append(f"[{region}] {title}")

print("__RESULT__:")
print(json.dumps({
    "distribution": cat_counts,
    "world_by_region": region_world_counts,
    "samples": samples
}))"""

env_args = {'var_function-call-13208856365886244928': ['authors', 'article_metadata'], 'var_function-call-13208856365886244455': ['articles'], 'var_function-call-2515222159544851485': 'file_storage/function-call-2515222159544851485.json', 'var_function-call-13593231486142691637': 6696, 'var_function-call-16822267018933619895': {'min': 13, 'max': 127570}, 'var_function-call-16039217225285372494': [{'_id': '6944ffdbcbef4a7a7193d6b3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ffdbcbef4a7a7193d6b4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ffdbcbef4a7a7193d6b5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ffdbcbef4a7a7193d6b6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ffdbcbef4a7a7193d6b7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8126212337696475554': 5, 'var_function-call-8676179416535457116': [{'_id': '6944ffdbcbef4a7a7193d6b3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ffdbcbef4a7a7193d6b4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ffdbcbef4a7a7193d6b5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ffdbcbef4a7a7193d6b6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ffdbcbef4a7a7193d6b7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17293137481658764797': 5, 'var_function-call-899974702503546662': 'file_storage/function-call-899974702503546662.json', 'var_function-call-10050718031818148829': {'Asia': 607, 'Africa': 608, 'Europe': 635, 'South America': 633, 'North America': 625}}

exec(code, env_args)
