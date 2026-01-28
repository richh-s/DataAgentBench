code = """import json
# load previous query results from storage
res = var_call_fsAIQL3orwcMndG9ih9icGzo
info = var_call_E0DuuSSqK78PEjIsTEIARQUx
# create mapping symbol -> company name (Company Description field contains company name and description)
mapping = {rec['Symbol']: rec['Company Description'] for rec in info}
# prepare final list in order from res
final = []
for rec in res:
    sym = rec['Symbol']
    cnt = int(rec['cnt'])
    name = mapping.get(sym, None)
    final.append({'Symbol': sym, 'Company Description': name, 'Count': cnt})
print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_ZRBtlxtgy59qSRwQ30i11mL9': 'file_storage/call_ZRBtlxtgy59qSRwQ30i11mL9.json', 'var_call_TPrlylFvNg0ArgMCp6iMvsZG': 'file_storage/call_TPrlylFvNg0ArgMCp6iMvsZG.json', 'var_call_aM25X4Tq3rODxYu5U2CBzpJ1': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'mapping_sample_count': 86}, 'var_call_fsAIQL3orwcMndG9ih9icGzo': [{'Symbol': 'SES', 'cnt': '51'}, {'Symbol': 'GLG', 'cnt': '42'}, {'Symbol': 'TMSR', 'cnt': '40'}, {'Symbol': 'VERB', 'cnt': '38'}, {'Symbol': 'SNSS', 'cnt': '32'}], 'var_call_E0DuuSSqK78PEjIsTEIARQUx': [{'Symbol': 'GLG', 'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
