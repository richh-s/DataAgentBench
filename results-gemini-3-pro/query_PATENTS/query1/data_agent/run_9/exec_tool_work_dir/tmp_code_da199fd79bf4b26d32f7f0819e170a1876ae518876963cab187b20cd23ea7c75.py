code = """import json
import re
import pandas as pd

# Load Level 5 symbols
with open(locals()['var_function-call-4209797250346039568'], 'r') as f:
    l5_data = json.load(f)
    level5_codes = set(item['symbol'] for item in l5_data)

# Load Patents
with open(locals()['var_function-call-333056328050436468'], 'r') as f:
    patents = json.load(f)

year_pattern = re.compile(r'\b(19|20)\d{2}\b')

extracted_years = []
valid_patents = 0
patents_with_l5 = 0

for p in patents[:1000]: # Check first 1000
    f_date = p.get('filing_date', '')
    match = year_pattern.search(f_date)
    if match:
        extracted_years.append(int(match.group(0)))
        valid_patents += 1
        
        cpc_str = p.get('cpc', '[]')
        try:
            cpc_list = json.loads(cpc_str)
            found = False
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 4:
                    l5 = code[:4]
                    if l5 in level5_codes:
                        found = True
            if found:
                patents_with_l5 += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "total_sample": 1000,
    "valid_years_count": valid_patents,
    "patents_with_l5_count": patents_with_l5,
    "sample_years": extracted_years[:20],
    "unique_years": list(set(extracted_years))
}))"""

env_args = {'var_function-call-3066016024932945511': ['cpc_definition'], 'var_function-call-3066016024932944250': ['publicationinfo'], 'var_function-call-12953216539531807597': [{'symbol': 'A01H', 'level': '5.0'}, {'symbol': 'A01F', 'level': '5.0'}, {'symbol': 'A01C', 'level': '5.0'}, {'symbol': 'A01G', 'level': '5.0'}, {'symbol': 'A23J', 'level': '5.0'}], 'var_function-call-12953216539531806840': 'file_storage/function-call-12953216539531806840.json', 'var_function-call-3195997769448221607': [{'symbol': 'C01B', 'level': '5.0'}, {'symbol': 'C01B33/00', 'level': '7.0'}], 'var_function-call-14113235830138341004': [], 'var_function-call-239168183394975619': [{'count(*)': '277813'}], 'var_function-call-4209797250346039568': 'file_storage/function-call-4209797250346039568.json', 'var_function-call-333056328050436468': 'file_storage/function-call-333056328050436468.json', 'var_function-call-9668353239010562032': []}

exec(code, env_args)
