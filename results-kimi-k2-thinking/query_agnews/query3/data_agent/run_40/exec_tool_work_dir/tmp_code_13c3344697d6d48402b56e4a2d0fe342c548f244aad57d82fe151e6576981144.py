code = """import json
import re

# Load Europe article metadata
metadata_file = locals()['var_functions.query_db:5']
with open(metadata_file, 'r') as f:
    europe_articles = json.load(f)

# Create sets for fast lookup
europe_article_ids = set(int(article['article_id']) for article in europe_articles)
europe_article_years = {int(article['article_id']): int(article['publication_date'][:4]) 
                        for article in europe_articles}

# Initialize counters
business_by_year = {year: 0 for year in range(2010, 2021)}
total_by_year = {year: 0 for year in range(2010, 2021)}

# Populate total_by_year
for article_id, year in europe_article_years.items():
    if year in total_by_year:
        total_by_year[year] += 1

# Business keywords pattern
business_keywords = [
    'business', 'economy', 'economic', 'finance', 'financial', 'market', 'markets',
    'stock', 'stocks', 'trade', 'trading', 'dollar', 'euro', 'oil', 'price', 'prices',
    'company', 'companies', 'corporate', 'profit', 'revenue', 'bank', 'banking',
    'investment', 'investing', 'wall st', 'wall street', 'IPO', 'shares', 'quarter',
    'earnings', 'sales', 'growth', 'GDP', 'inflation', 'interest rate', 'fed', 'federal reserve',
    'export', 'imports', 'deficit', 'surplus', 'billion', 'million', 'economist', 'sector',
    'industry', 'industrial', 'retail', 'consumer', 'consumers', 'jobs', 'unemployment',
    'manufacturing', 'factory', 'production', 'output', 'costs', 'rates', 'trade gap',
    'commercial', 'enterprise', 'fund', 'funding', 'capital', 'budget', 'monetary',
    'fiscal', 'tax', 'recession', 'recovery', 'boom', 'crisis', 'acquisition', 'merger',
    'shareholder', 'dividend', 'bond', 'bonds', 'currency', 'currencies', 'forex',
    'hedge fund', 'pension', 'portfolio', 'asset', 'assets', 'liability', 'audit',
    'quarterly', 'NASDAQ', 'NYSE', 'commodity', 'commodities', 'energy prices'
]

pattern = re.compile(r'\b(' + '|'.join(map(re.escape, business_keywords)) + r')\b', re.IGNORECASE)

print('__RESULT__:')
print(json.dumps({
    'europe_article_count': len(europe_article_ids),
    'year_range': '2010-2020',
    'business_keywords': len(business_keywords)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'sample_articles': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.query_db:10': [{'_id': '6969c8f361828b63eb846498', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c8f361828b63eb84649e', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969c8f361828b63eb8464a2', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969c8f361828b63eb8464a3', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969c8f361828b63eb8464aa', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:12': {'total_articles': 14860, 'year_range': '2010 to 2020', 'sample_data': {'3': 2020, '9': 2016, '13': 2015, '14': 2017, '21': 2020}}, 'var_functions.execute_python:14': {'article_count': 14860, 'sample_years': {'3': 2020, '9': 2016, '13': 2015, '14': 2017, '21': 2020, '27': 2013, '43': 2010, '60': 2017, '62': 2018, '63': 2010}, 'business_keywords_count': 38}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_articles': 14860, 'year_range': '2010 to 2020', 'first_10_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'last_10_ids': [127521, 127525, 127561, 127564, 127566, 127567, 127572, 127576, 127577, 127583]}, 'var_functions.execute_python:20': {'total_batches': 15, 'batch_sizes': [1000, 1000, 1000, 1000, 1000], 'total_articles': 14860}, 'var_functions.execute_python:22': {'total_articles': 14860, 'year_range': '2010-2020', 'business_keywords': 60}, 'var_functions.execute_python:24': {'batch_size': 1000, 'min_id': 3, 'max_id': 9038, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.execute_python:26': {'total_articles': 14860, 'yearly_totals': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}, 'expected_batches': 30}}

exec(code, env_args)
