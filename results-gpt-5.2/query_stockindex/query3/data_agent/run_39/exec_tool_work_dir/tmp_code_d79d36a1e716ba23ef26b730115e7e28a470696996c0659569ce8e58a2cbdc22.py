code = """import json, pandas as pd
rows = var_call_FRHuJoruVrwuT3hg1FhSXt62

df = pd.DataFrame(rows)
country_map2 = {
    'IXIC':'United States',
    'GDAXI':'Germany',
    'NSEI':'India',
    'TWII':'Taiwan',
    '399001.SZ':'China'
}
df['country'] = df['Index'].map(country_map2).fillna(df.get('country','Unknown'))

# format multiples
out_lines = []
for i,r in df.iterrows():
    out_lines.append(f"{i+1}. {r['Index']} — {r['country']} — total return multiple: {r['multiple']:.2f}x")
answer = "Top 5 indices by value from $1 invested monthly since 2000 (using first trading day each month, USD closes):\n" + "\n".join(out_lines)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_9FQratsz5fiBvcjfD6Cotnke': ['index_info'], 'var_call_jPgJrsQnZeAE6Bp8dl43bHpP': ['index_trade'], 'var_call_5IMktDah33pEtPM9sdniGwm4': 'file_storage/call_5IMktDah33pEtPM9sdniGwm4.json', 'var_call_FRHuJoruVrwuT3hg1FhSXt62': [{'Index': 'IXIC', 'country': 'Unknown', 'months': 257, 'total_invested_usd': 257.0, 'final_value_usd': 1239.2660191493503, 'multiple': 4.822046767118095}, {'Index': 'NSEI', 'country': 'Unknown', 'months': 165, 'total_invested_usd': 165.0, 'final_value_usd': 389.54602095962, 'multiple': 2.3608849755128487}, {'Index': 'GDAXI', 'country': 'Unknown', 'months': 257, 'total_invested_usd': 257.0, 'final_value_usd': 603.2978325969034, 'multiple': 2.3474623836455386}, {'Index': '399001.SZ', 'country': 'China', 'months': 258, 'total_invested_usd': 258.0, 'final_value_usd': 604.8926967800219, 'multiple': 2.344545336356674}, {'Index': 'TWII', 'country': 'Unknown', 'months': 257, 'total_invested_usd': 257.0, 'final_value_usd': 575.0133870840871, 'multiple': 2.2374061754244634}]}

exec(code, env_args)
