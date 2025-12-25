code = """import json
import re

# Load metadata
meta_path = locals()['var_function-call-4731593455298835981']
with open(meta_path, 'r') as f:
    meta_list = json.load(f)

# Create a dict: article_id -> year
# Also filter for Europe is already done in SQL
# Date filtering is already done in SQL
meta_dict = {}
for item in meta_list:
    aid = str(item['article_id'])
    date = item['publication_date'] # YYYY-MM-DD
    year = int(date.split('-')[0])
    meta_dict[aid] = year

# Load articles
articles_path = locals()['var_function-call-15644609291381088698']
with open(articles_path, 'r') as f:
    articles_list = json.load(f)

# Keywords
business_keywords = {
    'business', 'market', 'stock', 'trade', 'economy', 'economic', 'finance', 'financial', 'bank', 
    'invest', 'money', 'profit', 'dollar', 'euro', 'yen', 'currency', 'oil', 'gas', 'price', 
    'rates', 'interest', 'inflation', 'fed', 'central bank', 'wall st', 'ipo', 'share', 'dividend', 
    'earning', 'revenue', 'loss', 'deal', 'merger', 'acquisition', 'company', 'corp', 'inc', 
    'ceo', 'cfo', 'imf', 'wto', 'fund', 'bond', 'credit', 'debt', 'tax', 'budget', 'job', 
    'unemployment', 'retail', 'sales', 'growth', 'recession', 'industry', 'sector', 'commercial',
    'dow', 'nasdaq', 'nyse', 'treasury', 'deficit'
}

sports_keywords = {
    'sport', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'game', 
    'match', 'team', 'player', 'coach', 'win', 'won', 'score', 'cup', 'olympic', 'champion', 
    'league', 'tournament', 'medal', 'athlete', 'stadium'
}

tech_keywords = {
    'computer', 'software', 'hardware', 'internet', 'web', 'online', 'technology', 'tech', 
    'science', 'space', 'nasa', 'satellite', 'phone', 'mobile', 'gadget', 'chip', 'processor', 
    'microsoft', 'apple', 'google', 'linux', 'virus', 'hacker', 'browser', 'digital', 'network'
}

world_keywords = {
    'war', 'iraq', 'afghanistan', 'military', 'army', 'troop', 'soldier', 'police', 'president', 
    'minister', 'election', 'vote', 'politics', 'government', 'treaty', 'peace', 'nuclear', 
    'attack', 'bomb', 'kill', 'court', 'trial', 'law', 'crime', 'disaster', 'quake', 'flood',
    'parliament', 'senate', 'official', 'protest', 'riot'
}

def classify(title, desc):
    text = (title + " " + desc).lower()
    # Simple tokenization
    tokens = re.findall(r'\w+', text)
    
    counts = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
    
    for token in tokens:
        if token in business_keywords: counts['Business'] += 1
        if token in sports_keywords: counts['Sports'] += 1
        if token in tech_keywords: counts['Sci/Tech'] += 1
        if token in world_keywords: counts['World'] += 1
    
    # Determine max
    # Prioritize Business if needed, but max is standard
    if max(counts.values()) == 0:
        return 'Unknown'
    
    return max(counts, key=counts.get)

# Process
year_counts = {y: 0 for y in range(2010, 2021)}
business_articles_count = 0

for article in articles_list:
    aid = str(article.get('article_id'))
    if aid in meta_dict:
        # It's in Europe and in 2010-2020
        cat = classify(article.get('title', ''), article.get('description', ''))
        if cat == 'Business':
            y = meta_dict[aid]
            if 2010 <= y <= 2020:
                year_counts[y] += 1
                business_articles_count += 1

# Calculate Average
total_business = sum(year_counts.values())
num_years = 11
average = total_business / num_years

print("__RESULT__:")
print(json.dumps({
    "year_counts": year_counts,
    "total_business": total_business,
    "average": average
}))"""

env_args = {'var_function-call-4731593455298835981': 'file_storage/function-call-4731593455298835981.json', 'var_function-call-17144050128473710327': 'file_storage/function-call-17144050128473710327.json', 'var_function-call-11867796201877905916': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-3807024949478171761': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-182987056873605238': {'type': 'list', 'length': 5}, 'var_function-call-15644609291381088698': 'file_storage/function-call-15644609291381088698.json'}

exec(code, env_args)
