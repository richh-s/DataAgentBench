code = """import json
# Load metadata and articles results from storage keys
meta_path = var_call_U3o8FQVQchz7KL7rLo173iUa
with open(meta_path, 'r') as f:
    meta = json.load(f)
articles = var_call_VuYsFOI7fOIyAJWlS7gMti9b
# Build mapping
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    art_map[aid] = ((a.get('title') or ''), (a.get('description') or ''))
# Keywords for substring matching
keywords = ['business','market','markets','economy','economic','financial','finance','stock','stocks','shares','ipo','initial public offering','company','companies','firm','firms','bank','banks','oil','trade','trading','dollar','eurozone','euro','merger','acquisition','revenue','profit','profits','wall st','short-sellers','investor','investors']

from collections import defaultdict
counts = defaultdict(int)
missing = 0
processed = 0
for item in meta:
    aid = int(item['article_id'])
    pub = item.get('publication_date')
    if not pub:
        continue
    year = int(pub[:4])
    if year < 2010 or year > 2020:
        continue
    processed += 1
    title, desc = art_map.get(aid, ('',''))
    if title=='' and desc=='':
        missing += 1
        continue
    text = (title + ' ' + desc).lower()
    is_business = any(k in text for k in keywords)
    if is_business:
        counts[str(year)] += 1
# Ensure all years present
year_counts = {str(y): counts.get(str(y), 0) for y in range(2010, 2021)}
# total business is sum
total_business = sum(year_counts.values())
average = total_business / 11.0
result = {
    'processed_meta_entries_in_range': processed,
    'articles_documents_retrieved': len(art_map),
    'missing_article_documents': missing,
    'year_counts': year_counts,
    'total_business_articles': total_business,
    'average_per_year': average
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_U3o8FQVQchz7KL7rLo173iUa': 'file_storage/call_U3o8FQVQchz7KL7rLo173iUa.json', 'var_call_sDmdpQmjVmF9l0cQRKyOOQXG': 'file_storage/call_sDmdpQmjVmF9l0cQRKyOOQXG.json', 'var_call_VuYsFOI7fOIyAJWlS7gMti9b': [{'_id': '69599a33555dc95354967cc7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599a33555dc95354967ccd', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '69599a33555dc95354967cd1', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '69599a33555dc95354967cd2', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '69599a33555dc95354967cd9', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_call_eEZtzURLeFSuDmJupb3CKTHj': {'year_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total_business_articles': 0, 'average_per_year': 0.0}}

exec(code, env_args)
