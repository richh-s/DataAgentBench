code = """import json, pandas as pd

counts = pd.DataFrame(var_call_4HH9AVAOROCRVTld9P9B4E9g)
info = pd.DataFrame(var_call_rE88BS0x4Ie9sZ5hRaowyLXz)

counts['cnt'] = counts['cnt'].astype(int)
merged = counts.merge(info, left_on='symbol', right_on='Symbol', how='left')
merged = merged.sort_values(['cnt','symbol'], ascending=[False, True])

# Extract company name as requested
out_lines = []
for _, r in merged.iterrows():
    out_lines.append(r['company_name'])

print('__RESULT__:')
print(json.dumps({'company_names': out_lines}))"""

env_args = {'var_call_Kpm5Gsm2fwj4Ln8qQyOEmDvn': 'file_storage/call_Kpm5Gsm2fwj4Ln8qQyOEmDvn.json', 'var_call_Xwr045cIACRdwbk2QikswdHt': 'file_storage/call_Xwr045cIACRdwbk2QikswdHt.json', 'var_call_RKGIm2f7XH31L8K5WtJJcD0l': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_4HH9AVAOROCRVTld9P9B4E9g': [{'symbol': 'SES', 'cnt': '51'}, {'symbol': 'GLG', 'cnt': '42'}, {'symbol': 'TMSR', 'cnt': '40'}, {'symbol': 'VERB', 'cnt': '38'}, {'symbol': 'SNSS', 'cnt': '32'}], 'var_call_rE88BS0x4Ie9sZ5hRaowyLXz': [{'Symbol': 'GLG', 'company_name': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'company_name': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'company_name': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
