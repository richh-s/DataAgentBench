code = """import json
import pandas as pd

open_after_6pm_businesses = locals()['var_function-call-120665550301184073']
gmap_ids = [business['gmap_id'] for business in open_after_6pm_businesses]

# Prepare the gmap_id list for the SQL query
gmap_ids_str = ', '.join([f"'{gmap_id}'" for gmap_id in gmap_ids])

query = f"SELECT gmap_id, AVG(rating) AS average_rating FROM review WHERE gmap_id IN ({gmap_ids_str}) GROUP BY gmap_id;"

print('__RESULT__:')
print(json.dumps(query))"""

env_args = {'var_function-call-3480839269620664486': 'file_storage/function-call-3480839269620664486.json', 'var_function-call-120665550301184073': [{'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_9', 'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]'}, {'gmap_id': 'gmap_55', 'name': 'Mobile Moreno Valley Dispensary', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}], 'var_function-call-12162235543187213780': "'gmap_74', 'gmap_22', 'gmap_20', 'gmap_28', 'gmap_63', 'gmap_9', 'gmap_55'"}

exec(code, env_args)
