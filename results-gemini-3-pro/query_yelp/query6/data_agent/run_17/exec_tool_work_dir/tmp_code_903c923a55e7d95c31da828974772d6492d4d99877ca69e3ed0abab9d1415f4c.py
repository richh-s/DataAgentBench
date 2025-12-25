code = """import pandas as pd
import json

# Load data
file_path = locals()['var_function-call-11759411478294820503']
with open(file_path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Parse date
# The formats are mixed. pd.to_datetime with format=None (default) and mixed=True might work, 
# but "August 01, 2016 at 03:44 AM" might be tricky if not standard.
# However, pandas parser is generally smart. Let's try.
# If "at" causes issues, we can remove it.
df['date_clean'] = df['date'].str.replace(' at ', ' ')
df['dt'] = pd.to_datetime(df['date_clean'], errors='coerce')

# Check for nulls
if df['dt'].isnull().any():
    print("Warning: some dates failed to parse.")
    print(df[df['dt'].isnull()]['date'].head())

# Filter date
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30 23:59:59')
df_filtered = df[(df['dt'] >= start_date) & (df['dt'] <= end_date)].copy()

# Convert rating to int
df_filtered['rating'] = pd.to_numeric(df_filtered['rating'])

# Group by business_ref
stats = df_filtered.groupby('business_ref')['rating'].agg(['mean', 'count'])

# Filter count >= 5
candidates = stats[stats['count'] >= 5]

# Sort by mean rating desc
result = candidates.sort_values(by=['mean', 'count'], ascending=[False, False])

print("__RESULT__:")
print(result.reset_index().to_json(orient='records'))"""

env_args = {'var_function-call-7573052347303855368': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-7573052347303856453': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-2453884391973255384': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}, {'date': '21 May 2016, 18:48'}, {'date': 'November 01, 2021 at 05:11 PM'}, {'date': '2013-07-08 21:47:00'}, {'date': 'March 02, 2009 at 09:43 PM'}, {'date': 'March 16, 2014 at 12:40 AM'}, {'date': 'September 18, 2014 at 05:50 PM'}, {'date': '17 Apr 2017, 14:04'}, {'date': '2016-08-15 21:16:00'}, {'date': '08 Jun 2019, 07:10'}, {'date': '2016-07-18 21:37:00'}, {'date': '2019-05-30 11:54:00'}, {'date': '08 Feb 2013, 21:14'}, {'date': 'August 02, 2015 at 04:10 AM'}, {'date': 'October 26, 2016 at 03:04 PM'}, {'date': 'November 01, 2014 at 06:20 PM'}, {'date': '05 Jan 2017, 21:13'}, {'date': '2017-08-05 01:46:00'}], 'var_function-call-15794483793564709409': [{'count_star()': '2000'}], 'var_function-call-11759411478294820503': 'file_storage/function-call-11759411478294820503.json'}

exec(code, env_args)
