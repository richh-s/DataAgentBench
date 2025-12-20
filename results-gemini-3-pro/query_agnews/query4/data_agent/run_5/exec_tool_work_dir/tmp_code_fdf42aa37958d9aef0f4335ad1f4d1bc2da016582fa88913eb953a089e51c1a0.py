code = """import json
import collections
import re

# Load metadata
with open(locals()['var_function-call-1474084106243643964'], 'r') as f:
    metadata_list = json.load(f)

# Create a map article_id -> region
# IDs in metadata are strings (from preview), make sure to handle consistency
metadata = {str(row['article_id']): row['region'] for row in metadata_list}

# Load articles
with open(locals()['var_function-call-307996040387554200'], 'r') as f:
    articles = json.load(f)

# Keywords
categories = {
    "Sports": ["sport", "sports", "football", "soccer", "baseball", "basketball", "hockey", "tennis", "golf", "rugby", "cricket", "league", "team", "game", "match", "cup", "tournament", "championship", "olympic", "olympics", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "player", "coach", "score", "win", "won", "lose", "lost", "defeat", "victory", "medal", "stadium", "espn", "sox", "yankees", "lakers", "bulls"],
    "Business": ["business", "economy", "economic", "market", "stock", "stocks", "trade", "trading", "financial", "finance", "bank", "banking", "money", "dollar", "currency", "euro", "yen", "yuan", "invest", "investment", "investor", "company", "corp", "corporation", "inc", "firm", "profit", "revenue", "earnings", "sales", "deal", "merger", "acquisition", "ipo", "oil", "price", "prices", "cost", "rate", "rates", "inflation", "tax", "fed", "federal reserve", "ceo", "manager", "executive", "dow", "nasdaq", "wall street", "boeing", "airbus", "walmart"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", "mobile", "phone", "smartphone", "app", "google", "apple", "microsoft", "ibm", "intel", "facebook", "amazon", "nasa", "space", "astronomy", "galaxy", "planet", "mars", "moon", "robot", "ai", "artificial intelligence", "cyber", "virus", "hacker", "biology", "physics", "chemistry", "study", "research", "scientist", "cancer", "drug", "medical", "health", "disease", "microsoft", "windows", "linux", "browser", "server"],
    "World": ["world", "international", "politics", "political", "government", "president", "minister", "prime", "parliament", "congress", "senate", "election", "vote", "poll", "democracy", "diplomat", "diplomacy", "treaty", "summit", "un", "united nations", "eu", "european union", "nato", "war", "military", "army", "navy", "air force", "troops", "soldier", "rebel", "insurgent", "guerrilla", "terrorist", "terrorism", "attack", "bomb", "blast", "explosion", "kill", "killed", "death", "dead", "injure", "wound", "casualty", "conflict", "crisis", "refugee", "migrant", "immigration", "border", "police", "court", "law", "justice", "prison", "jail", "protest", "riot", "demonstration", "strike", "disaster", "earthquake", "tsunami", "hurricane", "typhoon", "storm", "flood", "drought", "famine", "iraq", "iran", "syria", "afghanistan", "pakistan", "israel", "palestine", "gaza", "ukraine", "russia", "china", "north korea", "sudan", "congo", "nigeria", "somalia", "libya", "yemen", "baghdad", "kabul", "tehran", "damascus", "moscow", "beijing", "jerusalem"]
}

region_counts = collections.defaultdict(int)
world_article_count = 0

for art in articles:
    aid = str(art['article_id'])
    if aid in metadata:
        region = metadata[aid]
        title = art.get('title', '') or ''
        desc = art.get('description', '') or ''
        text = (title + " " + desc).lower()
        
        # Tokenize (simple)
        tokens = re.findall(r'\w+', text)
        
        scores = {cat: 0 for cat in categories}
        for token in tokens:
            for cat, keywords in categories.items():
                if token in keywords:
                    scores[cat] += 1
        
        # Determine category
        # If max score is 0, default? Maybe skip or assume "World" if unknown? 
        # But question asks for "World" category. If no keywords, maybe not World.
        if any(scores.values()):
            best_cat = max(scores, key=scores.get)
            # Tie breaking? 
            # If tie, prioritize World if it's one of them? Or use order?
            # Let's check if there's a tie for max
            max_score = scores[best_cat]
            candidates = [c for c, s in scores.items() if s == max_score]
            if len(candidates) > 1:
                # Tie breaker logic
                # Usually: World > Business > Sci/Tech > Sports?
                # Or based on specific strong words?
                # Let's stick to simple max. If tie, maybe it picks the first one in list/dict order.
                # Let's prioritize World if involved.
                if "World" in candidates:
                    best_cat = "World"
                elif "Business" in candidates:
                    best_cat = "Business"
            
            if best_cat == "World":
                region_counts[region] += 1
                world_article_count += 1
        else:
            # No keywords match.
            # Could be categorized as "World" if it contains region name?
            # Or just ignore.
            pass

# Find region with max articles
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
    max_val = region_counts[max_region]
else:
    max_region = "None"
    max_val = 0

result = {
    "region_counts": region_counts,
    "max_region": max_region,
    "max_val": max_val,
    "total_world_articles": world_article_count
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1474084106243643964': 'file_storage/function-call-1474084106243643964.json', 'var_function-call-9489092853522118579': 'file_storage/function-call-9489092853522118579.json', 'var_function-call-17105952885415197022': [{'_id': '6944ed7c4e8b2b9e56808f77', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ed7c4e8b2b9e56808f78', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ed7c4e8b2b9e56808f79', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ed7c4e8b2b9e56808f7a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ed7c4e8b2b9e56808f7b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17682266178667585365': 6696, 'var_function-call-6775491050414127677': 'file_storage/function-call-6775491050414127677.json', 'var_function-call-4705261762392207793': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-7653748084012222185': 'file_storage/function-call-7653748084012222185.json', 'var_function-call-307996040387554200': 'file_storage/function-call-307996040387554200.json'}

exec(code, env_args)
