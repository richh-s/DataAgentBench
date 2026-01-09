code = """import json

rows = var_call_7AVh247hD636LpxYB2XqFcKW
fix = {'IXIC':'United States','GDAXI':'Germany','TWII':'Taiwan'}
for r in rows:
    c = r.get('Country')
    if isinstance(c, str):
        continue
    r['Country'] = fix.get(r['Index'])

ans_lines = []
for i,r in enumerate(rows, start=1):
    ans_lines.append(f"{i}. {r['Index']} — {r['Country']} — total return (DCA since 2000): {r['total_return_pct']:.1f}%")
answer = "Top 5 indices by overall return for monthly $1 DCA since 2000 (using first trading day each month, CloseUSD):\n" + "\n".join(ans_lines)
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_xN7QGS8DGTDZccYycOsH3Mw7': 'file_storage/call_xN7QGS8DGTDZccYycOsH3Mw7.json', 'var_call_aMRtFzom1Dse7n6ySG0WwHl3': ['index_info'], 'var_call_O8PCIru3pEzeo822r5WHCMD0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_7AVh247hD636LpxYB2XqFcKW': [{'Index': 'IXIC', 'Country': nan, 'return_multiple': 4.822046767118095, 'total_return_pct': 382.20467671180944}, {'Index': 'GDAXI', 'Country': nan, 'return_multiple': 2.3474623836455386, 'total_return_pct': 134.74623836455385}, {'Index': '399001.SZ', 'Country': 'China', 'return_multiple': 2.344545336356674, 'total_return_pct': 134.45453363566742}, {'Index': 'TWII', 'Country': nan, 'return_multiple': 2.2374061754244634, 'total_return_pct': 123.74061754244634}, {'Index': 'N225', 'Country': 'Japan', 'return_multiple': 2.1545960543214786, 'total_return_pct': 115.45960543214787}]}

exec(code, env_args)
