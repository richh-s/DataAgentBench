code = """import json

k_fund = locals()['var_function-call-16838995843230881233']
with open(k_fund, 'r') as f:
    funding_data = json.load(f)

res = [item['Project_Name'] for item in funding_data if "Clover" in item['Project_Name']]
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_function-call-16838995843230881233': 'file_storage/function-call-16838995843230881233.json', 'var_function-call-16838995843230880788': 'file_storage/function-call-16838995843230880788.json', 'var_function-call-13293051466899965091': 'file_storage/function-call-13293051466899965091.json', 'var_function-call-16442694046434714773': 12, 'var_function-call-11146164805513452029': ['Malibu Bluffs Park South Walkway Repairs', 'PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Clover Heights Storm Drain', 'Civic Center Stormwater Diversion Structure', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway', 'Malibu Canyon Road Traffic Study'], 'var_function-call-5515255172171098873': ['Westward Beach Road Drainage Improvements Project', 'PCH at Trancas Canyon Road Right Turn Lane', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Civic Center Stormwater Diversion Structure', 'PCH Median Improvements Project', 'Permanent Skate Park']}

exec(code, env_args)
