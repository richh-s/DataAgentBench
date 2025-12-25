code = """import json
import os

# Load articles
data_source = locals().get('var_function-call-5447638827878201766')

if isinstance(data_source, str) and os.path.exists(data_source):
    with open(data_source, 'r') as f:
        articles = json.load(f)
else:
    articles = []

# Keywords
categories = {
    'Sports': ['sport', 'sports', 'olympic', 'olympics', 'athens', 'medal', 'gold', 'silver', 'bronze', 'basketball', 'nba', 'football', 'nfl', 'soccer', 'fifa', 'baseball', 'mlb', 'hockey', 'nhl', 'tennis', 'atp', 'wta', 'golf', 'pga', 'racing', 'f1', 'nascar', 'cricket', 'rugby', 'boxing', 'wrestling', 'athlete', 'champion', 'championship', 'tournament', 'cup', 'league', 'team', 'coach', 'squad', 'player', 'game', 'match', 'score', 'win', 'lose', 'defeat', 'victory', 'record', 'title', 'semi-final', 'final', 'quarter-final', 'playoff', 'stadium', 'field', 'court', 'swimming', 'swim', 'gymnastics', 'track', 'marathon', 'sprint', 'doping'],
    'World': ['world', 'international', 'iraq', 'baghdad', 'president', 'bush', 'kerry', 'election', 'war', 'military', 'soldier', 'troop', 'bomb', 'attack', 'kill', 'dead', 'died', 'palestine', 'palestinian', 'israel', 'gaza', 'jerusalem', 'iran', 'nuclear', 'korea', 'china', 'russia', 'putin', 'darfur', 'sudan', 'un', 'united nations', 'treaty', 'minister', 'official', 'government', 'police', 'law', 'terror', 'blast', 'explosion', 'hurricane', 'storm', 'quake', 'crash'],
    'Business': ['business', 'economy', 'market', 'stock', 'share', 'wall', 'street', 'price', 'oil', 'gas', 'profit', 'revenue', 'deal', 'merger', 'buy', 'sell', 'trade', 'invest', 'bank', 'rate', 'dollar', 'company', 'corp', 'inc', 'ceo'],
    'Sci/Tech': ['technology', 'tech', 'science', 'computer', 'software', 'internet', 'web', 'online', 'google', 'microsoft', 'windows', 'linux', 'apple', 'chip', 'network', 'wireless', 'mobile', 'phone', 'virus', 'space', 'nasa', 'research', 'game', 'video', 'code', 'java', 'programming', 'developer', 'source', 'xml', 'database']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for k in keywords:
            if (' ' + k + ' ') in (' ' + text + ' '):
                scores[cat] += 1
            elif len(k) > 4 and k in text:
                 scores[cat] += 0.5 
    
    # Tie breaking: if Tech and Sports have equal score, prefer Tech if 'game' is the keyword
    # Actually, let's just use max
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown'
    return best_cat, scores

candidates = []
for a in articles:
    content = (a.get('title', '') + " " + a.get('description', '')).replace(chr(92), ' ')
    cat, scores = classify(content)
    # Store if Sports is the winner or close runner up? No, strict winner.
    # But print scores for debugging
    if cat == 'Sports':
        candidates.append({'article': a, 'scores': scores})

# Sort by description length
candidates.sort(key=lambda x: len(x['article'].get('description', '')), reverse=True)

# Take top 5
top_5 = candidates[:5]
result = []
for c in top_5:
    result.append({
        "title": c['article']['title'],
        "desc_len": len(c['article']['description']),
        "scores": c['scores'],
        "description_preview": c['article']['description'][:100]
    })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7029763466398930127': ['articles'], 'var_function-call-7029763466398929618': ['authors', 'article_metadata'], 'var_function-call-13427181582861214587': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4924959999504549548': {'title': 'No sports articles found', 'length': 0, 'count_sports': 0, 'total': 5}, 'var_function-call-17796284112926141359': [{'_id': '6944879a9fca835ad33c545b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944879a9fca835ad33c545c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944879a9fca835ad33c545d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944879a9fca835ad33c545e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944879a9fca835ad33c545f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5447638827878201766': 'file_storage/function-call-5447638827878201766.json', 'var_function-call-348266895830844216': {'title': 'Pretty Log4J', 'length': 708, 'count_sports': 5379, 'total': 20000, 'description_preview': "\\\\I've been a big fan of Log4J  for a while now but haven't migrated any code\\over for one central r"}}

exec(code, env_args)
