code = """import pandas as pd
import json

# Load data
with open(locals()['var_function-call-8257395849576273225'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Filter rating >= 4.5
# ratings are strings in the preview, e.g., "5". convert to numeric.
df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
df_high_rating = df[df['rating'] >= 4.5].copy()

# Filter year 2019
# We can try pd.to_datetime. 
# Since formats are mixed, let's try to convert and extract year.
# If to_datetime fails for some, we will inspect.
df_high_rating['dt'] = pd.to_datetime(df_high_rating['time'], errors='coerce')

# Check how many NaT we got
num_nat = df_high_rating['dt'].isna().sum()

# If NaT is high, we might need custom parsing, but usually pandas is good.
# Let's see the year
df_2019 = df_high_rating[df_high_rating['dt'].dt.year == 2019]

# Group by gmap_id and count
counts = df_2019.groupby('gmap_id').size().reset_index(name='count')
top_3 = counts.sort_values(by='count', ascending=False).head(3)

print("__RESULT__:")
print(top_3.to_json(orient='records'))"""

env_args = {'var_function-call-4093023164407682720': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-14002306630734960193': [{'COUNT(*)': '2000'}], 'var_function-call-8257395849576273225': 'file_storage/function-call-8257395849576273225.json'}

exec(code, env_args)
