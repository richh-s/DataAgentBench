code = """import json
import re

# Load metadata
with open(locals()['var_function-call-12371501432647915462'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
articles_var = locals()['var_function-call-4746464685426923532']
# Assume it's a file path based on previous success handling (or fail?)
# Wait, previous run didn't fail on loading, it failed on logic (0 matches).
# I used the robust loading logic.
try:
    with open(articles_var, 'r') as f:
        articles_list = json.load(f)
except:
    articles_list = articles_var

meta_map = {str(item['article_id']): item['year'] for item in metadata_list}

categories = {
    "Business": ["market", "stock", "trade", "economy", "economic", "business", "company", "companies", "bank", "profit", "revenue", "loss", "invest", "investment", "investor", "share", "dollar", "euro", "yen", "currency", "ceo", "cfo", "merger", "acquisition", "deal", "oil", "price", "prices", "sales", "corp", "corporate", "inc", "ltd", "exchange", "wall", "street", "fed", "federal", "reserve", "rate", "inflation", "ipo", "dow", "nasdaq", "bond", "futures", "yield", "earning", "earnings", "dividend", "forecast", "analyst", "retail", "consumer"]
}

debug_out = []
for art in articles_list[:20]: # Check first 20 articles in the DB
    aid = str(art['article_id'])
    if aid in meta_map:
        text = (art.get('title', '') + " " + art.get('description', '')).lower()
        tokens = re.findall(r'\w+', text)
        score = 0
        matches = []
        for token in tokens:
            if token in categories["Business"]:
                score += 1
                matches.append(token)
        debug_out.append({"aid": aid, "title": art.get('title'), "score": score, "matches": matches})

print("__RESULT__:")
print(json.dumps(debug_out))"""

env_args = {'var_function-call-12371501432647915462': 'file_storage/function-call-12371501432647915462.json', 'var_function-call-702335989468777751': 14860, 'var_function-call-1127075526552130781': [{'_id': '6944e792b459843e876ccea6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e792b459843e876ccea7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e792b459843e876ccea8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e792b459843e876ccea9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e792b459843e876cceaa', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4746464685426923532': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-18339336169262196336': 0.0}

exec(code, env_args)
