code = """import json
import os

# Load business articles (from var_functions.query_db:5)
business_articles = locals().get('var_functions.query_db:5')
if not business_articles:
    raise ValueError("Business articles not found")

# Load Europe metadata (from var_functions.query_db:6)
europe_meta_raw = locals().get('var_functions.query_db:6')
# If it's a file path (string), load it; otherwise it's already a list
if isinstance(europe_meta_raw, str):
    # It's a path to JSON file
    with open(europe_meta_raw, 'r') as f:
        europe_meta = json.load(f)
else:
    europe_meta = europe_meta_raw

# Extract business article IDs (as integers)
# The business articles data may have article_id as string; ensure int.
business_ids = set()
for doc in business_articles:
    aid = doc.get('article_id')
    if aid is not None:
        business_ids.add(int(aid))

# Process Europe articles; filter date range 2010-2020 inclusive
europe_counts_by_year = {}
# Initialize all years 2010-2020 with zero counts
for year in range(2010, 2021):
    europe_counts_by_year[year] = 0

for doc in europe_meta:
    # Each doc is dict with article_id, region, publication_date
    aid_str = doc.get('article_id')
    pub_date = doc.get('publication_date')  # str format YYYY-MM-DD
    if not aid_str or not pub_date:
        continue
    # Check if this article is a business article
    if int(aid_str) not in business_ids:
        continue
    # Parse year
    try:
        year = int(pub_date.split('-')[0])
    except Exception:
        continue
    if 2010 <= year <= 2020:
        europe_counts_by_year[year] += 1

# Sum and average across years
total_business_europe = sum(europe_counts_by_year.values())
num_years = len(europe_counts_by_year)  # Should be 11
average = total_business_europe / num_years if num_years else None

# Prepare result JSON
result = {
    "average_business_articles_per_year": average,
    "total_business_articles_in_europe_2010_2020": total_business_europe,
    "years_considered": num_years,
    "counts_by_year": europe_counts_by_year
}

# Print in required format
print('----BEGIN PRINT FORMAT----')
print('__RESULT__:')
print(json.dumps(result))
print('----END PRINT FORMAT----')"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': [{'_id': '6969c20389ee61063187120b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c20389ee61063187120c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c20389ee61063187120e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969c20389ee61063187120f', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969c20389ee610631871210', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
