code = """import json
import re

# Load Metadata (from file)
with open(locals()['var_function-call-12102332063729111063'], 'r') as f:
    metadata_raw = json.load(f)

# Load Articles (direct list)
articles_raw = locals()['var_function-call-1165826486750854528']

# Create Articles Dict
articles_dict = {str(a['article_id']): (a.get('title', '') + ' ' + a.get('description', '')) for a in articles_raw}

# Define Keywords (same as before)
categories = {
    'Business': ['business', 'economy', 'market', 'stock', 'finance', 'financial', 'bank', 'trade', 'invest', 'money', 'dollar', 'euro', 'gold', 'oil', 'price', 'profit', 'loss', 'share', 'deal', 'merger', 'acquisition', 'company', 'corp', 'inc', 'ltd', 'wall street', 'dow jones', 'nasdaq', 's&p', 'revenue', 'earnings', 'sale', 'retail', 'fed', 'rate', 'tax', 'debt', 'loan', 'credit', 'imf', 'wto', 'gdp', 'inflation', 'recession', 'job', 'employ', 'workforce', 'labor', 'strike', 'union', 'audit', 'budget', 'ceo', 'manager', 'executive', 'prices', 'futures', 'treasury', 'yield', 'bond', 'economic'],
    'Sports': ['sport', 'game', 'match', 'team', 'player', 'coach', 'win', 'lose', 'score', 'cup', 'league', 'championship', 'olympic', 'medal', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'racing', 'f1', 'nascar', 'cricket', 'rugby', 'athlete', 'stadium', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'tournament', 'round'],
    'SciTech': ['science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'net', 'site', 'mobile', 'phone', 'app', 'google', 'microsoft', 'apple', 'facebook', 'amazon', 'intel', 'ibm', 'nasa', 'space', 'astronomy', 'biology', 'physics', 'chemistry', 'research', 'study', 'scientist', 'discovery', 'invent', 'patent', 'gadget', 'device', 'electronic', 'digital', 'server', 'data', 'virus', 'hacker', 'robot', 'ai', 'browser', 'wireless', 'network', 'satellite', 'orbit'],
    'World': ['world', 'international', 'politics', 'government', 'president', 'minister', 'premier', 'senate', 'congress', 'parliament', 'law', 'court', 'legal', 'crime', 'police', 'arrest', 'prison', 'war', 'army', 'military', 'soldier', 'troop', 'attack', 'bomb', 'blast', 'kill', 'die', 'death', 'disaster', 'quake', 'flood', 'storm', 'fire', 'accident', 'crash', 'treaty', 'agreement', 'nuclear', 'weapon', 'peace', 'election', 'vote', 'poll', 'campaign', 'protest', 'demonstration', 'riot', 'crisis', 'conflict', 'refugee', 'migrant', 'un', 'eu', 'nato', 'diplomat', 'official', 'state', 'country', 'nation', 'security', 'terror', 'insurgent', 'rebel']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    words = re.findall(r'\w+', text)
    for word in words:
        for cat, kws in categories.items():
            if word in kws:
                scores[cat] += 1
    
    # Sort by score desc
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    best_cat, best_score = sorted_scores[0]
    
    # If tie or zero, check if 'Business' has > 0 and others 0?
    if best_score == 0:
        return 'Unknown'
    return best_cat

# Process
business_counts = {}
years = range(2010, 2021)
for y in years:
    business_counts[y] = 0

for item in metadata_raw:
    aid = str(item['article_id'])
    date = item['publication_date'] # YYYY-MM-DD
    year = int(date.split('-')[0])
    
    if year in years:
        # Get content
        content = articles_dict.get(aid)
        if content:
            cat = classify(content)
            if cat == 'Business':
                business_counts[year] += 1

total_business = sum(business_counts.values())
average = total_business / 11.0

print(f"Business Counts per Year: {business_counts}")
print(f"Total: {total_business}")
print(f"Average: {average}")

print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-12102332063729111063': 'file_storage/function-call-12102332063729111063.json', 'var_function-call-14273295165118230531': 'file_storage/function-call-14273295165118230531.json', 'var_function-call-8294512119571345844': 14860, 'var_function-call-8320919013075805354': [{'_id': '6944dc1fe2449a6347cdc96b', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dc1fe2449a6347cdc96c', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dc1fe2449a6347cdc96d', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dc1fe2449a6347cdc96e', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dc1fe2449a6347cdc96f', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1165826486750854528': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
