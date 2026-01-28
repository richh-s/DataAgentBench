code = """import json
from pathlib import Path

# Load metadata mapping from previous execute_python result
meta_path = var_call_HOoF0hbt90id6bAoZC0TLvp9
if isinstance(meta_path, str) and Path(meta_path).exists():
    with open(meta_path, 'r') as f:
        meta = json.load(f)
else:
    meta = var_call_HOoF0hbt90id6bAoZC0TLvp9

# meta contains 'article_ids' and 'id_to_date'
id_to_date = {int(k): v for k, v in meta.get('id_to_date', {}).items()}

# Load articles data from Mongo query result
articles_res = var_call_J1CmcpgfWi0gZVAmW4MQiKKe
# articles_res may be a path or a list
if isinstance(articles_res, str) and Path(articles_res).exists():
    with open(articles_res, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_res

# Build mapping article_id -> concatenated text
id_to_text = {}
for doc in articles:
    try:
        aid = int(doc.get('article_id'))
    except:
        continue
    title = doc.get('title') or ''
    desc = doc.get('description') or ''
    text = (title + ' ' + desc).lower()
    id_to_text[aid] = text

# Define business keywords
business_keywords = ['market','wall st','wallstreet','stock','stocks','share','shares','ipo','economy','economic','dollar','trade','bank','company','companies','merger','acquisition','profit','loss','revenue','earnings','investor','investment','financial','finance','oil export','oil exports','oil','eurozone']

# Count business articles per year (2010-2020 inclusive)
years = {str(y): 0 for y in range(2010, 2021)}
classified_count = 0
unknown_count = 0
for aid, pubdate in id_to_date.items():
    # Check year in range
    year = None
    if pubdate and len(pubdate) >= 4:
        year = pubdate[:4]
    if year not in years:
        continue
    text = id_to_text.get(aid)
    if not text:
        unknown_count += 1
        continue
    is_business = any(kw in text for kw in business_keywords)
    if is_business:
        years[year] += 1
        classified_count += 1

total_business = sum(years.values())
average_per_year = total_business / len(years) if len(years) > 0 else 0.0

result = {
    'total_business_articles_found': total_business,
    'average_per_year_2010_2020': average_per_year,
    'business_counts_by_year': years,
    'metadata_total_articles_in_europe_2010_2020': len(id_to_date),
    'articles_with_text_found': len(id_to_text),
    'articles_without_text': unknown_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_mMPfuHOhSWZTJsArBYyeF59A': 'file_storage/call_mMPfuHOhSWZTJsArBYyeF59A.json', 'var_call_HOoF0hbt90id6bAoZC0TLvp9': 'file_storage/call_HOoF0hbt90id6bAoZC0TLvp9.json', 'var_call_J1CmcpgfWi0gZVAmW4MQiKKe': [{'_id': '695997c33a6746570f382c21', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '695997c33a6746570f382c27', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '695997c33a6746570f382c2b', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '695997c33a6746570f382c2c', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '695997c33a6746570f382c33', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}]}

exec(code, env_args)
