code = """import json
import re
import os

data_var = locals()['var_function-call-4434163877750070566']

if isinstance(data_var, str) and os.path.exists(data_var):
    with open(data_var, 'r') as f:
        articles = json.load(f)
else:
    articles = data_var

# Define keywords
categories = {
    'Business': ['oil', 'prices', 'stocks', 'market', 'wall st', 'economy', 'business', 'company', 'profit', 'earnings', 'dollar', 'trade', 'bank', 'fed', 'rates', 'corp', 'inc', 'investor', 'sales', 'deal', 'merger', 'dow', 'nasdaq', 'inflation', 'budget', 'finance'],
    'Sci/Tech': ['technology', 'computer', 'software', 'internet', 'web', 'google', 'microsoft', 'space', 'nasa', 'science', 'tech', 'chip', 'virus', 'phone', 'wireless', 'network', 'online', 'digital', 'server', 'satellite', 'apple', 'ibm', 'intel', 'linux', 'browser'],
    'World': ['iraq', 'baghdad', 'president', 'minister', 'palestinian', 'israel', 'gaza', 'iran', 'nuclear', 'bomb', 'troops', 'military', 'government', 'official', 'united nations', 'un', 'war', 'peace', 'election', 'politics', 'afghanistan', 'china', 'russia', 'usa', 'eu', 'darfur', 'sudan', 'korea', 'bush', 'kerry'],
    'Sports': ['sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'olympic', 'medal', 'athlete', 'championship', 'tournament', 'world cup', 'super bowl', 'nba', 'nfl', 'mlb', 'nhl', 'premier league', 'team', 'coach', 'stadium', 'race', 'prix', 'f1', 'nascar', 'cricket', 'rugby', 'wrestling', 'boxing', 'match', 'game', 'score', 'win', 'loss', 'defeat', 'victory', 'player', 'squad', 'club', 'athens', 'games', 'cup', 'league', 'red sox', 'yankees', 'lakers', 'patriots', 'mets', 'bulls', 'pistons', 'spurs', 'heat', 'united', 'city', 'real madrid', 'barcelona']
}

def classify_article(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple word boundary check
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Return the category with max score
    # Prioritize Sports if it has a score > 0 and others are low, or just max.
    
    max_score = 0
    best_cat = "Unclassified"
    
    # Check max
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
            
    return best_cat, max_score

sports_articles = []
for art in articles:
    cat, score = classify_article(art.get('title', ''), art.get('description', ''))
    if cat == 'Sports':
        sports_articles.append(art)

# Find the one with max description length
longest_desc_article = None
max_len = -1

for art in sports_articles:
    desc = art.get('description', '')
    if desc:
        desc_len = len(desc)
        if desc_len > max_len:
            max_len = desc_len
            longest_desc_article = art

print("__RESULT__:")
if longest_desc_article:
    print(json.dumps({
        "total_articles": len(articles),
        "sports_articles_count": len(sports_articles),
        "title": longest_desc_article['title'],
        "description_length": max_len,
        "description": longest_desc_article['description']
    }))
else:
    print(json.dumps({"error": "No sports articles found"}))"""

env_args = {'var_function-call-5509199147272490073': ['articles'], 'var_function-call-5509199147272487546': ['authors', 'article_metadata'], 'var_function-call-4434163877750070566': [{'_id': '69446f5990bc312761c5bf55', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446f5990bc312761c5bf56', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446f5990bc312761c5bf57', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446f5990bc312761c5bf58', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446f5990bc312761c5bf59', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
