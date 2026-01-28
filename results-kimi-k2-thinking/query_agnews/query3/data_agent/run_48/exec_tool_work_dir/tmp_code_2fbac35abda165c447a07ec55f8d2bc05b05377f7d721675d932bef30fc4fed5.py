code = """import json
import re
from collections import defaultdict

# Read Europe articles metadata file
europe_file = locals()['var_functions.query_db:14']
with open(europe_file, 'r') as f:
    europe_articles = json.load(f)

# Group article_ids by year
articles_by_year = defaultdict(list)
for item in europe_articles:
    article_id = int(item['article_id'])
    year = int(item['publication_date'].split('-')[0])
    if 2010 <= year <= 2020:
        articles_by_year[year].append(article_id)

# Sort article_ids by year
all_article_ids = []
for year in sorted(articles_by_year.keys()):
    all_article_ids.extend(articles_by_year[year])

# Split into batches
batch_size = 300  # Safe batch size for MongoDB
batches = [all_article_ids[i:i + batch_size] for i in range(0, len(all_article_ids), batch_size)]

print('__RESULT__:')
print(json.dumps({
    'total_articles': len(all_article_ids),
    'num_batches': len(batches),
    'years_covered': sorted(articles_by_year.keys()),
    'first_batch_size': len(batches[0]) if batches else 0
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}, {'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '14', 'author_id': '223', 'region': 'Europe', 'publication_date': '2017-09-08'}, {'article_id': '21', 'author_id': '674', 'region': 'Europe', 'publication_date': '2020-04-06'}, {'article_id': '27', 'author_id': '244', 'region': 'Europe', 'publication_date': '2013-09-07'}, {'article_id': '43', 'author_id': '154', 'region': 'Europe', 'publication_date': '2010-03-12'}, {'article_id': '60', 'author_id': '530', 'region': 'Europe', 'publication_date': '2017-04-30'}, {'article_id': '62', 'author_id': '328', 'region': 'Europe', 'publication_date': '2018-09-12'}, {'article_id': '63', 'author_id': '83', 'region': 'Europe', 'publication_date': '2010-04-19'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': {'count': 14860, 'sample': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.execute_python:12': {'total_articles': 14860, 'num_batches': 30, 'first_batch': [3, 9, 13, 14, 21]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_europe_articles_2010_2020': 14860, 'articles_per_year': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}, 'sample_2015': [13, 179, 203, 243, 271]}, 'var_functions.query_db:18': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '179', 'title': 'Reverse Psychology', 'description': "\\\\I really hope SUN doesn't Open Source Java at JavaOne this year.  It would be a\\terrible decision and seriously hurt the tech industry.  Also, it would hurt SUN\\and I'm sure their responsible enough to realize this.\\\\(Lets hope that works!)\\\\"}, {'article_id': '203', 'title': "'Madden,' 'ESPN' Football Score in Different Ways", 'description': ' PROVIDENCE, R.I. (Reuters) - Was absenteeism a little high  on Tuesday among the guys at the office? EA Sports would like  to think it was because "Madden NFL 2005" came out that day,  and some fans of the football simulation are rabid enough to  take a sick day to play it.'}, {'article_id': '243', 'title': 'News: Warmer Weather, Human Disturbances Interact to Change Forests', 'description': "While a rapidly changing climate may alter the composition of northern Wisconsin's forests, disturbances such as logging also will play a critical role in how these sylvan ecosystems change over time. (University of Wisconsin-Madison press release)"}, {'article_id': '271', 'title': "Saturn's Moon Titan: Prebiotic Laboratory", 'description': "by Harry Bortman    In this second and final part of the interview, Lunine explains how Huygens may help scientists understand the origin of life on Earth, even if it doesn't detect life on Titan.    Astrobiology Magazine -- Titan is the only moon in our solar system with an atmosphere, and it is the organic chemistry that has been detected in that atmosphere that has sparked the imagination of planetary scientists like Lunine..."}], 'var_functions.execute_python:20': {'total_articles': 14860, 'articles_per_year': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}, 'num_batches': 30, 'total_article_ids': 14860}, 'var_functions.query_db:24': [{'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:26': {'total_sample': 5, 'business_in_sample': 5, 'sample_articles': [{'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}]}}

exec(code, env_args)
