code = """import json
from collections import defaultdict

# Load metadata from file path variable
metadata_path = var_call_5iSGxlNcLjT5bLUlRRSNkLiB
with open(metadata_path, 'r') as f:
    metadata = json.load(f)

# Load articles list from variable
articles = var_call_ZdqXKNfo1VOgDKc7awqUvNEJ

# Build mapping article_id -> combined text
article_text = {}
for a in articles:
    aid = str(a.get('article_id'))
    title = a.get('title','') or ''
    desc = a.get('description','') or ''
    article_text[aid] = (title + ' ' + desc).lower()

# Define business-related keywords
business_kw = [
    'business','market','markets','stock','stocks','wall st','wall street','shares',
    'economy','economic','bank','banks','investment','investor','investors','firm',
    'company','companies','oil','crude','commerce','commercial','merger','acquisition',
    'ipo','earnings','profit','profits','revenue','businessman','trade','trading','finance',
    'financial','equity','bond','bonds','restructur'
]

# Years range
years = list(range(2010, 2021))

# Count unique business article ids per year
year_articles = {y: set() for y in years}

for item in metadata:
    aid = str(item.get('article_id'))
    pub = item.get('publication_date')
    if not pub or len(pub) < 4:
        continue
    try:
        y = int(pub[:4])
    except:
        continue
    if y < 2010 or y > 2020:
        continue
    text = article_text.get(aid)
    if not text:
        # skip if no article text available
        continue
    # classify as business if any keyword appears
    is_business = any(k in text for k in business_kw)
    if is_business:
        year_articles[y].add(aid)

# Prepare counts per year
counts_by_year = {str(y): len(year_articles[y]) for y in years}
total = sum(counts_by_year[str(y)] for y in years)
average = total / len(years) if years else 0

result = {
    'counts_by_year': counts_by_year,
    'total_business_articles_2010_2020': total,
    'average_business_articles_per_year': round(average, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5iSGxlNcLjT5bLUlRRSNkLiB': 'file_storage/call_5iSGxlNcLjT5bLUlRRSNkLiB.json', 'var_call_ZdqXKNfo1VOgDKc7awqUvNEJ': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_call_dmEtJrPzgvAjGrbeQ18Efmtz': 'file_storage/call_dmEtJrPzgvAjGrbeQ18Efmtz.json'}

exec(code, env_args)
