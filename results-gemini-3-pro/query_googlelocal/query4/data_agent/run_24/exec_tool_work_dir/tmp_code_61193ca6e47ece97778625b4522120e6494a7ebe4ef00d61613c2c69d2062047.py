code = """import json
import pandas as pd
from datetime import datetime

# Load the file
with open(locals()['var_function-call-15851127763992265341'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Function to parse dates
def parse_date(date_str):
    if not date_str:
        return None
    try:
        # Try pandas to_datetime which handles many formats
        return pd.to_datetime(date_str)
    except:
        return None

# Convert 'time' column to datetime objects
# Since the format is mixed, pd.to_datetime with errors='coerce' is best, 
# but "at" might confuse it if not handled? 
# "September 03, 2020 at 04:15 PM" -> pandas usually handles standard strings, but 'at' might be an issue.
# Let's replace ' at ' with ' ' before parsing just in case.
df['time_clean'] = df['time'].str.replace(' at ', ' ', regex=False)
df['dt'] = pd.to_datetime(df['time_clean'], errors='coerce')

# Check for rows where parsing failed
failed = df[df['dt'].isna()]
if not failed.empty:
    # Just to be sure, print some failed ones if any significantly affect 2019 count
    print("Failed to parse:", failed['time'].head().tolist())

# Filter for 2019
df_2019 = df[df['dt'].dt.year == 2019]

# Filter for rating >= 4.5
# Rating is string in JSON ("5"), convert to numeric
df_2019['rating'] = pd.to_numeric(df_2019['rating'])
df_high = df_2019[df_2019['rating'] >= 4.5]

# Group by gmap_id and count
top_businesses = df_high.groupby('gmap_id').size().reset_index(name='count')
top_businesses = top_businesses.sort_values(by='count', ascending=False).head(3)

print("__RESULT__:")
print(top_businesses.to_json(orient='records'))"""

env_args = {'var_function-call-17323002390654581402': [{'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2021-04-12 17:07:52', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2018-04-23 16:24:26', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': '2017-07-10 22:12:19', 'rating': '5', 'gmap_id': 'gmap_44'}, {'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'gmap_id': 'gmap_44'}], 'var_function-call-18289292612286074314': [{'COUNT(*)': '2000'}], 'var_function-call-15851127763992265341': 'file_storage/function-call-15851127763992265341.json'}

exec(code, env_args)
