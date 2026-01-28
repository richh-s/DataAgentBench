code = """import json, re

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_qSNM8svbdwVUOUeF2YIBUzBK)

# find a snippet around 'Disaster Recovery Projects' in first such doc
for d in docs:
    txt = d.get('text','') or ''
    idx = txt.lower().find('disaster recovery projects')
    if idx!=-1:
        snippet = txt[idx: idx+2500]
        break
else:
    snippet = None

print('__RESULT__:')
print(json.dumps({'snippet': snippet}))"""

env_args = {'var_call_9VTcyE0rwaemK7cQ94kOlwa6': 'file_storage/call_9VTcyE0rwaemK7cQ94kOlwa6.json', 'var_call_qSNM8svbdwVUOUeF2YIBUzBK': 'file_storage/call_qSNM8svbdwVUOUeF2YIBUzBK.json', 'var_call_VEb87KrIX5pu8BEnQ3XJsuii': {'total_funding_usd': 0, 'matched_disaster_projects_started_2022_count': 0, 'matched_disaster_projects_started_2022': []}, 'var_call_V3VoQYl4KFgoq7mHfZHkep3h': {'docs_with_disaster_section': 5, 'unique_funding_projects_found_in_disaster_docs': 81, 'top_projects': [['PCH Signal Synchronization System Improvements Project', 5], ['Civic Center Water Treatment Facility Phase 2', 5], ['Marie Canyon Green Streets', 5], ['PCH Median Improvements Project', 5], ['Bluffs Park Shade Structure', 5], ['Clover Heights Storm Drain', 5], ['Malibu Road Slope Repairs', 5], ['Storm Drain Master Plan', 4], ['Broad Beach Road Water Quality Infrastructure Repairs', 4], ['Corral Canyon Road Bridge Repairs', 4], ['Corral Canyon Culvert Repairs', 4], ['Trancas Canyon Park Planting and Irrigation Repairs', 4], ['Clover Heights Storm Drain (FEMA Project)', 4], ['Civic Center Way Improvements', 4], ['Encinal Canyon Road Drainage Improvements', 4], ['Trancas Canyon Park Slope Stabilization Project', 4], ['Latigo Canyon Road Roadway/Retaining Wall Improvements', 4], ['Latigo Canyon Road Culvert Repairs', 4], ['Westward Beach Road Improvements Project', 4], ['Vehicle Protection Devices', 4], ['Civic Center Stormwater Diversion Structure', 4], ['Annual Street Maintenance', 4], ['Birdview Avenue Improvements', 4], ['PCH at Trancas Canyon Road Right Turn Lane', 3], ['Malibu Bluffs Park South Walkway', 3], ['PCH Median Improvements at Paradise Cove and Zuma Beach', 3], ['Permanent Skate Park', 3], ['Storm Drain Master Plan (FEMA Project)', 3], ['Malibu Park Drainage Improvements', 3], ['Guardrail Replacement Citywide', 3]]}}

exec(code, env_args)
