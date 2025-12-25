code = """import json

# Load stockinfo results
with open(locals()['var_function-call-16752680753660315634'], 'r') as f:
    candidates = json.load(f)

# Load stocktrade table list
with open(locals()['var_function-call-1875166123717712124'], 'r') as f:
    tables = json.load(f)
tables_set = set(tables)

# Filter
valid_candidates = []
for c in candidates:
    if c['Symbol'] in tables_set:
        valid_candidates.append(c)

print(f"Total candidates: {len(candidates)}")
print(f"Valid candidates (with tables): {len(valid_candidates)}")

print("__RESULT__:")
print(json.dumps(valid_candidates))"""

env_args = {'var_function-call-2069262803057118308': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'ETF': 'N', 'Listing Exchange': 'N'}], 'var_function-call-16752680753660315634': 'file_storage/function-call-16752680753660315634.json', 'var_function-call-1875166123717712124': 'file_storage/function-call-1875166123717712124.json'}

exec(code, env_args)
