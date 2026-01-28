code = """import json
# Load processed metadata result from previous step; variable name from earlier query
meta_var = var_call_qmYgEMvz62dagFM2YELqkXPq
# meta_var is likely a path to a .json file
if isinstance(meta_var, str) and meta_var.endswith('.json'):
    with open(meta_var, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_var

# articles list from Mongo query
articles = var_call_aHUtbqcjYl93FSSYO9BuhPll

# Build mapping from article_id (str) to article doc
article_map = {str(int(a['article_id'])): a for a in articles}

# id_year mapping in meta contains keys as strings
id_year = meta.get('id_year', {})

# Define keyword lists for categories
business_kw = ['business', 'economy', 'economic', 'economics', 'market', 'markets', 'stock', 'stocks', 'finance', 'financial', 'bank', 'banks', 'investment', 'investor', 'investors', 'revenue', 'earnings', 'profit', 'profits', 'oil prices', 'oil', 'unemployment']
sports_kw = ['football', 'soccer', 'basketball', 'baseball', 'cricket', 'tennis', 'golf', 'score', 'match', 'season', 'tournament', 'league', 'goal', 'coach', 'player', 'win', 'defeat']
tech_kw = ['technology', 'tech', 'computer', 'software', 'internet', 'AI', 'artificial intelligence', 'robot', 'science', 'scientist', 'research', 'nasa', 'space', 'gadget']
world_kw = ['president', 'election', 'government', 'minister', 'diplomat', 'protest', 'attack', 'war', 'militia', 'rebel', 'police', 'iraq', 'country', 'countries', 'trade deal', 'diplomatic']

# Lowercase keyword lists
business_kw = [k.lower() for k in business_kw]
sports_kw = [k.lower() for k in sports_kw]
tech_kw = [k.lower() for k in tech_kw]
world_kw = [k.lower() for k in world_kw]

# Initialize yearly counts for Business category for 2010-2020
yearly = {str(y): 0 for y in range(2010, 2021)}

# Helper to classify one article
def classify(text):
    if not text:
        return 'World'
    t = text.lower()
    # check business first
    for kw in business_kw:
        if kw in t:
            return 'Business'
    for kw in sports_kw:
        if kw in t:
            return 'Sports'
    for kw in tech_kw:
        if kw in t:
            return 'Science/Technology'
    for kw in world_kw:
        if kw in t:
            return 'World'
    # fallback: World
    return 'World'

# Iterate through id_year mapping
total_business = 0
matched = 0
for aid_str, year in id_year.items():
    try:
        year_int = int(year) if year is not None else None
    except:
        continue
    if year_int is None or year_int < 2010 or year_int > 2020:
        continue
    # find article
    art = article_map.get(str(int(aid_str)))
    if not art:
        # try original key
        art = article_map.get(aid_str)
    if not art:
        # cannot classify without text
        continue
    title = art.get('title','')
    desc = art.get('description','')
    text = (title or '') + ' ' + (desc or '')
    cat = classify(text)
    if cat == 'Business':
        yearly[str(year_int)] += 1
        total_business += 1
    matched += 1

# Compute average across 11 years (2010-2020 inclusive)
years_count = 2020 - 2010 + 1
average = total_business / years_count if years_count > 0 else 0

result = {
    'yearly_business_counts': yearly,
    'total_business_articles_2010_2020': total_business,
    'average_business_articles_per_year': round(average, 2),
    'years_included': [str(y) for y in range(2010, 2021)],
    'articles_matched_in_metadata': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_3X1uWWrdhN43YDBssiV1HmmL': 'file_storage/call_3X1uWWrdhN43YDBssiV1HmmL.json', 'var_call_qmYgEMvz62dagFM2YELqkXPq': 'file_storage/call_qmYgEMvz62dagFM2YELqkXPq.json', 'var_call_aHUtbqcjYl93FSSYO9BuhPll': [{'_id': '69599533a0edfe5ae5ee8b40', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69599533a0edfe5ae5ee8b41', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69599533a0edfe5ae5ee8b42', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69599533a0edfe5ae5ee8b43', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599533a0edfe5ae5ee8b44', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
