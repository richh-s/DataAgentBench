code = """import json, pandas as pd

# top candidates from both chunks
c1 = var_call_CzGaSBTCF7QO1JSAX3VImnzG
c2 = var_call_yrfW0F92yMn7Tezu95oqnPjs

cand = pd.DataFrame(c1 + c2)
cand['days_exceed_20pct'] = cand['days_exceed_20pct'].astype(float)
# overall top 5
cand_top = cand.sort_values(['days_exceed_20pct','Symbol'], ascending=[False, True]).head(5)

# map to company names
with open(var_call_7P2pKW2MvdjwPJAT38jWRKoj, 'r', encoding='utf-8') as f:
    cap = json.load(f)
cap_df = pd.DataFrame(cap)
name_map = cap_df.set_index('Symbol')['company_name'].to_dict()

cand_top['company_name'] = cand_top['Symbol'].map(name_map)

out = cand_top[['company_name']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_7P2pKW2MvdjwPJAT38jWRKoj': 'file_storage/call_7P2pKW2MvdjwPJAT38jWRKoj.json', 'var_call_bmf0BnCD1Y3a4ithfN0awrMh': 'file_storage/call_bmf0BnCD1Y3a4ithfN0awrMh.json', 'var_call_kFjbYZ0s15AJ39Vk9DSBz8tr': [{'Symbol': 'AGMH', 'cnt': '13'}], 'var_call_OGK4qMhQNVQY6NfHK9uE4rjV': {'a': 1}, 'var_call_OaUTqaJ748bgeupqPoS5SImr': {'tickers_n': 86, 'chunks': 2, 'first_query_len': 9773}, 'var_call_JHYRHuDoX4u0Y4SWiCXqAyhD': {'use_tickers_n': 86, 'kern_in_trade': False, 'missing_from_trade': ['KERN'], 'sample_last10': ['TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_EiO3AuR7kdL9AHjoE79ZZLWd': 'file_storage/call_EiO3AuR7kdL9AHjoE79ZZLWd.json', 'var_call_yQtAKpdX9sn4Zw7tTf9VwCh0': {'tickers_n': 86, 'chunks': 2, 'q1_preview': 'SELECT \'AGMH\' AS Symbol, COUNT(*)::BIGINT AS cnt FROM "AGMH" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High - Low) > 0.2*Low UNION ALL SELECT \'ALACU\' AS Symbol, COUNT(*)::BIGINT AS cnt FROM "ALACU" WHERE Date >= \'2019-01-01\' AND Date <= \'2019-12-31\' AND Low > 0 AND (High -'}, 'var_call_CzGaSBTCF7QO1JSAX3VImnzG': [{'Symbol': 'GLG', 'days_exceed_20pct': '42.0'}, {'Symbol': 'CBAT', 'days_exceed_20pct': '23.0'}, {'Symbol': 'FAMI', 'days_exceed_20pct': '23.0'}, {'Symbol': 'FTFT', 'days_exceed_20pct': '21.0'}, {'Symbol': 'BIOC', 'days_exceed_20pct': '21.0'}], 'var_call_VOSuYN1B4mdr74j5yUG4d2t6': {'chunks': [['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU'], ['OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']]}, 'var_call_yrfW0F92yMn7Tezu95oqnPjs': [{'Symbol': 'SES', 'days_exceed_20pct': '51.0'}, {'Symbol': 'TMSR', 'days_exceed_20pct': '40.0'}, {'Symbol': 'VERB', 'days_exceed_20pct': '38.0'}, {'Symbol': 'SNSS', 'days_exceed_20pct': '32.0'}, {'Symbol': 'PECK', 'days_exceed_20pct': '19.0'}]}

exec(code, env_args)
