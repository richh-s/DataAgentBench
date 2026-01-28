code = """import json
# data from previous query
data = var_call_28itDxWXWLSQ9KF43AnUk4Fk
# Define which indices belong to Asia (inferred)
asia_set = {"399001.SZ", "000001.SS", "NSEI", "HSI", "TWII", "N225"}
# Friendly names for clarity
names = {
    "399001.SZ": "SZSE Component Index (China - Shenzhen)",
    "000001.SS": "SSE Composite Index (China - Shanghai)",
    "NSEI": "Nifty 50 (India)",
    "HSI": "Hang Seng Index (Hong Kong)",
    "TWII": "Taiwan Weighted Index (Taiwan)",
    "N225": "Nikkei 225 (Japan)"
}
# Filter and convert types
asia_data = []
for d in data:
    if d.get('Index') in asia_set:
        try:
            avg = float(d.get('avg_intraday_volatility'))
        except:
            avg = None
        try:
            days = int(d.get('days'))
        except:
            days = None
        asia_data.append({
            'Index': d.get('Index'),
            'avg_intraday_volatility': avg,
            'days': days,
            'name': names.get(d.get('Index'))
        })
# Find the max by avg_intraday_volatility
if not asia_data:
    result = {'error': 'No Asia indices found in the data.'}
else:
    best = max(asia_data, key=lambda x: (x['avg_intraday_volatility'] if x['avg_intraday_volatility'] is not None else -1))
    result = best
# Print in required format as JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_G9OWvw5Fqh8tx0NEwnIPhlYY': ['index_trade'], 'var_call_Tu5aEIJoi5N8hG3th2p2Fsqi': ['index_info'], 'var_call_fJKb3yXN4KDf3J8AoAzavVN3': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'IXIC'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_call_28itDxWXWLSQ9KF43AnUk4Fk': [{'Index': '399001.SZ', 'avg_intraday_volatility': '0.020202435308195866', 'days': '2719'}, {'Index': '000001.SS', 'avg_intraday_volatility': '0.01731142407102674', 'days': '2752'}, {'Index': 'NSEI', 'avg_intraday_volatility': '0.01585173971531033', 'days': '1610'}, {'Index': 'HSI', 'avg_intraday_volatility': '0.01382304680245353', 'days': '4006'}, {'Index': 'GDAXI', 'avg_intraday_volatility': '0.013633557197891789', 'days': '3881'}, {'Index': 'TWII', 'avg_intraday_volatility': '0.01348835226084207', 'days': '2751'}, {'Index': 'J203.JO', 'avg_intraday_volatility': '0.012946183900303701', 'days': '1210'}, {'Index': 'SSMI', 'avg_intraday_volatility': '0.012884854571066692', 'days': '3559'}, {'Index': 'N100', 'avg_intraday_volatility': '0.012567255105983891', 'days': '2595'}, {'Index': 'IXIC', 'avg_intraday_volatility': '0.009869805134210418', 'days': '5624'}, {'Index': 'GSPTSE', 'avg_intraday_volatility': '0.009024336652288918', 'days': '4830'}, {'Index': 'N225', 'avg_intraday_volatility': '0.008720764073041308', 'days': '6349'}, {'Index': 'NYA', 'avg_intraday_volatility': '0.004147514635438383', 'days': '6265'}]}

exec(code, env_args)
