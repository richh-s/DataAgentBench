code = """import json
import re

# Load the Europe records (file path stored in var_call_IYY2ZN0ACwN3qlsiWrnZAkXO)
with open(var_call_IYY2ZN0ACwN3qlsiWrnZAkXO, 'r') as f:
    europe_records = json.load(f)

articles = var_call_wWQBWZ1z7IlTHyRr0nbDzRbk

# Build mapping from article_id to article document
article_map = {str(a['article_id']): a for a in articles}

# Define keyword sets for simple rule-based classification
business_keywords = [
    'economy', 'economic', 'market', 'markets', 'bank', 'banks', 'stock', 'stocks', 'share', 'shares',
    'investor', 'investors', 'investment', 'investments', 'business', 'company', 'companies', 'merger',
    'acquisition', 'acquisitions', 'firm', 'revenue', 'revenues', 'profit', 'profits', 'ipo', 'bond', 'bonds',
    'currency', 'inflation', 'interest rate', 'wall st', 'wall street', 'dow jones', 'nasdaq', 'ftse', 's&p'
]

sports_keywords = [
    'match', 'season', 'team', 'coach', 'scored', 'goal', 'tournament', 'league', 'olympic', 'win', 'won',
    'defeat', 'defeated', 'runner', 'score', 'race', 'boxing', 'football', 'soccer', 'basketball', 'tennis'
]

tech_keywords = [
    'technology', 'tech', 'scientist', 'research', 'nasa', 'space', 'ai', 'artificial intelligence', 'robot',
    'software', 'computer', 'smartphone', 'gadgets', 'internet', 'cyber', 'data', 'startup'
]

# Lowercase keywords for matching
bkw = [k.lower() for k in business_keywords]
skw = [k.lower() for k in sports_keywords]
tkw = [k.lower() for k in tech_keywords]

# Initialize counts for years 2010-2020 inclusive
years = list(range(2010, 2021))
counts = {str(y): 0 for y in years}
total_business = 0

for rec in europe_records:
    aid = str(rec.get('article_id'))
    pub = rec.get('publication_date', '')
    if not pub or len(pub) < 4:
        continue
    try:
        year = int(pub[:4])
    except:
        continue
    if year < 2010 or year > 2020:
        continue
    doc = article_map.get(aid)
    text = ''
    if doc:
        title = doc.get('title', '') or ''
        desc = doc.get('description', '') or ''
        text = (title + ' ' + desc).lower()
    else:
        text = ''

    # Classification: business first, then sports, then tech, else world
    is_business = any(k in text for k in bkw)
    if is_business:
        counts[str(year)] += 1
        total_business += 1
    else:
        # Not business; ignore for counting
        pass

# Compute average per year over 11 years (2010-2020 inclusive)
num_years = len(years)
avg_per_year = total_business / num_years if num_years > 0 else 0

result = {
    'average_per_year': round(avg_per_year, 2),
    'total_business_articles': total_business,
    'years': counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_IYY2ZN0ACwN3qlsiWrnZAkXO': 'file_storage/call_IYY2ZN0ACwN3qlsiWrnZAkXO.json', 'var_call_wWQBWZ1z7IlTHyRr0nbDzRbk': [{'_id': '69599700def3ed93a0cf168a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69599700def3ed93a0cf168b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69599700def3ed93a0cf168c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69599700def3ed93a0cf168d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599700def3ed93a0cf168e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
