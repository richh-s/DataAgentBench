code = """import json
recs = var_call_A3bJG9UHjOZxAqIy1hkRrw4w
country_map2 = {'IXIC':'United States','GDAXI':'Germany','NSEI':'India','TWII':'Taiwan','399001.SZ':'China'}
for r in recs:
    if r.get('country') is None:
        r['country'] = country_map2.get(r['idx'])
lines = []
for i,r in enumerate(recs, start=1):
    lines.append(f"{i}. {r['idx']} — {r['country']} — overall return multiple: {r['multiple']:.2f}x")
ans = "Top 5 indices by overall return for monthly investing since 2000 (CloseUSD; $1 invested on first trading day each month):\n" + "\n".join(lines)
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_fZBYlUx6uQezfyNSTEW6jvqQ': 'file_storage/call_fZBYlUx6uQezfyNSTEW6jvqQ.json', 'var_call_A3bJG9UHjOZxAqIy1hkRrw4w': [{'idx': 'IXIC', 'multiple': 4.822046767118095, 'months': 257, 'invested_usd': 257.0, 'final_value_usd': 1239.2660191493503, 'country': None, 'start_dt': '2000-01-06 00:00:00', 'last_dt': '2021-05-27 00:00:00'}, {'idx': 'NSEI', 'multiple': 2.3608849755128487, 'months': 165, 'invested_usd': 165.0, 'final_value_usd': 389.54602095962, 'country': None, 'start_dt': '2007-09-25 00:00:00', 'last_dt': '2021-05-31 00:00:00'}, {'idx': 'GDAXI', 'multiple': 2.347462383645538, 'months': 257, 'invested_usd': 257.0, 'final_value_usd': 603.2978325969033, 'country': None, 'start_dt': '2000-01-05 00:00:00', 'last_dt': '2021-05-31 00:00:00'}, {'idx': '399001.SZ', 'multiple': 2.344545336356674, 'months': 258, 'invested_usd': 258.0, 'final_value_usd': 604.8926967800219, 'country': 'China', 'start_dt': '2000-01-05 00:00:00', 'last_dt': '2021-06-02 00:00:00'}, {'idx': 'TWII', 'multiple': 2.2374061754244634, 'months': 257, 'invested_usd': 257.0, 'final_value_usd': 575.0133870840871, 'country': None, 'start_dt': '2000-01-17 00:00:00', 'last_dt': '2021-05-26 00:00:00'}]}

exec(code, env_args)
