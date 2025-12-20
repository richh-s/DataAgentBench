code = """import json
import re

# Load data
meta_var = locals()['var_function-call-12987280970809318212']
with open(meta_var, 'r') as f:
    meta_list = json.load(f)

art_var = locals()['var_function-call-10227214225653299707']
with open(art_var, 'r') as f:
    art_list = json.load(f)

id_to_year = {}
for m in meta_list:
    aid = int(m['article_id'])
    date = m['publication_date']
    year = int(date[:4])
    if 2010 <= year <= 2020:
        id_to_year[aid] = year

categories = {
    'Business': ['business', 'economy', 'market', 'financial', 'stock', 'share', 'trade', 'investment', 'bank', 'money', 'price', 'profit', 'loss', 'corp', 'tax', 'rate', 'dollar', 'euro', 'yen', 'budget', 'debt', 'inflation', 'recession', 'growth', 'sale', 'deal', 'merger', 'acquisition', 'industry', 'commercial', 'wall street', 'dow', 'nasdaq', 'oil', 'gas', 'energy', 'bonds', 'futures', 'forex', 'ceo', 'cfo', 'fed', 'treasury', 'imf', 'wto', 'opec'],
    'Sports': ['sport', 'game', 'team', 'cup', 'league', 'player', 'match', 'win', 'score', 'olympic', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf'],
    'SciTech': ['science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'space', 'nasa', 'study', 'research', 'virus', 'phone', 'mobile', 'apple', 'google', 'microsoft'],
    'World': ['world', 'war', 'peace', 'election', 'president', 'minister', 'attack', 'bomb', 'kill', 'government', 'police', 'court', 'law', 'china', 'russia', 'iran', 'iraq', 'uk', 'france', 'germany']
}

debug_results = []
count = 0

for art in art_list:
    aid = int(art['article_id'])
    if aid in id_to_year:
        title = art.get('title', '')
        desc = art.get('description', '')
        full_text = title + " " + desc
        text_lower = full_text.lower()
        
        scores = {}
        for cat, kws in categories.items():
            s = 0
            for kw in kws:
                if kw in text_lower: # relaxed check
                    s += 1
            scores[cat] = s
        
        debug_results.append({
            "id": aid,
            "text": full_text[:200], # truncated
            "scores": scores
        })
        count += 1
        if count >= 10:
            break

print("__RESULT__:")
print(json.dumps(debug_results))"""

env_args = {'var_function-call-12987280970809318212': 'file_storage/function-call-12987280970809318212.json', 'var_function-call-3327544021322435934': 'file_storage/function-call-3327544021322435934.json', 'var_function-call-5544368014430609247': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-11134278749745899859': [{'_id': '6944cce21659048c9db08bdd', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cce21659048c9db08bde', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cce21659048c9db08bdf', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cce21659048c9db08be0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cce21659048c9db08be1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1079264442624552925': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10815997547170822222': {'year_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'processed': 1, 'total_business': 0}, 'var_function-call-10227214225653299707': 'file_storage/function-call-10227214225653299707.json', 'var_function-call-16728244327291461152': {'year_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'processed': 14860, 'total_business': 0, 'average': 0.0}}

exec(code, env_args)
