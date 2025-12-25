code = """import json
import collections

# Load metadata path
metadata_path = locals()['var_function-call-7362815310734823686']
# Load articles path (the one with 150k limit)
articles_path = locals()['var_function-call-15882701907129142909']

# Read metadata
with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Create mapping article_id -> year for Europe articles
article_year_map = {}
for r in metadata_records:
    aid = str(r['article_id'])
    date = r['publication_date'] # YYYY-MM-DD
    year = int(date.split('-')[0])
    article_year_map[aid] = year

# Read articles
with open(articles_path, 'r') as f:
    articles_records = json.load(f)

print(f"Total articles loaded: {len(articles_records)}")

# Rebuild map for faster lookup of article text by ID
# Assuming article_id is unique
articles_dict = {}
for a in articles_records:
    articles_dict[str(a['article_id'])] = a

# Keywords
categories = {
    "Business": ["business", "economy", "economic", "market", "stock", "stocks", "wall street", "bond", "bonds", "invest", "investment", "investor", "finance", "financial", "corporate", "company", "companies", "profit", "earnings", "revenue", "loss", "trade", "deal", "merger", "acquisition", "bank", "banking", "fed", "federal reserve", "oil", "price", "prices", "euro", "dollar", "yen", "currency", "inflation", "recession", "sales", "retail", "growth", "ipo", "shares", "shareholder", "ceo", "cfo", "jobs", "unemployment", "debt", "budget", "deficit"],
    "World": ["world", "international", "peace", "war", "military", "army", "troops", "iraq", "iran", "afghanistan", "palestinian", "israel", "gaza", "bomb", "attack", "blast", "kill", "dead", "politics", "president", "minister", "prime minister", "election", "vote", "government", "official", "nuclear", "treaty", "un", "united nations", "security", "diplomat", "talks", "crisis", "conflict", "protest", "china", "russia", "us", "uk", "france", "germany", "europe"],
    "Sports": ["sport", "sports", "game", "match", "cup", "team", "player", "coach", "win", "won", "lose", "lost", "score", "season", "league", "champion", "championship", "olympic", "medal", "gold", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "race", "racing", "driver", "athlete"],
    "Sci/Tech": ["technology", "tech", "science", "scientific", "computer", "software", "hardware", "internet", "web", "online", "net", "google", "microsoft", "apple", "intel", "ibm", "server", "chip", "processor", "virus", "worm", "hacker", "security", "space", "nasa", "shuttle", "mission", "orbit", "moon", "mars", "astronomy", "physics", "biology", "study", "research", "cell", "stem cell", "gene", "medical", "drug", "cancer", "disease", "health", "doctor", "patient"]
}

business_counts_by_year = collections.defaultdict(int)
found_count = 0
missing_count = 0

# Iterate over relevant articles (from metadata)
for aid, year in article_year_map.items():
    if aid in articles_dict:
        found_count += 1
        article = articles_dict[aid]
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        scores = {cat: 0 for cat in categories}
        for cat, keywords in categories.items():
            for kw in keywords:
                if kw in text:
                    scores[cat] += 1
        
        best_cat = max(scores, key=scores.get)
        
        if scores[best_cat] > 0 and best_cat == "Business":
            business_counts_by_year[year] += 1
    else:
        missing_count += 1

# Calculate average for 2010-2020
total_business_articles = 0
years = range(2010, 2021)
count_list = []
for y in years:
    c = business_counts_by_year[y]
    count_list.append(c)
    total_business_articles += c

average = total_business_articles / len(years)

print("__RESULT__:")
print(json.dumps({
    "average": average, 
    "counts_per_year": dict(business_counts_by_year), 
    "found": found_count, 
    "missing": missing_count,
    "loaded_total": len(articles_records)
}))"""

env_args = {'var_function-call-7362815310734823686': 'file_storage/function-call-7362815310734823686.json', 'var_function-call-5837169514191744689': 14860, 'var_function-call-15464103905303230680': 'file_storage/function-call-15464103905303230680.json', 'var_function-call-12360763159906928774': [{'_id': '6944db67e28dfbaacfa3ae88', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944db67e28dfbaacfa3ae89', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944db67e28dfbaacfa3ae8a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944db67e28dfbaacfa3ae8b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944db67e28dfbaacfa3ae8c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8054706129410508577': [{'_id': '6944db67e28dfbaacfa3ae88', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944db67e28dfbaacfa3ae89', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944db67e28dfbaacfa3ae8a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944db67e28dfbaacfa3ae8b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944db67e28dfbaacfa3ae8c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13308618984475909885': 5, 'var_function-call-8165940882341443129': 'file_storage/function-call-8165940882341443129.json', 'var_function-call-6551584233653994266': {'average': 43.09090909090909, 'counts_per_year': {'2016': 46, '2015': 44, '2017': 46, '2020': 44, '2013': 47, '2018': 51, '2010': 35, '2011': 48, '2014': 39, '2019': 36, '2012': 38}, 'loaded_count': 20000}, 'var_function-call-12408369304236030022': {'found': 2273, 'missing': 12587}, 'var_function-call-5591751501812293114': {'max_id': 127583, 'min_id': 3, 'count': 14860}, 'var_function-call-15882701907129142909': 'file_storage/function-call-15882701907129142909.json'}

exec(code, env_args)
