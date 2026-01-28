code = """import json

tickers = var_call_zFLlHJFPlho5PrG7ibBaCPJo['first5']

parts = []
for t in tickers:
    parts.append(
        "SELECT '"+t+"' AS Symbol, COUNT(*)::BIGINT AS days_exceeded FROM \""+t+"\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND Low > 0 AND (High - Low) / Low > 0.2"
    )
q = " UNION ALL ".join(parts) + " ORDER BY days_exceeded DESC LIMIT 5;"

print('__RESULT__:')
print(json.dumps({'query': q}))"""

env_args = {'var_call_8z0hOoCRDAGDWUY6KxgLogHY': 'file_storage/call_8z0hOoCRDAGDWUY6KxgLogHY.json', 'var_call_sB1dlFjC01RJNrtqfKeMDI7e': 'file_storage/call_sB1dlFjC01RJNrtqfKeMDI7e.json', 'var_call_EwHLllYQrpKboI1PLYIB8yyd': [{'Symbol': 'AGMH', 'days_exceeded': '13'}], 'var_call_zFLlHJFPlho5PrG7ibBaCPJo': {'n': 86, 'first5': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX']}}

exec(code, env_args)
