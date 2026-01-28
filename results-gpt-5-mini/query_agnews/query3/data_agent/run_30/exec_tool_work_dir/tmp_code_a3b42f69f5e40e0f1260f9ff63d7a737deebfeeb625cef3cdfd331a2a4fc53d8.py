code = """import json
from collections import defaultdict
# Load files from storage keys
path_meta = var_call_mDfSGF2mERkGjJtj8IpDTfVY
path_articles = var_call_6wcVLI4WCaPnQkoCOFnsAIao
with open(path_meta, 'r') as f:
    meta = json.load(f)
with open(path_articles, 'r') as f:
    articles = json.load(f)
# Build article content map
content_map = {}
for a in articles:
    aid = str(int(a.get('article_id')))
    title = a.get('title') or ''
    desc = a.get('description') or ''
    content_map[aid] = (title, desc)
# Business keyword list
business_keywords = [
    'economy','economic','economics','market','markets','stock','stocks','share','shares',
    'firm','company','companies','corporate','bank','banks','investment','investor','ipo',
    'profit','loss','earnings','revenue','business','trade','trading','merger','acquisition',
    'commercial','finance','financial','inflation','gdp','eurozone','interest rate','bond','bonds',
    'oil prices','oil price','oil prices','oil price','unemployment','salary','salaries','wage','wages'
]
# Normalize keywords to lower
business_keywords = [k.lower() for k in business_keywords]

# For each Europe article id classify
id_to_year = meta.get('id_to_year', {})
# counts per year
counts = defaultdict(int)
classified_ids = []
for aid, year in id_to_year.items():
    aid_str = str(int(aid))
    title, desc = content_map.get(aid_str, ('',''))
    text = (title + ' ' + desc).lower()
    is_business = False
    for kw in business_keywords:
        if kw in text:
            is_business = True
            break
    if is_business:
        counts[year] += 1
        classified_ids.append(aid_str)
# Ensure years 2010-2020 inclusive present
year_counts = {str(y): int(counts.get(y,0)) for y in range(2010, 2021)}
total = sum(year_counts.values())
average = total / 11.0
result = {
    'year_counts': year_counts,
    'total_business_articles_in_europe_2010_2020': total,
    'average_per_year_2010_2020': average,
    'num_classified_ids': len(classified_ids)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_l6lMtIxOSgeKCkVENT08qPDd': 'file_storage/call_l6lMtIxOSgeKCkVENT08qPDd.json', 'var_call_mDfSGF2mERkGjJtj8IpDTfVY': 'file_storage/call_mDfSGF2mERkGjJtj8IpDTfVY.json', 'var_call_6wcVLI4WCaPnQkoCOFnsAIao': 'file_storage/call_6wcVLI4WCaPnQkoCOFnsAIao.json'}

exec(code, env_args)
