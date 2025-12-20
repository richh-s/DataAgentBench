code = """import json
import pandas as pd

# Load the articles
with open(locals()['var_function-call-4127698444615500778'], 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)
df['desc_len'] = df['description'].apply(lambda x: len(x) if x else 0)
df = df.sort_values('desc_len', ascending=False)

# Keywords
sports_keywords = ['olympic', 'medal', 'athens', 'team', 'game', 'cup', 'champion', 'league', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'hockey', 'sport', 'athlete', 'coach', 'tournament', 'match', 'win', 'score', 'nba', 'nfl', 'mlb', 'sox', 'yankees', 'lakers', 'paralympic', 'gold', 'silver', 'bronze', 'marathon', 'sprint', 'relay', 'swim', 'gymnast']

def is_sports(text):
    text = text.lower()
    score = 0
    matched = []
    for k in sports_keywords:
        if k in text:
            score += 1
            matched.append(k)
    return score, matched

candidates = []
for index, row in df.head(100).iterrows():
    title = row['title']
    desc = row['description']
    score, matched = is_sports(title + " " + desc)
    # Filter out weak matches if needed, but let's just inspect
    # "win" is a weak keyword, "score" can be business score. 
    # Let's require at least one strong keyword or score > 1 if using weak ones.
    # But for now, just list them.
    if score > 0:
        candidates.append({
            "title": title,
            "desc_len": row['desc_len'],
            "sports_score": score,
            "matched_keywords": matched,
            "description": desc
        })

print("__RESULT__:")
print(json.dumps(candidates[:10]))"""

env_args = {'var_function-call-6848399961709643430': [{'_id': '694466c40a1d7d23d2c60341', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694466c40a1d7d23d2c60342', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694466c40a1d7d23d2c60343', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694466c40a1d7d23d2c60344', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694466c40a1d7d23d2c60345', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16994264649481179618': [{'_id': '694466c40a1d7d23d2c60341', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694466c40a1d7d23d2c60342', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694466c40a1d7d23d2c60343', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694466c40a1d7d23d2c60344', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694466c40a1d7d23d2c60345', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3110163578011665506': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5651821707244129446': [{'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'desc_len': 214, 'sports_score': 0, 'matched_keywords': [], 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'desc_len': 195, 'sports_score': 0, 'matched_keywords': [], 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'desc_len': 184, 'sports_score': 0, 'matched_keywords': [], 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'desc_len': 160, 'sports_score': 0, 'matched_keywords': [], 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'desc_len': 94, 'sports_score': 1, 'matched_keywords': ['win'], 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-4127698444615500778': 'file_storage/function-call-4127698444615500778.json'}

exec(code, env_args)
