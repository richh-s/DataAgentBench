code = """import json
import collections
import re

# Load metadata
meta_path = locals()['var_function-call-2515222159544851485']
with open(meta_path, 'r') as f:
    metadata_list = json.load(f)

# Ensure IDs are strings
article_region = {str(item['article_id']): item['region'] for item in metadata_list}
target_ids = set(article_region.keys())

# Load articles
articles_path = locals()['var_function-call-899974702503546662']
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# Keywords
def make_regex(keywords):
    # Sort by length descending to match longer phrases first (though with OR it depends on engine, usually first match)
    # But here we use findall, so order in OR doesn't matter much for count, but for correctness of overlapping terms.
    # Actually, we just count all matches.
    keywords = sorted(keywords, key=len, reverse=True)
    pattern = r'\b(' + '|'.join(re.escape(k) for k in keywords) + r')\b'
    return re.compile(pattern, re.IGNORECASE)

categories_keywords = {
    "World": [
        "ministry", "minister", "ministers", "president", "presidents", "prime minister", "official", "officials", 
        "police", "military", "war", "wars", "bomb", "bombs", "bombing", "blast", "blasts", "kill", "killed", 
        "killing", "kills", "dead", "death", "deaths", "united nations", "parliament", "election", "elections", 
        "vote", "votes", "security", "china", "russia", "israel", "palestinian", "palestinians", "gaza", "darfur", 
        "sudan", "syria", "lebanon", "afghanistan", "pakistan", "baghdad", "tehran", "korea", "nuclear", "treaty", 
        "talks", "diplomat", "diplomats", "court", "trial", "hurricane", "tsunami", "terror", "terrorism", 
        "terrorist", "attack", "attacks", "troop", "troops", "rebel", "rebels", "insurgent", "insurgents", 
        "government", "governments", "senate", "congress", "bush", "putin", "blair", "sharon", "arafat", "budget", 
        "law", "laws", "politics", "political", "party", "parties", "leader", "leaders", "navy", "army", "soldier", 
        "soldiers", "peace", "conflict", "crisis", "hostage", "kidnap"
    ],
    "Sports": [
        "sport", "sports", "game", "games", "cup", "team", "teams", "league", "leagues", "match", "matches", 
        "score", "scores", "win", "wins", "won", "winning", "loss", "losses", "lost", "medal", "medals", "olympic", 
        "olympics", "player", "players", "coach", "coaches", "champion", "champions", "championship", "nfl", "nba", 
        "mlb", "nhl", "football", "soccer", "baseball", "basketball", "tennis", "golf", "racing", "f1", "nascar", 
        "stadium", "athlete", "athletes", "sox", "yankee", "yankees", "mets", "bulls", "lakers", "tournament", 
        "race", "races", "rugby", "cricket", "hockey", "boxing", "fifa", "uefa"
    ],
    "Business": [
        "market", "markets", "stock", "stocks", "share", "shares", "price", "prices", "profit", "profits", 
        "earnings", "revenue", "revenues", "dollar", "dollars", "euro", "euros", "yen", "bank", "banks", "fed", 
        "economy", "economic", "trade", "sale", "sales", "oil", "gas", "company", "companies", "corp", 
        "corporation", "inc", "business", "businesses", "deal", "deals", "merger", "mergers", "ceo", "invest", 
        "investment", "investments", "investor", "investors", "fund", "funds", "wall st", "wall street", "nasdaq", 
        "dow", "gold", "financial", "finance", "inflation", "rate", "rates", "job", "jobs", "hiring", "layoff", 
        "layoffs", "debt", "ipo"
    ],
    "Sci/Tech": [
        "google", "microsoft", "apple", "ibm", "intel", "software", "hardware", "internet", "web", "website", 
        "computer", "computers", "phone", "phones", "mobile", "cellphone", "space", "nasa", "science", "scientist", 
        "scientists", "tech", "technology", "technologies", "virus", "viruses", "chip", "chips", "linux", "windows", 
        "server", "servers", "online", "digital", "wireless", "broadband", "satellite", "satellites", "orbit", 
        "robot", "robots", "biotech", "browser", "browsers", "search engine", "hacker", "hackers", "spam", "blog", 
        "blogs"
    ]
}

cat_regexes = {cat: make_regex(kws) for cat, kws in categories_keywords.items()}

def classify(text):
    scores = {cat: 0 for cat in categories_keywords}
    for cat, regex in cat_regexes.items():
        matches = regex.findall(text)
        scores[cat] = len(matches)
    
    if max(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

cat_counts = collections.defaultdict(int)
region_world_counts = collections.defaultdict(int)
processed = 0

for article in articles_list:
    aid = str(article.get('article_id', ''))
    if aid in target_ids:
        processed += 1
        title = article.get('title', '')
        desc = article.get('description', '')
        full_text = f"{title} {desc}"
        cat = classify(full_text)
        cat_counts[cat] += 1
        
        if cat == "World":
            region = article_region[aid]
            region_world_counts[region] += 1

print("__RESULT__:")
print(json.dumps({
    "processed": processed,
    "distribution": cat_counts,
    "world_by_region": region_world_counts
}))"""

env_args = {'var_function-call-13208856365886244928': ['authors', 'article_metadata'], 'var_function-call-13208856365886244455': ['articles'], 'var_function-call-2515222159544851485': 'file_storage/function-call-2515222159544851485.json', 'var_function-call-13593231486142691637': 6696, 'var_function-call-16822267018933619895': {'min': 13, 'max': 127570}, 'var_function-call-16039217225285372494': [{'_id': '6944ffdbcbef4a7a7193d6b3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ffdbcbef4a7a7193d6b4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ffdbcbef4a7a7193d6b5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ffdbcbef4a7a7193d6b6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ffdbcbef4a7a7193d6b7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8126212337696475554': 5, 'var_function-call-8676179416535457116': [{'_id': '6944ffdbcbef4a7a7193d6b3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ffdbcbef4a7a7193d6b4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ffdbcbef4a7a7193d6b5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ffdbcbef4a7a7193d6b6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ffdbcbef4a7a7193d6b7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17293137481658764797': 5, 'var_function-call-899974702503546662': 'file_storage/function-call-899974702503546662.json', 'var_function-call-10050718031818148829': {'Asia': 607, 'Africa': 608, 'Europe': 635, 'South America': 633, 'North America': 625}, 'var_function-call-11906810069183535307': {'distribution': {'Business': 1548, 'Sci/Tech': 586, 'Unknown': 274, 'World': 3124, 'Sports': 1164}, 'world_by_region': {'Asia': 618, 'Africa': 607, 'Europe': 631, 'South America': 644, 'North America': 624}, 'samples': ['[Asia] IT Myth 5: Most IT projects fail', '[Africa] Earth is Rare, New Study Suggests (SPACE.com)', '[Asia] Indictments Using DNA on Rise Nationally (AP)', '[Europe] Reverse Psychology', "[South America] News: Climate Change Could Doom Alaska's Tundra"]}, 'var_function-call-11741193633354399439': {'distribution': {'Unknown': 6696}, 'world_by_region': {}, 'samples': []}}

exec(code, env_args)
