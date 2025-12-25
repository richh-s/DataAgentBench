code = """symbols = ["AEFC", "AIN", "AIV", "AIZP", "AJRD", "AL", "AMN", "AMP", "AMT", "ARD", "ARGD", "ARLO", "ASG", "AVA", "BANC", "BBU", "BBVA", "BDXA", "BKH", "BKT", "BLD", "BNS", "BV", "BZH", "CADE", "CAE", "CAF", "CBT", "CCC", "CCZ", "CHAP", "CIA", "CMA", "CMI", "CMSA", "CNK", "COTY", "CRC", "CRM", "CRS", "CSL", "CTS", "CUBE", "CURO", "CVIA", "CVX", "CXH", "DAC", "DDS", "DDT", "DEO", "DGX", "DMB", "DTQ", "DXC", "EARN", "EBS", "EGO", "EGY", "EIG"]
parts = []
for s in symbols:
    q = f"SELECT '{s}' as Symbol, SUM(CASE WHEN Close > Open THEN 1 ELSE 0 END) as Up, SUM(CASE WHEN Close < Open THEN 1 ELSE 0 END) as Down FROM \"{s}\" WHERE Date >= '2017-01-01' AND Date <= '2017-12-31'"
    parts.append(q)
print("__RESULT__:")
print(" UNION ALL ".join(parts))"""

env_args = {'var_function-call-16810398710687085223': [{'ETF': 'Y', 'Listing Exchange': 'P'}, {'ETF': 'N', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Q'}, {'ETF': 'Y', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'A'}, {'ETF': 'N', 'Listing Exchange': 'N'}, {'ETF': 'N', 'Listing Exchange': 'Z'}, {'ETF': 'N', 'Listing Exchange': 'P'}, {'ETF': 'Y', 'Listing Exchange': 'A'}], 'var_function-call-1631025954943238764': 'file_storage/function-call-1631025954943238764.json', 'var_function-call-4060108603261474737': 'file_storage/function-call-4060108603261474737.json', 'var_function-call-4127219778048163343': 'file_storage/function-call-4127219778048163343.json', 'var_function-call-2579092286742790265': 234, 'var_function-call-8724790248565907862': ['AEFC', 'AIN', 'AIV', 'AIZP', 'AJRD', 'AL', 'AMN', 'AMP', 'AMT', 'ARD', 'ARGD', 'ARLO', 'ASG', 'AVA', 'BANC', 'BBU', 'BBVA', 'BDXA', 'BKH', 'BKT', 'BLD', 'BNS', 'BV', 'BZH', 'CADE', 'CAE', 'CAF', 'CBT', 'CCC', 'CCZ', 'CHAP', 'CIA', 'CMA', 'CMI', 'CMSA', 'CNK', 'COTY', 'CRC', 'CRM', 'CRS', 'CSL', 'CTS', 'CUBE', 'CURO', 'CVIA', 'CVX', 'CXH', 'DAC', 'DDS', 'DDT', 'DEO', 'DGX', 'DMB', 'DTQ', 'DXC', 'EARN', 'EBS', 'EGO', 'EGY', 'EIG']}

exec(code, env_args)
