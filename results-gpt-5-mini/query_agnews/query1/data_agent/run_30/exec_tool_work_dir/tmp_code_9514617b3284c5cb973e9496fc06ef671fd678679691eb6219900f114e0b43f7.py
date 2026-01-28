code = """import json
import pandas as pd

data = var_call_ePklPbqaJQ8xEek2XlwlmWFa
# Ensure consistent types
for d in data:
    # Ensure description and title present
    d['title'] = d.get('title', '')
    d['description'] = d.get('description', '')

df = pd.DataFrame(data)

# Define simple sports keyword-based classifier
sports_keywords = {'game','match','season','team','player','score','goal','tournament','league','coach','football','soccer','basketball','baseball','tennis','golf','olympic','hockey','boxing','athletics','cricket','rugby'}

def is_sports_text(t):
    t = (t or '').lower()
    return any(k in t for k in sports_keywords)

# Determine if each article is sports by looking at title and description
df['is_sports'] = df['title'].apply(is_sports_text) | df['description'].apply(is_sports_text)

# Compute description lengths
df['desc_len'] = df['description'].astype(str).apply(len)

sports_df = df[df['is_sports']]

if sports_df.empty:
    result = {"title": None, "message": "No sports articles found"}
else:
    # Article with greatest description length among sports
    idx = sports_df['desc_len'].idxmax()
    title = str(df.at[idx, 'title'])
    result = {"title": title}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ePklPbqaJQ8xEek2XlwlmWFa': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
