code = """import json
import pandas as pd
import numpy as np

# Load metadata
meta_path = locals()['var_function-call-11639742510862021534']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

# Load already fetched articles
articles_path = locals()['var_function-call-5039010200560302586']
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

# IDs
meta_ids = sorted(list(set([int(item['article_id']) for item in meta_data])))
fetched_ids = set([int(item['article_id']) for item in articles_data])

missing_ids = sorted([i for i in meta_ids if i not in fetched_ids])

# Check for ranges
ranges = []
if missing_ids:
    start = missing_ids[0]
    prev = missing_ids[0]
    for x in missing_ids[1:]:
        if x > prev + 100: # Allow gaps of 100
            ranges.append((start, prev))
            start = x
        prev = x
    ranges.append((start, prev))

print(f"Number of missing IDs: {len(missing_ids)}")
print(f"Number of ranges (gap > 100): {len(ranges)}")
if len(ranges) < 50:
    print("Ranges:", ranges)
else:
    print("Too many ranges.")

# If too many ranges, maybe just print the list of IDs to a certain length
# and see if we can do batches.
# But simply, let's try to output the JSON for the first 5000 missing IDs to use in a query.
# The user wants the answer. I can do multiple queries.
# Let's split missing_ids into chunks of 4000.
chunks = [missing_ids[i:i + 4000] for i in range(0, len(missing_ids), 4000)]
print(f"Chunks needed: {len(chunks)}")

# Store chunks in a variable I can read? No, variables don't persist across tools unless output.
# I will print the first chunk of IDs as a JSON string to be used in the next query.
# I will convert them to STRINGS because article_id in Mongo seems to be string.
chunk1 = [str(i) for i in chunks[0]] if chunks else []

print("__RESULT__:")
print(json.dumps(chunk1))"""

env_args = {'var_function-call-11639742510862021534': 'file_storage/function-call-11639742510862021534.json', 'var_function-call-7912262759371964937': 'file_storage/function-call-7912262759371964937.json', 'var_function-call-7698643900256978742': 14860, 'var_function-call-13170610014898490485': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8382702086317822417': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17709649415609663654': {'counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091, 'total_articles_fetched': 5, 'total_articles_merged': 1}, 'var_function-call-5039010200560302586': 'file_storage/function-call-5039010200560302586.json', 'var_function-call-7485474422923815158': {'missing_count': 12587, 'max_meta_id': 127583, 'max_article_id': 19999}}

exec(code, env_args)
