code = """import json
import re

patents_path = locals()['var_function-call-5530323500134500439']

with open(patents_path, 'r') as f:
    patents = json.load(f)

debug_out = []
for i in range(2):
    p = patents[i]
    # Date debug
    d_str = p.get('filing_date', 'N/A')
    # Try finding any 4 digits
    m_year = re.search(r'\d{4}', str(d_str))
    
    # CPC debug
    cpc_str = p.get('cpc', '[]')
    cpc_parsed = None
    cpc_error = None
    try:
        cpc_parsed = json.loads(cpc_str)
    except Exception as e:
        cpc_error = str(e)
        
    debug_out.append({
        "raw_date": d_str,
        "year_found": m_year.group(0) if m_year else "None",
        "cpc_raw_len": len(cpc_str),
        "cpc_parsed_type": str(type(cpc_parsed)),
        "cpc_parsed_len": len(cpc_parsed) if isinstance(cpc_parsed, list) else None,
        "cpc_error": cpc_error,
        "first_code": cpc_parsed[0].get('code') if isinstance(cpc_parsed, list) and cpc_parsed else None
    })

print("__RESULT__:")
print(json.dumps(debug_out))"""

env_args = {'var_function-call-16354257400330351795': 'file_storage/function-call-16354257400330351795.json', 'var_function-call-16354257400330353054': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-10560939620404889531': [{'symbol': 'H01M', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}, {'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'H01M10/0565', 'level': '11.0'}], 'var_function-call-16184128629487448997': [{'len': '4', 'cnt': '677'}], 'var_function-call-4973736629774637364': [{'cnt': '277813'}], 'var_function-call-7207860585803115625': 'file_storage/function-call-7207860585803115625.json', 'var_function-call-5530323500134500439': 'file_storage/function-call-5530323500134500439.json', 'var_function-call-6282301310973396861': [], 'var_function-call-3212865062370055516': {'total': 277813, 'valid_years': 0, 'valid_cpc': 0, 'matched_l5': 0, 'year_min': None, 'year_max': None, 'top_years': {}}, 'var_function-call-8762404416262283466': 'file_storage/function-call-8762404416262283466.json', 'var_function-call-12606317811182743240': [{'raw_date': 'dated 5th March 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': 'March the 18th, 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': '29th March 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': 'on March 29th, 2019', 'type': "<class 'str'>", 'match': 'No Match'}, {'raw_date': '2nd April 2019', 'type': "<class 'str'>", 'match': 'No Match'}]}

exec(code, env_args)
