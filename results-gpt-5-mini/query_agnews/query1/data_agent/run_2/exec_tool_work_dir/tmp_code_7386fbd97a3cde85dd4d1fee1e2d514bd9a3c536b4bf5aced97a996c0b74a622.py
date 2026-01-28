code = """import json
import pandas as pd
# Accessing the query result stored in var_call_chO1ZamZcp4jty5yGnOIG9Lk
records = var_call_chO1ZamZcp4jty5yGnOIG9Lk

df = pd.DataFrame(records)
# Ensure description is string
df['description'] = df['description'].astype(str)
# Compute description length
df['desc_len'] = df['description'].str.len()

# Simple keyword-based categorization
sports_keywords = ['game','season','team','score','player','players','match','tournament','football','soccer','baseball','basketball','hockey','golf','tennis','olympic','athlete','coach','league','cup','goal','win','wins','defeat','victory','race']

def categorize(row):
    text = (row['title'] + ' ' + row['description']).lower()
    for kw in sports_keywords:
        if kw in text:
            return 'Sports'
    # Fallback heuristics
    if any(x in text for x in ['reuters','afp','oil','stocks','economy','investment','carlyle','wall st','iraq']):
        # classify based on presence
        if 'oil' in text or 'iraq' in text:
            return 'World'
        return 'Business'
    return 'World'

df['category'] = df.apply(categorize, axis=1)

# Filter sports articles
sports_df = df[df['category']=='Sports']

if not sports_df.empty:
    # find the sports article with max description length
    top = sports_df.loc[sports_df['desc_len'].idxmax()]
    top_title = top['title']
else:
    top_title = None

output = {
    'sports_articles': sports_df[['article_id','title','desc_len']].to_dict(orient='records'),
    'top_sports_title': top_title
}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_chO1ZamZcp4jty5yGnOIG9Lk': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
