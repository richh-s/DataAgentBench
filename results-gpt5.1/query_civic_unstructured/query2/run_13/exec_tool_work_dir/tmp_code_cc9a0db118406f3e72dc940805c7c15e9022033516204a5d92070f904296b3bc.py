code = """import json, pandas as pd

funding_records = var_call_Vdaf5AocBsUA9lWwVEELnOYh
funding = pd.DataFrame(funding_records)
funding['Amount'] = funding['Amount'].astype(int)

projects_2022 = {'Bluffs Park Shade Structure'}

mask = funding['Project_Name'].isin(projects_2022)

total = int(funding.loc[mask, 'Amount'].sum())

result = {"projects_2022_park": sorted(projects_2022), "total_funding": total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_EZnFkfXrvSwcsUTh5Fl9z4iQ': 'file_storage/call_EZnFkfXrvSwcsUTh5Fl9z4iQ.json', 'var_call_Vdaf5AocBsUA9lWwVEELnOYh': 'file_storage/call_Vdaf5AocBsUA9lWwVEELnOYh.json'}

exec(code, env_args)
