code = """import json

# Load the file path for year data
year_file_path = var_functions.query_db:20

# Read and process data
with open(year_file_path, 'r') as f:
    articles = json.load(f)

# Extract article IDs and organize by year
article_ids = [int(article['article_id']) for article in articles]
articles_by_year = {}
for article in articles:
    year = article['year']
    article_id = int(article['article_id'])
    if year not in articles_by_year:
        articles_by_year[year] = []
    articles_by_year[year].append(article_id)

print('__RESULT__:')
print(json.dumps({
    'total_articles': len(article_ids),
    'articles_by_year_count': {year: len(ids) for year, ids in articles_by_year.items()},
    'sample_article_ids': article_ids[:20]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'articles_per_year': {'2020': 1366, '2016': 1364, '2015': 1357, '2017': 1391, '2013': 1354, '2010': 1306, '2018': 1351, '2019': 1328, '2014': 1372, '2011': 1316, '2012': 1355}, 'sample_data': [{'article_id': 3, 'year': 2020, 'publication_date': '2020-03-04'}, {'article_id': 9, 'year': 2016, 'publication_date': '2016-05-24'}, {'article_id': 13, 'year': 2015, 'publication_date': '2015-10-17'}, {'article_id': 14, 'year': 2017, 'publication_date': '2017-09-08'}, {'article_id': 21, 'year': 2020, 'publication_date': '2020-04-06'}]}, 'var_functions.query_db:13': [{'_id': '6969c5d0c0cd6f23b7593a65', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c5d0c0cd6f23b7593a6b', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969c5d0c0cd6f23b7593a6f', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969c5d0c0cd6f23b7593a70', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969c5d0c0cd6f23b7593a77', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}, {'_id': '6969c5d0c0cd6f23b7593a7d', 'article_id': '27', 'title': 'HP shares tumble on profit news', 'description': 'Hewlett-Packard shares fall after disappointing third-quarter profits, while the firm warns the final quarter will also fall short of expectations.'}, {'_id': '6969c5d0c0cd6f23b7593a8d', 'article_id': '43', 'title': 'Grant to aid Lynn Central Square', 'description': 'Central Square in Lynn should be looking a bit brighter. New sidewalks, curbs, fences, lights, landscaping, and road improvements are planned for the Gateway Artisan Block, a key area of the square, with \\$830,000 in state grant money given to Lynn last week.'}, {'_id': '6969c5d0c0cd6f23b7593a9e', 'article_id': '60', 'title': 'Oldsmobile: The final parking lot', 'description': 'Why General Motors dropped the Oldsmobile. The four brand  paradoxes GM had to face - the name, the product, image re-positioning, and the consumer - all added up to a brand that had little hope of rebranding.'}, {'_id': '6969c5d0c0cd6f23b7593aa0', 'article_id': '62', 'title': 'Downhome Pinoy Blues, Intersecting Life Paths, and Heartbreak Songs', 'description': "The Blues is alive and well in the Philippines, as evidenced by this appreciation of the Pinoy Blues band 'Lampano Alley', penned by columnist Clarence Henderson as a counterpoint to his usual economics, business, and culture fare."}, {'_id': '6969c5d0c0cd6f23b7593aa1', 'article_id': '63', 'title': 'The Real Time Modern Manila Blues: Bill Monroe Meets Muddy Waters in the Orient', 'description': 'Globalization does strange things to people. A day in the life of a Manila Philippines based business consultant - proving that you really CAN talk about Muddy Walters, bluegrass and work all on the same page...'}], 'var_functions.query_db:16': [{'total_europe_articles': '14860'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
