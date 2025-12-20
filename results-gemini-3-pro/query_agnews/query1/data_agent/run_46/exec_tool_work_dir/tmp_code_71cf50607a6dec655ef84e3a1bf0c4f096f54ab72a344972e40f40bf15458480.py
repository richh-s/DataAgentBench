code = """import json
import os

# Load articles
data_source = locals().get('var_function-call-13427181582861214587')

if isinstance(data_source, str) and os.path.exists(data_source):
    with open(data_source, 'r') as f:
        articles = json.load(f)
elif isinstance(data_source, list):
    articles = data_source
else:
    articles = []

# Keywords
categories = {
    'Sports': ['sport', 'sports', 'olympic', 'olympics', 'athens', 'medal', 'gold', 'silver', 'bronze', 'basketball', 'nba', 'football', 'nfl', 'soccer', 'fifa', 'baseball', 'mlb', 'hockey', 'nhl', 'tennis', 'atp', 'wta', 'golf', 'pga', 'racing', 'f1', 'nascar', 'cricket', 'rugby', 'boxing', 'wrestling', 'athlete', 'champion', 'championship', 'tournament', 'cup', 'league', 'team', 'coach', 'squad', 'player', 'game', 'match', 'score', 'win', 'lose', 'defeat', 'victory', 'record', 'title', 'semi-final', 'final', 'quarter-final', 'playoff', 'stadium', 'field', 'court', 'swimming', 'swim', 'gymnastics', 'track', 'marathon', 'sprint'],
    'World': ['world', 'international', 'iraq', 'baghdad', 'president', 'bush', 'kerry', 'election', 'war', 'military', 'soldier', 'troop', 'bomb', 'attack', 'kill', 'dead', 'died', 'palestine', 'palestinian', 'israel', 'gaza', 'jerusalem', 'iran', 'nuclear', 'korea', 'china', 'russia', 'putin', 'darfur', 'sudan', 'un', 'united nations', 'treaty', 'minister', 'official', 'government', 'police', 'law', 'terror', 'blast', 'explosion', 'hurricane', 'storm', 'quake', 'crash'],
    'Business': ['business', 'economy', 'market', 'stock', 'share', 'wall', 'street', 'price', 'oil', 'gas', 'profit', 'revenue', 'deal', 'merger', 'buy', 'sell', 'trade', 'invest', 'bank', 'rate', 'dollar', 'company', 'corp', 'inc', 'ceo'],
    'Sci/Tech': ['technology', 'tech', 'science', 'computer', 'software', 'internet', 'web', 'online', 'google', 'microsoft', 'windows', 'linux', 'apple', 'chip', 'network', 'wireless', 'mobile', 'phone', 'virus', 'space', 'nasa', 'research', 'game', 'video']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for k in keywords:
            # Check for word boundary approximately
            # Adding spaces around text and keyword
            if (' ' + k + ' ') in (' ' + text + ' '):
                scores[cat] += 1
            # Also simple check if k is long enough to be unique
            elif len(k) > 4 and k in text:
                 scores[cat] += 0.5 
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown'
    return best_cat

sports_articles = []
for a in articles:
    # Combine title and description
    # Use chr(92) for backslash to avoid escape issues in tool call
    content = (a.get('title', '') + " " + a.get('description', '')).replace(chr(92), ' ')
    cat = classify(content)
    if cat == 'Sports':
        sports_articles.append(a)

if sports_articles:
    longest_sports_article = max(sports_articles, key=lambda x: len(x.get('description', '')))
    result_title = longest_sports_article.get('title')
    result_desc_len = len(longest_sports_article.get('description', ''))
else:
    result_title = "No sports articles found"
    result_desc_len = 0

print("__RESULT__:")
print(json.dumps({"title": result_title, "length": result_desc_len, "count_sports": len(sports_articles), "total": len(articles)}))"""

env_args = {'var_function-call-7029763466398930127': ['articles'], 'var_function-call-7029763466398929618': ['authors', 'article_metadata'], 'var_function-call-13427181582861214587': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
