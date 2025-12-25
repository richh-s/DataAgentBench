code = """import json

# Load stockinfo result
with open(locals()['var_function-call-14158479634354559369'], 'r') as f:
    stock_info = json.load(f)

# Load table list
with open(locals()['var_function-call-8638126572495910571'], 'r') as f:
    table_list = json.load(f)

table_set = set(table_list)
valid_stocks = [s['Symbol'] for s in stock_info if s['Symbol'] in table_set]

if not valid_stocks:
    print("__RESULT__:")
    print(json.dumps("SELECT 'NO DATA' as Symbol, 0 as HighVolDays"))
else:
    subqueries = []
    for sym in valid_stocks:
        # Construct query part
        q = "SELECT '" + sym + "' AS Symbol, COUNT(*) AS HighVolDays FROM \"" + sym + "\" WHERE Date >= '2019-01-01' AND Date <= '2019-12-31' AND (High - Low) > 0.2 * Low"
        subqueries.append(q)

    full_query = " UNION ALL ".join(subqueries)
    final_query = "SELECT Symbol, HighVolDays FROM (" + full_query + ") ORDER BY HighVolDays DESC LIMIT 5"

    print("__RESULT__:")
    print(json.dumps(final_query))"""

env_args = {'var_function-call-14158479634354559369': 'file_storage/function-call-14158479634354559369.json', 'var_function-call-8638126572495910571': 'file_storage/function-call-8638126572495910571.json', 'var_function-call-17903326411462472332': [{'Symbol': 'AGMH', 'Company Description': 'AGM Group Holdings Inc. specializes in providing financial technology solutions and services, focusing on enhancing efficiency and performance for businesses in the financial sector.'}, {'Symbol': 'ALACU', 'Company Description': 'Alberton Acquisition Corporation is a special purpose acquisition company focused on merging with or acquiring promising businesses to bring them public and enhance their growth potential.'}, {'Symbol': 'AMHC', 'Company Description': 'Amplitude Healthcare Acquisition Corporation is a special purpose acquisition company focused on identifying and merging with promising healthcare businesses to accelerate their growth and innovation.'}, {'Symbol': 'ANDA', 'Company Description': 'Andina Acquisition Corp. III is a special purpose acquisition company focused on identifying and partnering with promising businesses in Latin America to facilitate their growth and expansion.'}, {'Symbol': 'APEX', 'Company Description': 'Apex Global Brands Inc. specializes in creating and marketing a diverse portfolio of fashion and lifestyle brands, connecting consumers with trendy and innovative products worldwide.'}]}

exec(code, env_args)
