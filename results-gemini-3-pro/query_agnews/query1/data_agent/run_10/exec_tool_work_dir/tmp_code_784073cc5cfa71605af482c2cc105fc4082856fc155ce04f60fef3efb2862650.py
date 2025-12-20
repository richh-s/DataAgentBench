code = """import json
import pandas as pd

# Load the articles
try:
    articles = locals()['var_function-call-6219379591243311347']
except KeyError:
    # If passed as file path
    with open('var_function-call-6219379591243311347.json', 'r') as f:
        articles = json.load(f)

df = pd.DataFrame(articles)
print(f"Total articles: {len(df)}")

# Define keywords
keywords = {
    'Sports': ['sport', 'game', 'team', 'match', 'cup', 'win', 'loss', 'score', 'player', 'coach', 'olympic', 'medal', 'champion', 'league', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf', 'hockey', 'racing', 'athlete', 'f1', 'nascar', 'athens', 'greece', 'relay', 'swimming', 'gymnastics'],
    'Business': ['market', 'stock', 'price', 'company', 'corp', 'inc', 'profit', 'quarter', 'oil', 'economy', 'bank', 'trade', 'dollar', 'business', 'industry', 'ceo', 'sales', 'invest'],
    'Sci/Tech': ['computer', 'software', 'technology', 'internet', 'web', 'google', 'microsoft', 'apple', 'space', 'nasa', 'science', 'research', 'phone', 'mobile', 'chip', 'virus', 'linux', 'online'],
    'World': ['iraq', 'war', 'president', 'minister', 'government', 'country', 'police', 'kill', 'bomb', 'peace', 'election', 'un', 'official', 'gaza', 'israel', 'palestin', 'iran', 'nuclear']
}

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    
    # If there is a tie or all 0, default to something or mark as unknown?
    # Usually max score is enough.
    return max(scores, key=scores.get)

df['category'] = df.apply(classify, axis=1)

# Filter for Sports
sports_df = df[df['category'] == 'Sports'].copy()
print(f"Sports articles found: {len(sports_df)}")

if len(sports_df) > 0:
    # Calculate description length
    sports_df['desc_len'] = sports_df['description'].str.len()
    
    # Sort by length desc
    sports_df = sports_df.sort_values('desc_len', ascending=False)
    
    # Get top one
    top_article = sports_df.iloc[0]
    result = {
        "title": top_article['title'],
        "desc_len": int(top_article['desc_len']),
        "description": top_article['description'] # for verification
    }
else:
    result = "No sports articles found."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7032265624609699214': ['articles'], 'var_function-call-7032265624609701055': ['authors', 'article_metadata'], 'var_function-call-1088229014867811489': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1286037897333998160': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-14093300406947084892': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6219379591243311347': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
