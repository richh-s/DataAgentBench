code = """import json

citing_assignees_info = locals()['var_function-call-3658823678110237683']
cpc_titles_data = locals()['var_function-call-10417554577926254518']

cpc_code_to_title = {item['symbol']: item['titleFull'] for item in cpc_titles_data}

final_result = []
for item in citing_assignees_info:
    assignee = item['assignee']
    cpc_code = item['cpc_code']
    title_full = cpc_code_to_title.get(cpc_code, 'Title Not Found')
    final_result.append({'citing_assignee': assignee, 'cpc_subclass_title': title_full})

# Remove duplicates by converting to a set of tuples and then back to a list of dicts
# This ensures each assignee-CPC title pair is unique in the final output
unique_results = []
seen = set()
for entry in final_result:
    # Create a hashable representation of the dictionary
    entry_tuple = tuple(sorted(entry.items()))
    if entry_tuple not in seen:
        seen.add(entry_tuple)
        unique_results.append(entry)

print('__RESULT__:')
print(json.dumps(unique_results))"""

env_args = {'var_function-call-13930125777228040085': ['publicationinfo'], 'var_function-call-1621381890062432431': [], 'var_function-call-10802364016398363406': [], 'var_function-call-13532911310427381018': 'file_storage/function-call-13532911310427381018.json', 'var_function-call-10059552934646644970': ['US-6767662-B2', 'US-9061071-B2', 'US-11376346-B2', 'US-6750960-B2', 'US-11546022-B2', 'US-11667770-B2'], 'var_function-call-15593298384675158215': 'file_storage/function-call-15593298384675158215.json', 'var_function-call-3658823678110237683': [{'assignee': 'UNKNOWN', 'cpc_code': 'H01M8/2425'}, {'assignee': 'UNKNOWN', 'cpc_code': 'H01M8/2425'}, {'assignee': 'UNKNOWN', 'cpc_code': 'H01M4/9066'}], 'var_function-call-17281492053636503966': ['H01M8/2425', 'H01M4/9066'], 'var_function-call-18095356360088900741': ['cpc_definition'], 'var_function-call-10417554577926254518': [{'symbol': 'H01M4/9066', 'titleFull': 'Metals or alloys specially used in fuel cell operating at high temperature, e.g. SOFC of metal-ceramic composites or mixtures, e.g. cermets'}, {'symbol': 'H01M8/2425', 'titleFull': 'High-temperature cells with solid electrolytes'}]}

exec(code, env_args)
