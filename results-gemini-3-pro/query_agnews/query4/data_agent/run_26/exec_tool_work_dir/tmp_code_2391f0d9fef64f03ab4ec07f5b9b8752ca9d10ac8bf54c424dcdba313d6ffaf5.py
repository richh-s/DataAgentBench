code = """import json
import re
from collections import Counter

# Load metadata
with open(locals()['var_function-call-7563536920776079185'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-6222205374982262712'], 'r') as f:
    articles_list = json.load(f)

articles_map = {str(a['article_id']): a for a in articles_list}

keywords = {
    "Business": ["oil", "price", "prices", "stock", "stocks", "profit", "earnings", "quarter", "deal", "sales", "revenue", "company", "corp", "inc", "share", "shares", "dollar", "economy", "fed", "bank", "market", "markets", "trade", "deficit", "inflation", "investor", "fund", "billion", "million", "ipo", "wall", "street", "dow", "nasdaq", "nyse", "bond", "currency", "gold", "bid", "buy", "sell", "acquire", "merger", "ceo"],
    "Sci/Tech": ["software", "internet", "microsoft", "google", "apple", "ibm", "computer", "technology", "tech", "space", "nasa", "orbit", "virus", "study", "research", "science", "phone", "mobile", "wireless", "network", "server", "chip", "web", "online", "digital", "windows", "linux", "browser", "spam", "hacker", "satellite", "telescope", "intel", "oracle", "broadband", "download", "search", "engine", "biotech", "pc"],
    "Sports": ["game", "team", "cup", "league", "player", "coach", "win", "won", "loss", "lost", "victory", "defeat", "score", "medal", "olympic", "championship", "season", "baseball", "football", "basketball", "soccer", "tennis", "golf", "hockey", "sport", "sports", "athlete", "tournament", "match", "racing", "driver", "f1", "rugby", "cricket", "nba", "nfl", "mlb", "nhl", "fifa", "finals"],
    "World": ["president", "minister", "prime", "official", "government", "war", "peace", "treaty", "talks", "nuclear", "bomb", "blast", "attack", "kill", "killed", "dead", "wound", "troops", "soldiers", "army", "military", "rebel", "guerrilla", "strike", "iraq", "iran", "israel", "palestin", "gaza", "afghanistan", "baghdad", "kabul", "darfur", "sudan", "un", "united", "nations", "security", "council", "eu", "european", "union", "protest", "election", "vote", "leader", "parliament", "senate", "lawmaker", "hostage", "terror", "terrorist", "qaeda", "explosion", "crash", "disaster", "storm", "hurricane", "typhoon", "earthquake", "tsunami", "aid", "refugee", "rights", "court", "trial", "judge", "police", "putin", "bush", "kerry", "arafat", "sharon", "chavez", "china", "russia", "japan", "korea", "state", "politics", "diplomat", "embassy", "border", "foreign", "international"]
}

def classify(text):
    tokens = set(re.findall(r'\w+', text.lower()))
    scores = {cat: 0 for cat in keywords}
    for cat, keys in keywords.items():
        for k in keys:
            if k in tokens:
                scores[cat] += 1
    max_score = max(scores.values())
    if max_score == 0:
        return "Unclassified"
    if scores["World"] == max_score: return "World"
    if scores["Business"] == max_score: return "Business"
    if scores["Sports"] == max_score: return "Sports"
    return max(scores, key=scores.get)

cat_counts = Counter()
world_region_counts = Counter()
intersection = 0

for m in metadata_list:
    aid = str(m['article_id'])
    if aid in articles_map:
        intersection += 1
        art = articles_map[aid]
        full_text = art['title'] + " " + art['description']
        cat = classify(full_text)
        cat_counts[cat] += 1
        if cat == "World":
            world_region_counts[m['region']] += 1

print("__RESULT__:")
print(json.dumps({
    "intersection_count": intersection,
    "all_categories": dict(cat_counts),
    "world_by_region": dict(world_region_counts)
}))"""

