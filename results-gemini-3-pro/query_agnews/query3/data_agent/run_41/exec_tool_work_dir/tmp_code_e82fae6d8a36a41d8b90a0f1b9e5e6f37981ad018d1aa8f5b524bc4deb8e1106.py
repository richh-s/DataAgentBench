code = """import json

# Load SQL data
with open(locals()['var_function-call-7467905940371766253'], 'r') as f:
    sql_data = json.load(f)

# Map article_id to year
article_years = {}
for item in sql_data:
    try:
        aid = int(item['article_id'])
        year = int(item['publication_date'][:4])
        article_years[aid] = year
    except:
        pass

# Load Mongo data
with open(locals()['var_function-call-1394331188292423332'], 'r') as f:
    mongo_data = json.load(f)

# Keywords
keywords = [
    "business", "economy", "economic", "financial", "finance", "market", "stock", "wall street", 
    "nasdaq", "dow jones", "invest", "trade", "corporate", "commercial", "bank", "banking", 
    "profit", "revenue", "merger", "acquisition", "fiscal", "tax", "debt", "loan", "credit", 
    "rates", "inflation", "recession", "currency", "forex", "imf", "gdp", "treasury", "bond", 
    "equity", "asset", "dividend", "shareholder", "ipo", "oil price", "retail sales", "fed", 
    "central bank", "eurozone", "ecb", "unemployment", "jobless", "dow", "jobs", "industry", 
    "sector", "manufacturing", "growth", "spending", "deficit", "euro", "dollar", "yen"
]

year_counts = {y: 0 for y in range(2010, 2021)}
matched_count = 0

for article in mongo_data:
    try:
        aid = int(article.get('article_id', -1))
    except:
        continue
    
    if aid in article_years:
        year = article_years[aid]
        if 2010 <= year <= 2020:
            title = article.get('title', '')
            desc = article.get('description', '')
            text = (title + " " + desc).lower()
            
            # Check keywords
            is_business = False
            for kw in keywords:
                # Simple substring match
                if kw in text:
                    is_business = True
                    break
            
            if is_business:
                year_counts[year] += 1
                matched_count += 1

average = sum(year_counts.values()) / 11.0

print("__RESULT__:")
print(json.dumps({
    "year_counts": year_counts,
    "total_business": matched_count,
    "average": average
}))"""

env_args = {'var_function-call-7467905940371766253': 'file_storage/function-call-7467905940371766253.json', 'var_function-call-1644599123648687577': {'count': 14860, 'sample_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_function-call-668677080249719797': [{'_id': '6944e28f9f41bd8ac07c2355', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e28f9f41bd8ac07c2356', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e28f9f41bd8ac07c2357', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e28f9f41bd8ac07c2358', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e28f9f41bd8ac07c2359', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17424594795480808404': {'year_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total_business': 0, 'average': 0.0}, 'var_function-call-888419918606495775': {'sql_count': 14860, 'mongo_count': 5, 'overlap_count': 1, 'sample_titles': ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)']}, 'var_function-call-1394331188292423332': 'file_storage/function-call-1394331188292423332.json'}

exec(code, env_args)
