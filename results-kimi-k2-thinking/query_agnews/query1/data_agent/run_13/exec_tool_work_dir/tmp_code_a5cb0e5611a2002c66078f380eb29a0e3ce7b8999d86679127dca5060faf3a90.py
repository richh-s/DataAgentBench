code = """import json

# Load the articles from the query
articles = locals()['var_functions.query_db:0']

# Display all articles with their descriptions and character counts
articles_with_desc_length = []

print("All articles in database:")
for i, article in enumerate(articles):
    title = article['title']
    desc = article['description']
    desc_length = len(desc)
    article_id = article['article_id']
    
    articles_with_desc_length.append({
        'article_id': article_id,
        'title': title,
        'description': desc,
        'desc_length': desc_length
    })
    
    print("Article #" + str(i+1) + " - ID: " + str(article_id))
    print("Title: " + title)
    print("Description length: " + str(desc_length) + " characters")
    print("Description: " + desc)
    print()

# Sort by description length to find the longest
sorted_articles = sorted(articles_with_desc_length, key=lambda x: x['desc_length'], reverse=True)

print("Articles sorted by description length (longest first):")
for i, article in enumerate(sorted_articles):
    print(str(i+1) + ". ID: " + str(article['article_id']) + " - Length: " + str(article['desc_length']) + " chars")
    print("   Title: " + article['title'])
    print()

# Convert to JSON string
result = json.dumps(sorted_articles, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': [{'_id': '69696c6a0c41ae9ae8ecd6d1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69696c6a0c41ae9ae8ecd6d2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69696c6a0c41ae9ae8ecd6d3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69696c6a0c41ae9ae8ecd6d4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69696c6a0c41ae9ae8ecd6d5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:6': 'Total: 5, Sports: 0'}

exec(code, env_args)
