code = """import json
import pandas as pd
import random

file_path = locals()['var_function-call-5860854601306860093']
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)
print(f"Total articles: {len(df)}")

# Re-run classification to see distribution
# (Using the same keywords as before)
keywords = {
    'Business': ['oil', 'price', 'stocks', 'market', 'wall st', 'economy', 'dollar', 'trade', 'profit', 'shares', 'company', 'inc', 'corp', 'bank', 'rate', 'fed', 'ipo', 'inflation', 'invest', 'fund', 'business', 'sales', 'gm', 'ford', 'boeing', 'airways', 'ceo'],
    'Sci/Tech': ['google', 'web', 'software', 'computer', 'technology', 'space', 'nasa', 'internet', 'microsoft', 'virus', 'science', 'study', 'research', 'phone', 'mobile', 'linux', 'apple', 'server', 'chip', 'network', 'spam', 'online', 'digital', 'search engine', 'intel'],
    'World': ['iraq', 'war', 'president', 'government', 'country', 'minister', 'official', 'united nations', 'police', 'kill', 'bomb', 'military', 'blast', 'palestinian', 'israel', 'china', 'russia', 'bush', 'kerry', 'election', 'troops', 'gaza', 'baghdad', 'afghanistan', 'iran', 'nuclear', 'attack', 'force', 'sudan', 'darfur', 'venezuela', 'chavez', 'putin'],
    'Sports': ['olympic', 'medal', 'gold', 'team', 'game', 'win', 'cup', 'soccer', 'football', 'baseball', 'basketball', 'tennis', 'golf', 'athlete', 'champion', 'coach', 'player', 'score', 'victory', 'defeat', 'league', 'athens', 'sox', 'yankees', 'lakers', 'red sox', 'mets', 'bulls', 'knicks', 'rangers', 'race', 'swimming', 'gymnastics', 'marathon', 'silver', 'bronze', 'sports', 'nfl', 'nba', 'mlb', 'nhl', 'fifa']
}

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text: # simple substring check is faster and sometimes sufficient for debug
                 scores[cat] += 1
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return "Unknown"
    return max_cat

df['category'] = df.apply(classify, axis=1)
print(df['category'].value_counts())

# Print some random titles
sample = df.sample(10)['title'].tolist()
print("Random titles:", sample)

result = {
    "total": len(df),
    "counts": df['category'].value_counts().to_dict(),
    "random_titles": sample
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7527779804282538118': ['articles'], 'var_function-call-7527779804282539207': ['authors', 'article_metadata'], 'var_function-call-7980116427146039164': [{'_id': '69446821247247aa632a648a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-7980116427146037227': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-15646640609932424543': [{'_id': '69446821247247aa632a648a', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446821247247aa632a648b', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446821247247aa632a648c', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446821247247aa632a648d', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446821247247aa632a648e', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5860854601306860093': 'file_storage/function-call-5860854601306860093.json', 'var_function-call-2079702809120062311': {'error': 'No sports articles found', 'sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'Stocks End Up, But Near Year Lows (Reuters)', 'Money Funds Fell in Latest Week (AP)', 'Fed minutes show dissent over inflation (USATODAY.com)', 'Safety Net (Forbes.com)', 'Wall St. Bears Claw Back Into the Black']}}

exec(code, env_args)
