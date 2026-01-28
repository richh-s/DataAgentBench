code = """import json
# Access previous query results from storage variables
records_info = var_call_zkwqFg2gCCMQGCSQCpwwnqER
records_trade = var_call_06J9VmOecWUCPeQospJOOXa7

# Extract values
symbol = records_info[0].get('Symbol') if records_info else None
company_desc = records_info[0].get('Company Description') if records_info else None
# Try to extract company name from description (up to first comma)
company_name = None
if company_desc:
    company_name = company_desc.split(' is ')[0].strip()
    # If split didn't work, fallback to symbol
    if not company_name:
        company_name = symbol

max_adj_raw = records_trade[0].get('max_adj_close') if records_trade else None
max_adj = None
if max_adj_raw is not None:
    try:
        max_adj = float(max_adj_raw)
    except:
        max_adj = None

result = {
    'symbol': symbol,
    'company': company_name,
    'year': 2020,
    'max_adj_close': max_adj,
    'max_adj_close_rounded_2': round(max_adj, 2) if max_adj is not None else None
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zkwqFg2gCCMQGCSQCpwwnqER': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_06J9VmOecWUCPeQospJOOXa7': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
