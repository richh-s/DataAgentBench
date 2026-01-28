code = """import json
rows = json.load(open(var_call_0Je4Yy8pNdn3rY4jEnJEpfyN))
descs = json.load(open(var_call_7AbEnFqsk57rCUjGAensEV09))

# Map symbols to description order from query result
symbol_order = [r['Symbol'] for r in rows]

# Build symbol -> description from descs (unordered)
desc_map = {}
for d in descs:
    # crude extraction: company name is text before first ' is ' or ' specializes' or ' engages'
    text = d.get('Company Description','')
    desc_map[text] = text

# Prepare final list: match rows to desc entries by symbols via a lookup query earlier had same order as input symbols
# We know the query requested symbols ('SES','GLG','TMSR','VERB','SNSS') in that specific order? Actually not. Let's map by symbol from previous SQL input.

# We'll prepare final mapping manually using the descs list but we must pair symbol to company name extracted from description text start up to first verb.

import re
result = []
for d in descs:
    text = d.get('Company Description','')
    # extract company name as everything before first ' is' or ' specializes' or ' engages' or ' focuses' or ' specializes in'
    m = re.split(r"\s(is|specializes|engages|focuses|focuses on|is dedicated|provides|operates)", text, maxsplit=1)
    name = m[0].strip()
    result.append(name)

# rows order: SES, GLG, TMSR, VERB, SNSS based on SQL result
final = [
    (rows[0]['Symbol'], result[1]),
    (rows[1]['Symbol'], result[0]),
    (rows[2]['Symbol'], result[3]),
    (rows[3]['Symbol'], result[4]),
    (rows[4]['Symbol'], result[2])
]

# Create answer list of company names in order of rows
ans = [name for sym,name in final]
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_glwAqwUanNo8ExlokGyMH5xr': 'file_storage/call_glwAqwUanNo8ExlokGyMH5xr.json', 'var_call_b8L0GzZtBYwGmNoVw96WDvnt': 'file_storage/call_b8L0GzZtBYwGmNoVw96WDvnt.json', 'var_call_3rCgDdperyl00Y2GTbxKWHEa': 'file_storage/call_3rCgDdperyl00Y2GTbxKWHEa.json', 'var_call_Phj0Ocjc3o8Ydg7irHG2GHq1': {'symbols_considered_count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_SPTjz6NxUPJwCqBAqotOVftP': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_0Je4Yy8pNdn3rY4jEnJEpfyN': [{'Symbol': 'SES', 'cnt': '51'}, {'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'TMSR', 'cnt': '40'}, {'Symbol': 'VERB', 'cnt': '38'}, {'Symbol': 'SNSS', 'cnt': '32'}], 'var_call_7AbEnFqsk57rCUjGAensEV09': [{'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
