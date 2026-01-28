code = """import json, pathlib

funding = var_call_NvqCRnfgsoEgZjwpaDBaQaUm
# Completed in 2022 park-related project identified from civic doc: Bluffs Park Shade Structure
completed_2022 = {'Bluffs Park Shade Structure'}

total = 0
included=[]
for r in funding:
    pn = r['Project_Name']
    amt = int(r['Total_Amount'])
    if pn in completed_2022:
        total += amt
        included.append({'Project_Name': pn, 'Total_Amount': amt})

print('__RESULT__:')
print(json.dumps({'total_funding': total, 'included': included}))"""

env_args = {'var_call_pZYPMVicdmBSCYrwRtbA6ApW': ['Funding'], 'var_call_W7LR9U57MoPAvg0vnr3DxBQ2': ['civic_docs'], 'var_call_2wio0siV2Oiezi44FZZJWnUI': 'file_storage/call_2wio0siV2Oiezi44FZZJWnUI.json', 'var_call_GA1kZuYM4iPHeHOTLsOa19MX': {'projects': [], 'count': 0}, 'var_call_FblSdvFQbESOdA84gPeKNNJn': 'file_storage/call_FblSdvFQbESOdA84gPeKNNJn.json', 'var_call_vF95wa5K8urB8NQcMZ0MiJbH': {'projects': [], 'count': 0}, 'var_call_HDL0pK8SePyYKGzqjrXyyb7G': 'file_storage/call_HDL0pK8SePyYKGzqjrXyyb7G.json', 'var_call_IaPFHeEyaxikBo1ZQlERRPzn': {'projects': [], 'count': 0}, 'var_call_NvqCRnfgsoEgZjwpaDBaQaUm': [{'Project_Name': 'Bluffs Park Shade Structure', 'Total_Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Total_Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Total_Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Total_Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Total_Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Total_Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Total_Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Total_Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Total_Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Total_Amount': '50000'}, {'Project_Name': 'Permanent Skate Park', 'Total_Amount': '97000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Total_Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Total_Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Total_Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Total_Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Total_Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Total_Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Total_Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Total_Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Total_Amount': '23000'}], 'var_call_79wPTb3bAUdPstXtJ1NPbie0': 'file_storage/call_79wPTb3bAUdPstXtJ1NPbie0.json'}

exec(code, env_args)
