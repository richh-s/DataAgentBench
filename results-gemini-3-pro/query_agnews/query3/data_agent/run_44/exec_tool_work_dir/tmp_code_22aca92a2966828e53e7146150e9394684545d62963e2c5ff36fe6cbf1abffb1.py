code = """import json
import pandas as pd

# Load SQLite result (relevant article IDs and dates)
file_path_sqlite = locals()['var_function-call-12172117661927561958']
with open(file_path_sqlite, 'r') as f:
    sqlite_data = json.load(f)

# Create a dictionary for quick lookup of date by article_id
# article_id is string in sqlite_data
id_to_date = {item['article_id']: item['publication_date'] for item in sqlite_data}
relevant_ids = set(id_to_date.keys())

# Load all MongoDB batches
file_paths_mongo = [
    locals()['var_function-call-14756335687159860654'],
    locals()['var_function-call-15687200365796344565'],
    locals()['var_function-call-10571458413555414671']
]

articles = []
for fp in file_paths_mongo:
    with open(fp, 'r') as f:
        batch = json.load(f)
        articles.extend(batch)

# Filter articles
filtered_articles = []
for art in articles:
    aid = art.get('article_id')
    # aid in mongo might be int or string. The preview showed string "0".
    # Ensure it's string for comparison with relevant_ids
    aid_str = str(aid)
    if aid_str in relevant_ids:
        # Attach date
        art['publication_date'] = id_to_date[aid_str]
        filtered_articles.append(art)

print(f"Total relevant articles found: {len(filtered_articles)}")

# Classification keywords for Business
business_keywords = [
    "market", "stock", "economy", "trade", "profit", "bank", "company", 
    "merger", "acquisition", "deal", "oil price", "dollar", "euro", "yen", 
    "fed ", "federal reserve", "finance", "invest", "business", "corporate", 
    "revenue", "sales", "ipo", "wall st", "nasdaq", "dow jones", "inflation",
    "recession", "gdp", "deficit", "currency", "imf", "treasury", "sec ", 
    "earning", "dividend", "debt", "loan", "interest rate", "retail", "consumer"
]
# Lowercase keywords

def is_business(title, description):
    text = (title + " " + description).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Count business articles per year
year_counts = {year: 0 for year in range(2010, 2021)}

business_article_count = 0
for art in filtered_articles:
    if is_business(art.get('title', ''), art.get('description', '')):
        business_article_count += 1
        date = art['publication_date'] # YYYY-MM-DD
        year = int(date[:4])
        if 2010 <= year <= 2020:
            year_counts[year] += 1

print(f"Total Business articles identified: {business_article_count}")
print(f"Yearly counts: {year_counts}")

# Calculate average
total_business = sum(year_counts.values())
average_per_year = total_business / 11.0

print(f"Average: {average_per_year}")

print("__RESULT__:")
print(json.dumps({"average": average_per_year, "yearly_counts": year_counts}))"""

env_args = {'var_function-call-12172117661927561958': 'file_storage/function-call-12172117661927561958.json', 'var_function-call-9564384694485848292': 'file_storage/function-call-9564384694485848292.json', 'var_function-call-14780778531642950489': {'count': 14860}, 'var_function-call-18146700259937133705': [{'_id': '6944e464c20877073e5de45d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e464c20877073e5de45e', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e464c20877073e5de45f', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e464c20877073e5de460', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e464c20877073e5de461', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14838788922583566838': {'min': 3, 'max': 127583}, 'var_function-call-11078228526487049007': [{'_id': '6944e464c20877073e5de45d', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-14756335687159860654': 'file_storage/function-call-14756335687159860654.json', 'var_function-call-15687200365796344565': 'file_storage/function-call-15687200365796344565.json', 'var_function-call-10571458413555414671': 'file_storage/function-call-10571458413555414671.json'}

exec(code, env_args)
