code = """import json

# Read Europe metadata
file_path = locals()['var_functions.query_db:10']
with open(file_path, 'r') as f:
    europe_metadata = json.load(f)

# Group by year and get a few samples from each year for manual inspection
from collections import defaultdict
articles_by_year = defaultdict(list)
for item in europe_metadata:
    year = item['publication_date'][:4]
    articles_by_year[year].append(item['article_id'])

# Get first 30 article IDs overall to examine their content
first_30_ids = [item['article_id'] for item in europe_metadata[:30]]

# Group some business-related keywords for heuristic
business_keywords = [
    'business', 'stock', 'market', 'economy', 'economic',
    'trade', 'oil', 'price', 'company', 'share',
    'bank', 'investment', 'finance', 'financial',
    'job', 'employment', 'growth', 'rate', 'rates',
    'sector', 'industry', 'eurozone', 'euro', 'european'
]

print('__RESULT__:')
print(json.dumps({
    'first_30_ids': first_30_ids,
    'business_keywords': business_keywords,
    'year_article_count': {year: len(ids) for year, ids in sorted(articles_by_year.items())}
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.query_db:14': [{'_id': '6969c42c8494de621543382e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c42c8494de621543382f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c42c8494de6215433830', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c42c8494de6215433831', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c42c8494de6215433832', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:16': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.query_db:18': [], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_europe_articles': 14860, 'sample_europe_ids_int': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'sample_europe_ids_str': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63'], 'sample_article_ids_from_db': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 'match_check': True}, 'var_functions.execute_python:24': {'total_articles': 14860, 'batch_size': 1000, 'num_batches': 15}, 'var_functions.execute_python:26': {'year_range': '2010 to 2020', 'total_years': 11, 'year_distribution': {'2020': 1366, '2016': 1364, '2015': 1357, '2017': 1391, '2013': 1354, '2010': 1306, '2018': 1351, '2019': 1328, '2014': 1372, '2011': 1316, '2012': 1355}, 'articles_2010': 1306, 'articles_2020': 1366}, 'var_functions.execute_python:28': {'total_samples': 506, 'sample_article_ids': ['10250', '9630', '17910', '54139', '7216', '60263', '10471', '118537', '75319', '25113', '60045', '84013', '88282', '74033', '85497', '43537', '62368', '32847', '47632', '114136', '90797', '55845', '102190', '22958', '21239', '77851', '79554', '61182', '99783', '71562', '32503', '66889', '9952', '99638', '83829', '110413', '61208', '48893', '124547', '82483', '86450', '78866', '23090', '18642', '39332', '25060', '48156', '2585', '298', '19909', '40191', '88846', '57829', '100739', '110737', '3320', '53580', '89060', '53447', '87502', '53338', '1108', '64905', '85622', '98088', '124711', '17334', '64069', '92178', '99709', '30141', '31095', '5575', '78498', '9074', '29417', '1887', '43991', '40594', '56525', '106034', '30058', '57273', '103603', '21330', '123812', '82167', '25801', '19645', '100262', '91906', '53460', '19552', '122372', '50463', '35416', '23955', '97914', '20981', '12598']}, 'var_functions.execute_python:30': {'total_articles': 14860, 'article_dates_sample': {'3': '2020-03-04', '9': '2016-05-24', '13': '2015-10-17', '14': '2017-09-08', '21': '2020-04-06'}}, 'var_functions.query_db:32': [], 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
