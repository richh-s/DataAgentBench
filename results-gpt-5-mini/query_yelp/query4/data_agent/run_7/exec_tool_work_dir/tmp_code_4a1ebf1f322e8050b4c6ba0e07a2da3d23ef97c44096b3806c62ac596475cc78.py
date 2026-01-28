code = """import json
import pandas as pd

# Load business docs
with open(var_call_a4tjcgXpcAH3ZeQ2RVEVExh0, 'r') as f:
    docs = json.load(f)

# Create df
df = pd.DataFrame(docs)

# Inspect keys and sample
info = {'columns': df.columns.tolist(), 'num_rows': len(df), 'head': df.head(10).to_dict(orient='records')}
import json
print("__RESULT__:")
print(json.dumps(info))"""

env_args = {'var_call_rOGdUkWyGCSFzHjSQs9yUcKm': ['business', 'checkin'], 'var_call_7s61UCAIDop1liwo1vPB7xQe': ['review', 'tip', 'user'], 'var_call_FekEckYHEJU4LcfALlmJ26B8': 'file_storage/call_FekEckYHEJU4LcfALlmJ26B8.json', 'var_call_y3A2nxDih0pCWz7NwAV9bfGk': 'file_storage/call_y3A2nxDih0pCWz7NwAV9bfGk.json', 'var_call_bAtxBNzZYeH67OXyH1CPG8r5': {'category': None, 'business_count': 0, 'average_rating': None}, 'var_call_ydIDn5hahz93v1O8NuB0VQ6f': [], 'var_call_HtalBylRE2GeWzulrEqWZeYF': {'num_docs': 91, 'all_keys': ['_id', 'attributes', 'business_id'], 'sample_first_5': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}}, {'_id': '6859a000fe8b31cd7362e2ac', 'business_id': 'businessid_47', 'attributes': {'ByAppointmentOnly': 'False', 'BusinessAcceptsCreditCards': 'True', 'GoodForKids': 'True', 'RestaurantsPriceRange2': '2', 'BikeParking': 'False', 'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': True, 'valet': False}"}}, {'_id': '6859a000fe8b31cd7362e2ad', 'business_id': 'businessid_88', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'GoodForKids': 'True', 'BusinessAcceptsCreditCards': 'True', 'ByAppointmentOnly': 'False', 'BikeParking': 'True'}}, {'_id': '6859a000fe8b31cd7362e2af', 'business_id': 'businessid_33', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'BusinessAcceptsCreditCards': 'True', 'AcceptsInsurance': 'False', 'ByAppointmentOnly': 'False', 'RestaurantsPriceRange2': '2', 'WheelchairAccessible': 'True', 'BikeParking': 'False'}}, {'_id': '6859a000fe8b31cd7362e2b0', 'business_id': 'businessid_74', 'attributes': {'BusinessParking': "{'garage': False, 'street': False, 'validated': False, 'lot': False, 'valet': False}", 'RestaurantsPriceRange2': '4', 'BikeParking': 'False'}}]}, 'var_call_a4tjcgXpcAH3ZeQ2RVEVExh0': 'file_storage/call_a4tjcgXpcAH3ZeQ2RVEVExh0.json'}

exec(code, env_args)
