code = """import json
trade_res = var_call_tCUHUV1XgeobeiEpfkK3g7MY
info_res = var_call_nXTc17XwQKv5IZUzipIcBB75

# Map symbols to company descriptions in the order returned by stockinfo query
symbols = [r['symbol'] for r in trade_res]
# The info_res order may not match; create mapping from symbol to description by searching stockinfo
with open(var_call_aCAbdB3jQgRTH8mqdp5wsMj6, 'r') as f:
    stockinfo = json.load(f)
map_desc = {r['Symbol']: r['Company Description'] for r in stockinfo}

results = []
for r in trade_res:
    sym = r['symbol']
    cnt = float(r['cnt']) if r['cnt'] is not None else 0.0
    desc = map_desc.get(sym, None)
    results.append({'symbol': sym, 'company': desc, 'count': int(cnt)})

# Prepare final list of company names only in descending order
companies = [r['company'] for r in results]

out = {'companies': companies, 'details': results}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_aCAbdB3jQgRTH8mqdp5wsMj6': 'file_storage/call_aCAbdB3jQgRTH8mqdp5wsMj6.json', 'var_call_tJA9EW3OouFCqMIGZNLFpvYc': 'file_storage/call_tJA9EW3OouFCqMIGZNLFpvYc.json', 'var_call_aSp5DOh5raQx05jOOLGTzCz5': {'num_stockinfo_symbols': 86, 'num_available': 86, 'available_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_8SKu7RYsins1PIkv4xw1FOnT': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_tCUHUV1XgeobeiEpfkK3g7MY': [{'symbol': 'SES', 'cnt': '51.0'}, {'symbol': 'GLG', 'cnt': '42.0'}, {'symbol': 'TMSR', 'cnt': '40.0'}, {'symbol': 'VERB', 'cnt': '38.0'}, {'symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_nXTc17XwQKv5IZUzipIcBB75': [{'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
