code = """import json

# Get Europe article IDs
metadata_file = locals()['var_functions.query_db:5']
with open(metadata_file, 'r') as f:
    europe_articles = json.load(f)

# Create mapping of article_id to year
article_years = {int(article['article_id']): int(article['publication_date'][:4]) 
                 for article in europe_articles}

# Batch the article IDs (fetch 1000 at a time)
all_article_ids = sorted(article_years.keys())
batches = [all_article_ids[i:i+1000] for i in range(0, len(all_article_ids), 1000)]

print('__RESULT__:')
print(json.dumps({
    'total_batches': len(batches),
    'batch_sizes': [len(batch) for batch in batches[:5]],
    'total_articles': len(all_article_ids)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'sample_articles': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.query_db:10': [{'_id': '6969c8f361828b63eb846498', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c8f361828b63eb84649e', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969c8f361828b63eb8464a2', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969c8f361828b63eb8464a3', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969c8f361828b63eb8464aa', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:12': {'total_articles': 14860, 'year_range': '2010 to 2020', 'sample_data': {'3': 2020, '9': 2016, '13': 2015, '14': 2017, '21': 2020}}, 'var_functions.execute_python:14': {'article_count': 14860, 'sample_years': {'3': 2020, '9': 2016, '13': 2015, '14': 2017, '21': 2020, '27': 2013, '43': 2010, '60': 2017, '62': 2018, '63': 2010}, 'business_keywords_count': 38}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_articles': 14860, 'year_range': '2010 to 2020', 'first_10_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'last_10_ids': [127521, 127525, 127561, 127564, 127566, 127567, 127572, 127576, 127577, 127583]}}

exec(code, env_args)
