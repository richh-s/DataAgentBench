code = """import json

# Access the full output from the previous tool call
full_output_dict = locals()['var_function-call-12487969826265871953']['query_db_response']
raw_result_string = full_output_dict['results'][0]

# Find the first '[' and the last ']' to extract the JSON array string
start_json_index = raw_result_string.find('[')
end_json_index = raw_result_string.rfind(']')

articles = []
if start_json_index != -1 and end_json_index != -1 and start_json_index < end_json_index:
    json_array_str = raw_result_string[start_json_index : end_json_index + 1]
    
    try:
        articles = json.loads(json_array_str)
    except json.JSONDecodeError as e:
        print('__RESULT__:')
        print(json.dumps(f"Failed to decode JSON array string: {e}. Snippet around error: {json_array_str[max(0, e.pos - 50):e.pos + 50]}"))
        exit()
else:
    print('__RESULT__:')
    print(json.dumps("Could not find the JSON array in the raw result string."))
    exit()

sports_articles = []
for article in articles:
    title = article.get('title', '').lower()
    description = article.get('description', '').lower()
    sports_keywords = [
        'sport', 'team', 'game', 'match', 'athletic', 'league', 'cup', 'olympic',
        'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf',
        'race', 'player', 'coach', 'championship', 'super bowl', 'world series',
        'nba', 'nfl', 'mlb', 'fifa', 'track and field'
    ]

    if any(keyword in title or keyword in description for keyword in sports_keywords):
        sports_articles.append(article)

if not sports_articles:
    print('__RESULT__:')
    print(json.dumps("No sports articles found."))
else:
    longest_description_article = None
    max_description_length = -1
    for article in sports_articles:
        description = article.get('description', '')
        description_length = len(description)
        if description_length > max_description_length:
            max_description_length = description_length
            longest_description_article = article

    if longest_description_article:
        print('__RESULT__:')
        print(json.dumps(longest_description_article.get('title', 'No title available')))
    else:
        print('__RESULT__:')
        print(json.dumps("No sports articles found with descriptions."))"""

env_args = {'var_function-call-12487969826265871953': [{'_id': '6943c2a7099e0eb129bb5bd7', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c2a7099e0eb129bb5bd8', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c2a7099e0eb129bb5bd9', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c2a7099e0eb129bb5bda', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c2a7099e0eb129bb5bdb', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
