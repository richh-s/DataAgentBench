code = """import json
# Access previous tool results
# var_call_K7vCPdj9qX458HBv3QMuzxu1 is a file path (large), var_call_XkhLGesdSwoxJJEuFqwUhCJ4 is a result list

def load_storage(var):
    # if var is a string and looks like a file path to json, load it
    if isinstance(var, str):
        try:
            with open(var, 'r') as f:
                return json.load(f)
        except Exception:
            return var
    else:
        return var

data_map = load_storage(var_call_K7vCPdj9qX458HBv3QMuzxu1)
query_res = load_storage(var_call_XkhLGesdSwoxJJEuFqwUhCJ4)

# Build company_map
company_map = data_map.get('company_map', {}) if isinstance(data_map, dict) else {}

# Extract top symbols from query result
top_symbols = [r['symbol'] for r in query_res]

# Helper to extract company name from description
def extract_name(desc):
    if not desc or not isinstance(desc, str):
        return None
    # common delimiters
    delims = [' is ', ' specializes', ' focuses', ' focused', ' provides', ' operates', ' offers', ' is a ', ' develops', ' headquartered', ' is focused', ' is an ']
    for d in delims:
        if d in desc:
            return desc.split(d)[0].strip()
    # fallback: take up to first comma
    if ',' in desc:
        return desc.split(',')[0].strip()
    # otherwise return full desc
    return desc.strip()

company_names = []
for sym in top_symbols:
    desc = company_map.get(sym)
    name = extract_name(desc) if desc else None
    if not name:
        name = sym
    company_names.append(name)

print('__RESULT__:')
print(json.dumps(company_names))"""

env_args = {'var_call_PVAfm8uVITZvm5Qg3urNUhRO': 'file_storage/call_PVAfm8uVITZvm5Qg3urNUhRO.json', 'var_call_wtLJ5gytvW712GxaYrXyCriN': 'file_storage/call_wtLJ5gytvW712GxaYrXyCriN.json', 'var_call_K7vCPdj9qX458HBv3QMuzxu1': 'file_storage/call_K7vCPdj9qX458HBv3QMuzxu1.json', 'var_call_1asL4LvVzhj6mWDNuP4FOItF': {'count': 86, 'first10': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS']}, 'var_call_dm8OkqrnXjz6Wy3NmLcgXeQo': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_XkhLGesdSwoxJJEuFqwUhCJ4': [{'symbol': 'SES', 'cnt': '51'}, {'symbol': 'GLG', 'cnt': '42'}, {'symbol': 'TMSR', 'cnt': '40'}, {'symbol': 'VERB', 'cnt': '38'}, {'symbol': 'SNSS', 'cnt': '32'}]}

exec(code, env_args)
