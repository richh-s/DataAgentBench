code = """import json
import pandas as pd

# Load the articles data
articles_data = [{"_id": "69697637eccee0c86d6ace83", "article_id": "0", "title": "Wall St. Bears Claw Back Into the Black (Reuters)", "description": "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {"_id": "69697637eccee0c86d6ace84", "article_id": "1", "title": "Carlyle Looks Toward Commercial Aerospace (Reuters)", "description": "Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market."}, {"_id": "69697637eccee0c86d6ace85", "article_id": "2", "title": "Oil and Economy Cloud Stocks' Outlook (Reuters)", "description": "Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums."}, {"_id": "69697637eccee0c86d6ace86", "article_id": "3", "title": "Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)", "description": "Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday."}, {"_id": "69697637eccee0c86d6ace87", "article_id": "4", "title": "Oil prices soar to all-time record, posing new menace to US economy (AFP)", "description": "AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections."}]

# Load articles metadata
articles_metadata = [{"article_id": 0, "category": "Sports"}, {"article_id": 1, "category": "Business"}, {"article_id": 2, "category": "Business"}, {"article_id": 3, "category": "World"}, {"article_id": 4, "category": "Science/Technology"}]

# Convert to DataFrames
df = pd.DataFrame(articles_data)
meta_df = pd.DataFrame(articles_metadata)

# Convert article_id to integer
df['article_id'] = df['article_id'].astype(int)
# Merge the dataframes
df_merged = df.merge(meta_df, on='article_id')
print('Before merge:', df)
print('Articles metadata:', articles_metadata)
df['article_id'] = df['article_id'].astype(int)
df['description_length'] = df['description'].astype(str).str.len()

# Try matching by title keywords for sports
sports_keywords = ['sport', 'game', 'match', 'player', 'team', 'football', 'soccer', 'baseball', 'basketball', 'golf', 'olympics', 'championship', 'nba', 'nfl', 'mlb', 'nhl']

# Look at the titles and descriptions to manually categorize them
titles_and_desc = []
for _, row in df.iterrows():
    titles_and_desc.append({
        'article_id': row['article_id'],
        'title': row['title'],
        'description': row['description'],
        'description_length': row['description_length']
    })

print('Articles:')
for item in titles_and_desc:
    print(item)

# Check for sports articles by looking at content
sports_articles = []
for article in titles_and_desc:
    # Look for sports keywords in title and description
    content = (article['title'] + ' ' + article['description']).lower()
    is_sports = any(keyword in content for keyword in sports_keywords)
    
    if is_sports:
        article['is_sports'] = True
        sports_articles.append(article)
    else:
        article['is_sports'] = False

# Also try content-based classification
for article in titles_and_desc:
    title_lower = article['title'].lower()
    desc_lower = article['description'].lower()
    
    business_score = 0
    sports_score = 0
    science_score = 0
    
    if 'reuters' in desc_lower or 'wall st' in title_lower or 'stock' in title_lower:
        business_score += 2
    
    if 'economy' in desc_lower or 'economic' in desc_lower:
        business_score += 2
    
    if any(word in title_lower for word in ['sport', 'game', 'team', 'player', 'hockey', 'football']):
        sports_score += 3
    
    # Assign category based on scores
    if sports_score > business_score and sports_score > science_score:
        article['category'] = 'Sports'
        if article not in sports_articles:
            sports_articles.append(article)
    elif business_score > sports_score and business_score > science_score:
        article['category'] = 'Business'
    elif science_score > sports_score and science_score > business_score:
        article['category'] = 'Science/Technology'
    else:
        article['category'] = 'World'

print('Sports articles found:', len(sports_articles))
if sports_articles:
    print('Sports articles:')
    for article in sports_articles:
        print(article)

    # Find the sports article with the longest description
    longest_sports = max(sports_articles, key=lambda x: x['description_length'])
    print('Longest sports article:', longest_sports['title'])
    result = longest_sports['title']
else:
    print('No sports articles found')
    result = 'No sports articles found'

# Print result in required format
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '69697637eccee0c86d6ace83', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697637eccee0c86d6ace84', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697637eccee0c86d6ace85', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697637eccee0c86d6ace86', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697637eccee0c86d6ace87', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
