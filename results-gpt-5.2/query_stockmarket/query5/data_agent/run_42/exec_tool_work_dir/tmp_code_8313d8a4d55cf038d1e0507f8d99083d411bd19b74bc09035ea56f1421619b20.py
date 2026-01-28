code = """import json, pandas as pd

top = var_call_2W1Wk8YGo2lWI6XXStMZ6XwL
info = var_call_y0ociNElWESZh2tnEbKyaPf4

df_top = pd.DataFrame(top)
df_info = pd.DataFrame(info)
df_top['days'] = df_top['days'].astype(int)

df = df_top.merge(df_info, on='Symbol', how='left').sort_values(['days','Symbol'], ascending=[False, True])

names = df['company_name'].tolist()
answer = "\n".join(names)

print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_mO6KgQoztucnkZrYAtJwnebP': 'file_storage/call_mO6KgQoztucnkZrYAtJwnebP.json', 'var_call_WGeI64HmUooUEC6F9TmLIOLq': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'n': 86}, 'var_call_pT5LP1Ih8zWQyd1KBdU8QMPx': 'file_storage/call_pT5LP1Ih8zWQyd1KBdU8QMPx.json', 'var_call_80PSEyPrvSNkjvdjfuyRL6Qx': {'eligible': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'eligible_n': 86, 'missing_n': 0, 'missing': []}, 'var_call_2W1Wk8YGo2lWI6XXStMZ6XwL': [{'Symbol': 'SES', 'days': '51'}, {'Symbol': 'GLG', 'days': '42'}, {'Symbol': 'TMSR', 'days': '40'}, {'Symbol': 'VERB', 'days': '38'}, {'Symbol': 'SNSS', 'days': '32'}], 'var_call_y0ociNElWESZh2tnEbKyaPf4': [{'Symbol': 'GLG', 'company_name': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'company_name': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'company_name': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
