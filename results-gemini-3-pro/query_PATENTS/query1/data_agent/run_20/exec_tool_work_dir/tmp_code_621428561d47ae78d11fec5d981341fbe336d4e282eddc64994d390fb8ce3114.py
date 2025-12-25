code = """import json
import re

# Load publications
with open(locals()['var_function-call-499717155122339469'], 'r') as f:
    data = json.load(f)

years = []
for row in data:
    fdate = row.get('filing_date', '')
    match = re.search(r'\b(19|20)\d{2}\b', fdate)
    if match:
        years.append(int(match.group(0)))

if not years:
    print("__RESULT__:")
    print(json.dumps({"error": "No years found"}))
else:
    min_y = min(years)
    max_y = max(years)
    print("__RESULT__:")
    print(json.dumps({"min_year": min_y, "max_year": max_y, "count": len(years)}))"""

env_args = {'var_function-call-8960863123887240605': 'file_storage/function-call-8960863123887240605.json', 'var_function-call-9121606955539458114': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-14205884976276555357': [{'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-8893913274727555308': [{'symbol': 'A62B', 'level': '5.0'}, {'symbol': 'A63G', 'level': '5.0'}, {'symbol': 'A63K', 'level': '5.0'}, {'symbol': 'A63B', 'level': '5.0'}, {'symbol': 'A63J', 'level': '5.0'}, {'symbol': 'A63C', 'level': '5.0'}, {'symbol': 'A63D', 'level': '5.0'}, {'symbol': 'A63F', 'level': '5.0'}, {'symbol': 'C25D', 'level': '5.0'}, {'symbol': 'A63H', 'level': '5.0'}], 'var_function-call-12910028673437125087': [{'symbol': 'C01B', 'level': '5.0'}], 'var_function-call-5759197899414802183': [{'count(*)': '277813'}], 'var_function-call-5770235724509795009': 'file_storage/function-call-5770235724509795009.json', 'var_function-call-499717155122339469': 'file_storage/function-call-499717155122339469.json', 'var_function-call-8433321875573929793': []}

exec(code, env_args)
