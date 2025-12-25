code = """import json
import re
import collections

# Load data (already in memory in previous context, but safer to reload or reference locals if possible, 
# but execute_python context is fresh unless variables are persisted? 
# The system prompt says "All previous tool results are available as variables".
# It does NOT say variables from previous execute_python calls are available.
# "Inside execute_python code you may read storage entries using the provided key names... 
# You cannot modify or reassign those storage-provided variables...".
# "You must print the final result...".
# So local variables from previous execute_python are LOST.
# I must reload from the storage keys.

# Keys:
# metadata: var_function-call-9402959819383380444
# articles: var_function-call-6775040428661401644

with open(locals()['var_function-call-9402959819383380444'], 'r') as f:
    metadata_list = json.load(f)

with open(locals()['var_function-call-6775040428661401644'], 'r') as f:
    articles_list = json.load(f)

articles_content = {}
for art in articles_list:
    aid = str(art['article_id'])
    articles_content[aid] = {
        'title': art.get('title', ''),
        'description': art.get('description', '')
    }

# Keywords (same lists, but I will use regex to compile them for efficiency or just loop with \b)
# I'll use a compiled regex for each category to count all matches at once?
# Or just one big regex per category?
# Regex: `\b(word1|word2|...)\b`
# This is much faster and handles word boundaries.

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
        "kabul", "tehran", "moscow", "beijing", "pyongyang", "ukraine", "crimea", "sudan", "darfur", "world"
    ],
    "Sports": [
        "sport", "sports", "game", "match", "team", "player", "coach", "league", "cup", "championship", "tournament", 
        "olympic", "olympics", "medal", "gold", "silver", "bronze", "football", "soccer", "basketball", "baseball", 
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
        "spending", "budget", "deficit", "debt", "bond", "treasury", "imf", "wto", "corp"
    ],
    "Sci_Tech": [
        "technology", "tech", "science", "scientific", "research", "researcher", "study", "scientist", 
        "computer", "software", "hardware", "internet", "web", "online", "digital", "mobile", "phone", 
        "smartphone", "app", "google", "microsoft", "apple", "intel", "ibm", "facebook", "twitter", 
        "amazon", "yahoo", "ebay", "virus", "security", "space", "nasa", "shuttle", "mission", "planet", 
        "mars", "moon", "galaxy", "astronomy", "biology", "genetics", "medical", "medicine", "health", 
        "cancer", "disease", "drug", "treatment", "robot", "laser", "wireless", "network", "server", 
        "data", "browser", "search engine", "chip", "processor", "satellite", "orbit", "telescope",
        "it", "cyber", "device", "broadband", "silicon"
    ]
}

# Compile regex patterns
# Escape keywords to handle special chars if any
patterns = {}
for cat, kws in keywords.items():
    # Sort by length desc to match longer phrases first (e.g. "united nations" before "united")
    # though with \b OR \b it doesn't matter much for counting, but good practice.
    kws.sort(key=len, reverse=True)
    pattern_str = r'\b(' + '|'.join(re.escape(kw) for kw in kws) + r')\b'
    patterns[cat] = re.compile(pattern_str, re.IGNORECASE)

world_counts = collections.defaultdict(int)
total_classified = 0
cat_counts = collections.defaultdict(int)

for row in metadata_list:
    aid = str(row['article_id'])
    region = row['region']
    
    if aid in articles_content:
        content = articles_content[aid]
        full_text = content['title'] + " " + content['description']
        
        scores = {}
        for cat, pattern in patterns.items():
            # count matches
            # re.findall finds all non-overlapping matches
            matches = pattern.findall(full_text)
            scores[cat] = len(matches)
        
        # Determine category
        # If max score is 0, Unknown
        # If tie, pick first (World is checked first in dict iteration order? No, dict is insertion ordered in 3.7+)
        # Let's enforce priority logic if needed. 
        # But simple max is standard.
        
        best_cat = "Unknown"
        max_score = 0
        
        # To avoid arbitrary tie-breaking based on dict order, let's look at the scores.
        # But for now, max() is fine.
        if any(scores.values()):
            best_cat = max(scores, key=scores.get)
            max_score = scores[best_cat]
        
        cat_counts[best_cat] += 1
        
        if best_cat == "World":
            world_counts[region] += 1

print("__RESULT__:")
print(json.dumps({
    "world_counts_by_region": world_counts,
    "total_classified": cat_counts
}))"""

env_args = {'var_function-call-9402959819383380444': 'file_storage/function-call-9402959819383380444.json', 'var_function-call-4777546986780690904': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_function-call-5898384611534578925': [{'_id': '69450cd080dae318e2b3a6cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450cd080dae318e2b3a6d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450cd080dae318e2b3a6d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450cd080dae318e2b3a6d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450cd080dae318e2b3a6d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3661929660469194168': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1182930291285511740': {'count': 5}, 'var_function-call-6775040428661401644': 'file_storage/function-call-6775040428661401644.json', 'var_function-call-4109657372586011047': {'max_region': 'Africa', 'max_count': 106, 'counts': {'Asia': 83, 'North America': 102, 'Europe': 80, 'South America': 91, 'Africa': 106}, 'debug': [{'id': '67', 'title': 'IT Myth 5: Most IT projects fail', 'region': 'Asia', 'cat': 'World'}, {'id': '86', 'title': 'Oracle Sales Data Seen Being Released (Reuters)', 'region': 'Asia', 'cat': 'World'}, {'id': '97', 'title': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'region': 'North America', 'cat': 'World'}, {'id': '141', 'title': 'Indictments Using DNA on Rise Nationally (AP)', 'region': 'Asia', 'cat': 'World'}, {'id': '179', 'title': 'Reverse Psychology', 'region': 'Europe', 'cat': 'World'}]}}

exec(code, env_args)
