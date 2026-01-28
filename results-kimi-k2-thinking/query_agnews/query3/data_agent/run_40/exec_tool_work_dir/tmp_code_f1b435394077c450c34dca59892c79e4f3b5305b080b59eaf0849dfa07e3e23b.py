code = """import json
import re

# Load sample articles
first_batch_file = locals()['var_functions.query_db:16']
with open(first_batch_file, 'r') as f:
    sample_articles = json.load(f)

# Simplified business classification
def is_business_article(title, description):
    text = f"{title} {description}".lower()
    
    business_terms = [
        'economy', 'economic', 'stock', 'stocks', 'market', 'markets',
        'finance', 'financial', 'bank', 'banking', 'investment', 'investing',
        'trade', 'trading', 'dollar', 'euro', 'oil', 'price', 'prices',
        'profit', 'revenue', 'company', 'companies', 'shares', 'IPO',
        'earnings', 'growth', 'inflation', 'GDP', 'fed', 'federal reserve',
        'deficit', 'commercial', 'corporate', 'wall st', 'wall street'
    ]
    
    for term in business_terms:
        if term in text:
            return True
    return False

# Test classification
classified_articles = []
detailed_samples = []

for article in sample_articles[:30]:
    article_id = int(article['article_id'])
    title = article['title']
    description = article['description']
    is_business = is_business_article(title, description)
    
    classified_articles.append({
        'article_id': article_id,
        'title': title[:80],
        'is_business': is_business
    })
    
    if article_id <= 25:  # Get detailed info for first 25
        detailed_samples.append({
            'article_id': article_id,
            'title': title,
            'is_business': is_business
        })

# Count business articles in sample
business_count = sum(1 for a in classified_articles if a['is_business'])

print('__RESULT__:')
print(json.dumps({
    'total_tested': len(classified_articles),
    'business_count': business_count,
    'business_percentage': business_count / len(classified_articles),
    'sample_articles': detailed_samples[:15]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'sample_articles': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.query_db:10': [{'_id': '6969c8f361828b63eb846498', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c8f361828b63eb84649e', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969c8f361828b63eb8464a2', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969c8f361828b63eb8464a3', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969c8f361828b63eb8464aa', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:12': {'total_articles': 14860, 'year_range': '2010 to 2020', 'sample_data': {'3': 2020, '9': 2016, '13': 2015, '14': 2017, '21': 2020}}, 'var_functions.execute_python:14': {'article_count': 14860, 'sample_years': {'3': 2020, '9': 2016, '13': 2015, '14': 2017, '21': 2020, '27': 2013, '43': 2010, '60': 2017, '62': 2018, '63': 2010}, 'business_keywords_count': 38}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_articles': 14860, 'year_range': '2010 to 2020', 'first_10_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63], 'last_10_ids': [127521, 127525, 127561, 127564, 127566, 127567, 127572, 127576, 127577, 127583]}, 'var_functions.execute_python:20': {'total_batches': 15, 'batch_sizes': [1000, 1000, 1000, 1000, 1000], 'total_articles': 14860}, 'var_functions.execute_python:22': {'total_articles': 14860, 'year_range': '2010-2020', 'business_keywords': 60}, 'var_functions.execute_python:24': {'batch_size': 1000, 'min_id': 3, 'max_id': 9038, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_functions.execute_python:26': {'total_articles': 14860, 'yearly_totals': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}, 'expected_batches': 30}, 'var_functions.execute_python:28': {'europe_article_count': 14860, 'year_range': '2010-2020', 'business_keywords': 95}, 'var_functions.execute_python:30': {'samples': [{'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)...', 'is_business': False}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)...", 'is_business': False}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)...', 'is_business': False}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US ...', 'is_business': False}, {'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)...', 'is_business': False}, {'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)...', 'is_business': False}, {'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)...', 'is_business': False}, {'article_id': '8', 'title': 'Safety Net (Forbes.com)...', 'is_business': False}, {'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black...', 'is_business': False}, {'article_id': '10', 'title': "Oil and Economy Cloud Stocks' Outlook...", 'is_business': False}, {'article_id': '11', 'title': 'No Need for OPEC to Pump More-Iran Gov...', 'is_business': False}, {'article_id': '12', 'title': 'Non-OPEC Nations Should Up Output-Purnomo...', 'is_business': False}, {'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start...', 'is_business': False}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap...', 'is_business': False}, {'article_id': '15', 'title': 'Rescuing an Old Saver...', 'is_business': False}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School...', 'is_business': False}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds...', 'is_business': False}, {'article_id': '18', 'title': 'US trade deficit swells in June...', 'is_business': False}, {'article_id': '19', 'title': "Shell 'could be target for Total'...", 'is_business': False}, {'article_id': '20', 'title': 'Google IPO faces Playboy slip-up...', 'is_business': False}], 'business_keywords_count': 82}}

exec(code, env_args)
