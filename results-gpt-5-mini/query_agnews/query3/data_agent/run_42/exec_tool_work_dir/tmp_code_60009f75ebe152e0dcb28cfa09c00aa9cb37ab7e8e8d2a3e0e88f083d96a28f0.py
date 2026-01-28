code = """import json
from collections import defaultdict

# Load metadata data
if isinstance(var_call_1PK3eT0GPz7pjC0XG76LYiBs, str):
    with open(var_call_1PK3eT0GPz7pjC0XG76LYiBs, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
else:
    metadata = var_call_1PK3eT0GPz7pjC0XG76LYiBs

# Load articles data
articles = var_call_QWIlKbPsnYP06zdsGRQm59Yu

# Build article_id -> text
article_text = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    article_text[aid] = (title + ' ' + desc).lower()

# Keywords for business category
business_keywords = [
    'business','economy','economies','economic','market','markets','stock','stocks','company','companies',
    'firm','investment','investor','investors','commercial','bank','banks','financial','finance','oil','crude',
    'revenue','profit','profits','merger','acquisition','acquisitions','ipo','wall st','wall street','short-sell',
    'short-sellers','reuters -', 'businessweek'
]

# Initialize counts for years 2010-2020
year_counts = {str(y): 0 for y in range(2010, 2021)}

# Process metadata records
for rec in metadata:
    try:
        aid = int(rec.get('article_id'))
    except:
        continue
    pubdate = rec.get('publication_date')
    if not pubdate or len(pubdate) < 4:
        continue
    year = int(pubdate[:4])
    if year < 2010 or year > 2020:
        continue
    text = article_text.get(aid, '').lower()
    is_business = False
    for kw in business_keywords:
        if kw in text:
            is_business = True
            break
    if is_business:
        year_counts[str(year)] += 1

# Compute average over 11 years
total = sum(year_counts.values())
average = total / 11.0

output = {
    'year_counts': year_counts,
    'total_business_articles': total,
    'average_per_year': round(average, 2)
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_1PK3eT0GPz7pjC0XG76LYiBs': 'file_storage/call_1PK3eT0GPz7pjC0XG76LYiBs.json', 'var_call_5JYrlKAz6sbXzQoaH4QQ65nl': 'file_storage/call_5JYrlKAz6sbXzQoaH4QQ65nl.json', 'var_call_QWIlKbPsnYP06zdsGRQm59Yu': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
