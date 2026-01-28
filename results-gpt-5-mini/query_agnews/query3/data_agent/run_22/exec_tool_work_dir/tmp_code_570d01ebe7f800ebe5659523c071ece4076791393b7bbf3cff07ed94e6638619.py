code = """import json
from collections import defaultdict
# paths from previous query_db calls
meta_path = var_call_qIvueCq5gTNkJLTTzXw17dGe
arts_path = var_call_ExslwoYm41QDMlFyQfPxa4lN
with open(meta_path, 'r') as f:
    meta = json.load(f)
with open(arts_path, 'r') as f:
    arts = json.load(f)
# build article map
art_map = {int(a['article_id']): {'title': a.get('title',''), 'description': a.get('description','')} for a in arts}
# keywords for business
keywords = [
    'business','economy','economies','economic','economic growth','market','markets','stock','stocks',
    'share','shares','bank','banks','finance','financial','investment','investor','ipo','merger','acquisition',
    'mergers','acquisitions','trade deficit','trade','inflation','interest rate','interest rates','reuters -',
    'oil prices','oil price','oil','eurozone','eurozone economy','eurozone economy','eurozone economy'
]
# normalize keywords
keywords = [k.lower() for k in keywords]
# Initialize counts
counts = {str(y): 0 for y in range(2010, 2021)}
seen = set()
for rec in meta:
    try:
        aid = int(rec['article_id'])
        pub = rec['publication_date']
        year = int(pub[:4])
    except:
        continue
    if year < 2010 or year > 2020:
        continue
    # avoid duplicates
    if aid in seen:
        continue
    # get article text
    a = art_map.get(aid)
    if not a:
        # if article missing, skip
        continue
    text = (a.get('title','') + ' ' + a.get('description','')).lower()
    is_business = False
    for kw in keywords:
        if kw in text:
            is_business = True
            break
    if is_business:
        counts[str(year)] += 1
        seen.add(aid)
# compute average
year_list = list(range(2010,2021))
total = sum(counts[str(y)] for y in year_list)
avg = total / len(year_list) if len(year_list)>0 else 0
result = {
    'counts': {int(k): v for k, v in counts.items()},
    'total_business_articles': total,
    'years_considered': year_list,
    'average_per_year': avg
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_qIvueCq5gTNkJLTTzXw17dGe': 'file_storage/call_qIvueCq5gTNkJLTTzXw17dGe.json', 'var_call_xGh9CuJF2DfEyVvvL5kR1ofV': 'file_storage/call_xGh9CuJF2DfEyVvvL5kR1ofV.json', 'var_call_ExslwoYm41QDMlFyQfPxa4lN': 'file_storage/call_ExslwoYm41QDMlFyQfPxa4lN.json'}

exec(code, env_args)
