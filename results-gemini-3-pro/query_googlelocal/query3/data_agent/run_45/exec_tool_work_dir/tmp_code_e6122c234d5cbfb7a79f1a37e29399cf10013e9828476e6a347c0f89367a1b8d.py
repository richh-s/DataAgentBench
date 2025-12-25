code = """import json

# File path for businesses
file_path_biz = locals()['var_function-call-9505002775633145034']
with open(file_path_biz, 'r') as f:
    businesses = json.load(f)

# Ratings from previous step
ratings_data = locals()['var_function-call-13697623795193988147']
if isinstance(ratings_data, str):
    ratings_data = json.loads(ratings_data)

# Convert ratings to dict
rating_map = {r['gmap_id']: float(r['avg_rating']) for r in ratings_data}

# Filter businesses that are in the rating map
results = []
for b in businesses:
    gid = b['gmap_id']
    if gid in rating_map:
        results.append({
            'name': b['name'],
            'hours': b['hours'],
            'avg_rating': rating_map[gid]
        })

# Sort by avg_rating descending
results.sort(key=lambda x: x['avg_rating'], reverse=True)

# Top 5
top_5 = results[:5]

print("__RESULT__:")
print(json.dumps(top_5))"""

env_args = {'var_function-call-16930252738869414104': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'hours': 'None'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_function-call-13480375080291303633': [{'count': '79'}], 'var_function-call-9505002775633145034': 'file_storage/function-call-9505002775633145034.json', 'var_function-call-1520574728960295240': ['gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_11', 'gmap_61', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_40', 'gmap_60'], 'var_function-call-13697623795193988147': [{'gmap_id': 'gmap_11', 'avg_rating': '4.9603174603174605'}, {'gmap_id': 'gmap_12', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_20', 'avg_rating': '4.178571428571429'}, {'gmap_id': 'gmap_21', 'avg_rating': '3.933333333333333'}, {'gmap_id': 'gmap_22', 'avg_rating': '4.333333333333333'}, {'gmap_id': 'gmap_24', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_28', 'avg_rating': '3.875'}, {'gmap_id': 'gmap_30', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_32', 'avg_rating': '4.166666666666667'}, {'gmap_id': 'gmap_33', 'avg_rating': '2.125'}, {'gmap_id': 'gmap_36', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857'}, {'gmap_id': 'gmap_51', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_53', 'avg_rating': '4.894736842105263'}, {'gmap_id': 'gmap_55', 'avg_rating': '1.0'}, {'gmap_id': 'gmap_60', 'avg_rating': '1.8235294117647058'}, {'gmap_id': 'gmap_61', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_63', 'avg_rating': '4.4375'}, {'gmap_id': 'gmap_65', 'avg_rating': '4.115384615384615'}, {'gmap_id': 'gmap_67', 'avg_rating': '4.451612903225806'}, {'gmap_id': 'gmap_68', 'avg_rating': '4.0'}, {'gmap_id': 'gmap_7', 'avg_rating': '4.837837837837838'}, {'gmap_id': 'gmap_74', 'avg_rating': '4.666666666666667'}, {'gmap_id': 'gmap_8', 'avg_rating': '5.0'}, {'gmap_id': 'gmap_9', 'avg_rating': '5.0'}]}

exec(code, env_args)
