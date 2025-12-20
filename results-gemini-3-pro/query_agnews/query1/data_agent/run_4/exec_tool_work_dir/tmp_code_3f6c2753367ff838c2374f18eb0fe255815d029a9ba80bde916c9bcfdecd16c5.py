code = """import json
import os
import re

# Access the data
data_key = 'var_function-call-5264877127341526861'
file_path = locals().get(data_key)

if not file_path or not os.path.exists(file_path):
    print("__RESULT__:")
    print(json.dumps("Error: File not found."))
else:
    with open(file_path, 'r') as f:
        articles = json.load(f)

    # Keywords
    categories = {
        'Business': ['market', 'stock', 'price', 'company', 'corp', 'inc', 'ltd', 'share', 'profit', 'loss', 'quarter', 'revenue', 'economy', 'bank', 'deal', 'merger', 'acquisition', 'dollar', 'euro', 'oil', 'gas', 'trade', 'business', 'industry', 'ceo', 'cfo', 'executive', 'dow jones', 'nasdaq', 'investor', 'sales', 'fed', 'rates', 'deficit', 'inflation'],
        'Sci/Tech': ['computer', 'software', 'hardware', 'internet', 'web', 'online', 'technology', 'tech', 'science', 'space', 'nasa', 'satellite', 'microsoft', 'google', 'intel', 'linux', 'virus', 'spam', 'hacker', 'phone', 'mobile', 'wireless', 'network', 'broadband', 'chip', 'processor', 'search engine', 'apple', 'ibm', 'server', 'game', 'video game', 'research', 'drug', 'study'],
        'World': ['president', 'minister', 'prime minister', 'official', 'government', 'police', 'military', 'army', 'troops', 'war', 'peace', 'attack', 'bomb', 'blast', 'killed', 'injured', 'dead', 'iraq', 'iran', 'palestine', 'israel', 'afghanistan', 'united nations', 'un', 'eu', 'treaty', 'election', 'vote', 'poll', 'politics', 'china', 'russia', 'darfur', 'sudan', 'gaza', 'baghdad', 'korea', 'nuclear'],
        'Sports': ['olympics', 'olympic', 'gold', 'medal', 'athens', 'swimming', 'gymnastics', 'basketball', 'football', 'soccer', 'baseball', 'red sox', 'yankees', 'nba', 'nfl', 'nhl', 'tournament', 'championship', 'world cup', 'athlete', 'coach', 'sport', 'game', 'match', 'score', 'victory', 'defeat', 'cup', 'team', 'league', 'squad', 'racing', 'driver', 'formula one', 'f1', 'tennis', 'golf', 'tiger woods', 'boxing', 'cricket', 'rugby', 'hockey', 'sox', 'mets', 'dodgers', 'lakers', 'spurs', 'pistons', 'patriots', 'eagles', 'united', 'real madrid', 'arsenal', 'chelsea', 'milan', 'juventus', 'doping', 'marathon']
    }

    def classify(title, desc):
        text = (title + " " + desc).lower()
        scores = {cat: 0 for cat in categories}
        tokens = re.findall(r'\w+', text)
        
        for cat, keywords in categories.items():
            for kw in keywords:
                if kw in tokens:
                    scores[cat] += 1
        
        # Adjustments
        if 'oil' in tokens: scores['Business'] += 2
        if 'iraq' in tokens: scores['World'] += 2
        if 'olympics' in tokens or 'olympic' in tokens or 'athens' in tokens: scores['Sports'] += 3
        if 'google' in tokens: scores['Sci/Tech'] += 2
        if 'game' in tokens and 'video' not in tokens: scores['Sports'] += 1
        if 'game' in tokens and 'video' in tokens: scores['Sci/Tech'] += 2
        
        max_cat = max(scores, key=scores.get)
        if scores[max_cat] == 0:
            return "Unknown"
        return max_cat

    sports_articles = []
    for art in articles:
        cat = classify(art.get('title', ''), art.get('description', ''))
        if cat == 'Sports':
            sports_articles.append(art)
    
    # Sort by description length descending
    sports_articles.sort(key=lambda x: len(x.get('description', '')), reverse=True)
    
    result = {
        "total_articles": len(articles),
        "sports_count": len(sports_articles),
        "top_sports_article": sports_articles[0] if sports_articles else None
    }
    
    print("__RESULT__:")
    print(json.dumps(result))"""

env_args = {'var_function-call-16303435935020228874': ['articles'], 'var_function-call-16303435935020230519': ['authors', 'article_metadata'], 'var_function-call-11932383749502743792': [{'_id': '69446602bc717173969e3f7b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-11932383749502745537': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-17726508914481105227': [{'_id': '69446602bc717173969e3f7b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446602bc717173969e3f7c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446602bc717173969e3f7d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446602bc717173969e3f7e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446602bc717173969e3f7f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11472611331630481807': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11703216715718506924': 'No sports articles found.', 'var_function-call-5264877127341526861': 'file_storage/function-call-5264877127341526861.json'}

exec(code, env_args)