env_args = {'var_function-call-11816980968405379270': [{'cnt': '6696'}], 'var_function-call-7563536920776079185': 'file_storage/function-call-7563536920776079185.json', 'var_function-call-6086744208252917915': [{'_id': '69450900ace3ac604ce5d0d1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450900ace3ac604ce5d0d2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450900ace3ac604ce5d0d3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450900ace3ac604ce5d0d4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450900ace3ac604ce5d0d5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17851143244503824995': 'file_storage/function-call-17851143244503824995.json', 'var_function-call-1253223201269786800': {'world_counts': {'Europe': 195, 'South America': 194, 'Africa': 216, 'Asia': 192, 'North America': 201}, 'total_classified': {'World': 998}, 'sample_classifications': [{'title': 'Google IPO Auction Off to Rocky Start', 'cat': 'World'}, {'title': 'US trade deficit swells in June', 'cat': 'World'}, {'title': 'Google auction begins on Friday', 'cat': 'World'}, {'title': 'Delightful Dell', 'cat': 'World'}, {'title': "Chrysler's Bling King", 'cat': 'World'}]}, 'var_function-call-9285416872269923308': {'world_counts': {}, 'sample_debug': [{'title': 'Google IPO Auction Off to Rocky Start', 'cat': 'Unclassified', 'scores': {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}, 'matches': {'Business': [], 'Sci/Tech': [], 'Sports': [], 'World': []}}, {'title': 'US trade deficit swells in June', 'cat': 'Unclassified', 'scores': {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}, 'matches': {'Business': [], 'Sci/Tech': [], 'Sports': [], 'World': []}}, {'title': 'Google auction begins on Friday', 'cat': 'Unclassified', 'scores': {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}, 'matches': {'Business': [], 'Sci/Tech': [], 'Sports': [], 'World': []}}, {'title': 'Delightful Dell', 'cat': 'Unclassified', 'scores': {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}, 'matches': {'Business': [], 'Sci/Tech': [], 'Sports': [], 'World': []}}, {'title': "Chrysler's Bling King", 'cat': 'Unclassified', 'scores': {'Business': 0, 'Sci/Tech': 0, 'Sports': 0, 'World': 0}, 'matches': {'Business': [], 'Sci/Tech': [], 'Sports': [], 'World': []}}]}, 'var_function-call-17962675828582514856': {'world_counts': {'South America': 76, 'Europe': 61, 'Asia': 67, 'North America': 70, 'Africa': 84}, 'unclassified': 109, 'sample_debug': [{'title': 'Google IPO Auction Off to Rocky Start', 'cat': 'Business', 'tokens': ['anticipated', 'inc', 'a', 'to', 'offering', 'company', 'start', 'on', 'bullet', 'washington']}, {'title': 'US trade deficit swells in June', 'cat': 'Business', 'tokens': ['exploded', '19', 'costs', 'a', 'in', 'to', '8bn', 'us', 'trade', 'according']}, {'title': 'Google auction begins on Friday', 'cat': 'Sci/Tech', 'tokens': ['which', 'in', 'floated', 'be', 'on', 'as', 'engine', 'takes', 'web', 'search']}, {'title': 'Delightful Dell', 'cat': 'Business', 'tokens': ['it', 'dell', 'company', 'grim', 'delightful', 'show', 'over', 'results', 'the', 's']}, {'title': "Chrysler's Bling King", 'cat': 'Unclassified', 'tokens': ['chrysler', 'hip', 'car', 'year', 'and', 'a', 'king', 'to', 'maverick', 'carmaker']}]}, 'var_function-call-13989530094935432962': {'all_categories': {'Business': 239, 'Sci/Tech': 117, 'Unclassified': 109, 'Sports': 175, 'World': 358}, 'world_by_region': {'South America': 76, 'Europe': 61, 'Asia': 67, 'North America': 70, 'Africa': 84}, 'sample_date': None}, 'var_function-call-15106803611117629762': {'max_id': 127570, 'min_id': 13, 'count': 6696}, 'var_function-call-6222205374982262712': 'file_storage/function-call-6222205374982262712.json'}

exec(code, env_args)
