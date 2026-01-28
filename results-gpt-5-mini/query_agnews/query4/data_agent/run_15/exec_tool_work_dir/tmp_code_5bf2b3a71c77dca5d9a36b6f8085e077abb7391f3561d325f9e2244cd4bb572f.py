code = """import json
# Load metadata records for 2015 from file path variable
md_file = var_call_DmVudIOV502t5IH27ghYXMnM
with open(md_file, 'r') as f:
    metadata_records = json.load(f)
# Load articles data
articles_data = var_call_983DMX7lIjrCyCqTV5JxYr3n
# If articles_data is a string path, load file
if isinstance(articles_data, str):
    with open(articles_data, 'r') as f:
        articles = json.load(f)
else:
    articles = articles_data
# Build mapping from article_id (int) to title and description
article_map = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    article_map[aid] = {'title': title, 'description': desc}

# Keywords for simple rule-based classification
sports_kw = [
    'match','goal','season','league','cup','olympic','olympics','tournament','coach','player','players',
    'football','soccer','basketball','tennis','golf','baseball','defeat','beat','win','won','draw','penalty',
    'squad','fifa','nba','nfl','mlb','score','scored','goalkeeper','striker'
]
business_kw = [
    'stock','stocks','market','oil','economy','shares','bank','investment','investor','business','acquisition',
    'merger','earnings','revenue','profit','inflation','billion','million','company','companies','investment firm',
    'private investment','firm','carlyle','bond','debt','ipo'
]
tech_kw = [
    'technology','scientist','research','nasa','space','software','internet','robot','tech','smartphone','gadget',
    'study','scientists','scientific','engineer','ai','artificial intelligence','startup','cyber','computer','data'
]

def classify_article(title, desc):
    text = (title + ' ' + desc).lower()
    # sports first
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    # default to World
    return 'World'

# Count world articles per region for metadata records
region_counts = {}
missing_articles = 0
for rec in metadata_records:
    try:
        aid = int(rec.get('article_id'))
    except:
        continue
    region = rec.get('region') or 'Unknown'
    art = article_map.get(aid)
    if not art:
        missing_articles += 1
        continue
    cat = classify_article(art['title'], art['description'])
    if cat == 'World':
        region_counts[region] = region_counts.get(region, 0) + 1

# Determine top region
if region_counts:
    top_region = max(region_counts.items(), key=lambda x: x[1])[0]
    top_count = region_counts[top_region]
else:
    top_region = None
    top_count = 0

output = {'top_region': top_region, 'count': top_count, 'counts': region_counts, 'missing_articles': missing_articles}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_DmVudIOV502t5IH27ghYXMnM': 'file_storage/call_DmVudIOV502t5IH27ghYXMnM.json', 'var_call_49XxCJm4DpMBdzFcx3j45t7l': 'file_storage/call_49XxCJm4DpMBdzFcx3j45t7l.json', 'var_call_983DMX7lIjrCyCqTV5JxYr3n': [{'_id': '6959a5a08ffb68ddc2fe4019', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a5a08ffb68ddc2fe401a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a5a08ffb68ddc2fe401b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a5a08ffb68ddc2fe401c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a5a08ffb68ddc2fe401d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
