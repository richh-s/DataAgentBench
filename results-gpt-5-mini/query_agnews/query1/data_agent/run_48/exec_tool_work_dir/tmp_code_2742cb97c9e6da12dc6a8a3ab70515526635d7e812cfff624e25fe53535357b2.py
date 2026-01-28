code = """import json
# var_call_jQANsMN05Xlp0l88BGMZI2eW is available from previous query
data = var_call_jQANsMN05Xlp0l88BGMZI2eW
sports_keywords = ['sport','football','soccer','basketball','baseball','hockey','tennis','golf','cricket','goal','score','match','season','coach','player','team','win','olympic','world cup','cup']
found = []
for rec in data:
    text = (rec.get('title','') + ' ' + rec.get('description','')).lower()
    if any(kw in text for kw in sports_keywords):
        found.append(rec)
if not found:
    result = {"sports_found": False, "message": "No sports articles found"}
else:
    for r in found:
        r['description_length'] = len(r.get('description',''))
    maxlen = max(r['description_length'] for r in found)
    candidates = [r for r in found if r['description_length']==maxlen]
    titles = [r['title'] for r in candidates]
    result = {"sports_found": True, "max_description_length": maxlen, "titles": titles}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jQANsMN05Xlp0l88BGMZI2eW': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
