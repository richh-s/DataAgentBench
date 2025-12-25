code = """import json
import collections

# Load metadata path
metadata_path = locals()['var_function-call-7362815310734823686']

# Load articles path
articles_path = locals()['var_function-call-8165940882341443129']

# Read metadata
with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Create mapping article_id -> year for Europe articles
article_year_map = {}
for r in metadata_records:
    # article_id in metadata seems to be string in the JSON preview "3", "9". 
    # But I should handle both str and int just in case.
    aid = str(r['article_id'])
    date = r['publication_date'] # YYYY-MM-DD
    year = int(date.split('-')[0])
    article_year_map[aid] = year

# Read articles
with open(articles_path, 'r') as f:
    articles_records = json.load(f)

print(f"Total articles loaded: {len(articles_records)}")

# Keywords
categories = {
    "Business": ["business", "economy", "economic", "market", "stock", "stocks", "wall street", "bond", "bonds", "invest", "investment", "investor", "finance", "financial", "corporate", "company", "companies", "profit", "earnings", "revenue", "loss", "trade", "deal", "merger", "acquisition", "bank", "banking", "fed", "federal reserve", "oil", "price", "prices", "euro", "dollar", "yen", "currency", "inflation", "recession", "sales", "retail", "growth", "ipo", "shares", "shareholder", "ceo", "cfo", "jobs", "unemployment", "debt", "budget", "deficit"],
    "World": ["world", "international", "peace", "war", "military", "army", "troops", "iraq", "iran", "afghanistan", "palestinian", "israel", "gaza", "bomb", "attack", "blast", "kill", "dead", "politics", "president", "minister", "prime minister", "election", "vote", "government", "official", "nuclear", "treaty", "un", "united nations", "security", "diplomat", "talks", "crisis", "conflict", "protest", "china", "russia", "us", "uk", "france", "germany", "europe"],
    "Sports": ["sport", "sports", "game", "match", "cup", "team", "player", "coach", "win", "won", "lose", "lost", "score", "season", "league", "champion", "championship", "olympic", "medal", "gold", "football", "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "race", "racing", "driver", "athlete"],
    "Sci/Tech": ["technology", "tech", "science", "scientific", "computer", "software", "hardware", "internet", "web", "online", "net", "google", "microsoft", "apple", "intel", "ibm", "server", "chip", "processor", "virus", "worm", "hacker", "security", "space", "nasa", "shuttle", "mission", "orbit", "moon", "mars", "astronomy", "physics", "biology", "study", "research", "cell", "stem cell", "gene", "medical", "drug", "cancer", "disease", "health", "doctor", "patient"]
}

business_counts_by_year = collections.defaultdict(int)

for article in articles_records:
    aid = str(article['article_id'])
    
    if aid in article_year_map:
        year = article_year_map[aid]
        
        # Combine title and description
        text = (article.get('title', '') + " " + article.get('description', '')).lower()
        
        # Count keywords
        scores = {cat: 0 for cat in categories}
        for cat, keywords in categories.items():
            for kw in keywords:
                if kw in text:
                    scores[cat] += 1
        
        # Determine category
        best_cat = max(scores, key=scores.get)
        
        # Handling ties or zeros:
        # If all 0, maybe check if "oil" is in it (covered by Business) or "iraq" (World).
        # We'll stick to max score.
        # If best_cat has 0 score, we ignore it.
        if scores[best_cat] > 0 and best_cat == "Business":
            business_counts_by_year[year] += 1
        else:
            # Maybe check specific patterns?
            pass

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
print(json.dumps({"average": average, "counts_per_year": dict(business_counts_by_year), "loaded_count": len(articles_records)}))"""

env_args = {'var_function-call-7362815310734823686': 'file_storage/function-call-7362815310734823686.json', 'var_function-call-5837169514191744689': 14860, 'var_function-call-15464103905303230680': 'file_storage/function-call-15464103905303230680.json', 'var_function-call-12360763159906928774': [{'_id': '6944db67e28dfbaacfa3ae88', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944db67e28dfbaacfa3ae89', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944db67e28dfbaacfa3ae8a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944db67e28dfbaacfa3ae8b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944db67e28dfbaacfa3ae8c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8054706129410508577': [{'_id': '6944db67e28dfbaacfa3ae88', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944db67e28dfbaacfa3ae89', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944db67e28dfbaacfa3ae8a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944db67e28dfbaacfa3ae8b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944db67e28dfbaacfa3ae8c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13308618984475909885': 5, 'var_function-call-8165940882341443129': 'file_storage/function-call-8165940882341443129.json'}

exec(code, env_args)
