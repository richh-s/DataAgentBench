code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-12959410789541669173'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse time
def parse_time(t_str):
    try:
        # Remove ' at ' to help parsing
        t_clean = t_str.replace(' at ', ' ')
        return pd.to_datetime(t_clean)
    except:
        return None

df['dt'] = df['time'].apply(parse_time)

# Filter for year 2019
df_2019 = df[df['dt'].dt.year == 2019]

# Count by gmap_id
counts = df_2019['gmap_id'].value_counts().head(3)

result = []
for gmap_id, count in counts.items():
    result.append({"gmap_id": gmap_id, "count": int(count)})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1697742831342600266': [{'time': 'September 03, 2020 at 04:15 PM'}, {'time': '2021-04-12 17:07:52'}, {'time': '2018-04-23 16:24:26'}, {'time': '2017-07-10 22:12:19'}, {'time': 'May 19, 2021 at 03:55 AM'}], 'var_function-call-13829490820287811327': [{'rating': '5'}, {'rating': '3'}, {'rating': '4'}, {'rating': '1'}, {'rating': '2'}], 'var_function-call-12471910125509247684': [{'gmap_id': 'gmap_35', 'review_count': '19'}, {'gmap_id': 'gmap_53', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'review_count': '14'}], 'var_function-call-18050659555735811691': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}], 'var_function-call-17096775400124660122': [{'time': '2019-10-05 02:12:18'}, {'time': '2019-09-01 19:44:53'}, {'time': '29 Oct 2019, 06:11'}, {'time': '2019-10-15 05:37:34'}, {'time': '07 Dec 2019, 05:34'}], 'var_function-call-17706588200446007906': [{'COUNT(*)': '1666'}], 'var_function-call-12959410789541669173': 'file_storage/function-call-12959410789541669173.json'}

exec(code, env_args)
