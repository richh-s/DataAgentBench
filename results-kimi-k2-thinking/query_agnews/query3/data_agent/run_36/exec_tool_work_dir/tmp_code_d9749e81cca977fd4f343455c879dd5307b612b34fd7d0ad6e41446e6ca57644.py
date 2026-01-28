code = """import json
import re
from collections import defaultdict

# Read European articles with years
year_file_path = var_functions.query_db:20
with open(year_file_path, 'r') as f:
    europe_articles_meta = json.load(f)

# Read all articles content (2000 sample)
content_file_path = var_functions.query_db:24
with open(content_file_path, 'r') as f:
    all_articles_content = json.load(f)

# Create a mapping of article_id to content
content_map = {int(article['article_id']): article for article in all_articles_content}

# Business keywords
business_keywords = [
    'business', 'economy', 'stock', 'stocks', 'wall st', 'wall street', 'dollar', 'trade', 'deficit', 'oil', 'google', 'ipo', 'shares', 'profit', 'loss', 'investment', 'bank', 'banking', 'market', 'markets', 'finance', 'financial', 'economic', 'corporate', 'company', 'companies', 'sector', 'industry', 'retail', 'sales', 'rate', 'rates', 'interest', 'jobs', 'employment', 'unemployment', 'growth', 'gdp', 'inflation', 'revenue', 'earnings', 'fund', 'funds', 'investor', 'investors', 'capital', 'currency', 'currencies', 'export', 'import', 'price', 'prices', 'cost', 'costs', 'budget', 'deficit', 'surplus', 'boom', 'recession', 'crisis', 'merger', 'acquisition', 'deal', 'deals'
]

# Process the European articles
business_articles_by_year = defaultdict(int)
total_processed = 0

for article_meta in europe_articles_meta:
    article_id = int(article_meta['article_id'])
    year = article_meta['year']
    
    if article_id in content_map:
        article = content_map[article_id]
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        
        # Check if it's business-related
        is_business = False
        for keyword in business_keywords:
            if keyword in title or keyword in description:
                is_business = True
                break
        
        if is_business:
            business_articles_by_year[year] += 1
            total_processed += 1

# Calculate average
years_2010_2020 = [str(year) for year in range(2010, 2021)]
business_counts = [business_articles_by_year.get(year, 0) for year in years_2010_2020]
total_business = sum(business_counts)
average_per_year = total_business / len(years_2010_2020)

result = {
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_business_articles_2010_2020': total_business,
    'business_articles_by_year': dict(business_articles_by_year)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_europe_articles': 14860, 'articles_per_year': {'2020': 1366, '2016': 1364, '2015': 1357, '2017': 1391, '2013': 1354, '2010': 1306, '2018': 1351, '2019': 1328, '2014': 1372, '2011': 1316, '2012': 1355}, 'sample_data': [{'article_id': 3, 'year': 2020, 'publication_date': '2020-03-04'}, {'article_id': 9, 'year': 2016, 'publication_date': '2016-05-24'}, {'article_id': 13, 'year': 2015, 'publication_date': '2015-10-17'}, {'article_id': 14, 'year': 2017, 'publication_date': '2017-09-08'}, {'article_id': 21, 'year': 2020, 'publication_date': '2020-04-06'}]}, 'var_functions.query_db:13': [{'_id': '6969c5d0c0cd6f23b7593a65', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c5d0c0cd6f23b7593a6b', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969c5d0c0cd6f23b7593a6f', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969c5d0c0cd6f23b7593a70', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969c5d0c0cd6f23b7593a77', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}, {'_id': '6969c5d0c0cd6f23b7593a7d', 'article_id': '27', 'title': 'HP shares tumble on profit news', 'description': 'Hewlett-Packard shares fall after disappointing third-quarter profits, while the firm warns the final quarter will also fall short of expectations.'}, {'_id': '6969c5d0c0cd6f23b7593a8d', 'article_id': '43', 'title': 'Grant to aid Lynn Central Square', 'description': 'Central Square in Lynn should be looking a bit brighter. New sidewalks, curbs, fences, lights, landscaping, and road improvements are planned for the Gateway Artisan Block, a key area of the square, with \\$830,000 in state grant money given to Lynn last week.'}, {'_id': '6969c5d0c0cd6f23b7593a9e', 'article_id': '60', 'title': 'Oldsmobile: The final parking lot', 'description': 'Why General Motors dropped the Oldsmobile. The four brand  paradoxes GM had to face - the name, the product, image re-positioning, and the consumer - all added up to a brand that had little hope of rebranding.'}, {'_id': '6969c5d0c0cd6f23b7593aa0', 'article_id': '62', 'title': 'Downhome Pinoy Blues, Intersecting Life Paths, and Heartbreak Songs', 'description': "The Blues is alive and well in the Philippines, as evidenced by this appreciation of the Pinoy Blues band 'Lampano Alley', penned by columnist Clarence Henderson as a counterpoint to his usual economics, business, and culture fare."}, {'_id': '6969c5d0c0cd6f23b7593aa1', 'article_id': '63', 'title': 'The Real Time Modern Manila Blues: Bill Monroe Meets Muddy Waters in the Orient', 'description': 'Globalization does strange things to people. A day in the life of a Manila Philippines based business consultant - proving that you really CAN talk about Muddy Walters, bluegrass and work all on the same page...'}], 'var_functions.query_db:16': [{'total_europe_articles': '14860'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
