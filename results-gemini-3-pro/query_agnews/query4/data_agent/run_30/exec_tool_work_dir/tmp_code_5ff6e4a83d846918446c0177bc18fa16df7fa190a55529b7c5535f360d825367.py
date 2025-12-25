code = """import json
import collections
import re

# Load metadata (2015 articles)
with open(locals()['var_function-call-9402959819383380444'], 'r') as f:
    metadata_list = json.load(f)

# Load articles content
# The file path is in var_function-call-6775040428661401644
with open(locals()['var_function-call-6775040428661401644'], 'r') as f:
    articles_list = json.load(f)

# Create a dictionary for articles content: id -> {title, description}
# Normalize IDs to string
articles_content = {}
for art in articles_list:
    aid = str(art['article_id'])
    articles_content[aid] = {
        'title': art.get('title', ''),
        'description': art.get('description', '')
    }

# Keywords
keywords = {
    "World": [
        "president", "minister", "leader", "official", "government", "parliament", "congress", "senate", 
        "united nations", "un", "eu", "nato", "war", "peace", "military", "troops", "army", "police", 
        "attack", "bomb", "blast", "killed", "dead", "injured", "crisis", "conflict", "nuclear", "weapon", 
        "treaty", "talks", "meeting", "summit", "election", "vote", "poll", "campaign", "party", 
        "democrat", "republican", "palestinian", "israel", "iraq", "iran", "syria", "russia", "china", 
        "korea", "afghanistan", "pakistan", "africa", "europe", "asia", "middle east", "latin america", 
        "court", "trial", "judge", "law", "ban", "protest", "strike", "riot", "refugee", "human rights",
        "prime minister", "premier", "chancellor", "diplomat", "embassy", "border", "territory", "rebel",
        "militia", "terrorist", "terrorism", "qaeda", "isis", "taliban", "gaza", "beirut", "baghdad",
        "kabul", "tehran", "moscow", "beijing", "pyongyang", "ukraine", "crimea", "sudan", "darfur"
    ],
    "Sports": [
        "sport", "game", "match", "team", "player", "coach", "league", "cup", "championship", "tournament", 
        "olympic", "medal", "gold", "silver", "bronze", "football", "soccer", "basketball", "baseball", 
        "hockey", "tennis", "golf", "cricket", "rugby", "racing", "driver", "score", "win", "won", "loss", 
        "lost", "beat", "defeat", "victory", "season", "final", "nfl", "nba", "mlb", "nhl", "fifa", "uefa",
        "stadium", "athlete", "squad", "roster", "draft", "playoff", "super bowl", "world cup", "formula one",
        "nascar", "grand prix", "wimbledon", "open", "tour", "cyclist", "doping", "marathon"
    ],
    "Business": [
        "business", "company", "firm", "corporation", "inc", "market", "stock", "share", "trade", "exchange", 
        "wall street", "dow", "nasdaq", "economy", "economic", "finance", "financial", "bank", "invest", 
        "investment", "investor", "profit", "loss", "revenue", "sales", "price", "cost", "dollar", "euro", 
        "yen", "currency", "inflation", "rate", "fed", "federal reserve", "tax", "jobs", "unemployment", 
        "oil", "gas", "energy", "deal", "merger", "acquisition", "buyout", "bid", "offer", "ipo", "ceo", 
        "executive", "manager", "dividend", "earnings", "quarter", "forecast", "consumer", "retail", 
        "spending", "budget", "deficit", "debt", "bond", "treasury", "imf", "wto"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "scientific", "research", "researcher", "study", "scientist", 
        "computer", "software", "hardware", "internet", "web", "online", "digital", "mobile", "phone", 
        "smartphone", "app", "google", "microsoft", "apple", "intel", "ibm", "facebook", "twitter", 
        "amazon", "yahoo", "ebay", "virus", "security", "space", "nasa", "shuttle", "mission", "planet", 
        "mars", "moon", "galaxy", "astronomy", "biology", "genetics", "medical", "medicine", "health", 
        "cancer", "disease", "drug", "treatment", "robot", "laser", "wireless", "network", "server", 
        "data", "browser", "search engine", "chip", "processor", "satellite", "orbit", "telescope"
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            # Count occurrences or just checking presence?
            # Simple count
            if kw in text:
                scores[cat] += 1
    
    # Custom adjustments
    # If "oil" in Business and World, context matters.
    # But simple max score might work.
    
    # Sort by score desc
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    if sorted_scores[0][1] == 0:
        return "Unknown"
    
    # Tie breaking?
    # Priority: Sports > Sci_Tech > Business > World?
    # Actually, World is often the catch-all for general news, but Business is specific.
    # Let's trust the count.
    
    return sorted_scores[0][0]

world_articles_by_region = collections.defaultdict(int)
debug_log = []

for row in metadata_list:
    aid = str(row['article_id'])
    region = row['region']
    
    if aid in articles_content:
        content = articles_content[aid]
        full_text = content['title'] + " " + content['description']
        category = classify(full_text)
        
        if category == "World":
            world_articles_by_region[region] += 1
            if len(debug_log) < 5:
                debug_log.append({"id": aid, "title": content['title'], "region": region, "cat": category})

# Find region with max
if world_articles_by_region:
    max_region = max(world_articles_by_region, key=world_articles_by_region.get)
    max_count = world_articles_by_region[max_region]
else:
    max_region = "None"
    max_count = 0

print("__RESULT__:")
print(json.dumps({
    "max_region": max_region,
    "max_count": max_count,
    "counts": world_articles_by_region,
    "debug": debug_log
}))"""

env_args = {'var_function-call-9402959819383380444': 'file_storage/function-call-9402959819383380444.json', 'var_function-call-4777546986780690904': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_function-call-5898384611534578925': [{'_id': '69450cd080dae318e2b3a6cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450cd080dae318e2b3a6d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450cd080dae318e2b3a6d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450cd080dae318e2b3a6d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450cd080dae318e2b3a6d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3661929660469194168': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1182930291285511740': {'count': 5}, 'var_function-call-6775040428661401644': 'file_storage/function-call-6775040428661401644.json'}

exec(code, env_args)
