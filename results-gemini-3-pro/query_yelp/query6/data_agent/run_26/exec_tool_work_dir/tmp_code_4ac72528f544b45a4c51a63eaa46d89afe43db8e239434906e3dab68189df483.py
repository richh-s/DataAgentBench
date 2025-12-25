code = """import pandas as pd
import json

# Load data
with open('var_function-call-7399918071576645466.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Convert rating to int
df['rating'] = pd.to_numeric(df['rating'])

# Convert date. 
# Some formats have "at", some don't. pd.to_datetime is usually smart enough.
df['dt'] = pd.to_datetime(df['date'], errors='coerce')

# Filter for date range
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30')

# Note: Timestamps in data seem to include time. 
# "2016-06-30" as end_date means 2016-06-30 00:00:00. 
# I should probably include the whole day of June 30. 
# So end_date should be 2016-06-30 23:59:59 or < 2016-07-01.
# The query says "between January 1, 2016 and June 30, 2016". Usually inclusive.
end_date_inclusive = pd.Timestamp('2016-07-01')

mask = (df['dt'] >= start_date) & (df['dt'] < end_date_inclusive)
filtered_df = df[mask]

# Group by business
grouped = filtered_df.groupby('business_ref').agg(
    avg_rating=('rating', 'mean'),
    review_count=('rating', 'count')
).reset_index()

# Filter count >= 5
final_candidates = grouped[grouped['review_count'] >= 5]

# Sort
final_candidates = final_candidates.sort_values(by='avg_rating', ascending=False)

print("__RESULT__:")
print(final_candidates.head(5).to_json(orient='records'))"""

env_args = {'var_function-call-3326859269727256751': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-3326859269727259902': [{'review_id': 'reviewid_135', 'user_id': 'userid_548', 'business_ref': 'businessref_34', 'rating': '2', 'useful': '0', 'funny': '0', 'cool': '0', 'text': "Sure, it's cheap, but there isn't much to see. I think you'd have to have a big interest in the topic to find it exciting, and kids would be bored. I think it only lasted maybe 10-15 minutes. Our tour person was somewhat knowledgeable and seemed into it, but he didn't give us much time to read the information on each level. I had to take photos of the plaques to read later, and half of them need replacing, as they are so sun-bleached they're virtually unreadable (tour guide said they're being replaced soon and that the other half were already replaced). I really thought it needed to be higher up to give a good view. The Lewis and Clark State Historic Site just down the road was more interesting and free. If you live around here like I do and have nothing better to do, you might want to give it a go if the topic interests you, but if you're a tourist, this is not something you should waste your time on.", 'date': 'August 01, 2016 at 03:44 AM'}], 'var_function-call-12716936718522398800': [{'count_star()': '2000'}], 'var_function-call-7399918071576645466': 'file_storage/function-call-7399918071576645466.json'}

exec(code, env_args)
