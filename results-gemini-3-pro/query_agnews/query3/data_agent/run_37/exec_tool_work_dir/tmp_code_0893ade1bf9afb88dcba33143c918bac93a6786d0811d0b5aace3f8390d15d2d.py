code = """import json
import re

# Load metadata
with open(locals()['var_function-call-7163315103813395117'], 'r') as f:
    metadata_list = json.load(f)

# Create a dictionary article_id -> year
article_year = {}
for item in metadata_list:
    aid = int(item['article_id'])
    year = int(item['publication_date'].split('-')[0])
    article_year[aid] = year

# Load articles
with open(locals()['var_function-call-1852811640888224843'], 'r') as f:
    articles_list = json.load(f)

# Business keywords
business_keywords = [
    'market', 'stock', 'economy', 'economic', 'financial', 'finance', 'invest', 'bank', 
    'trade', 'profit', 'loss', 'share', 'dollar', 'currency', 'oil price', 'rates', 
    'inflation', 'fed ', 'ipo', 'revenue', 'tax', 'wall street', 'wall st', 'dow jones', 
    'nasdaq', 'fiscal', 'recession', 'debt', 'loan', 'growth', 'sales', 'retail', 'prices', 
    'ceo', 'company', 'corp', 'inc', 'money', 'capital', 'bonds', 'commodity', 'gold', 
    'futures', 'job', 'employment', 'unemployment', 'budget', 'deficit', 'surplus', 
    'export', 'import', 'tariff', 'wto', 'imf', 'ecb', 'central bank', 'treasury'
]

# Helper to check category
def is_business(text):
    text = text.lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Count per year
counts = {}
# Initialize years 2010-2020
for y in range(2010, 2021):
    counts[y] = 0

matched_count = 0
total_checked = 0

for article in articles_list:
    aid = int(article['article_id'])
    if aid in article_year:
        total_checked += 1
        # Check if business
        text = article['title'] + " " + article['description']
        if is_business(text):
            y = article_year[aid]
            if 2010 <= y <= 2020:
                counts[y] += 1
            matched_count += 1

print(f"Total Europe Articles (2010-2020) checked: {total_checked}")
print(f"Identified as Business: {matched_count}")
print(f"Counts per year: {counts}")

# Calculate average
total_business = sum(counts.values())
num_years = 11
average = total_business / num_years

print("__RESULT__:")
print(json.dumps({"average": average, "counts": counts, "total_business": total_business}))"""

env_args = {'var_function-call-7163315103813395117': 'file_storage/function-call-7163315103813395117.json', 'var_function-call-5122762543207161340': 'file_storage/function-call-5122762543207161340.json', 'var_function-call-9421319568468456406': 14860, 'var_function-call-11340183391818589866': [{'_id': '6944de90636c4ab819a4ae19', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944de90636c4ab819a4ae1a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944de90636c4ab819a4ae1b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944de90636c4ab819a4ae1c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944de90636c4ab819a4ae1d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7351061642432085030': 5, 'var_function-call-1852811640888224843': 'file_storage/function-call-1852811640888224843.json'}

exec(code, env_args)
