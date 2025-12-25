code = """import json
import pandas as pd

# Load metadata
metadata_file = locals()['var_function-call-1557171304419617632']
with open(metadata_file, 'r') as f:
    metadata_data = json.load(f)
df_meta = pd.DataFrame(metadata_data)

# Load articles
articles_file = locals()['var_function-call-5731472771954016204']
with open(articles_file, 'r') as f:
    articles_data = json.load(f)
df_articles = pd.DataFrame(articles_data)

# Ensure ID types match
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Define categorization logic
def get_category(text):
    text = text.lower()
    business_keywords = ['stocks', 'stock', 'market', 'markets', 'economy', 'economic', 'oil', 'price', 'prices', 'business', 'profit', 'profits', 'sales', 'trade', 'dollar', 'euro', 'bank', 'banks', 'invest', 'investment', 'investor', 'rate', 'rates', 'quarter', 'revenue', 'share', 'shares', 'company', 'companies', 'corp', 'inc', 'wall st', 'financial', 'finance', 'growth', 'earnings', 'deal', 'merger', 'acquisition', 'bond', 'yield', 'futures', 'nasdaq', 'dow', 'index', 'fed', 'federal reserve', 'inflation', 'ceo', 'cfo', 'bankrupt', 'bankruptcy', 'sector', 'spending', 'retail', 'consumer', 'job', 'jobs', 'unemployment', 'bid', 'contract', 'cost', 'costs']
    
    sports_keywords = ['sport', 'sports', 'game', 'games', 'cup', 'match', 'score', 'win', 'won', 'loss', 'lost', 'team', 'teams', 'season', 'league', 'player', 'players', 'coach', 'olympic', 'olympics', 'champion', 'championship', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'medal', 'athlete', 'race', 'racing', 'tournament', 'stadium']
    
    scitech_keywords = ['computer', 'computers', 'software', 'technology', 'tech', 'science', 'space', 'nasa', 'web', 'internet', 'google', 'microsoft', 'apple', 'linux', 'virus', 'security', 'chip', 'chips', 'mobile', 'phone', 'phones', 'network', 'online', 'server', 'data', 'satellite', 'orbit', 'moon', 'mars', 'research', 'study', 'scientist', 'browser']
    
    world_keywords = ['president', 'minister', 'iraq', 'war', 'military', 'bomb', 'killed', 'kill', 'police', 'government', 'election', 'official', 'officials', 'country', 'state', 'un', 'united nations', 'eu', 'europe', 'china', 'russia', 'iran', 'israel', 'palestine', 'nuclear', 'blast', 'attack', 'peace', 'treaty', 'talks', 'parliament', 'vote', 'law', 'court', 'judge']
    
    counts = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
    for k in business_keywords: 
        if k in text: counts['Business'] += 1
    for k in sports_keywords: 
        if k in text: counts['Sports'] += 1
    for k in scitech_keywords: 
        if k in text: counts['Sci/Tech'] += 1
    for k in world_keywords: 
        if k in text: counts['World'] += 1
        
    if max(counts.values()) == 0: return 'Other'
    return max(counts, key=counts.get)

df['full_text'] = df['title'] + " " + df['description']
df['category'] = df['full_text'].apply(get_category)

# Filter for Business
df['year'] = pd.to_datetime(df['publication_date']).dt.year
business_articles = df[df['category'] == 'Business']

# Count per year
yearly_counts = business_articles.groupby('year').size()

# Fill missing years
all_years = range(2010, 2021)
yearly_counts = yearly_counts.reindex(all_years, fill_value=0)

# Calculate average
average_per_year = yearly_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "average": average_per_year, 
    "yearly_counts": yearly_counts.to_dict(),
    "merged_count": len(df),
    "business_count": len(business_articles)
}))"""

env_args = {'var_function-call-1557171304419617632': 'file_storage/function-call-1557171304419617632.json', 'var_function-call-4617174131752082327': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7069929063851328032': {'average': 0.0, 'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}}, 'var_function-call-16646869839963219750': {'len_meta': 14860, 'len_articles': 5, 'len_merged': 1, 'sample_titles': ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)'], 'sample_ids': [3]}, 'var_function-call-15799201340390799595': 'file_storage/function-call-15799201340390799595.json', 'var_function-call-11763493102629390558': 127583, 'var_function-call-5731472771954016204': 'file_storage/function-call-5731472771954016204.json'}

exec(code, env_args)
