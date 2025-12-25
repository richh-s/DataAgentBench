code = """import json
import pandas as pd
import re

# Load SQL result (Metadata)
with open(locals()['var_function-call-3374216410515213481'], 'r') as f:
    meta_data = json.load(f)
meta_df = pd.DataFrame(meta_data)
meta_df['article_id'] = meta_df['article_id'].astype(str)
meta_df['year'] = meta_df['publication_date'].apply(lambda x: int(x[:4]))

# Load Mongo result (Articles)
mongo_res_key = 'var_function-call-9702471243371213876'
# It's a file path
with open(locals()[mongo_res_key], 'r') as f:
    articles_data = json.load(f)
articles_df = pd.DataFrame(articles_data)
articles_df['article_id'] = articles_df['article_id'].astype(str)

# Merge
# Inner join because we only care about the articles in the metadata (Europe 2010-2020)
merged_df = pd.merge(meta_df, articles_df, on='article_id', how='inner')

print(f"Merged Count: {len(merged_df)}")

# Classification Logic
categories = {
    'Business': ['business', 'economy', 'market', 'stock', 'trade', 'finance', 'financial', 'corporate', 'company', 'companies', 'profit', 'revenue', 'merger', 'acquisition', 'bank', 'banking', 'inflation', 'currency', 'dollar', 'euro', 'investor', 'investment', 'sales', 'deal', 'oil', 'price', 'rates', 'fed', 'growth', 'debt', 'fiscal', 'bond', 'fund', 'industry', 'sector', 'ceo'],
    'Sci/Tech': ['technology', 'science', 'computer', 'internet', 'software', 'hardware', 'web', 'online', 'google', 'microsoft', 'apple', 'space', 'nasa', 'mobile', 'phone', 'network', 'digital', 'data', 'virus', 'research', 'study', 'chip', 'satellite', 'linux', 'biotech', 'robot', 'gadget'],
    'Sports': ['sport', 'sports', 'game', 'match', 'team', 'player', 'win', 'won', 'loss', 'lost', 'score', 'cup', 'league', 'championship', 'champion', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'coach', 'tournament', 'medal', 'athlete', 'stadium'],
    'World': ['world', 'international', 'president', 'minister', 'government', 'war', 'peace', 'military', 'army', 'politics', 'political', 'election', 'official', 'country', 'state', 'united nations', 'un', 'iraq', 'iran', 'china', 'russia', 'eu', 'treaty', 'nuclear', 'bomb', 'attack', 'police', 'security', 'crisis', 'conflict']
}

def classify(row):
    text = (row['title'] + " " + row['description']).lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple substring match? Or word boundary?
            # Simple substring might match "business" in "businessman" (ok)
            # "win" in "winter" (bad).
            # Let's use word boundary regular expression for better accuracy?
            # Or just simple ' in ' check for speed/simplicity.
            # Given the text is news, words are usually distinct.
            # Let's count occurrences.
            scores[cat] += text.count(kw)
    
    # Return category with max score
    # If all 0, default to something? Or maybe "World" as generic?
    # Or keep as "Unknown".
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'World' # Default fallback
    return best_cat

merged_df['category'] = merged_df.apply(classify, axis=1)

# Filter for Business
business_df = merged_df[merged_df['category'] == 'Business']

# Group by Year
counts = business_df.groupby('year').size()

# Fill missing years with 0
all_years = range(2010, 2021) # 2010 to 2020 inclusive
final_counts = []
for y in all_years:
    c = counts.get(y, 0)
    final_counts.append(c)

# Calculate Average
average = sum(final_counts) / len(final_counts)

print("__RESULT__:")
print(json.dumps({
    "merged_count": len(merged_df),
    "business_count": len(business_df),
    "counts_per_year": {y: c for y, c in zip(all_years, final_counts)},
    "average": average
}))"""

env_args = {'var_function-call-3374216410515213481': 'file_storage/function-call-3374216410515213481.json', 'var_function-call-12759151671204922172': {'count': 14860, 'sample_ids': ['3', '9', '13', '14', '21']}, 'var_function-call-7294554086190964966': [{'_id': '6944e3aa8c0a78c2c4426de9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e3aa8c0a78c2c4426dea', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e3aa8c0a78c2c4426deb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e3aa8c0a78c2c4426dec', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e3aa8c0a78c2c4426ded', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9133333367317080493': [{'_id': '6944e3aa8c0a78c2c4426de9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e3aa8c0a78c2c4426dea', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e3aa8c0a78c2c4426deb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e3aa8c0a78c2c4426dec', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e3aa8c0a78c2c4426ded', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9103702986714134022': 'Done', 'var_function-call-9717317479383567751': {'type': "<class 'list'>", 'is_file': False, 'count': 5}, 'var_function-call-2426896890545291028': {'max_id': 127583, 'min_id': 3, 'count': 14860}, 'var_function-call-9702471243371213876': 'file_storage/function-call-9702471243371213876.json'}

exec(code, env_args)
