code = """import json
# load metadata records (file path stored in var_call_lHMvQvEmX9h6BOCb6lygiCdV)
meta_path = var_call_lHMvQvEmX9h6BOCb6lygiCdV
with open(meta_path, 'r') as f:
    meta = json.load(f)
# articles data is in var_call_F1Z5909zoxp0agnatzcdm0yl
articles = var_call_F1Z5909zoxp0agnatzcdm0yl
# build mapping from article_id to publication year for Europe articles
article_year = {}
for rec in meta:
    try:
        aid = int(rec['article_id'])
        year = int(rec['publication_date'][:4])
        if 2010 <= year <= 2020:
            article_year[aid] = year
    except Exception:
        continue
# build mapping from article_id to combined text
articles_map = {}
for a in articles:
    try:
        aid = int(a['article_id'])
        text = ((a.get('title') or '') + ' ' + (a.get('description') or '')).lower()
        articles_map[aid] = text
    except Exception:
        continue
# keywords for Business
keywords = [
    'economy','economic','finance','financial','market','markets','stock','stocks','wall st','wall street',
    'oil','bank','investment','investments','investor','investors','business','commercial','merger','acquir',
    'profit','earnings','revenue','shares','trade','trading','billion','million'
]
# count per year
counts = {year: 0 for year in range(2010, 2021)}
for aid, year in article_year.items():
    text = articles_map.get(aid, '')
    is_business = False
    for kw in keywords:
        if kw in text:
            is_business = True
            break
    if is_business:
        counts[year] += 1
# compute average across 2010-2020 inclusive
total = sum(counts.values())
avg = total / len(counts) if counts else 0
# prepare result
result = {'average_business_articles_per_year': avg, 'total_business_articles_2010_2020': total, 'years_considered': list(counts.keys()), 'counts_per_year': counts}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lHMvQvEmX9h6BOCb6lygiCdV': 'file_storage/call_lHMvQvEmX9h6BOCb6lygiCdV.json', 'var_call_Z16eVfJW6ANAwC9B8D8ZjvsZ': 'file_storage/call_Z16eVfJW6ANAwC9B8D8ZjvsZ.json', 'var_call_F1Z5909zoxp0agnatzcdm0yl': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
