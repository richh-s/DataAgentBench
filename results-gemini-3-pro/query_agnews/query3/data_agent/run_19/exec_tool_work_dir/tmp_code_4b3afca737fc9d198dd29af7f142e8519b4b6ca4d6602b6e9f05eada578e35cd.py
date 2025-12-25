code = """import json
import re

# Load metadata
meta_path = locals()['var_function-call-3309949836529129021']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

# Create mapping id -> year
id_to_year = {}
for item in meta_data:
    aid = int(item['article_id'])
    date = item['publication_date'] # YYYY-MM-DD
    year = int(date[:4])
    id_to_year[aid] = year

# Load articles
articles_path = locals()['var_function-call-13481976754616309225']
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

# Keywords
business_keywords = [
    'business', 'economy', 'economic', 'market', 'stock', 'wall street', 'invest', 
    'profit', 'revenue', 'bank', 'trade', 'corporate', 'company', 'companies', 
    'deal', 'merger', 'acquisition', 'tax', 'inflation', 'fed', 'treasury', 
    'dollar', 'euro', 'currency', 'job', 'unemployment', 'sales', 'retail', 
    'earnings', 'finance', 'financial', 'imf', 'wto', 'debt', 'loan', 'credit',
    'recession', 'growth', 'prices', 'rates', 'nasdaq', 'dow', 'nyse', 's&p'
]

# Helper to classify
def is_business(text):
    text = text.lower()
    for kw in business_keywords:
        # Simple substring match or regex word boundary?
        # Regex is safer to avoid 'company' in 'accompany'
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            return True
    return False

# Count per year
counts = {y: 0 for y in range(2010, 2021)}

for art in articles_data:
    aid = int(art['article_id'])
    if aid in id_to_year:
        # It's a European article in the date range
        # Combine title and description
        content = (art.get('title', '') + " " + art.get('description', ''))
        if is_business(content):
            y = id_to_year[aid]
            if 2010 <= y <= 2020:
                counts[y] += 1

# Calculate average
total_years = 11
total_business_articles = sum(counts.values())
average = total_business_articles / total_years

print("__RESULT__:")
print(json.dumps({"counts": counts, "average": average}))"""

env_args = {'var_function-call-3309949836529129021': 'file_storage/function-call-3309949836529129021.json', 'var_function-call-15332399369623468447': 'file_storage/function-call-15332399369623468447.json', 'var_function-call-4327695410428056510': [{'_id': '6944d2f520a43c7643e366da', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d2f520a43c7643e366db', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d2f520a43c7643e366dc', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d2f520a43c7643e366dd', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d2f520a43c7643e366de', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13272302297528658977': {'max_id': 127583, 'count': 14860}, 'var_function-call-7149556956729787320': 'file_storage/function-call-7149556956729787320.json', 'var_function-call-448433232395470169': {'num_ranges': 8002, 'query_len': 277413, 'sample_ranges': [[3, 3], [9, 14], [21, 21], [27, 27], [43, 43]]}, 'var_function-call-17829606646422682140': {'num_ranges': 1, 'query_len': 92, 'fetched_count': 127581, 'total_needed': 14860}, 'var_function-call-13481976754616309225': [{'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}]}

exec(code, env_args)
