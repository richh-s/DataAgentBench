code = """import json
# read query result
res = var_call_HncEm9oWgu1Ibbn32HooVc5a
# read company descriptions
info = var_call_2yvLW9RQp2PziHytANGf3vlA

# build mapping symbol -> company description
mapping = {r['Symbol']: r['Company Description'] for r in info}
# order according to res
ordered = [mapping.get(r['Symbol'], r['Symbol']) for r in res]

print('__RESULT__:')
print(json.dumps(ordered))"""

env_args = {'var_call_cOi9OMUYcXvqMM1mSCci0y6k': 'file_storage/call_cOi9OMUYcXvqMM1mSCci0y6k.json', 'var_call_ppF3FrkgSKRwnihegO5SvHTe': 'file_storage/call_ppF3FrkgSKRwnihegO5SvHTe.json', 'var_call_TMURrJll9tJcyuctHiZPZw1t': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_HncEm9oWgu1Ibbn32HooVc5a': [{'Symbol': 'SES', 'days': '51.0'}, {'Symbol': 'GLG', 'days': '42.0'}, {'Symbol': 'TMSR', 'days': '40.0'}, {'Symbol': 'VERB', 'days': '38.0'}, {'Symbol': 'SNSS', 'days': '32.0'}], 'var_call_2yvLW9RQp2PziHytANGf3vlA': [{'Symbol': 'GLG', 'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
