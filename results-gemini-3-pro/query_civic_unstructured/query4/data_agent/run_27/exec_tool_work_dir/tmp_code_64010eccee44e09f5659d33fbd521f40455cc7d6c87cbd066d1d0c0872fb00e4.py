code = """import json

# Load data
try:
    with open(locals()['var_function-call-14484383312997892465'], 'r') as f:
        funding_recs = json.load(f)
    # The result from previous step is a list of strings
    found_projects = locals()['var_function-call-8176490038360037782']
except:
    funding_recs = []
    found_projects = []

# Filter funding records
matched_funding = [r for r in funding_recs if r['Project_Name'] in found_projects]

total_amount = sum(float(r['Amount']) for r in matched_funding)
count = len(matched_funding)

print("__RESULT__:")
print(json.dumps({"count": count, "total_funding": total_amount, "projects": found_projects}))"""

env_args = {'var_function-call-17327225246919229533': 'file_storage/function-call-17327225246919229533.json', 'var_function-call-6904797110646759006': 'file_storage/function-call-6904797110646759006.json', 'var_function-call-15743062509627089682': ['Funding'], 'var_function-call-6371047367361917112': 'file_storage/function-call-6371047367361917112.json', 'var_function-call-640204841284110003': 'file_storage/function-call-640204841284110003.json', 'var_function-call-8176490038360037782': ['Marie Canyon Green Streets', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Civic Center Water Treatment Facility Phase 2', 'PCH Median Improvements Project', 'Bluffs Park Shade Structure', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'PCH Signal Synchronization System Improvements Project'], 'var_function-call-8625744080577818283': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}], 'var_function-call-14484383312997892465': 'file_storage/function-call-14484383312997892465.json'}

exec(code, env_args)
