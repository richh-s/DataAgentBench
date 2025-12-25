code = """import json
import re

file_path = locals()['var_function-call-18177868496750435891']
with open(file_path, 'r') as f:
    data = json.load(f)

article = data[0]
title = article.get("title", "")
desc = article.get("description", "")
text = (str(title) + " " + str(desc)).lower()

tokens_re = re.findall(r'\b[a-z]+\b', text)
tokens_split = text.split()

debug_info = {
    "article_keys": list(article.keys()),
    "title_val": title,
    "desc_val": desc,
    "text_preview": text[:100],
    "tokens_re_count": len(tokens_re),
    "tokens_split_sample": tokens_split[:5]
}

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-17820231337409902993': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11407415087239536050': [{'_id': '694486b6b33217ab0ded7866', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694486b6b33217ab0ded7867', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694486b6b33217ab0ded7868', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694486b6b33217ab0ded7869', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694486b6b33217ab0ded786a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-357563551933968648': {'total_articles': 5, 'sports_articles_count': 0, 'best_article_title': None, 'max_length': -1}, 'var_function-call-4127149747257172605': [{'cnt': '127600'}], 'var_function-call-18177868496750435891': 'file_storage/function-call-18177868496750435891.json', 'var_function-call-16215107973573645152': {'total_sports': 0, 'best_title': None, 'max_len': -1}, 'var_function-call-17906700582839264187': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Money Funds Fell in Latest Week (AP)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Safety Net (Forbes.com)', 'tokens_sample': [], 'scores': {'Sports': 0}}, {'title': 'Wall St. Bears Claw Back Into the Black', 'tokens_sample': [], 'scores': {'Sports': 0}}]}

exec(code, env_args)
