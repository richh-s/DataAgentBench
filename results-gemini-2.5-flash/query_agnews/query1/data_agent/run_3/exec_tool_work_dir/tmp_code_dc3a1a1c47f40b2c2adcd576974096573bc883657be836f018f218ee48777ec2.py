code = """import json

raw_output_string = locals()['var_function-call-3553061123882171801']['query_db_response']['results'][0]

# Find the first '[' and the last ']'
start_index = raw_output_string.find('[')
end_index = raw_output_string.rfind(']')

if start_index != -1 and end_index != -1 and start_index < end_index:
    json_string = raw_output_string[start_index : end_index + 1]
    
    try:
        all_articles = json.loads(json_string)
    except json.JSONDecodeError as e:
        result = {"error": f"JSON decoding error after extracting string: {e}", "extracted_string_preview": json_string[:200]}
else:
    result = {"error": "Could not find a valid JSON array within the raw output string."}

if 'error' not in result:
    sports_articles = []

    sports_keywords = ['sport', 'sports', 'athletic', 'game', 'match', 'team', 'league', 'cup', 'tournament', 'championship', 'score', 'player', 'coach', 'football', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'race', 'win', 'loss']

    for article_dict in all_articles:
        title = article_dict.get('title', '').lower()
        description = article_dict.get('description', '').lower()

        if any(keyword in title for keyword in sports_keywords) or \
           any(keyword in description for keyword in sports_keywords):
            sports_articles.append(article_dict)

    if not sports_articles:
        result = {"error": "No sports articles found."}
    else:
        max_desc_len = -1
        article_with_longest_desc = None
        for article in sports_articles:
            desc_len = len(article.get('description', ''))
            if desc_len > max_desc_len:
                max_desc_len = desc_len
                article_with_longest_desc = article

        if article_with_longest_desc:
            result = {"title": article_with_longest_desc.get('title')}
        else:
            result = {"error": "No sports article with a description found."}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_function-call-3553061123882171801': [{'_id': '6943ad31662233f6885122c5', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943ad31662233f6885122c6', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943ad31662233f6885122c7', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943ad31662233f6885122c8', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943ad31662233f6885122c9', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
