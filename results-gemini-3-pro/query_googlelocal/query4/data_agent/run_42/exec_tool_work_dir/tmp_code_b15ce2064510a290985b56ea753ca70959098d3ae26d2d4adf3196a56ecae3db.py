code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-15487975259407895354'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert rating to float to be sure
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df = df[df['rating'] >= 4.5]

# Function to check if year is 2019
def is_2019(time_str):
    if not isinstance(time_str, str):
        return False
    # Try parsing with pandas
    try:
        dt = pd.to_datetime(time_str, infer_datetime_format=True)
        return dt.year == 2019
    except:
        # Fallback to string check if parsing fails (though pd.to_datetime is robust)
        # Check for specific patterns if needed, but '2019' usually indicates the year in these formats
        # Be careful about 20:19 time.
        # If it's YYYY-MM-DD, it starts with 2019
        if time_str.strip().startswith('2019-'):
            return True
        # If it contains ", 2019" or " 2019 at"
        if ', 2019' in time_str or ' 2019 at' in time_str or ' 2019,' in time_str:
            return True
        return False

# Since pd.to_datetime can be slow on list apply, but here dataset is small (238 rows), it's fine.
# Actually, the dataset is small enough.
df['is_2019'] = df['time'].apply(is_2019)

df_2019 = df[df['is_2019']]

counts = df_2019['gmap_id'].value_counts().head(3)
result = counts.to_dict()

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-721172923845096452': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-8153778282409362311': [{'gmap_id': 'gmap_35', 'cnt': '19'}, {'gmap_id': 'gmap_53', 'cnt': '17'}, {'gmap_id': 'gmap_20', 'cnt': '14'}], 'var_function-call-4223877372712285810': [{'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}], 'var_function-call-18078184365457644896': [{'COUNT(*)': '238'}], 'var_function-call-15487975259407895354': 'file_storage/function-call-15487975259407895354.json'}

exec(code, env_args)
