code = """import json
import pandas as pd

# Load metadata results from file or variable
meta_var = var_call_ZFOrRqUBFvvr9LSa0p86BV4z
if isinstance(meta_var, str):
    with open(meta_var, 'r') as f:
        metadata = json.load(f)
else:
    metadata = meta_var

articles = var_call_qPknD0s6fdAhwFQxSIfjGm7p

# Build article text map
articles_map = {str(a['article_id']): ((a.get('title') or '') + ' ' + (a.get('description') or '')).lower() for a in articles}

# Define keyword sets
business_kw = ['business','market','markets','stock','stocks','oil','prices','price','economy','economic','bank','banks','firm','investment','investor','company','companies','commercial','shares','earnings','revenue','profit','profits','carlyle','wall st','short-sellers','short sellers','crude']
sports_kw = ['match','goal','league','tournament','season','coach','player','players','win','score','olympic','football','soccer','basketball','baseball','tennis','golf','race','racing']
science_kw = ['technology','tech','scientist','research','lab','space','scientific','nasa','robot','ai','artificial intelligence','software','hardware','computer','science','biotech','innovation']

# Count business articles per year 2010-2020
counts = {str(year): 0 for year in range(2010, 2021)}
missing_articles = 0
for rec in metadata:
    aid = str(rec.get('article_id'))
    pub = rec.get('publication_date')
    if not pub or len(pub) < 4:
        continue
    year = int(pub[:4])
    if year < 2010 or year > 2020:
        continue
    text = articles_map.get(aid, '').lower()
    if text == '':
        missing_articles += 1
    is_business = any(kw in text for kw in business_kw)
    is_sports = any(kw in text for kw in sports_kw)
    is_science = any(kw in text for kw in science_kw)
    # Assign category priority: business, sports, science, else world
    if is_business and not (is_sports or is_science):
        counts[str(year)] += 1
    elif is_business and (is_sports or is_science):
        # If overlaps, prefer business
        counts[str(year)] += 1
    else:
        # not business -> ignore for business counts
        pass

# Compute average per year over 11 years
total_business = sum(counts.values())
average = total_business / len(counts) if len(counts) > 0 else 0

result = {
    'counts_per_year': counts,
    'total_business_articles': total_business,
    'average_per_year': average,
    'missing_articles_in_articles_db': missing_articles
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZFOrRqUBFvvr9LSa0p86BV4z': 'file_storage/call_ZFOrRqUBFvvr9LSa0p86BV4z.json', 'var_call_qPknD0s6fdAhwFQxSIfjGm7p': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
