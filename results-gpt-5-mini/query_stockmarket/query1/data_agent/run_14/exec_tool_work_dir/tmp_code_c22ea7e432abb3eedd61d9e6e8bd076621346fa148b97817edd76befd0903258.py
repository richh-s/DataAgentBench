code = """import json
# var_call_oEB7zjm9bZycFXfBqm3Lea7y and var_call_vZnLk1O6WSJ1V1jDPjbodCTK are available
result = {
    "company_symbol": var_call_oEB7zjm9bZycFXfBqm3Lea7y[0]["Symbol"],
    "company_name": var_call_oEB7zjm9bZycFXfBqm3Lea7y[0]["Company Description"],
    "max_adj_close_2020": float(var_call_vZnLk1O6WSJ1V1jDPjbodCTK[0]["max_adj_close"])
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_oEB7zjm9bZycFXfBqm3Lea7y': [{'Symbol': 'REAL', 'Company Description': 'The RealReal, Inc. is a leader in the luxury consignment market, offering a platform for buying and selling authenticated pre-owned designer fashion, jewelry, and art.'}], 'var_call_vZnLk1O6WSJ1V1jDPjbodCTK': [{'max_adj_close': '18.440000534057617'}]}

exec(code, env_args)
