code = """import json
from collections import defaultdict
# Load metadata query result from file path var_call_U3o8FQVQchz7KL7rLo173iUa
meta_path = var_call_U3o8FQVQchz7KL7rLo173iUa
with open(meta_path, 'r') as f:
    meta = json.load(f)
# Load articles data from var_call_VuYsFOI7fOIyAJWlS7gMti9b (already a list)
articles = var_call_VuYsFOI7fOIyAJWlS7gMti9b
# Build mapping article_id -> article text
art_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    art_map[aid] = (title, desc)
# Prepare keyword set for business classification
import re
business_keywords = [r'\bbusiness\b', r'\bmarket\b', r'\bmarkets\b', r'\beconomy\b', r'\beconomic\b', r'\bfinancial\b', r'\bfinance\b', r'\bstock\b', r'\bstocks\b', r'\bshares\b', r'\bipo\b', r'\binitial public offering\b', r'\bcompany\b', r'\bcompanies\b', r'\bfirm\b', r'\bfirms\b', r'\bbank\b', r'\bbanks\b', r'\boil\b', r'\btrade\b', r'\btrading\b', r'\bdollar\b', r'\beurozone\b', r'\beuro\b', r'\bmerger\b', r'\bacquisition\b', r'\brevenue\b', r'\bprofit\b', r'\bprofits\b', r'\bwall st\b', r'\bshort-sellers\b', r'\binvestor\b', r'\binvestors\b', r'\bbankruptc|bankruptcy']
pattern = re.compile('|'.join(business_keywords), re.IGNORECASE)
# Count business articles per year for years 2010..2020
counts = defaultdict(int)
total_business = 0
for item in meta:
    try:
        aid = int(item.get('article_id'))
    except:
        continue
    pub = item.get('publication_date')
    if not pub:
        continue
    year = int(pub[:4])
    if year < 2010 or year > 2020:
        continue
    title, desc = art_map.get(aid, ('',''))
    text = (title + ' ' + desc).lower()
    if pattern.search(text):
        counts[str(year)] += 1
        total_business += 1
# Ensure all years present
year_counts = {str(y): counts.get(str(y), 0) for y in range(2010, 2021)}
average = total_business / 11.0
# Prepare result dict
result = {
    'year_counts': year_counts,
    'total_business_articles': total_business,
    'average_per_year': average
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_U3o8FQVQchz7KL7rLo173iUa': 'file_storage/call_U3o8FQVQchz7KL7rLo173iUa.json', 'var_call_sDmdpQmjVmF9l0cQRKyOOQXG': 'file_storage/call_sDmdpQmjVmF9l0cQRKyOOQXG.json', 'var_call_VuYsFOI7fOIyAJWlS7gMti9b': [{'_id': '69599a33555dc95354967cc7', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599a33555dc95354967ccd', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '69599a33555dc95354967cd1', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '69599a33555dc95354967cd2', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '69599a33555dc95354967cd9', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}]}

exec(code, env_args)
