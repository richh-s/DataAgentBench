code = """import re, json

def is_business(title, description):
    text = f"{title} {description}".lower()
    keywords = [
        'market', 'markets', 'stock', 'stocks', 'share', 'shares', 'bond', 'bonds',
        'investment', 'investor', 'investors', 'economy', 'economic', 'gdp',
        'unemployment', 'inflation', 'revenue', 'profit', 'losses', 'earnings',
        'merger', 'acquisition', 'ipo', 'bank', 'banks', 'interest rate',
        'currency', 'currencies', 'trade', 'trading', 'business', 'company',
        'companies', 'corporate', 'finance', 'financial', 'budget', 'tariff',
        'tariffs', 'export', 'exports', 'import', 'imports', 'deficit', 'surplus'
    ]
    return any(k in text for k in keywords)

result = json.dumps({'info': 'classification function ready'})
print("__RESULT__:")
print(result)"""

env_args = {'var_call_fLYT2U2c9rcfmcZfieiXnmIl': 'file_storage/call_fLYT2U2c9rcfmcZfieiXnmIl.json', 'var_call_HRXa5UBh9aV00EaGDnI9ulav': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
