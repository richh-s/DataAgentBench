code = """import pandas as pd, json

df_cnt = pd.DataFrame(var_call_lsCW0VYHwrJ3wf00db1n8zpz)
df_cnt['cnt'] = df_cnt['cnt'].astype(int)
df_info = pd.DataFrame(var_call_hMXDLEJRNMc0aW2hyeqQo6YJ)

out = df_cnt.merge(df_info, on='Symbol', how='left').sort_values(['cnt','Symbol'], ascending=[False, True])
lines = []
for _, r in out.iterrows():
    lines.append(f"{r['company_name']}")

print('__RESULT__:')
print(json.dumps("\n".join(lines)))"""

env_args = {'var_call_DqrJ20Dt6kRZ0Xf4cm1RtXQg': 'file_storage/call_DqrJ20Dt6kRZ0Xf4cm1RtXQg.json', 'var_call_ViohjA2g7kDqYXIDjjz3qdWZ': {'n_total': 86, 'n_common': 86, 'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL']}, 'var_call_AREtt9xxwb8L8HlhehNmyqYW': 'file_storage/call_AREtt9xxwb8L8HlhehNmyqYW.json', 'var_call_hnx1eRDETSlVjqPpzvEPm2bU': {'n_symbols': 86, 'n_in_trade_db': 86, 'missing': []}, 'var_call_ovQldcXoVs3xtAx60Qaj23Nq': 'file_storage/call_ovQldcXoVs3xtAx60Qaj23Nq.json', 'var_call_NGSwwKZFnPmGtdMnODemeDfy': 'file_storage/call_NGSwwKZFnPmGtdMnODemeDfy.json', 'var_call_lsCW0VYHwrJ3wf00db1n8zpz': [{'Symbol': 'SES', 'cnt': '51'}, {'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'TMSR', 'cnt': '40'}, {'Symbol': 'VERB', 'cnt': '38'}, {'Symbol': 'SNSS', 'cnt': '32'}], 'var_call_hMXDLEJRNMc0aW2hyeqQo6YJ': [{'Symbol': 'GLG', 'company_name': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'company_name': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'company_name': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'company_name': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'company_name': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
