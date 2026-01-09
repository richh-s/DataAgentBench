code = """import json
import pandas as pd

top5 = pd.DataFrame(var_call_ZiBpdp4cEchUODNlf5EYfV8z)

country_map = {
  '399001.SZ': 'China (Shenzhen Stock Exchange)',
  '000001.SS': 'China (Shanghai Stock Exchange)',
  'N225': 'Japan (Tokyo Stock Exchange)',
  'IXIC': 'United States (NASDAQ)',
  'N100': 'Europe (Euronext / pan-European)'
}

top5['Country'] = top5['Index'].map(country_map).fillna('Unknown')
# ensure numeric
for c in ['DCA_Return_Multiplier','Months']:
    top5[c] = pd.to_numeric(top5[c], errors='coerce')

out = top5[['Index','Country','DCA_Return_Multiplier','Months']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_YuWv4jOvt2e0MSzTrSEggocQ': ['index_trade'], 'var_call_8C1SPOJa5X63t3w3T7w2rD4k': ['index_info'], 'var_call_xZeP80RvrdhlzmS8GlsT7cto': [], 'var_call_drp7bB72MFSgcOswXS0RHUoy': [{'Date': 'January 27, 2015 at 12:00 AM', 'n': '11'}, {'Date': '2017-10-12 00:00:00', 'n': '11'}, {'Date': '2015-01-16 00:00:00', 'n': '11'}, {'Date': '2012-06-18 00:00:00', 'n': '10'}, {'Date': '2013-05-21 00:00:00', 'n': '10'}, {'Date': '15 May 2019, 00:00', 'n': '10'}, {'Date': '2012-05-25 00:00:00', 'n': '10'}, {'Date': 'June 19, 2019 at 12:00 AM', 'n': '10'}, {'Date': '12 Nov 2010, 00:00', 'n': '10'}, {'Date': '07 Apr 2011, 00:00', 'n': '10'}], 'var_call_ZiBpdp4cEchUODNlf5EYfV8z': [{'Index': '399001.SZ', 'DCA_Return_Multiplier': '259.11225532857605', 'Months': '258'}, {'Index': 'N225', 'DCA_Return_Multiplier': '257.7654476327984', 'Months': '258'}, {'Index': 'IXIC', 'DCA_Return_Multiplier': '257.5928016844276', 'Months': '257'}, {'Index': 'N100', 'DCA_Return_Multiplier': '257.53799932019905', 'Months': '258'}, {'Index': '000001.SS', 'DCA_Return_Multiplier': '257.3925179045435', 'Months': '257'}]}

exec(code, env_args)
