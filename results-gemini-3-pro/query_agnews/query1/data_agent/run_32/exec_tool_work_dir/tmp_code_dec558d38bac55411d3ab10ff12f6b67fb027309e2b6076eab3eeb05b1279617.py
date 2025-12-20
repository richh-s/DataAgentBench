code = """import json
import re

# Load data
file_path = locals()['var_function-call-7930120477363260112']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
categories = {
    'Sports': ['sport', 'sports', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'boxing', 'racing', 'olympics', 'olympic', 'medal', 'athlete', 'stadium', 'championship', 'tournament', 'world cup', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'grand slam', 'super bowl', 'games', 'game', 'team', 'coach', 'score', 'cup', 'match', 'league'],
    'Business': ['business', 'economy', 'economic', 'market', 'stock', 'stocks', 'trade', 'investment', 'investor', 'profit', 'revenue', 'bank', 'banking', 'finance', 'financial', 'dollar', 'euro', 'currency', 'inflation', 'fed', 'federal reserve', 'oil', 'price', 'prices', 'company', 'corp', 'inc', 'merger', 'acquisition', 'ceo', 'wall st', 'nasdaq', 'dow jones'],
    'Sci/Tech': ['technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'wireless', 'network', 'google', 'microsoft', 'apple', 'intel', 'linux', 'windows', 'server', 'virus', 'hacker', 'space', 'nasa', 'astronomy', 'biology', 'physics', 'research', 'study', 'scientific', 'processor'],
    'World': ['world', 'international', 'government', 'politics', 'political', 'president', 'minister', 'prime minister', 'election', 'war', 'military', 'army', 'navy', 'peace', 'treaty', 'un', 'united nations', 'security', 'terror', 'terrorism', 'iraq', 'iran', 'china', 'russia', 'usa', 'uk', 'israel', 'palestine', 'europe', 'asia', 'africa', 'latin america', 'official', 'authorities', 'police', 'bomb', 'blast', 'kill', 'attack']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, keywords in categories.items():
        for kw in keywords:
            # Simple substring match or word boundary match.
            # Using regex with word boundaries is safer
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Get max score
    max_score = -1
    best_cat = None
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            # Tie breaking? Maybe ambiguous.
            # If tie between Sports and others, maybe check specific strong keywords.
            pass
            
    return best_cat, max_score, scores

sports_articles = []

for art in articles:
    text = (art.get('title', '') + " " + art.get('description', ''))
    cat, score, scores = classify(text)
    
    # If scores are all 0, it's unclassified.
    if score > 0 and cat == 'Sports':
        sports_articles.append(art)
    elif score > 0 and scores['Sports'] == score: # Tie handling, if Sports is one of the top
         sports_articles.append(art)

# Find longest description
longest_desc_len = -1
best_article = None

for art in sports_articles:
    desc = art.get('description', '')
    if len(desc) > longest_desc_len:
        longest_desc_len = len(desc)
        best_article = art

print("__RESULT__:")
print(json.dumps(best_article))"""

env_args = {'var_function-call-8759093046017392632': ['articles'], 'var_function-call-8759093046017390813': ['authors', 'article_metadata'], 'var_function-call-16077717350409753983': [{'_id': '69447aefbeeefe51a60f0cf3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447aefbeeefe51a60f0cf4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447aefbeeefe51a60f0cf5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447aefbeeefe51a60f0cf6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447aefbeeefe51a60f0cf7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-2782645133135892755': [{'_id': '69447aefbeeefe51a60f0cf3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447aefbeeefe51a60f0cf4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447aefbeeefe51a60f0cf5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447aefbeeefe51a60f0cf6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447aefbeeefe51a60f0cf7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5354562691669940980': [{'_id': '69447aefbeeefe51a60f0cf3', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69447aefbeeefe51a60f0cf4', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69447aefbeeefe51a60f0cf5', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69447aefbeeefe51a60f0cf6', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69447aefbeeefe51a60f0cf7', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7930120477363260112': 'file_storage/function-call-7930120477363260112.json', 'var_function-call-2596779725741786289': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}]}

exec(code, env_args)
