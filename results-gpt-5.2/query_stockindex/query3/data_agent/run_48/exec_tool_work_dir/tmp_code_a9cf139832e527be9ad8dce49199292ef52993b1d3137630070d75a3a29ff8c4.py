code = """import json, pandas as pd

rows = var_call_d9WTOgWh7vdK8HGlgPmf2BQi

def country_for_index(idx: str) -> str:
    # minimal mapping based on common major indices
    mapping = {
        '399001.SZ': 'China',          # Shenzhen Component (SZSE)
        '000001.SS': 'China',          # SSE Composite (Shanghai)
        'IXIC': 'United States',       # NASDAQ Composite
        'NYA': 'United States',        # NYSE Composite
        'NSEI': 'India',               # NIFTY 50 (NSE)
    }
    return mapping.get(idx, 'Unknown')

out = []
for r in rows:
    out.append({
        'Index': r['Index'],
        'Country': country_for_index(r['Index']),
        'OverallGrowth': float(r['OverallGrowth']),
        'Months': int(r['Months']),
    })

result = json.dumps(out)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_aGYrP5ET6fA58mrEDUr0sRrH': ['index_info'], 'var_call_7rrUF5w39S0v7HIJGJVmPZKm': ['index_trade'], 'var_call_URMhRajg0xezfCdDZZeHfESe': [], 'var_call_bbm6d5rc8dODDxPfuzZWoGbz': [{'sample_date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'sample_date': '2017-10-12 00:00:00', 'n': '11'}, {'sample_date': '2015-01-16 00:00:00', 'n': '11'}, {'sample_date': '2012-06-18 00:00:00', 'n': '10'}, {'sample_date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'sample_date': '27 Sep 2013, 00:00', 'n': '10'}, {'sample_date': '12 Nov 2010, 00:00', 'n': '10'}, {'sample_date': '15 May 2019, 00:00', 'n': '10'}, {'sample_date': '2017-06-14 00:00:00', 'n': '10'}, {'sample_date': 'July 12, 2010 at 12:00 AM', 'n': '10'}], 'var_call_d9WTOgWh7vdK8HGlgPmf2BQi': [{'Index': '399001.SZ', 'OverallGrowth': '3.7592027372691157', 'Months': '257'}, {'Index': 'IXIC', 'OverallGrowth': '3.4892179344618204', 'Months': '256'}, {'Index': 'NSEI', 'OverallGrowth': '3.103308772715655', 'Months': '164'}, {'Index': 'NYA', 'OverallGrowth': '2.518350405505012', 'Months': '256'}, {'Index': '000001.SS', 'OverallGrowth': '2.3553662336011323', 'Months': '256'}]}

exec(code, env_args)
