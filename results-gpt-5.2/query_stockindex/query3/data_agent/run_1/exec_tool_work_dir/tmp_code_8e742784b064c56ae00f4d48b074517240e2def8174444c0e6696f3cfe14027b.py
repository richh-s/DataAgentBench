code = """import json

top5 = var_call_ZUduLRJb6ZkTVEwaIgvofRYU

country_map = {
    'IXIC':'United States',
    'NSEI':'India',
    'GDAXI':'Germany',
    '399001.SZ':'China',
    'TWII':'Taiwan',
    '000001.SS':'China',
    'GSPTSE':'Canada',
    'HSI':'Hong Kong',
    'J203.JO':'South Africa',
    'N100':'United States',
    'N225':'Japan',
    'NYA':'United States',
    'SSMI':'Switzerland'
}

for r in top5:
    r['country'] = country_map.get(r['Index'], r.get('country','Unknown'))

# build plain text answer
lines = []
for i,r in enumerate(top5, start=1):
    lines.append(f"{i}. {r['Index']} — {r['country']} — overall return multiple: {r['multiple']:.2f}x")
answer = "Top 5 indices by overall return from regular monthly investing since 2000 (using month-end CloseUSD):\n" + "\n".join(lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_ryiXunWus6mqQh1ibHkPJRe9': ['index_info'], 'var_call_qS2g06b5g97CAOMhjZ7rFZaD': ['index_trade'], 'var_call_lZlRbskbKMvFjEA7vJaatpbx': 'file_storage/call_lZlRbskbKMvFjEA7vJaatpbx.json', 'var_call_ZUduLRJb6ZkTVEwaIgvofRYU': [{'Index': 'IXIC', 'country': 'United States', 'multiple': 4.816205036184269, 'months': 257, 'first_month': '2000-01-31 00:00:00', 'last_month': '2021-05-31 00:00:00'}, {'Index': 'NSEI', 'country': 'India', 'multiple': 2.3564091777426452, 'months': 165, 'first_month': '2007-09-30 00:00:00', 'last_month': '2021-05-31 00:00:00'}, {'Index': 'GDAXI', 'country': 'Germany', 'multiple': 2.3537005565588847, 'months': 257, 'first_month': '2000-01-31 00:00:00', 'last_month': '2021-05-31 00:00:00'}, {'Index': '399001.SZ', 'country': 'China', 'multiple': 2.3383811889670953, 'months': 258, 'first_month': '2000-01-31 00:00:00', 'last_month': '2021-06-30 00:00:00'}, {'Index': 'TWII', 'country': 'Unknown', 'multiple': 2.2447368452852596, 'months': 257, 'first_month': '2000-01-31 00:00:00', 'last_month': '2021-05-31 00:00:00'}], 'var_call_hbjiJHG3ZBdV0lj5ZHhDmneq': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}]}

exec(code, env_args)
