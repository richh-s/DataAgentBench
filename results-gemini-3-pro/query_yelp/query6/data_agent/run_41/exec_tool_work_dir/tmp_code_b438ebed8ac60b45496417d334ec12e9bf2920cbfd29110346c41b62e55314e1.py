code = """import json
import pandas as pd
from dateutil import parser

# Load the reviews
with open('var_function-call-14899900195905272096.json', 'r') as f:
    reviews = json.load(f)

df = pd.DataFrame(reviews)

# Function to parse date
def parse_date(date_str):
    try:
        return parser.parse(date_str)
    except:
        return None

df['parsed_date'] = df['date'].apply(parse_date)

# Filter by date range
start_date = pd.Timestamp('2016-01-01')
end_date = pd.Timestamp('2016-06-30 23:59:59') # Inclusive of the whole day

filtered_df = df[(df['parsed_date'] >= start_date) & (df['parsed_date'] <= end_date)].copy()

# Group by business_ref
stats = filtered_df.groupby('business_ref').agg(
    avg_rating=('rating', lambda x: x.astype(int).mean()),
    review_count=('rating', 'count')
).reset_index()

# Filter count >= 5
eligible = stats[stats['review_count'] >= 5]

# Sort by avg_rating desc, then review_count desc
top_business = eligible.sort_values(by=['avg_rating', 'review_count'], ascending=[False, False]).head(1)

result = top_business.to_dict(orient='records')
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-10257306587086123065': [{'_id': '6859a000fe8b31cd7362e2ab', 'business_id': 'businessid_49', 'name': 'Steps to Learning Montessori Preschool', 'review_count': '8', 'is_open': '1', 'attributes': {'BusinessAcceptsCreditCards': 'True', 'WiFi': "u'no'", 'BusinessAcceptsBitcoin': 'False'}, 'hours': {'Monday': '0:0-0:0', 'Tuesday': '8:0-17:0', 'Wednesday': '8:0-17:0', 'Thursday': '8:0-17:0', 'Friday': '8:0-17:0'}, 'description': 'Located at 6901 Phelps Rd in Goleta, CA, this facility offers a nurturing environment for young learners, providing a range of services in Education, Elementary Schools, Child Care & Day Care, Local Services, Preschools, and Montessori Schools.'}], 'var_function-call-9547475191440027522': [{'business_ref': 'businessref_9', 'avg_rating': '4.0', 'review_count': '5'}], 'var_function-call-13402205198756970306': [{'date': 'August 01, 2016 at 03:44 AM'}, {'date': 'June 14, 2021 at 11:39 AM'}, {'date': '29 May 2013, 23:01'}], 'var_function-call-1001635337210120739': [{'count_star()': '2000'}], 'var_function-call-14899900195905272096': 'file_storage/function-call-14899900195905272096.json'}

exec(code, env_args)
