code = """import json
import pandas as pd
import re

# Load the data
data_var = locals()['var_function-call-17765770427402153169']
if isinstance(data_var, str):
    with open(data_var, 'r') as f:
        articles = json.load(f)
else:
    articles = data_var

df = pd.DataFrame(articles)

# Keywords
strong_sports_keywords = {
    'olympic', 'olympics', 'athens', 'medal', 'gold medal', 'silver medal', 'bronze medal', 
    'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'super bowl', 'world series', 'stanley cup', 
    'nascar', 'f1', 'formula one', 'pga', 'lpga', 'world cup', 'premier league', 'champions league', 
    'quarterback', 'touchdown', 'homerun', 'slam dunk', 'hat-trick', 'sprint', 'marathon', 
    'tour de france', 'lance armstrong', 'michael phelps', 'ian thorpe', 'tiger woods', 
    'roger federer', 'serena williams', 'venus williams', 'maria sharapova', 'michael schumacher',
    'red sox', 'yankees', 'lakers', 'pistons', 'patriots', 'eagles', 'real madrid', 'manchester united', 'arsenal',
    'chelsea', 'barcelona', 'ac milan', 'juventus', 'inter milan', 'bayern munich', 'liverpool',
    'doping', 'drug test', 'athlete', 'athletics'
}

medium_sports_keywords = {
    'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'golf', 'hockey', 'boxing', 
    'racing', 'cricket', 'rugby', 'volleyball', 'badminton', 'swimming', 'gymnastics',
    'championship', 'tournament', 'league', 'cup', 'match', 'score', 'coach', 'referee', 'umpire'
}

def calculate_sports_score(text):
    text_lower = text.lower()
    score = 0
    # Check strong keywords
    for k in strong_sports_keywords:
        if k in text_lower:
            score += 5
    # Check medium keywords
    for k in medium_sports_keywords:
        # Avoid matching partial words like "cup" in "hiccup" or "occupation" (though "cup" is short)
        # Use regex for short words
        if len(k) <= 4:
            if re.search(r'\b' + re.escape(k) + r'\b', text_lower):
                score += 2
        else:
            if k in text_lower:
                score += 2
    return score

df['full_text'] = df['title'].astype(str) + " " + df['description'].astype(str)
df['sports_score'] = df['full_text'].apply(calculate_sports_score)
df['desc_len'] = df['description'].astype(str).apply(len)

# Filter for probable sports articles (score >= 2 to be safe, e.g. one medium keyword)
sports_candidates = df[df['sports_score'] >= 2].copy()

# Sort by description length descending
top_candidates = sports_candidates.sort_values(by='desc_len', ascending=False).head(5)

result = top_candidates[['title', 'description', 'desc_len', 'sports_score']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-9486180232665500453': ['articles'], 'var_function-call-9486180232665501096': ['authors', 'article_metadata'], 'var_function-call-14264674136081503679': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-14264674136081505188': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-6725456994874746152': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944762b1d6282a841d85ada', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944762b1d6282a841d85adb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944762b1d6282a841d85adc', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944762b1d6282a841d85add', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15686240030509850180': [{'_id': '6944762b1d6282a841d85ad9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944762b1d6282a841d85ada', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944762b1d6282a841d85adb', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944762b1d6282a841d85adc', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944762b1d6282a841d85add', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3132922975050485119': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again.", 'sports_score': 1, 'desc_len': 94}], 'var_function-call-17765770427402153169': 'file_storage/function-call-17765770427402153169.json'}

exec(code, env_args)
