code = """import json

with open(locals()['var_function-call-5494353567466373155'], 'r') as f:
    candidates = json.load(f)

queries = []
chunk_size = 50
current_chunk = []

for i, cand in enumerate(candidates):
    sym = cand['Symbol']
    # Construct query without complex f-string nesting
    part1 = "SELECT '" + sym + "' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as UpDays, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as DownDays FROM "
    part2 = "\"" + sym + "\""
    part3 = " WHERE Date LIKE '2017%'"
    q = part1 + part2 + part3
    
    current_chunk.append(q)
    
    if len(current_chunk) == chunk_size or i == len(candidates) - 1:
        queries.append(" UNION ALL ".join(current_chunk))
        current_chunk = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-2069262803057118308': [{'Symbol': 'AEFC', 'Company Description': 'Aegon Funding Company LLC is part of Aegon N.V., a global financial services group offering life insurance, pensions, and asset management solutions to help people achieve a lifetime of financial security.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AIN', 'Company Description': 'Albany International Corporation specializes in producing advanced materials and engineered components, serving industries such as aerospace and paper manufacturing with innovative solutions.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AIV', 'Company Description': 'Apartment Investment and Management Company specializes in owning and managing a diverse portfolio of apartment communities, offering quality rental housing across various regions.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AIZP', 'Company Description': 'Assurant, Inc. specializes in providing a diverse range of insurance products and services, focusing on lifestyle and housing solutions to protect what matters most to their customers.', 'ETF': 'N', 'Listing Exchange': 'N'}, {'Symbol': 'AJRD', 'Company Description': 'Aerojet Rocketdyne Holdings, Inc. specializes in developing advanced propulsion systems and aerospace technologies, playing a crucial role in powering rockets and missiles for both defense and space exploration.', 'ETF': 'N', 'Listing Exchange': 'N'}], 'var_function-call-16752680753660315634': 'file_storage/function-call-16752680753660315634.json', 'var_function-call-1875166123717712124': 'file_storage/function-call-1875166123717712124.json', 'var_function-call-5494353567466373155': 'file_storage/function-call-5494353567466373155.json', 'var_function-call-15524641868399404744': 234}

exec(code, env_args)
