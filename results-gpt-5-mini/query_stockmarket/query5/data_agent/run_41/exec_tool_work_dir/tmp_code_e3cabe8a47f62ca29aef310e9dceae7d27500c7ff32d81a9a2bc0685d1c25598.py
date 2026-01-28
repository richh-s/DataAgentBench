code = """import json
rows = var_call_0Je4Yy8pNdn3rY4jEnJEpfyN
descs = var_call_7AbEnFqsk57rCUjGAensEV09

# rows and descs are lists of dicts already
import re
# Extract company names from descriptions
def extract_name(text):
    m = re.split(r"\s(is|specializes|engages|focuses|focuses on|is dedicated|provides|operates)", text, maxsplit=1)
    return m[0].strip()

names = [extract_name(d['Company Description']) for d in descs]
# descs came from query with IN order unspecified; we need to map symbol to description by matching known company names to symbols
# From earlier we asked stockinfo WHERE Symbol IN ('SES','GLG','TMSR','VERB','SNSS') - the order returned corresponds to the order in result set var_call_7AbEnFqsk57rCUjGAensEV09
# We need to associate each description to correct symbol. The descriptions list order corresponds to the query result order which may not match symbol order.

# Let's build mapping based on unique words: GLG likely 'TD Holdings, Inc.' Wait earlier we saw descriptions list: [TD Holdings... , Synthesis Energy Systems..., Sunesis Pharmaceuticals..., TMSR Holding Company Limited..., Verb Technology Company, Inc.]
# From these, GLG is 'TD Holdings, Inc.'? Actually GLG ticker likely 'TD Holdings, Inc.' That's mapping from earlier long preview where GLG was 'TD Holdings, Inc.' But safe approach: match by company name keywords to symbols

desc_texts = [d['Company Description'] for d in descs]
map_sym_desc = {}
for text in desc_texts:
    if 'TD Holdings' in text or 'commodity trading' in text:
        map_sym_desc['GLG'] = extract_name(text)
    elif 'Synthesis Energy Systems' in text or 'transforming low-cost carbon resources' in text:
        map_sym_desc['SES'] = extract_name(text)
    elif 'Sunesis Pharmaceuticals' in text or 'cancer therapies' in text:
        map_sym_desc['SNSS'] = extract_name(text)
    elif 'TMSR Holding' in text:
        map_sym_desc['TMSR'] = extract_name(text)
    elif 'Verb Technology' in text or 'interactive video' in text:
        map_sym_desc['VERB'] = extract_name(text)

# Now rows from counts are: [SES, GLG, TMSR, VERB, SNSS]
ordered_symbols = [r['Symbol'] for r in rows]
ans = [map_sym_desc[sym] for sym in ordered_symbols]

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_glwAqwUanNo8ExlokGyMH5xr': 'file_storage/call_glwAqwUanNo8ExlokGyMH5xr.json', 'var_call_b8L0GzZtBYwGmNoVw96WDvnt': 'file_storage/call_b8L0GzZtBYwGmNoVw96WDvnt.json', 'var_call_3rCgDdperyl00Y2GTbxKWHEa': 'file_storage/call_3rCgDdperyl00Y2GTbxKWHEa.json', 'var_call_Phj0Ocjc3o8Ydg7irHG2GHq1': {'symbols_considered_count': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_SPTjz6NxUPJwCqBAqotOVftP': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_0Je4Yy8pNdn3rY4jEnJEpfyN': [{'Symbol': 'SES', 'cnt': '51'}, {'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'TMSR', 'cnt': '40'}, {'Symbol': 'VERB', 'cnt': '38'}, {'Symbol': 'SNSS', 'cnt': '32'}], 'var_call_7AbEnFqsk57rCUjGAensEV09': [{'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
