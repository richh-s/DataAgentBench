code = """import json
import re

# Load business data
business_file = locals()['var_functions.query_db:2']
with open(business_file, 'r') as f:
    businesses = json.load(f)

# Debug specific businesses that should qualify
print("Debugging Vons Chicken and Angel-A Massage:")
for business in businesses:
    if 'Vons Chicken' in business['name']:
        print(f"Vons Chicken hours: {repr(business['hours'])}")
        # Try to parse
        try:
            hours_data = eval(business['hours'])
            for day_entry in hours_data:
                if 'Thursday' in day_entry[0]:
                    print(f"  Thursday hours: {repr(day_entry[1])}")
        except Exception as e:
            print(f"  Error parsing: {e}")
            
    if 'Angel-A Massage' in business['name']:
        print(f"Angel-A Massage hours: {repr(business['hours'])}")
        try:
            hours_data = eval(business['hours'])
            for day_entry in hours_data:
                if 'Thursday' in day_entry[0]:
                    print(f"  Thursday hours: {repr(day_entry[1])}")
        except Exception as e:
            print(f"  Error parsing: {e}")

print('__RESULT__:')
print(json.dumps({'status': 'debug complete'}))"""

env_args = {'var_functions.query_db:0': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 66, 'sample': {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}}, 'var_functions.execute_python:8': {'total_businesses': 66, 'eligible_businesses': 28, 'sample_eligible': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'business_count': 66, 'review_count': 665, 'review_sample': [{'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}]}, 'var_functions.execute_python:14': {'eligible_count': 0, 'with_reviews': 0, 'top_5': [], 'all_ranked': []}, 'var_functions.execute_python:16': {'total_businesses': 66, 'eligible_count': 0, 'eligible_sample': []}}

exec(code, env_args)
