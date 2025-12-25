code = """import json
import pandas as pd

# Load ratings
file_path_ratings = locals()['var_function-call-11078630846747515908']
with open(file_path_ratings, 'r') as f:
    ratings_data = json.load(f)

# Load businesses
# Assuming var_function-call-6456467801347399663 contains the list object because I printed it directly
# Wait, if the tool execution returns a printed string, the result variable holds that string (or object if parsed).
# The system said "The result is stored under key... The result is: [...]"
# This implies the result is a Python list (if parsed from JSON) or a JSON string.
# Since I used print(json.dumps(late_businesses)), the result is a JSON string representing the list.
# But execute_python usually returns the raw output string.
# Let's check if I can access it directly. If it's a string, I need to json.loads it.

# Actually, I can just use the previous variable `late_businesses` if I can access it.
# But the environment is fresh or variables might not persist across execute_python calls?
# "Inside execute_python code you may read storage entries..."
# Storage entries are from tool results.
# So I must read `var_function-call-6456467801347399663`.

late_businesses_raw = locals()['var_function-call-6456467801347399663']
if isinstance(late_businesses_raw, str):
    try:
        late_businesses = json.loads(late_businesses_raw)
    except:
        # If it's a file path? No, the previous result was small enough to be inline.
        # But if it is a list already?
        late_businesses = late_businesses_raw
else:
    late_businesses = late_businesses_raw

# Convert ratings to DataFrame
df_ratings = pd.DataFrame(ratings_data)
# Ensure rating is numeric
df_ratings['rating'] = pd.to_numeric(df_ratings['rating'])

# Calculate average rating per gmap_id
avg_ratings = df_ratings.groupby('gmap_id')['rating'].mean().reset_index()
avg_ratings.rename(columns={'rating': 'average_rating'}, inplace=True)

# Convert businesses to DataFrame
df_businesses = pd.DataFrame(late_businesses)

# Merge
df_final = pd.merge(df_businesses, avg_ratings, on='gmap_id', how='left')

# Sort by average_rating descending
# If ratings are equal, maybe sort by name or review count? 
# Let's sort by rating desc.
df_final = df_final.sort_values(by='average_rating', ascending=False)

# Select top 5
top_5 = df_final.head(5)

# Format for output
result_list = top_5[['name', 'hours', 'average_rating']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_function-call-17526194597046591921': [{'name': 'City Textile', 'gmap_id': 'gmap_44', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'hours': 'None', 'MISC': 'None', 'state': 'Open now'}], 'var_function-call-12219215353860809743': [{'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}, {'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}], 'var_function-call-8631971219953678902': [{'count': '66'}], 'var_function-call-11765510306618497496': 'file_storage/function-call-11765510306618497496.json', 'var_function-call-6456467801347399663': [{'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]', 'gmap_id': 'gmap_74'}, {'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'gmap_id': 'gmap_22'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'gmap_id': 'gmap_20'}, {'name': 'J B Oriental Inc', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]', 'gmap_id': 'gmap_32'}, {'name': 'Orient Massage', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]', 'gmap_id': 'gmap_21'}, {'name': 'Good Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]', 'gmap_id': 'gmap_28'}, {'name': 'The Beauty Bar', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "9AM–8PM"], ["Sunday", "Closed"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'gmap_id': 'gmap_30'}, {'name': 'The Boochyard @ Local Roots', 'hours': '[["Thursday", "3–8PM"], ["Friday", "3–9PM"], ["Saturday", "12–9PM"], ["Sunday", "12–8PM"], ["Monday", "Closed"], ["Tuesday", "3–8PM"], ["Wednesday", "3–8PM"]]', 'gmap_id': 'gmap_53'}, {'name': 'Regus - California, Irvine - Oracle Tower', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]', 'gmap_id': 'gmap_63'}, {'name': 'Excel Hair & Nails', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]', 'gmap_id': 'gmap_65'}, {'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'gmap_id': 'gmap_51'}, {'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'gmap_id': 'gmap_36'}, {'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'gmap_id': 'gmap_12'}, {'name': "Rossy's Beauty Salon", 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "9AM–3PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'gmap_id': 'gmap_7'}, {'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'gmap_id': 'gmap_8'}, {'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]', 'gmap_id': 'gmap_9'}, {'name': 'Paradise tattoo', 'hours': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]', 'gmap_id': 'gmap_11'}, {'name': 'Off The Hoof', 'hours': '[["Thursday", "11AM–10PM"], ["Friday", "11AM–10PM"], ["Saturday", "11AM–10PM"], ["Sunday", "11AM–9PM"], ["Monday", "11AM–9PM"], ["Tuesday", "11AM–9PM"], ["Wednesday", "11AM–9PM"]]', 'gmap_id': 'gmap_61'}, {'name': 'Mobile Moreno Valley Dispensary', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]', 'gmap_id': 'gmap_55'}, {'name': 'Advanced Auto Upholstery', 'hours': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]', 'gmap_id': 'gmap_68'}, {'name': 'LuXe Organic Nails Boutique', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]', 'gmap_id': 'gmap_67'}, {'name': 'Widows Peak Salon', 'hours': '[["Thursday", "11AM–8PM"], ["Friday", "11AM–7PM"], ["Saturday", "10AM–6PM"], ["Sunday", "10AM–2PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'gmap_id': 'gmap_40'}, {'name': 'The Dream Junction', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "9AM–7PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]', 'gmap_id': 'gmap_60'}], 'var_function-call-1366610007587751947': "SELECT gmap_id, rating FROM review WHERE gmap_id IN ('gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_11', 'gmap_61', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_40', 'gmap_60')", 'var_function-call-11078630846747515908': 'file_storage/function-call-11078630846747515908.json'}

exec(code, env_args)
