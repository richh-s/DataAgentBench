code = """import json

# Access the raw dictionary output from the previous tool call
# This variable `var_function-call-12487969826265871953` is directly the dictionary containing 'query_db_response'
raw_tool_output = locals()['var_function-call-12487969826265871953']

# Ensure `raw_tool_output` is a dictionary
if not isinstance(raw_tool_output, dict):
    print('__RESULT__:')
    print(json.dumps(f"Error: Expected `raw_tool_output` to be a dictionary, but got {type(raw_tool_output)}."))
    exit()

# Safely get the 'query_db_response' dictionary
query_db_response = raw_tool_output.get('query_db_response')
if not isinstance(query_db_response, dict):
    print('__RESULT__:')
    print(json.dumps(f"Error: Expected 'query_db_response' to be a dictionary, but got {type(query_db_response)}."))
    exit()

# Safely get the 'results' list from `query_db_response`
results_list = query_db_response.get('results')
if not isinstance(results_list, list) or not results_list:
    print('__RESULT__:')
    print(json.dumps("Error: 'results' field in 'query_db_response' is not a non-empty list."))
    exit()

# The actual JSON string (with extra text) is the first element of `results_list`
raw_json_string_with_extra = results_list[0]
if not isinstance(raw_json_string_with_extra, str):
    print('__RESULT__:')
    print(json.dumps(f"Error: Expected the first element of 'results_list' to be a string, but got {type(raw_json_string_with_extra)}."))
    exit()

# Extract only the JSON array part from the string
start_index = raw_json_string_with_extra.find('[')
end_index = raw_json_string_with_extra.rfind(']')

articles = []
if start_index != -1 and end_index != -1 and start_index < end_index:
    json_array_str = raw_json_string_with_extra[start_index : end_index + 1]
    
    try:
        articles = json.loads(json_array_str)
    except json.JSONDecodeError as e:
        print('__RESULT__:')
        print(json.dumps(f"JSON decoding error after extraction: {e}. Problematic snippet: {json_array_str[max(0, e.pos - 50):e.pos + 50]}"))
        exit()
else:
    print('__RESULT__:')
    print(json.dumps("Could not find a valid JSON array within the extracted string."))
    exit()

# Ensure `articles` is a list before proceeding
if not isinstance(articles, list):
    print('__RESULT__:')
    print(json.dumps(f"Error: Expected `articles` to be a list after JSON decoding, but received type {type(articles)}."))
    exit()

sports_articles = []
for article in articles:
    # Ensure each `article` in the list is a dictionary
    if not isinstance(article, dict):
        print('__RESULT__:')
        print(json.dumps(f"Error: Expected each article to be a dictionary, but got type {type(article)}."))
        exit()
    
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

env_args = {'var_function-call-12487969826265871953': [{'_id': '6943c2a7099e0eb129bb5bd7', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943c2a7099e0eb129bb5bd8', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943c2a7099e0eb129bb5bd9', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943c2a7099e0eb129bb5bda', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943c2a7099e0eb129bb5bdb', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11259735096289266444': "Error: Expected locals()['var_function-call-12487969826265871953'] to be a dictionary, but got <class 'list'>.", 'var_function-call-13306462991264116527': "Error: Expected 'query_db_response' to be a dictionary, but got <class 'NoneType'>.", 'var_function-call-1355461034923485381': "Error: Expected `raw_tool_output` to be a dictionary, but got <class 'list'>.", 'var_function-call-9319404328678013317': "Error: Expected `raw_tool_output` to be a dictionary, but got <class 'list'>.", 'var_function-call-1403719193110198792': "Error: Expected 'query_db_response' to be a dictionary, but got <class 'NoneType'>.", 'var_function-call-5030784390411462746': "Error: Expected 'query_db_response' to be a dictionary, but got <class 'NoneType'>."}

exec(code, env_args)
