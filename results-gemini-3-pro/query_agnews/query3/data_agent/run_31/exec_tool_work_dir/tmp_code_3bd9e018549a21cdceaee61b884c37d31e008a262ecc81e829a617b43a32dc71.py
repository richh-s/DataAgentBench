code = """import json
import pandas as pd
import re

# Load metadata
with open(locals()['var_function-call-8183838540505517503'], 'r') as f:
    metadata_list = json.load(f)

# Create a map: article_id (int) -> year (int)
# Only strictly within 2010-2020
article_year_map = {}
for entry in metadata_list:
    aid = int(entry['article_id'])
    date = entry['publication_date'] # YYYY-MM-DD
    year = int(date[:4])
    if 2010 <= year <= 2020:
        article_year_map[aid] = year

# Load articles
with open(locals()['var_function-call-11579754966878934648'], 'r') as f:
    articles_list = json.load(f)

# Keywords for Business
business_keywords = {
    'market', 'stock', 'stocks', 'share', 'shares', 'economy', 'economic', 'finance', 'financial',
    'bank', 'banking', 'fund', 'funds', 'money', 'trade', 'trading', 'investment', 'investor', 'investing',
    'profit', 'profits', 'revenue', 'revenues', 'loss', 'losses', 'wall st', 'wall street', 
    'dow', 'dow jones', 'nasdaq', 'tax', 'taxes', 'rate', 'rates', 'price', 'prices', 
    'oil', 'crude', 'gas', 'gold', 'dollar', 'euro', 'yen', 'currency', 
    'company', 'companies', 'corp', 'corporation', 'inc', 'business', 'businesses', 
    'industry', 'industrial', 'deal', 'deals', 'merger', 'acquisition', 'bid', 'bidding', 
    'sale', 'sales', 'budget', 'deficit', 'fed', 'federal reserve', 'treasury', 
    'yield', 'loan', 'loans', 'credit', 'debt', 'debts', 'ceo', 'cfo', 'executive', 
    'growth', 'inflation', 'recession', 'spending', 'cost', 'costs', 'retail', 'retailer'
}

# Function to classify
def is_business(text):
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    words = set(text.split())
    # Check intersection
    if words.intersection(business_keywords):
        return True
    return False

# Count Business articles per year
counts = {y: 0 for y in range(2010, 2021)}

for article in articles_list:
    try:
        aid = int(article.get('article_id', -1))
    except:
        continue
        
    if aid in article_year_map:
        year = article_year_map[aid]
        # Combine title and description
        text = (article.get('title', '') + ' ' + article.get('description', ''))
        if is_business(text):
            counts[year] += 1

# Calculate average
total_business = sum(counts.values())
num_years = 11
average = total_business / num_years

print("__RESULT__:")
print(json.dumps({"counts": counts, "average": average, "total": total_business}))"""

env_args = {'var_function-call-8183838540505517503': 'file_storage/function-call-8183838540505517503.json', 'var_function-call-1505226483977166881': 'file_storage/function-call-1505226483977166881.json', 'var_function-call-5130672257415933786': 14860, 'var_function-call-13256661063451631781': [{'_id': '6944dadf33aefa6592744307', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dadf33aefa6592744308', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dadf33aefa6592744309', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dadf33aefa659274430a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dadf33aefa659274430b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3261169261183607461': [{'_id': '6944dadf33aefa6592744307', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dadf33aefa6592744308', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dadf33aefa6592744309', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dadf33aefa659274430a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dadf33aefa659274430b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11579754966878934648': 'file_storage/function-call-11579754966878934648.json'}

exec(code, env_args)
