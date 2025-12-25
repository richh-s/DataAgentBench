code = """import json
products = [r["Product2Id"] for r in var_call_vbtstz0wXaY0U1XMJ3YFmqpa]
# assume AI processing unit is the most recent distinct product in this period
unique_preserving = []
for p in products:
    if p not in unique_preserving:
        unique_preserving.append(p)
result = unique_preserving[0] if unique_preserving else None
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bLj1MZepr24WbGajK5xWj2wl': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_vbtstz0wXaY0U1XMJ3YFmqpa': [{'Product2Id': '#01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hTUkIAM'}, {'Product2Id': '01tWt000006hV8LIAU'}, {'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
