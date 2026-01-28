code = """import json
from collections import defaultdict

# Load metadata query result (file path stored in var_call_XvectxODeRSqQPEq7oNorDKh)
fp_meta = var_call_XvectxODeRSqQPEq7oNorDKh
with open(fp_meta, 'r') as f:
    meta = json.load(f)

# Load articles data from variable
articles = var_call_OgS7Io0LfvIT4WGfx2Isa8X0

# Build mapping from article_id (int) to combined text
article_text = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid] = (title + ' ' + desc).lower()

# Define simple business-related keywords
business_keywords = [
    'business', 'market', 'markets', 'stock', 'stocks', 'wall st', 'wall street', 'economy', 'economies',
    'earnings', 'investment', 'investor', 'investors', 'bank', 'finance', 'financial', 'company', 'companies',
    'merger', 'acquisition', 'acquisitions', 'revenue', 'profit', 'profits', 'billion', 'million', 'carlyle',
    'private investment', 'aerospace', 'oil prices', 'oil price', 'oil and economy', 'crude', 'indices'
]

# Count business articles per year for Europe metadata entries between 2010 and 2020 inclusive
counts = defaultdict(int)
for r in meta:
    try:
        aid = int(r.get('article_id'))
        pub = r.get('publication_date')
        year = int(pub[:4])
    except:
        continue
    if year < 2010 or year > 2020:
        continue
    text = article_text.get(aid, '').lower()
    is_business = False
    for kw in business_keywords:
        if kw in text:
            is_business = True
            break
    if is_business:
        counts[year] += 1

# Ensure all years are present
counts_by_year = {str(y): counts.get(y, 0) for y in range(2010, 2021)}
total = sum(counts_by_year.values())
num_years = 2020 - 2010 + 1
average = total / num_years if num_years > 0 else 0.0

result = {
    'average_business_articles_per_year': round(average, 2),
    'counts_by_year': counts_by_year,
    'total_business_articles': total,
    'years_included': [str(y) for y in range(2010, 2021)]
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_XvectxODeRSqQPEq7oNorDKh': 'file_storage/call_XvectxODeRSqQPEq7oNorDKh.json', 'var_call_OvHgN3g8D7aoNDexancD0G8I': 'file_storage/call_OvHgN3g8D7aoNDexancD0G8I.json', 'var_call_OgS7Io0LfvIT4WGfx2Isa8X0': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
