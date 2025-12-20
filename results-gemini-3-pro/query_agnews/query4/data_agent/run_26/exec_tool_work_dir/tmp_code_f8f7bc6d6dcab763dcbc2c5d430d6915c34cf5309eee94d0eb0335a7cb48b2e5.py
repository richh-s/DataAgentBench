code = """import json
import pandas as pd
from collections import Counter
import re

# Load SQL result (metadata for 2015)
with open(locals()['var_function-call-7563536920776079185'], 'r') as f:
    metadata_list = json.load(f)

# Load Mongo result (articles)
with open(locals()['var_function-call-17851143244503824995'], 'r') as f:
    articles_list = json.load(f)

# Create lookup for articles
# article_id in metadata is likely int or string. In Mongo it is string.
# Let's normalize to string.
articles_map = {str(a['article_id']): a for a in articles_list}

# Keywords
keywords = {
    "Business": ["oil", "price", "prices", "stock", "stocks", "profit", "earnings", "quarter", "deal", "sales", "revenue", "company", "corp", "inc", "share", "shares", "dollar", "economy", "economic", "fed", "bank", "market", "markets", "trade", "deficit", "inflation", "investor", "fund", "billion", "million", "growth", "rates", "wall st", "wall street", "audit", "budget", "ceo", "cfo"],
    "Sci/Tech": ["software", "internet", "microsoft", "google", "apple", "ibm", "computer", "technology", "tech", "space", "nasa", "orbit", "virus", "study", "research", "science", "phone", "mobile", "wireless", "network", "server", "chip", "web", "online", "digital", "windows", "linux", "browser", "spam", "hacker", "satellite", "telescope"],
    "Sports": ["game", "team", "cup", "league", "player", "coach", "win", "won", "loss", "lost", "victory", "defeat", "score", "medal", "olympic", "championship", "season", "baseball", "football", "basketball", "soccer", "tennis", "golf", "hockey", "sport", "sports", "athlete", "tournament", "match", "racing", "driver", "f1", "rugby", "cricket"],
    "World": ["president", "minister", "prime", "official", "government", "war", "peace", "treaty", "talks", "nuclear", "bomb", "blast", "attack", "kill", "dead", "wound", "troops", "soldiers", "army", "military", "rebel", "guerrilla", "strike", "iraq", "iran", "israel", "palestin", "gaza", "afghanistan", "baghdad", "kabul", "darfur", "sudan", "un", "united nations", "security council", "eu", "european union", "protest", "election", "vote", "leader", "parliament", "senate", "lawmaker", "hostage", "terror", "terrorist", "qaeda", "explosion", "crash", "disaster", "storm", "hurricane", "typhoon", "earthquake", "tsunami", "aid", "refugee", "human rights", "court", "trial", "judge", "police"]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, keys in keywords.items():
        for k in keys:
            # Simple substring match or word boundary? Substring is easier but might match partial words.
            # Let's use word boundary if possible, or just simple check.
            # "oil" in "boil" is bad. Use regex or split.
            # Using simple regex for word boundaries
            if re.search(r'\b' + re.escape(k) + r'\b', text):
                scores[cat] += 1
    
    # Return category with max score
    # Handle ties: prioritize World > Business > Sports > Sci/Tech? Or just pick first max.
    # If all 0, default to World? Or Unknown.
    if sum(scores.values()) == 0:
        return "World" # Default fallback, or maybe "Business" is safer? 
                       # Looking at the data, many are business/world. 
                       # Let's assume World for now as it's the target.
    
    return max(scores, key=scores.get)

# Process
region_counts = Counter()
world_region_counts = Counter()
category_counts = Counter()

debug_list = []

for m in metadata_list:
    aid = str(m['article_id'])
    region = m['region']
    if aid in articles_map:
        art = articles_map[aid]
        full_text = art['title'] + " " + art['description']
        cat = classify(full_text)
        
        category_counts[cat] += 1
        
        if cat == "World":
            world_region_counts[region] += 1
            if len(debug_list) < 5:
                debug_list.append({"title": art['title'], "cat": cat})
        
        # Check classification for non-World for debugging
        if cat != "World" and len(debug_list) < 10:
             debug_list.append({"title": art['title'], "cat": cat})

# Result
print("__RESULT__:")
print(json.dumps({
    "world_counts": dict(world_region_counts),
    "total_classified": dict(category_counts),
    "sample_classifications": debug_list
}))"""

env_args = {'var_function-call-11816980968405379270': [{'cnt': '6696'}], 'var_function-call-7563536920776079185': 'file_storage/function-call-7563536920776079185.json', 'var_function-call-6086744208252917915': [{'_id': '69450900ace3ac604ce5d0d1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450900ace3ac604ce5d0d2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450900ace3ac604ce5d0d3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450900ace3ac604ce5d0d4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450900ace3ac604ce5d0d5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17851143244503824995': 'file_storage/function-call-17851143244503824995.json'}

exec(code, env_args)
