code = """import json

key = 'var_function-call-2233720746890943577' # valid_stocks file
filename = locals()[key]

with open(filename, 'r') as f:
    valid_stocks = json.load(f)

queries = []
current_batch = []
batch_size = 80 # Safe limit

for i, stock in enumerate(valid_stocks):
    symbol = stock['Symbol']
    # Shortened query
    q = "SELECT '" + symbol + "' S,SUM(Close>Open) U,SUM(Close<Open) D FROM \"" + symbol + "\" WHERE Date LIKE '2017%'"
    current_batch.append(q)
    
    if len(current_batch) >= batch_size or i == len(valid_stocks) - 1:
        full_query = " UNION ALL ".join(current_batch)
        queries.append(full_query)
        current_batch = []

print("__RESULT__:")
print(json.dumps(queries))"""

env_args = {'var_function-call-5968356060284998567': [{'ETF': 'Y'}, {'ETF': 'N'}], 'var_function-call-6878344860899223603': 'file_storage/function-call-6878344860899223603.json', 'var_function-call-1087427795925907459': 'file_storage/function-call-1087427795925907459.json', 'var_function-call-2233720746890943577': 'file_storage/function-call-2233720746890943577.json', 'var_function-call-13650588708312413850': [{'Date': '1987-09-30'}], 'var_function-call-13436990775014540560': 234, 'var_function-call-4100983673863005846': 'file_storage/function-call-4100983673863005846.json', 'var_function-call-5348722218540468901': [11943, 11931, 11942, 10742], 'var_function-call-10255236117286346878': [{'sum(("Close" > Open))': '3753.0'}]}

exec(code, env_args)
