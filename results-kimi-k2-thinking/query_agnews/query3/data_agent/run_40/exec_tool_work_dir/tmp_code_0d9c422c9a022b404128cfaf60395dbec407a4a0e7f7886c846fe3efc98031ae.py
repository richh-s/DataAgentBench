code = """import json
import re

# Read the Europe articles metadata
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    europe_articles = json.load(f)

# Create a dictionary mapping article_id to publication year
article_years = {}
for article in europe_articles:
    article_id = int(article['article_id'])
    date = article['publication_date']
    year = int(date.split('-')[0])
    article_years[article_id] = year

# Business keywords pattern
business_keywords = [
    'business', 'economy', 'economic', 'finance', 'financial', 'market', 'markets',
    'stock', 'stocks', 'trade', 'trading', 'dollar', 'euro', 'oil', 'price', 'prices',
    'company', 'companies', 'corporate', 'profit', 'revenue', 'bank', 'banking',
    'investment', 'investing', 'wall st', 'wall street', 'IPO', 'shares', 'quarter',
    'earnings', 'sales', 'growth', 'GDP', 'inflation', 'interest rate', 'fed', 'federal reserve'
]

# Create regex pattern
pattern = re.compile(r'\b(' + '|'.join(map(re.escape, business_keywords)) + r')\b', re.IGNORECASE)

print('__RESULT__:')
print(json.dumps({
    'total_articles': len(article_years),
    'year_range': f"{min(article_years.values())} to {max(article_years.values())}",
    'sample_data': dict(list(article_years.items())[:5])
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'sample_articles': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.query_db:10': [{'_id': '6969c8f361828b63eb846498', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c8f361828b63eb84649e', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969c8f361828b63eb8464a2', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969c8f361828b63eb8464a3', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969c8f361828b63eb8464aa', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}]}

exec(code, env_args)
