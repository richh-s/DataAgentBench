code = """import json, re
# Load metadata records from file
meta_path = var_call_Zvd9beiaubpkKZ7mIFvoQAlQ
with open(meta_path, 'r') as f:
    meta_records = json.load(f)
# Load articles list from storage variable
articles = var_call_zAdC63AQ6zay67b0oZ41gcOp
# Build article_id -> text mapping
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    text = (title + ' ' + desc).lower()
    article_map[aid] = text

# Business keywords (lowercase)
business_keywords = [
    'business', 'economy', 'economic', 'market', 'markets', 'stock', 'stocks', 'shares', 'wall st', 'wall street',
    'finance', 'financial', 'bank', 'banks', 'investment', 'investor', 'investors', 'merger', 'acquisition',
    'profit', 'loss', 'earnings', 'revenue', 'inflation', 'interest rate', 'bond', 'bonds', 'trade', 'trading',
    'oil prices', 'oil', 'commodities', 'company', 'companies', 'private equity', 'aerospace', 'commercial', 'firm'
]
# Precompile patterns for word boundary safe matching
patterns = [re.compile(re.escape(k)) for k in business_keywords]

# Count business articles per year
counts = {str(y): 0 for y in range(2010, 2021)}
matched_ids = set()
for r in meta_records:
    try:
        aid = int(r.get('article_id'))
        pub = r.get('publication_date')
        year = int(pub[:4])
    except:
        continue
    if 2010 <= year <= 2020:
        text = article_map.get(aid, '').lower()
        is_business = False
        for pat in patterns:
            if pat.search(text):
                is_business = True
                break
        if is_business:
            counts[str(year)] += 1
            matched_ids.add(aid)

# Compute average
total = sum(counts.values())
num_years = 2020 - 2010 + 1
average = total / num_years if num_years else 0.0

output = {
    'year_counts': counts,
    'total_business_articles': total,
    'average_per_year': average,
    'matched_article_ids_sample_count': len(matched_ids)
}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_Bl0KkE0hJGL4FcVBoMVc4K5h': ['articles'], 'var_call_Zvd9beiaubpkKZ7mIFvoQAlQ': 'file_storage/call_Zvd9beiaubpkKZ7mIFvoQAlQ.json', 'var_call_4FbB0MIO31TPsvCucDwKSMrR': 'file_storage/call_4FbB0MIO31TPsvCucDwKSMrR.json', 'var_call_zAdC63AQ6zay67b0oZ41gcOp': [{'_id': '6959a189648abb444849de80', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a189648abb444849de81', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a189648abb444849de82', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a189648abb444849de83', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a189648abb444849de84', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
