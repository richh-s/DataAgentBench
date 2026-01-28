code = """import json
# load query result
res = var_call_warLwfeNrvoMEDMFUVDMKvve
# load company descriptions
descs = var_call_uerNjGxA4Ujod4ZZGNTSbEvo
# map symbol to company name (Company Description field contains name and description; take up to first ' is ' or ',' or ' specializes' or full string)
mapping = {}
for r in descs:
    sym = r['Symbol']
    desc = r['Company Description']
    # attempt to extract company name (before first ' is' or ' specializes' or ' engages' or ' specializes in')
    name = desc
    for sep in [' is ', ' specializes', ' focuses', ' engages', ' specializes in', ' is dedicated to', ' engages in']:
        if sep in desc:
            name = desc.split(sep)[0]
            break
    mapping[sym] = name.strip()

output = []
for r in res:
    sym = r['symbol']
    cnt = int(r['cnt'])
    name = mapping.get(sym, sym)
    output.append({'symbol': sym, 'company_name': name, 'count': cnt})

# prepare final list of company names in order
final_names = [o['company_name'] for o in output]
print("__RESULT__:")
print(json.dumps(final_names))"""

env_args = {'var_call_ew9VLDirbm4RMvpPwbqpbkGx': 'file_storage/call_ew9VLDirbm4RMvpPwbqpbkGx.json', 'var_call_XHnP7G8F1ai6OXCc44J1pueW': 'file_storage/call_XHnP7G8F1ai6OXCc44J1pueW.json', 'var_call_5UDzeVJG4ngebJ6Ug6kNpcLL': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_warLwfeNrvoMEDMFUVDMKvve': [{'symbol': 'SES', 'cnt': '51'}, {'symbol': 'GLG', 'cnt': '42'}, {'symbol': 'TMSR', 'cnt': '40'}, {'symbol': 'VERB', 'cnt': '38'}, {'symbol': 'SNSS', 'cnt': '32'}], 'var_call_uerNjGxA4Ujod4ZZGNTSbEvo': [{'Symbol': 'GLG', 'Company Description': 'TD Holdings, Inc. is involved in commodity trading and supply chain management, specializing in the distribution of non-ferrous metals and other industrial materials.'}, {'Symbol': 'SES', 'Company Description': 'Synthesis Energy Systems, Inc. specializes in transforming low-cost carbon resources into clean energy and valuable chemical products, driving innovation in sustainable energy solutions.'}, {'Symbol': 'SNSS', 'Company Description': 'Sunesis Pharmaceuticals, Inc. is dedicated to developing innovative cancer therapies, striving to advance treatments that target the underlying mechanisms of the disease.'}, {'Symbol': 'TMSR', 'Company Description': 'TMSR Holding Company Limited engages in the development and distribution of advanced industrial materials, focusing on enhancing efficiency and sustainability in various manufacturing processes.'}, {'Symbol': 'VERB', 'Company Description': 'Verb Technology Company, Inc. specializes in developing interactive video-based sales and marketing applications designed to enhance customer engagement and drive business growth.'}]}

exec(code, env_args)
