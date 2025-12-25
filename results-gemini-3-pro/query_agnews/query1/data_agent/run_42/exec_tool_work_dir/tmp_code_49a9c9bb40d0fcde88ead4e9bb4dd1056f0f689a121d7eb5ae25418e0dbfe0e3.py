code = """import json
import re

file_path = locals()['var_function-call-14251754240139237620']

with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
keywords = {
    'Business': ['oil', 'price', 'stock', 'economy', 'wall st', 'market', 'company', 'profit', 'dollar', 'bank', 'trade', 'business', 'ipo', 'fed', 'inflation', 'investor', 'sales', 'corp', 'inc'],
    'Sci/Tech': ['computer', 'software', 'technology', 'internet', 'microsoft', 'google', 'intel', 'space', 'nasa', 'web', 'virus', 'linux', 'science', 'tech', 'online', 'pc', 'apple', 'ibm'],
    'World': ['iraq', 'war', 'president', 'government', 'minister', 'palestinian', 'israel', 'bomb', 'official', 'un', 'peace', 'troops', 'country', 'world', 'baghdad', 'gaza', 'leader', 'election'],
    'Sports': ['olympic', 'athens', 'medal', 'gold', 'silver', 'bronze', 'team', 'game', 'win', 'cup', 'coach', 'sport', 'football', 'baseball', 'basketball', 'soccer', 'tennis', 'hockey', 'champion', 'athlete', 'player', 'sox', 'yankees', 'mets', 'bulls', 'lakers', 'nfl', 'nba', 'mlb', 'nhl', 'rugby', 'cricket', 'race', 'victory', 'defeat', 'score', 'tournament', 'match', 'f1']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for w in words:
            if w in text:
                scores[cat] += 1
    
    # Return category with max score
    # If tie or 0, might be an issue, but let's take max
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown'
    return best_cat

sports_articles = []
for art in articles:
    # Combine title and description for classification
    text = (art.get('title', '') + " " + art.get('description', '')).lower()
    cat = classify(text)
    if cat == 'Sports':
        sports_articles.append(art)

# Find the one with max description length
if not sports_articles:
    print("__RESULT__:")
    print("No sports articles found")
else:
    max_len = -1
    best_art = None
    for art in sports_articles:
        desc_len = len(art.get('description', ''))
        if desc_len > max_len:
            max_len = desc_len
            best_art = art
            
    print("__RESULT__:")
    print(json.dumps({"title": best_art['title'], "length": max_len, "description": best_art['description']}))"""

env_args = {'var_function-call-421718428905845327': [{'_id': '694484ac1eb216d85781ec21', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694484ac1eb216d85781ec22', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694484ac1eb216d85781ec23', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694484ac1eb216d85781ec24', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694484ac1eb216d85781ec25', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '694484ac1eb216d85781ec26', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '694484ac1eb216d85781ec27', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '694484ac1eb216d85781ec28', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '694484ac1eb216d85781ec29', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '694484ac1eb216d85781ec2a', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_function-call-5747374927598452492': [{'_id': '694484ac1eb216d85781ec21', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694484ac1eb216d85781ec22', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694484ac1eb216d85781ec23', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694484ac1eb216d85781ec24', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694484ac1eb216d85781ec25', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9425809562068439331': [{'_id': '694484ac1eb216d85781ec21', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694484ac1eb216d85781ec22', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694484ac1eb216d85781ec23', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694484ac1eb216d85781ec24', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694484ac1eb216d85781ec25', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14907584402056121809': 5, 'var_function-call-14251754240139237620': 'file_storage/function-call-14251754240139237620.json'}

exec(code, env_args)
