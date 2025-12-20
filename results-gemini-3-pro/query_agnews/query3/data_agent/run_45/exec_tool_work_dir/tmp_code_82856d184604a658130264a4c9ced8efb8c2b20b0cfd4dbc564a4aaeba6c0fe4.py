code = """import json
import pandas as pd
import re

# Load metadata
metadata_file = locals()['var_function-call-6625241908070332927']
with open(metadata_file, 'r') as f:
    metadata_list = json.load(f)
df_meta = pd.DataFrame(metadata_list)
df_meta['article_id'] = df_meta['article_id'].astype(int)

# Load articles
articles_file = locals()['var_function-call-3790426654130503154']
with open(articles_file, 'r') as f:
    articles_list = json.load(f)
df_articles = pd.DataFrame(articles_list)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Filter for Business
# Define keywords
business_keywords = [
    'market', 'stock', 'trade', 'profit', 'finance', 'financial', 'economy', 'economic', 
    'bank', 'investment', 'investor', 'dollar', 'euro', 'currency', 'oil', 'price', 
    'company', 'merger', 'acquisition', 'share', 'growth', 'revenue', 'business', 
    'tax', 'job', 'debt', 'loan', 'recession', 'inflation', 'fed', 'ipo', 'wall st', 
    'dow jones', 'nasdaq', 's&p', 'cpi', 'gdp', 'ceo', 'cfo', 'retail', 'sales', 
    'deal', 'bonds', 'treasury', 'yield', 'rate', 'dividend', 'earnings', 'quarter', 
    'analyst', 'forecast', 'sector', 'industry', 'corporat', 'fund', 'capital', 
    'equity', 'commodity', 'futures', 'index', 'exchange', 'valuation', 'asset', 
    'budget', 'deficit', 'surplus', 'spending', 'cut', 'hike', 'billions', 'millions',
    'takeover', 'bid', 'offer', 'bankruptcy', 'audit', 'accounting'
]

# Tech keywords to exclude if ambiguous? 
# Usually tech business (IPO, earnings) is Business. 
# Tech product reviews are Sci/Tech.
# Sports keywords: game, match, cup, league, player, coach, score, win, lose, team.
# World keywords: war, peace, kill, bomb, president, minister, police, court, trial, election (can be business impact though).

# Simple logic: If title or description contains business keywords.
def is_business(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    # Check for presence of business keywords
    for kw in business_keywords:
        # Use regex to match whole words or parts? 
        # Simple substring match might be too aggressive (e.g. "rate" in "create").
        # Let's use word boundaries or just verify spaces.
        # Given the data, let's try simple substring but be careful with short words.
        # "fed" -> " fed ", "fed ", " fed".
        if re.search(r'\b' + re.escape(kw) + r'\b', text):
            return True
    return False

df['is_business'] = df.apply(is_business, axis=1)

# Filter
business_df = df[df['is_business'] == True].copy()

# Extract Year
business_df['year'] = pd.to_datetime(business_df['publication_date']).dt.year

# Filter Year 2010-2020
business_df = business_df[(business_df['year'] >= 2010) & (business_df['year'] <= 2020)]

# Count per year
counts = business_df.groupby('year').size()

# Fill missing years with 0
all_years = range(2010, 2021)
counts = counts.reindex(all_years, fill_value=0)

average_articles = counts.mean()

print("__RESULT__:")
print(json.dumps({
    "counts_per_year": counts.to_dict(),
    "average": average_articles,
    "total_business": len(business_df),
    "total_merged": len(df)
}))"""

env_args = {'var_function-call-6625241908070332927': 'file_storage/function-call-6625241908070332927.json', 'var_function-call-16753801428595803261': 'TOO_MANY', 'var_function-call-6611812941830838374': 14860, 'var_function-call-2647792999411181703': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1579965867563204147': [{'article_id': 3, 'publication_date': '2020-03-04', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}], 'var_function-call-9194869213981365014': {'metadata_count': 14860, 'articles_count': 5, 'articles_preview': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_function-call-3790426654130503154': 'file_storage/function-call-3790426654130503154.json'}

exec(code, env_args)
