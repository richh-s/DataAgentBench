code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-13549811498987056306']

with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

def is_2019(time_str):
    if not isinstance(time_str, str):
        return False
    if re.search(r'(?:^|\D)2019(?:\D|$)', time_str):
        return True
    return False

df['is_2019'] = df['time'].apply(is_2019)
df_2019 = df[df['is_2019']]

counts = df_2019['gmap_id'].value_counts().reset_index()
counts.columns = ['gmap_id', 'count']

print("__RESULT__:")
print(counts.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-8757251067354364186': ['review'], 'var_function-call-17071403760519993033': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-13920282489321228867': [{'COUNT(*)': '2000'}], 'var_function-call-13549811498987056306': 'file_storage/function-call-13549811498987056306.json', 'var_function-call-12314329056861903974': [{'gmap_id': 'gmap_35', 'count': 19}, {'gmap_id': 'gmap_53', 'count': 17}, {'gmap_id': 'gmap_20', 'count': 14}], 'var_function-call-6880039279302083964': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}]}

exec(code, env_args)
