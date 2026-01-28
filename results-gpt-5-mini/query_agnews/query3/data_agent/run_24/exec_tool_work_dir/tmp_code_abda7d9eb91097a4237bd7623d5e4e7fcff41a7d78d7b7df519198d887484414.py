code = """import json, re

def load_var(v):
    # if v is a path string to a json file, load it; else return it
    if isinstance(v, str):
        try:
            with open(v, 'r') as f:
                return json.load(f)
        except Exception:
            return v
    else:
        return v

meta = load_var(var_call_5evaam3bM5d5VRQf5L0cjdL7)
articles = load_var(var_call_jP1z2GBvFE6wBj0oLDQIOVGb)

# meta contains 'article_ids' list and 'year_map' dict
europe_ids = set(int(x) for x in meta['article_ids'])
year_map = {int(k):v for k,v in meta['year_map'].items()}

# prepare keyword lists
business_kw = [r'\bmarket(s)?\b', r'\bstock(s)?\b', r'\beconom(y|ic)\b', r'\bbusiness\b', r'\bfirm(s)?\b', r'\bcompany\b', r'\bcompanies\b', r'\bbank(s)?\b', r'\binvest(ment|or|ors|ing)\b', r'\btrading\b', r'\bshare(s)?\b', r'\bbond(s)?\b', r'\bmerger(s)?\b', r'\bacquisition(s)?\b', r'\bWall\s?St(reet)?\b', r'\bWall\s?Street\b', r'\bIPO\b', r'\bprofits?\b', r'\bearnings?\b']

sports_kw = [r'\bgoal(s)?\b', r'\bmatch(es)?\b', r'\btournament\b', r'\bleague\b', r'\bplayer(s)?\b', r'\bcoach\b', r'\bscore(s)?\b', r'\bseason\b', r'\bOlympic(s)?\b', r'\bfootball\b', r'\bsoccer\b', r'\bbasketball\b']

science_kw = [r'\bscience\b', r'\bscientist(s)?\b', r'\bresearch\b', r'\btechnology\b', r'\btech\b', r'\bNASA\b', r'\bspace\b', r'\bsoftware\b', r'\bcomputer(s)?\b', r'\bAI\b', r'\brobot(s)?\b', r'\bstudy\b']

# compile
business_re = re.compile('|'.join(business_kw), flags=re.IGNORECASE)
sports_re = re.compile('|'.join(sports_kw), flags=re.IGNORECASE)
science_re = re.compile('|'.join(science_kw), flags=re.IGNORECASE)

# initialize counts for years 2010..2020
counts = {str(y): 0 for y in range(2010, 2021)}

# build article map from articles list
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except Exception:
        continue
    article_map[aid] = a

# classify and count
for aid in europe_ids:
    if aid not in article_map:
        continue
    year = year_map.get(aid)
    if year is None or year < 2010 or year > 2020:
        continue
    a = article_map[aid]
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    text = (title + ' ' + desc).lower()

    category = 'World'
    if sports_re.search(text):
        category = 'Sports'
    elif science_re.search(text):
        category = 'Science/Technology'
    elif business_re.search(text):
        category = 'Business'
    else:
        category = 'World'

    if category == 'Business':
        counts[str(year)] += 1

total_business = sum(counts.values())
avg_per_year = total_business / 11.0

out = {'counts_per_year': counts, 'total_business': total_business, 'average_per_year': round(avg_per_year, 2)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ERF3gFj16azSSIJ8NVCzuylk': 'file_storage/call_ERF3gFj16azSSIJ8NVCzuylk.json', 'var_call_5evaam3bM5d5VRQf5L0cjdL7': 'file_storage/call_5evaam3bM5d5VRQf5L0cjdL7.json', 'var_call_jP1z2GBvFE6wBj0oLDQIOVGb': [{'_id': '69599b612885712cd4b92039', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69599b612885712cd4b9203a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69599b612885712cd4b9203b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69599b612885712cd4b9203c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599b612885712cd4b9203d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
