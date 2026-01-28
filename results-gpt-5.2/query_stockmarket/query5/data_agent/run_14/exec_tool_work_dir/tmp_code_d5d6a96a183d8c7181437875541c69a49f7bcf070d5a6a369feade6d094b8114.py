code = """import json, pandas as pd

top = pd.DataFrame(var_call_yyzVYg4VyIFJ8sFLXyJfOKy2)
info = pd.DataFrame(var_call_kmhyBGAshoF5XOyccfBv8BKq)
# company_name in this dataset includes description; take the name up to first period if present
info['company_name_clean'] = info['company_name'].str.split('.').str[0].str.strip()
merged = top.merge(info, on='Symbol', how='left')
merged['company_name_clean'] = merged['company_name'].str.split('.').str[0].str.strip()
merged['days_over_20pct'] = merged['days_over_20pct'].astype(float).astype(int)
merged = merged.sort_values(['days_over_20pct','Symbol'], ascending=[False, True])
result_lines = [f"{r.company_name_clean} ({r.Symbol})" for r in merged.itertuples(index=False)]
print('__RESULT__:')
print(json.dumps({'companies': result_lines}))"""

env_args = {'var_call_uLyJm1FW9XUZpkWFLLdTk1x8': 'file_storage/call_uLyJm1FW9XUZpkWFLLdTk1x8.json', 'var_call_mA403jh9R1Bu4KDfW34Zcfk9': {'n_total_symbols': 86, 'n_common_symbols': 76, 'symbols_sample': ['AGMH', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT']}, 'var_call_wiTjaVSyXiJ9Z5mRdl3fhPV8': 'file_storage/call_wiTjaVSyXiJ9Z5mRdl3fhPV8.json', 'var_call_RpQZQrWBDHz8pu7tIwc07vow': {'n_syms_considered': 30, 'n_in_trade_db': 30, 'syms_in_trade': ['AGMH', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT']}, 'var_call_yyzVYg4VyIFJ8sFLXyJfOKy2': [{'Symbol': 'CBAT', 'days_over_20pct': '23.0'}, {'Symbol': 'FAMI', 'days_over_20pct': '23.0'}, {'Symbol': 'BIOC', 'days_over_20pct': '21.0'}, {'Symbol': 'FTFT', 'days_over_20pct': '21.0'}, {'Symbol': 'EYEG', 'days_over_20pct': '18.0'}], 'var_call_kmhyBGAshoF5XOyccfBv8BKq': [{'Symbol': 'BIOC', 'company_name': 'Biocept, Inc. specializes in developing advanced diagnostic solutions that help detect and analyze cancer cells, driving innovation in personalized medicine and cancer treatment.'}, {'Symbol': 'CBAT', 'company_name': 'CBAK Energy Technology, Inc. specializes in developing and manufacturing high-performance lithium-ion batteries, playing a pivotal role in powering electric vehicles and renewable energy solutions.'}, {'Symbol': 'EYEG', 'company_name': 'Eyegate Pharmaceuticals, Inc. is focused on developing innovative therapies for eye diseases, aiming to improve vision health through advanced pharmaceutical solutions.'}, {'Symbol': 'FAMI', 'company_name': 'Farmmi, Inc. specializes in the cultivation and distribution of high-quality agricultural products, with a focus on mushrooms and other nutritious foods.'}, {'Symbol': 'FTFT', 'company_name': 'Future FinTech Group Inc. specializes in the development and marketing of blockchain-based products and financial technology solutions, aiming to revolutionize the digital economy with innovative applications.'}]}

exec(code, env_args)
