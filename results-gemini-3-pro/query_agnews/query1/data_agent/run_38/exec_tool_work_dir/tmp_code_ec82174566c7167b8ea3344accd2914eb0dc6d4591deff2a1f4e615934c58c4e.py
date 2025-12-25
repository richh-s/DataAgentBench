code = """import json

# Load the articles
with open(locals()['var_function-call-9571403557217770297'], 'r') as f:
    articles = json.load(f)

# Define sports keywords
sports_keywords = [
    "sport", "football", "baseball", "basketball", "hockey", "tennis", "soccer", "golf", 
    "olympics", "olympic", "medal", "athens", "game", "match", "cup", "tournament", 
    "league", "team", "coach", "player", "athlete", "win", "lose", "victory", "defeat", 
    "score", "nba", "nfl", "mlb", "nhl", "fifa", "uefa", "champion", "record", 
    "swimming", "gymnastics", "track", "field", "marathon", "sprint", "relay", 
    "doping", "drug", "gold", "silver", "bronze"
]

# Function to score an article
def get_sports_score(text):
    text = text.lower()
    score = 0
    for kw in sports_keywords:
        score += text.count(kw)
    return score

# Filter and score
sports_articles = []
for art in articles:
    # Combine title and description for context
    text = art['title'] + " " + art['description']
    score = get_sports_score(text)
    
    # We also need to be careful about false positives. 
    # For now, let's assume a threshold or just take the ones with high scores.
    # However, some sports articles might have few keywords.
    # Let's inspect the data distribution.
    if score > 0:
        sports_articles.append((art, score))

# Sort by score descending to see top sports candidates
sports_articles.sort(key=lambda x: x[1], reverse=True)

# Let's print the top 10 detected sports articles to verify my logic
top_candidates = [ (a['title'], a['description'], s) for a, s in sports_articles[:5] ]

# Now, find the one with longest description among the filtered list.
# I'll try to use a stricter filter if needed. 
# Let's assume distinct categories exist. 
# Maybe I can look for metadata? No, metadata was author/region/date.

# Let's filter by a reasonable threshold, say score >= 2? 
# Or just treat the non-zero score as candidates and find the max length?
# The danger is a business article mentioning a "record" oil price (keyword 'record').
# "Oil prices soar to all-time record" -> contains 'record' -> score 1.
# So I should exclude common words like "record" if they appear alone? 
# Or use specific sports terms.
# "record" is tricky. "win" is tricky ("win contract").
# "team" is tricky ("management team").
# "score" ("settle score").

# Refined keywords for strict sports detection
strict_sports_keywords = [
    "olympics", "olympic", "athens", "medal", "nba", "nfl", "mlb", "nhl", 
    "fifa", "uefa", "wimbledon", "tournament", "championship", "world cup", 
    "super bowl", "quarterback", "touchdown", "homerun", "slam dunk", 
    "gold medal", "silver medal", "bronze medal"
]

def is_strictly_sports(text):
    text = text.lower()
    for kw in strict_sports_keywords:
        if kw in text:
            return True
    return False

# Filter using strict keywords first?
# Or maybe just print the candidates for "longest description" and see if the top one is sports.

# Let's calculate description length for all articles
for art in articles:
    art['desc_len'] = len(art['description'])

# Sort all articles by description length descending
articles_by_len = sorted(articles, key=lambda x: x['desc_len'], reverse=True)

# Print top 10 longest description articles with their titles and snippets
# and my sports score.
result_preview = []
for art in articles_by_len[:10]:
    text = art['title'] + " " + art['description']
    score = get_sports_score(text)
    strict = is_strictly_sports(text)
    result_preview.append({
        "title": art['title'],
        "desc_snippet": art['description'][:50],
        "desc_len": art['desc_len'],
        "sports_score": score,
        "is_strict_sports": strict
    })

print("__RESULT__:")
print(json.dumps(result_preview, indent=2))"""

env_args = {'var_function-call-10047601114484748362': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-9571403557217770297': [{'_id': '6944814a2d282254f98124f6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944814a2d282254f98124f7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944814a2d282254f98124f8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944814a2d282254f98124f9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944814a2d282254f98124fa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
