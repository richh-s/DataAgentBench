code = """import json
import pandas as pd
import re

# Load the articles
try:
    with open('var_function-call-12865582274226652090.json', 'r') as f:
        articles = json.load(f)
except FileNotFoundError:
    # Fallback for testing if file doesn't exist in this environment mockup
    articles = [] 

df = pd.DataFrame(articles)

# Keywords
keywords = {
    'Sports': [
        'sport', 'sports', 'game', 'games', 'team', 'teams', 'match', 'matches', 'cup', 'win', 'wins', 'winning', 'won', 'winner', 
        'lose', 'lost', 'loss', 'score', 'scored', 'scores', 'player', 'players', 'coach', 'coaches', 
        'olympic', 'olympics', 'medal', 'medals', 'gold', 'silver', 'bronze', 'champion', 'champions', 'championship', 
        'league', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf', 'hockey', 'racing', 'athlete', 'athletes',
        'f1', 'nascar', 'athens', 'greece', 'relay', 'swimming', 'swimmer', 'gymnastics', 'gymnast', 
        'stadium', 'tournament', 'wimbledon', 'open', 'grand slam', 'tour de france', 'nfl', 'nba', 'mlb', 'nhl', 
        'fifa', 'uefa', 'club', 'united', 'arsenal', 'chelsea', 'liverpool', 'manchester', 'red sox', 'yankees', 
        'lakers', 'bulls', 'knicks', 'cowboys', 'patriouts', 'giants', 'mets', 'rangers', 'flyers', 'bruins', 
        'penguins', 'tigers', 'lions', 'bears', 'packers', 'vikings', 'dolphins', 'heat', 'magic', 'suns', 'spurs',
        'mavericks', 'rockets', 'astros', 'cardinals', 'braves', 'phillies', 'nationals', 'capitals', 'wizards',
        'quarterback', 'pitcher', 'batter', 'goal', 'touchdown', 'homerun', 'basket', 'points', 'set', 'match point'
    ],
    'Business': [
        'market', 'markets', 'stock', 'stocks', 'price', 'prices', 'company', 'companies', 'corp', 'corporation', 'inc', 
        'profit', 'profits', 'loss', 'losses', 'quarter', 'earnings', 'oil', 'crude', 'economy', 'economic', 'bank', 'banks', 
        'trade', 'trading', 'dollar', 'euro', 'currency', 'business', 'industry', 'ceo', 'cfo', 'sales', 'revenue', 'invest', 
        'investment', 'investor', 'investors', 'share', 'shares', 'wall st', 'wall street', 'dow', 'nasdaq', 's&p', 'fed', 
        'federal reserve', 'inflation', 'rates', 'interest', 'deal', 'merger', 'acquisition', 'ipo', 'audit', 'accounting'
    ],
    'Sci/Tech': [
        'computer', 'computers', 'software', 'hardware', 'technology', 'tech', 'internet', 'web', 'online', 'digital', 
        'google', 'microsoft', 'apple', 'intel', 'ibm', 'oracle', 'linux', 'windows', 'browser', 'search engine', 
        'space', 'nasa', 'science', 'scientist', 'scientists', 'research', 'study', 'phone', 'mobile', 'wireless', 
        'chip', 'processor', 'virus', 'worm', 'security', 'hacker', 'spam', 'email', 'satellite', 'orbit', 'mars', 'moon',
        'biology', 'physics', 'chemistry', 'genetics', 'genome', 'stem cell', 'cloning', 'robot', 'robotics'
    ],
    'World': [
        'iraq', 'iraqi', 'war', 'wars', 'president', 'bush', 'kerry', 'minister', 'government', 'country', 'nation', 
        'police', 'military', 'army', 'soldier', 'soldiers', 'kill', 'killed', 'killing', 'bomb', 'bombing', 'blast', 
        'peace', 'treaty', 'election', 'elections', 'vote', 'voters', 'un', 'united nations', 'official', 'officials', 
        'gaza', 'israel', 'israeli', 'palestine', 'palestinian', 'iran', 'iranian', 'nuclear', 'weapon', 'weapons', 
        'terror', 'terrorism', 'terrorist', 'qaeda', 'attack', 'attacks', 'baghdad', 'kabul', 'afghanistan', 'darfur', 
        'sudan', 'russia', 'russian', 'china', 'chinese', 'japan', 'japanese', 'korea', 'korean', 'uk', 'britain', 
        'germany', 'france', 'french', 'eu', 'europe', 'european'
    ]
}

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    words_in_text = text.split()
    
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for keyword in words:
            # Check for word boundary or just containment? 
            # Containment is safer for variations, but can have false positives (e.g. "port" in "sports")
            # But I'm checking if keyword is in text. 
            # Better to check word matches.
            if keyword in words_in_text:
                scores[cat] += 1
            elif keyword in text: # Fallback for multi-word keywords like "wall street"
                 scores[cat] += 1
    
    # Adjust scores based on specific exclusions or weights if needed
    # e.g. "oil" is strong indicator for Business/World.
    
    # Return category with max score
    # If tie, prioritize Sports if it has a score > 0
    m = max(scores.values())
    if m == 0:
        return "Unknown"
    
    # Get all with max score
    candidates = [k for k, v in scores.items() if v == m]
    if len(candidates) == 1:
        return candidates[0]
    else:
        # Tie breaker: prioritize Sports > World > Business > Sci/Tech?
        # Actually, "game" can be in Sci/Tech. "win" in Business.
        # Let's check context. 
        # For now, just return the first one in the list order.
        return candidates[0]

df['category'] = df.apply(classify, axis=1)

# Filter for Sports
sports_df = df[df['category'] == 'Sports'].copy()

result_info = {}
if len(sports_df) > 0:
    # Calculate description length
    sports_df['desc_len'] = sports_df['description'].astype(str).str.len()
    
    # Sort by length desc
    sports_df = sports_df.sort_values('desc_len', ascending=False)
    
    # Get top 5 to inspect (in case the top one is ambiguous)
    top_5 = sports_df[['title', 'description', 'desc_len']].head(5).to_dict(orient='records')
    result_info['top_5_sports'] = top_5
    result_info['count'] = len(sports_df)
else:
    result_info['error'] = "No sports articles found"

print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_function-call-7032265624609699214': ['articles'], 'var_function-call-7032265624609701055': ['authors', 'article_metadata'], 'var_function-call-1088229014867811489': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1286037897333998160': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-14093300406947084892': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6219379591243311347': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17044733738529564342': {'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'desc_len': 94, 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'var_function-call-12865582274226652090': 'file_storage/function-call-12865582274226652090.json'}

exec(code, env_args)
