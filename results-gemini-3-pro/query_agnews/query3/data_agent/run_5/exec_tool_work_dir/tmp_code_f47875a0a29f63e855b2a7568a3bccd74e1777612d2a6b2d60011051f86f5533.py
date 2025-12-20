code = """import json

# Load metadata (file path)
path_meta = locals()['var_function-call-9733408424743850930']
with open(path_meta, 'r') as f:
    metadata_list = json.load(f)

# Load articles (direct list)
articles_list = locals()['var_function-call-8535152676187507582']
# If it happens to be a string (json dump), parse it. If it's a list, use it.
if isinstance(articles_list, str):
    # Check if it's a file path or json string?
    # Usually if it's not a file path message, it's the object.
    # But if the output was truncated in the chat, the variable might still be the full object.
    # If the tool returns a string representation, I might need to load it.
    try:
        articles_list = json.loads(articles_list)
    except:
        # Maybe it's a file path that I missed?
        if articles_list.endswith('.json'):
             with open(articles_list, 'r') as f:
                articles_list = json.load(f)

# Create lookup for articles
# Ensure articles_list is a list
if not isinstance(articles_list, list):
    # Fallback: maybe it was a file path and I missed the 'stored in file' message nuances
    # But let's assume it's a list or I handled the string case.
    # We'll print type to debug if it fails again.
    print(f"DEBUG: articles_list type: {type(articles_list)}")
    # If it's a dict (e.g. single result?), wrap in list
    if isinstance(articles_list, dict):
        articles_list = [articles_list]

articles_map = {str(a['article_id']): a for a in articles_list}

# Keywords for Business
keywords = [
    'business', 'economy', 'economic', 'financial', 'finance', 'market', 'stock', 'stocks', 'trade', 'trading',
    'corporate', 'corporation', 'industry', 'industrial', 'profit', 'investment', 'invest', 'investor', 
    'bank', 'banking', 'dollar', 'euro', 'currency', 'revenue', 'merger', 'acquisition', 'fiscal', 
    'tax', 'debt', 'loan', 'credit', 'interest', 'rate', 'rates', 'imf', 'wto', 'treasury', 'ipo', 
    'share', 'shares', 'dividend', 'bond', 'bonds', 'recession', 'inflation', 'capital', 
    'wall street', 'wall st', 'dow', 'nasdaq', 's&p', 'oil', 'crude', 'gasoline', 'energy', 'firm', 'companies', 'company', 'ceo', 'cfo',
    'retail', 'sales', 'deal', 'deals', 'audit', 'budget'
]

def is_business(text):
    text = text.lower()
    for kw in keywords:
        if kw in text:
            return True
    return False

counts = {year: 0 for year in range(2010, 2021)}

for item in metadata_list:
    aid = str(item.get('article_id'))
    date_str = item.get('publication_date')
    
    if aid in articles_map and date_str:
        try:
            year = int(date_str.split('-')[0])
        except:
            continue
            
        if 2010 <= year <= 2020:
            art = articles_map[aid]
            content = (art.get('title', '') + " " + art.get('description', ''))
            
            if is_business(content):
                counts[year] += 1

total_business = sum(counts.values())
average = total_business / 11.0

print("__RESULT__:")
print(json.dumps({"counts": counts, "average": average}))"""

env_args = {'var_function-call-9733408424743850930': 'file_storage/function-call-9733408424743850930.json', 'var_function-call-16979807596985196136': 14860, 'var_function-call-1857885893302130095': [{'_id': '6944c3c823e500c020aebf3f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3c823e500c020aebf40', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c3c823e500c020aebf41', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c3c823e500c020aebf42', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c3c823e500c020aebf43', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8535152676187507582': [{'_id': '6944c3c823e500c020aebf3f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c3c823e500c020aebf40', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c3c823e500c020aebf41', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c3c823e500c020aebf42', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c3c823e500c020aebf43', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
