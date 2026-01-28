code = """import json
# load the previous execute_python result file
with open(var_call_DgwM8rtcNlluOUwPr8x6x2xL, 'r') as f:
    data = json.load(f)

# extract total
total = data.get('total_amount_sum_unique_funding_ids')
# For safety, compute from matched_funding_records amounts
matched = data.get('matched_funding_records', [])
calc = sum(int(r.get('amount',0)) for r in matched)

result = {'total_from_field': total, 'total_recalc_from_records': calc}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qqvsBQmMn9KBlsyFeW4qV9D0': ['civic_docs'], 'var_call_n9AZpz1dFRUuqubYzQvaSoqT': 'file_storage/call_n9AZpz1dFRUuqubYzQvaSoqT.json', 'var_call_vOINh3VzqNQkq7TY5jjtXxJr': ['Funding'], 'var_call_5Ta0B5Rj8lZjdUtJWzhXyTkF': 'file_storage/call_5Ta0B5Rj8lZjdUtJWzhXyTkF.json', 'var_call_DgwM8rtcNlluOUwPr8x6x2xL': 'file_storage/call_DgwM8rtcNlluOUwPr8x6x2xL.json'}

exec(code, env_args)
