code = """import json
biz_list = [b["business_id"] for b in var_call_1COAGomrIDdGYIexpUWkmZXD]
# convert to corresponding business_ref list
refs = [bid.replace("businessid_", "businessref_") for bid in biz_list]
result = json.dumps(refs)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_MfoYHC0AXR42EBuU5PuOL27D': [], 'var_call_1COAGomrIDdGYIexpUWkmZXD': [{'business_id': 'businessid_52'}, {'business_id': 'businessid_84'}, {'business_id': 'businessid_76'}, {'business_id': 'businessid_87'}, {'business_id': 'businessid_65'}, {'business_id': 'businessid_94'}, {'business_id': 'businessid_90'}, {'business_id': 'businessid_16'}]}

exec(code, env_args)
