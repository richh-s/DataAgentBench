code = """import json

path_patents = locals()['var_function-call-1425838539260044447']

debug_info = {}

with open(path_patents, 'r') as f:
    patents = json.load(f)

p = patents[0]
cpc_raw = p.get('cpc')
debug_info['cpc_raw_type'] = str(type(cpc_raw))
debug_info['cpc_raw_preview'] = cpc_raw[:100] if cpc_raw else None

try:
    cpc_parsed = json.loads(cpc_raw)
    debug_info['cpc_parsed_type'] = str(type(cpc_parsed))
    debug_info['cpc_parsed_len'] = len(cpc_parsed)
    if len(cpc_parsed) > 0:
        debug_info['first_item'] = cpc_parsed[0]
except Exception as e:
    debug_info['parse_error'] = str(e)

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-17682530284056883508': 'file_storage/function-call-17682530284056883508.json', 'var_function-call-1425838539260044447': 'file_storage/function-call-1425838539260044447.json', 'var_function-call-767001268371460585': [], 'var_function-call-2505620898448165995': 'DEBUG_DONE', 'var_function-call-4017213322786989118': {'sample_level_5': ['G01B', 'G21C', 'E02F', 'F41H', 'A22C', 'A24B', 'H99Z', 'A61Q', 'C21B', 'D05B'], 'match_mode': 'subclass', 'dates_preview': ['dated 5th March 2019', 'March the 18th, 2019', '29th March 2019', 'on March 29th, 2019', '2nd April 2019'], 'codes_preview': [], 'total_matches': 0, 'unique_matched_codes': 0}}

exec(code, env_args)
