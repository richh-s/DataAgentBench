code = """import json
# load processed metadata for 2015
p_meta = var_call_89Uu7jc5r16mBnKwG8ZESekf
with open(p_meta, 'r') as f:
    meta_data = json.load(f)
metadata = meta_data['metadata']
# load articles
p_articles = var_call_EJMRiSlcJxqUG5FL6X7tKk3m
with open(p_articles, 'r') as f:
    articles = json.load(f)
# build article_id -> text map
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        try:
            aid = int(str(a.get('article_id')))
        except:
            continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    art_map[aid] = (title + ' ' + desc).lower()

# keyword sets
sports_kw = ['football','soccer','match','goal','season','tournament','olympic','nba','mlb','nfl','cricket','rugby','fifa','world cup','championship','f1','race','tennis','golf','score','scores','boxing','wimbledon','goalkeeper','striker','coach','manager','cup']
business_kw = ['stock','stocks','market','markets','economy','economic','company','companies','shares','ipo','profit','profits','bank','business','investment','investor','deal','merger','acquisition','billion','million','interest rates','unemployment']
sci_kw = ['technology','tech','scientist','scientists','research','nasa','space','scientific','science','computer','software','internet','google','apple','microsoft','android','ios','robot','ai','artificial intelligence','study','researchers','satellite']

def classify(text):
    if not text:
        return 'World'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# count regions for World category in 2015
region_counts = {}
missing = 0
for m in metadata:
    aid = m['article_id']
    region = m.get('region') or 'Unknown'
    text = art_map.get(aid)
    if text is None:
        missing += 1
        continue
    cat = classify(text)
    if cat == 'World':
        region_counts[region] = region_counts.get(region, 0) + 1

# find top region
if region_counts:
    top_region = max(region_counts.items(), key=lambda x: x[1])[0]
    top_count = region_counts[top_region]
else:
    top_region = None
    top_count = 0

out = {'top_region': top_region, 'count': top_count, 'region_counts': region_counts, 'missing_articles': missing}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aU6jDJSlzaDHjwOp7Q8SA18p': 'file_storage/call_aU6jDJSlzaDHjwOp7Q8SA18p.json', 'var_call_89Uu7jc5r16mBnKwG8ZESekf': 'file_storage/call_89Uu7jc5r16mBnKwG8ZESekf.json', 'var_call_8ggzNK2VNmchsfrVvzfESMVU': {'min_id': 13, 'max_id': 127570, 'count': 6696}, 'var_call_EJMRiSlcJxqUG5FL6X7tKk3m': 'file_storage/call_EJMRiSlcJxqUG5FL6X7tKk3m.json'}

exec(code, env_args)
