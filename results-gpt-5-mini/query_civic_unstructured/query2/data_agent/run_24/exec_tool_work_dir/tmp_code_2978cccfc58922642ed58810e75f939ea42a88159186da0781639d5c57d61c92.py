code = """import json

# Sum amounts from the park_records result
park_records = var_call_3COXn1FarHfitfk9aTRWAjBc
# compute total
total = sum(int(r['Amount']) for r in park_records)

print("__RESULT__:")
print(json.dumps(f"Total funding for park-related projects completed in 2022: ${total}"))"""

env_args = {'var_call_hrawrctsouX7uyMEWqR3rdZM': ['civic_docs'], 'var_call_vr3n5PyiecSjEweMrZb1UBzg': ['Funding'], 'var_call_QNC7P8mjljZASGfnnZi9S4PP': 'file_storage/call_QNC7P8mjljZASGfnnZi9S4PP.json', 'var_call_jifqAMOUNn9PorNbe5w6A4Vg': 'file_storage/call_jifqAMOUNn9PorNbe5w6A4Vg.json', 'var_call_tLI5AGkLxPC0Dm9UGN4L4tvU': 'Total funding for park-related projects completed in 2022: $1123000', 'var_call_3COXn1FarHfitfk9aTRWAjBc': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': 21000}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': 39000}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': 41000}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': 69000}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': 44000}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': 91000}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': 81000}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': 17000}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': 14000}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': 50000}, {'Project_Name': 'Permanent Skate Park', 'Amount': 97000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': 78000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': 44000}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': 92000}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': 24000}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': 65000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': 68000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': 43000}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': 32000}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': 23000}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': 90000}]}

exec(code, env_args)
