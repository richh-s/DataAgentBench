code = """import json
# reload the stored query result directly from storage keys available
res = var_call_BXaFLU9Rhslng2T01omraUuZ

symbol_to_name = {r['Symbol']: r['Company Description'] for r in res}

# top5 order from earlier query
top5 = var_call_cLjpaVoDTU3jRiNXhIUrYiNJ
ordered_symbols = [r['symbol'] for r in top5]

output = [symbol_to_name.get(s, s) for s in ordered_symbols]
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_6NSl2R2f3iawMBi3p1IM7pmk': 'file_storage/call_6NSl2R2f3iawMBi3p1IM7pmk.json', 'var_call_hDmmcXxjphXCqF7h3DP2z3Rr': 'file_storage/call_hDmmcXxjphXCqF7h3DP2z3Rr.json', 'var_call_wSbUZA0GcUcGaRIFUXbXlJos': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_cLjpaVoDTU3jRiNXhIUrYiNJ': [{'symbol': 'SES', 'cnt': '51.0'}, {'symbol': 'GLG', 'cnt': '42.0'}, {'symbol': 'TMSR', 'cnt': '40.0'}, {'symbol': 'VERB', 'cnt': '38.0'}, {'symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_BXaFLU9Rhslng2T01omraUuZ': [{'Symbol': 'GLG', 'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
