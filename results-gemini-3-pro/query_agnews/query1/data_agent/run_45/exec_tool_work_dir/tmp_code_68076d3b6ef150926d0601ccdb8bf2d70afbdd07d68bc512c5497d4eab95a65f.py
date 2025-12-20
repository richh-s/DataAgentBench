code = """import json
import re

file_path = locals()['var_function-call-18177868496750435891']
with open(file_path, 'r') as f:
    data = json.load(f)

# Re-define keywords for debug
keywords = {
    "Sports": {"sport", "olympic", "game", "team", "win", "score", "cup"}
}

debug_results = []
for i in range(10):
    article = data[i]
    title = article.get("title", "") or ""
    desc = article.get("description", "") or ""
    text = (title + " " + desc).lower()
    tokens = set(re.findall(r'\b[a-z]+\b', text))
    
    scores = {}
    for cat, kws in keywords.items():
        scores[cat] = len(tokens.intersection(kws))
    
    debug_results.append({
        "title": title,
        "tokens_sample": list(tokens)[:5],
        "scores": scores
    })

print("__RESULT__:")
print(json.dumps(debug_results))"""

env_args = {'var_function-call-17820231337409902993': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11407415087239536050': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-357563551933968648': {'total_articles': 5, 'sports_articles_count': 0, 'best_article_title': None, 'max_length': -1}, 'var_function-call-4127149747257172605': [{'cnt': '127600'}], 'var_function-call-18177868496750435891': 'file_storage/function-call-18177868496750435891.json', 'var_function-call-16215107973573645152': {'total_sports': 0, 'best_title': None, 'max_len': -1}}

exec(code, env_args)
