code = """import json

avg = var_call_TdJHTBp6WK291mH1pwasawjw

if avg is None:
    answer = "There are no papers identified as ACM-published among those cited in 2018 in the provided data, so the average citation count for ACM papers cited in 2018 cannot be computed (it is effectively undefined)."
else:
    answer = f"The average citation count for ACM-published papers cited in 2018 is {avg:.2f}."

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_S7z9w3BrERVsGPrcnjI454c1': 'file_storage/call_S7z9w3BrERVsGPrcnjI454c1.json', 'var_call_4JydZyY1BVYpeqHKZpkc3LHp': 'file_storage/call_4JydZyY1BVYpeqHKZpkc3LHp.json', 'var_call_TdJHTBp6WK291mH1pwasawjw': None}

exec(code, env_args)
