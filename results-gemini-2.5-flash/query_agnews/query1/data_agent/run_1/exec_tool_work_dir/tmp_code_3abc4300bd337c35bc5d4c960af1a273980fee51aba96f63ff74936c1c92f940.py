code = """import json

# Get the raw string result from the previous tool call
raw_result_string = locals()['var_function-call-8009334219944431032']['query_db_response']['results'][0]

# Find the first '[' and last ']' to extract the pure JSON array string.
json_array_start_index = raw_result_string.find('[')
json_array_end_index = raw_result_string.rfind(']')

articles = []
final_answer = ""

if json_array_start_index != -1 and json_array_end_index != -1:
    json_articles_string = raw_result_string[json_array_start_index : json_array_end_index + 1]
    
    # The primary issue observed is that `\'` appears in the description, which is not valid JSON.
    # Replace `\\'` (Python string literal for backslash followed by single quote) with `'` (Python string literal for a single quote)
    # This converts `Wall Street\'s` to `Wall Street's` which is valid JSON.
    json_articles_string = json_articles_string.replace("\\'", "'")

    try:
        # Now, attempt to load the cleaned JSON string
        articles = json.loads(json_articles_string)
    except json.JSONDecodeError as e:
        final_answer = f"JSON decoding failed: {e}. Problematic string snippet: {json_articles_string[:200]}..."

    if not final_answer and articles: # Only proceed if JSON decoding was successful and articles list is not empty
        sports_keywords = ['sport', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'olympics', 'game', 'match', 'athlete', 'team', 'league', 'championship', 'cup']
        
        max_desc_length = -1
        sports_article_title = ''
        
        for article in articles:
            title = article.get('title', '').lower()
            description = article.get('description', '').lower()
            
            is_sports_article = False
            for keyword in sports_keywords:
                if keyword in title or keyword in description:
                    is_sports_article = True
                    break
        
            if is_sports_article:
                desc_length = len(article.get('description', ''))
                if desc_length > max_desc_length:
                    max_desc_length = desc_length
                    sports_article_title = article.get('title', '')
        
        if sports_article_title:
            final_answer = sports_article_title
        else:
            final_answer = "No sports articles found."
    elif not final_answer: # JSON decoding successful but articles list is empty
        final_answer = "No articles found in the database."
else:
    final_answer = "Error: Could not extract JSON array from the tool output."

print('__RESULT__:')
print(json.dumps(final_answer))"""

env_args = {'var_function-call-8009334219944431032': [{'_id': '6943aab942b29793b81b3167', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943aab942b29793b81b3168', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943aab942b29793b81b3169', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943aab942b29793b81b316a', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943aab942b29793b81b316b', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
