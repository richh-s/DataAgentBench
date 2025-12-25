code = """import json

# Load metadata info
with open(locals()['var_function-call-17031659575952169499'], 'r') as f:
    meta_data = json.load(f)

# The ids list contains integers
target_ids = set(meta_data['ids'])
# The id_year_map has string keys (because JSON) and string values (year)
id_year_map = meta_data['id_year_map']

# Load articles
with open(locals()['var_function-call-5440553202201869458'], 'r') as f:
    articles = json.load(f)

# Business keywords
# Expanded list to be more robust
business_keywords = [
    "business", "economy", "market", "stock", "trade", "finance", "financial", 
    "bank", "company", "corporate", "investment", "investor", "profit", "revenue", 
    "earnings", "share", "dollar", "euro", "currency", "oil", "price", "money", 
    "debt", "fund", "growth", "inflation", "recession", "tax", "jobs", "labor",
    "ceo", "manager", "deal", "sale", "purchase", "merger", "acquisition", 
    "ipo", "fed", "central bank", "rates", "interest", "sector", "industry",
    "wall st", "dow jones", "nasdaq", "s&p", "dividend", "bonds", "futures",
    "treasury", "loan", "mortgage", "retail", "consumer", "spending", "deficit",
    "surplus", "budget", "gdp", "wto", "imf", "opec", "airline", "manufacturer"
]

# Initialize counts for years 2010-2020
counts = {str(y): 0 for y in range(2010, 2021)}

for art in articles:
    # article_id in articles is string
    aid_str = art.get('article_id')
    if aid_str is None:
        continue
    
    try:
        aid_int = int(aid_str)
    except ValueError:
        continue
        
    if aid_int in target_ids:
        # Check category
        title = art.get('title', '')
        desc = art.get('description', '')
        text = (title + ' ' + desc).lower()
        
        # Check for business keywords
        # Simple containment
        if any(kw in text for kw in business_keywords):
            year = id_year_map.get(str(aid_int))
            if year in counts:
                counts[year] += 1

total = sum(counts.values())
num_years = 11 # 2010 to 2020 inclusive
average = total / num_years

print("__RESULT__:")
print(json.dumps({
    "counts": counts,
    "total": total,
    "average": average
}))"""

env_args = {'var_function-call-16631268004823778356': 'file_storage/function-call-16631268004823778356.json', 'var_function-call-17031659575952169499': 'file_storage/function-call-17031659575952169499.json', 'var_function-call-18046042313745119508': [{'_id': '6944dcda061ef77560ea6d84', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dcda061ef77560ea6d85', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dcda061ef77560ea6d86', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dcda061ef77560ea6d87', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dcda061ef77560ea6d88', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5440553202201869458': 'file_storage/function-call-5440553202201869458.json'}

exec(code, env_args)
