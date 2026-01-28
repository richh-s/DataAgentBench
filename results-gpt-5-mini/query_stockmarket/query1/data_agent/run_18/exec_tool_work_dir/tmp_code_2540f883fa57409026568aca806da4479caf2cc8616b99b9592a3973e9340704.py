code = """import json
# use the previous query results stored in variables
# var_call_cx2Pobj9ysPgg2Wz4GumEmli and var_call_8pDlydRnQ6WPI4cN1Ijx45bz
company_info = var_call_cx2Pobj9ysPgg2Wz4GumEmli
max_adj = var_call_8pDlydRnQ6WPI4cN1Ijx45bz

result = {
    "symbol": company_info[0]["Symbol"],
    "company": company_info[0]["Company Description"],
    "year": 2020,
    "max_adjusted_close": float(max_adj[0]["max_adj_close"])
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_cx2Pobj9ysPgg2Wz4GumEmli': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_8pDlydRnQ6WPI4cN1Ijx45bz': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
