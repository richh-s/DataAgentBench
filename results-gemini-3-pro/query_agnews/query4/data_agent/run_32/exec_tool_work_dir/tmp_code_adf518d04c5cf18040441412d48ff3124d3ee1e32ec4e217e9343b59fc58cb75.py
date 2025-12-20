code = """import json
from collections import Counter

# Load metadata
with open(locals()['var_function-call-5900547977647289407'], 'r') as f:
    metadata_list = json.load(f)

# Create a map of article_id -> region for 2015 articles
# Ensure ID normalization (string)
article_region_map = {str(item['article_id']): item['region'] for item in metadata_list}

# Load articles content
with open(locals()['var_function-call-11413350339637926914'], 'r') as f:
    content_list = json.load(f)

# Keywords
keywords = {
    "World": [
        "afghanistan", "africa", "arab", "attack", "baghdad", "blast", "bomb", "border", "britain", 
        "china", "court", "crisis", "diplomat", "earthquake", "egypt", "election", "europe", 
        "explosion", "force", "foreign", "france", "gaza", "germany", "government", "hostage", 
        "india", "international", "iran", "iraq", "israel", "japan", "killed", "korea", "law", 
        "leader", "libya", "military", "minister", "missile", "moscow", "nation", "nato", 
        "nuclear", "official", "pakistan", "palestine", "parliament", "peace", "police", "politics", 
        "president", "prime minister", "protest", "province", "putin", "rebel", "refugee", "region", 
        "russia", "security", "soldier", "state", "strike", "suicide", "syria", "taliban", "terror", 
        "troop", "turkey", "ukraine", "un", "united nations", "war", "weapon", "world", "yemen"
    ],
    "Sports": [
        "baseball", "basketball", "champion", "coach", "cup", "defeat", "football", "game", "gold", 
        "golf", "hockey", "league", "medal", "mlb", "nascar", "nba", "nfl", "nhl", "olympic", 
        "player", "race", "score", "season", "soccer", "sport", "stadium", "team", "tennis", 
        "tournament", "victory", "win", "world cup"
    ],
    "Business": [
        "bank", "bond", "business", "buy", "ceo", "company", "corp", "deal", "dollar", "dow", 
        "earnings", "economy", "euro", "federal", "finance", "firm", "fund", "growth", "inc", 
        "industry", "invest", "job", "loss", "market", "merger", "money", "nasdaq", "oil", 
        "price", "profit", "quarter", "rate", "report", "revenue", "sale", "share", "stock", 
        "trade", "wall street"
    ],
    "Sci/Tech": [
        "android", "apple", "app", "astronomy", "biology", "browser", "cancer", "cell", "computer", 
        "device", "disease", "drug", "facebook", "galaxy", "gene", "google", "health", "internet", 
        "mars", "microsoft", "mission", "mobile", "moon", "nasa", "network", "online", "phone", 
        "planet", "research", "robot", "satellite", "science", "scientist", "server", "software", 
        "space", "study", "tech", "technology", "virus", "web", "windows", "wireless"
    ]
}

region_world_count = Counter()
debug_samples = []

for article in content_list:
    aid = str(article['article_id'])
    if aid in article_region_map:
        # It's a 2015 article
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        # Score categories
        scores = {cat: 0 for cat in keywords}
        for cat, words in keywords.items():
            for word in words:
                if word in text: # Simple substring match? Better to tokenize?
                    # Tokenize by splitting on non-alphanumeric
                    # But for simplicity, simple ' in ' check, but bounded by spaces?
                    # "win" in "winter" -> False positive. 
                    # Let's try simple ' ' + word + ' ' logic or regex?
                    # Or just count occurrences. 
                    scores[cat] += text.count(word)
        
        # Determine category
        # If max score is 0, classify as ... ? Maybe skip or assign 'World' if political words present?
        # Let's pick max.
        best_cat = max(scores, key=scores.get)
        
        # Tie-breaking logic:
        # If scores are equal, e.g. World: 1, Business: 1. "China oil deal".
        # If tied, maybe prioritize World? Or check specific keywords?
        # For now, just take max.
        
        if scores[best_cat] > 0 and best_cat == 'World':
            region = article_region_map[aid]
            region_world_count[region] += 1
            if len(debug_samples) < 5:
                debug_samples.append({"title": article['title'], "scores": scores, "region": region})

print("__RESULT__:")
print(json.dumps({"counts": dict(region_world_count), "debug": debug_samples}))"""

env_args = {'var_function-call-5900547977647289407': 'file_storage/function-call-5900547977647289407.json', 'var_function-call-8253439238580865499': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52]}, 'var_function-call-11413350339637926914': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
