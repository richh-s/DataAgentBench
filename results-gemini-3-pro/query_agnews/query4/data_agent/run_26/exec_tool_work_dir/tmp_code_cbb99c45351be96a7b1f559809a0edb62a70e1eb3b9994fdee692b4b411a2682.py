code = """import json
import re
from collections import Counter

# Load data
with open(locals()['var_function-call-7563536920776079185'], 'r') as f:
    metadata_list = json.load(f)

with open(locals()['var_function-call-17851143244503824995'], 'r') as f:
    articles_list = json.load(f)

articles_map = {str(a['article_id']): a for a in articles_list}

print(f"Metadata count: {len(metadata_list)}")
print(f"Articles map count: {len(articles_map)}")
sample_ids = list(articles_map.keys())[:5]
print(f"Sample article IDs in map: {sample_ids}")

# Check overlap
intersection = 0
for m in metadata_list:
    if str(m['article_id']) in articles_map:
        intersection += 1
print(f"Intersection count: {intersection}")

keywords = {
    "Business": ["oil", "price", "stock", "profit", "earnings", "quarter", "deal", "sales", "revenue", "company", "corp", "inc", "share", "dollar", "economy", "fed", "bank", "market", "trade", "deficit", "inflation", "investor", "fund", "billion", "million", "ipo", "wall st", "dow", "nasdaq", "nyse", "bond", "currency", "gold", "bid", "buy", "sell", "acquire", "merger", "ceo"],
    "Sci/Tech": ["software", "internet", "microsoft", "google", "apple", "ibm", "computer", "technology", "tech", "space", "nasa", "orbit", "virus", "study", "research", "science", "phone", "mobile", "wireless", "network", "server", "chip", "web", "online", "digital", "windows", "linux", "browser", "spam", "hacker", "satellite", "telescope", "intel", "oracle", "broadband", "download", "search engine", "biotech"],
    "Sports": ["game", "team", "cup", "league", "player", "coach", "win", "won", "loss", "lost", "victory", "defeat", "score", "medal", "olympic", "championship", "season", "baseball", "football", "basketball", "soccer", "tennis", "golf", "hockey", "sport", "athlete", "tournament", "match", "racing", "driver", "f1", "rugby", "cricket", "nba", "nfl", "mlb", "nhl", "fifa"],
    "World": ["president", "minister", "prime", "official", "government", "war", "peace", "treaty", "talks", "nuclear", "bomb", "blast", "attack", "kill", "dead", "wound", "troops", "soldiers", "army", "military", "rebel", "guerrilla", "strike", "iraq", "iran", "israel", "palestin", "gaza", "afghanistan", "baghdad", "kabul", "darfur", "sudan", "un", "united nations", "security council", "eu", "european union", "protest", "election", "vote", "leader", "parliament", "senate", "lawmaker", "hostage", "terror", "terrorist", "qaeda", "explosion", "crash", "disaster", "storm", "hurricane", "typhoon", "earthquake", "tsunami", "aid", "refugee", "human rights", "court", "trial", "judge", "police", "putin", "bush", "kerry", "arafat", "sharon", "chavez"]
}

def classify_debug(text):
    text_lower = text.lower()
    scores = {cat: 0 for cat in keywords}
    matched_words = {cat: [] for cat in keywords}
    
    for cat, keys in keywords.items():
        for k in keys:
            if re.search(r'\b' + re.escape(k) + r'\b', text_lower):
                scores[cat] += 1
                matched_words[cat].append(k)
    
    # Simple scoring
    max_score = max(scores.values())
    if max_score == 0:
        return "Unclassified", scores, matched_words
    
    # Get all categories with max_score
    candidates = [cat for cat, s in scores.items() if s == max_score]
    # Priority: World > Sports > Business > Sci/Tech (Arbitrary but helps ties)
    # Or just pick first.
    return candidates[0], scores, matched_words

region_counts = Counter()
debug_list = []

for m in metadata_list:
    aid = str(m['article_id'])
    if aid in articles_map:
        art = articles_map[aid]
        full_text = art['title'] + " " + art['description']
        cat, scores, matches = classify_debug(full_text)
        
        if cat == "World":
            region_counts[m['region']] += 1
        
        if len(debug_list) < 5:
            debug_list.append({
                "title": art['title'], 
                "cat": cat, 
                "scores": scores,
                "matches": matches
            })

print("__RESULT__:")
print(json.dumps({
    "world_counts": dict(region_counts),
    "sample_debug": debug_list
}))"""

env_args = {'var_function-call-11816980968405379270': [{'cnt': '6696'}], 'var_function-call-7563536920776079185': 'file_storage/function-call-7563536920776079185.json', 'var_function-call-6086744208252917915': [{'_id': '69450900ace3ac604ce5d0d1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450900ace3ac604ce5d0d2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450900ace3ac604ce5d0d3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450900ace3ac604ce5d0d4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450900ace3ac604ce5d0d5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17851143244503824995': 'file_storage/function-call-17851143244503824995.json', 'var_function-call-1253223201269786800': {'world_counts': {'Europe': 195, 'South America': 194, 'Africa': 216, 'Asia': 192, 'North America': 201}, 'total_classified': {'World': 998}, 'sample_classifications': [{'title': 'Google IPO Auction Off to Rocky Start', 'cat': 'World'}, {'title': 'US trade deficit swells in June', 'cat': 'World'}, {'title': 'Google auction begins on Friday', 'cat': 'World'}, {'title': 'Delightful Dell', 'cat': 'World'}, {'title': "Chrysler's Bling King", 'cat': 'World'}]}}

exec(code, env_args)
