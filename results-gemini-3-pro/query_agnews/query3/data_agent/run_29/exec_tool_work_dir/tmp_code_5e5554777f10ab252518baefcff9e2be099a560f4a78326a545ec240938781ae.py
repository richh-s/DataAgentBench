code = """import json

# Load metadata
with open(locals()['var_function-call-17075212337781938676'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-427199543917706096'], 'r') as f:
    articles_list = json.load(f)

# Create a map of article_id -> year for relevant articles
# The SQL query already filtered for Europe and 2010-2020.
meta_map = {}
for item in metadata_list:
    aid = str(item['article_id'])
    date = item['publication_date'] # YYYY-MM-DD
    year = int(date.split('-')[0])
    meta_map[aid] = year

# Keywords for Business category
keywords = [
    'business', 'economy', 'economic', 'financial', 'finance', 'market', 'stock', 
    'trade', 'investment', 'investor', 'profit', 'bank', 'banking', 'dollar', 
    'euro', 'currency', 'rate', 'money', 'corporate', 'company', 'tax', 'debt', 
    'ipo', 'merger', 'acquisition', 'share', 'revenue', 'inflation', 'recession',
    'wall st', 'dow jones', 'nasdaq', 'commodity', 'commodities', 'price', 
    'spending', 'budget', 'deficit', 'employment', 'jobless', 'retail', 'sales'
]

# Count business articles per year
yearly_counts = {y: 0 for y in range(2010, 2021)}

business_article_count = 0
processed_ids = set()

for article in articles_list:
    aid = str(article['article_id'])
    
    # Only process if it's in our relevant metadata (Europe, 2010-2020)
    if aid in meta_map:
        if aid in processed_ids:
            continue
        processed_ids.add(aid)
        
        title = article.get('title', '').lower()
        desc = article.get('description', '').lower()
        text = title + ' ' + desc
        
        # Check for keywords
        is_business = False
        for kw in keywords:
            # Simple substring match
            if kw in text:
                is_business = True
                break
        
        if is_business:
            year = meta_map[aid]
            if year in yearly_counts:
                yearly_counts[year] += 1
            business_article_count += 1

# Calculate average
total_business = sum(yearly_counts.values())
num_years = 11 # 2010 to 2020 inclusive
average = total_business / num_years

result = {
    "yearly_counts": yearly_counts,
    "total_business_articles": total_business,
    "average_per_year": average
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-17075212337781938676': 'file_storage/function-call-17075212337781938676.json', 'var_function-call-10681608177601974937': {'count': 14860, 'ids_preview': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_function-call-13798772103698685076': [{'_id': '6944d9733f9754d4d7ac81c6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d9733f9754d4d7ac81c7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d9733f9754d4d7ac81c8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d9733f9754d4d7ac81c9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d9733f9754d4d7ac81ca', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3915920404042500315': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-427199543917706096': 'file_storage/function-call-427199543917706096.json'}

exec(code, env_args)
