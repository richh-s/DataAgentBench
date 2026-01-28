code = """import json
import pandas as pd

# Access the review data
var_name = 'var_functions.query_db:22'
review_var = locals().get(var_name)
reviews = []

if review_var is not None:
    if isinstance(review_var, str) and review_var.endswith('.json'):
        with open(review_var, 'r') as f:
            reviews = json.load(f)
    else:
        reviews = review_var

print(f"Loaded {len(reviews)} reviews")

# Convert to DataFrame
df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = pd.to_numeric(df_reviews['rating'])

# Calculate average rating per business
avg_ratings = df_reviews.groupby('gmap_id')['rating'].agg(['mean', 'count']).reset_index()
avg_ratings.columns = ['gmap_id', 'avg_rating', 'review_count']

print(f"Average ratings calculated for {len(avg_ratings)} businesses")

# Load businesses data
var_name_business = 'var_functions.execute_python:20'
business_var = locals().get(var_name_business)
businesses_data = []

if business_var is not None:
    if isinstance(business_var, str) and business_var.endswith('.json'):
        with open(business_var, 'r') as f:
            business_info = json.load(f)
    else:
        business_info = business_var
    
    # Extract businesses list from the result
    businesses_data = business_info.get('businesses', [])
    
print(f"Loaded {len(businesses_data)} businesses")

# Convert businesses to DataFrame
df_businesses = pd.DataFrame(businesses_data)

# Merge ratings with business info
df_final = pd.merge(df_businesses, avg_ratings, on='gmap_id', how='left')

# Sort by average rating (descending) and get top 5
df_top5 = df_final.sort_values('avg_rating', ascending=False).head(5)

# Handle any None values
if df_top5['avg_rating'].isnull().any():
    df_top5 = df_top5.fillna(0)

print(f"Top 5 businesses identified:")
for idx, row in df_top5.iterrows():
    print(f"  {row['name']}: {row['avg_rating']:.2f} ({row['review_count']} reviews)")

# Prepare final result
result = []
for idx, row in df_top5.iterrows():
    result.append({
        'name': row['name'],
        'hours': row['hours'],
        'avg_rating': round(row['avg_rating'], 2),
        'review_count': int(row['review_count'])
    })

final_output = {
    'top_5_businesses': result
}

print('__RESULT__:')
print(json.dumps(final_output))"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.query_db:2': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'hours': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'hours': '[["Thursday", "9AM–5PM"], ["Friday", "9AM–5PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "9AM–5PM"], ["Tuesday", "9AM–5PM"], ["Wednesday", "9AM–5PM"]]'}, {'gmap_id': 'gmap_45', 'name': 'Matrix International Textiles', 'hours': '[["Thursday", "8:30AM–5:30PM"], ["Friday", "8:30AM–5:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "8:30AM–5:30PM"], ["Tuesday", "8:30AM–5:30PM"], ["Wednesday", "8:30AM–5:30PM"]]'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:20': {'businesses': [{'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'hours': '[["Thursday", "6:30AM–6PM"], ["Friday", "6:30AM–6PM"], ["Saturday", "6:30AM–6PM"], ["Sunday", "7AM–12PM"], ["Monday", "Closed"], ["Tuesday", "6:30AM–6PM"], ["Wednesday", "6:30AM–6PM"]]'}, {'gmap_id': 'gmap_74', 'name': 'Vons Chicken', 'hours': '[["Thursday", "11AM–9:30PM"], ["Friday", "11AM–9:30PM"], ["Saturday", "11AM–9:30PM"], ["Sunday", "11AM–9:30PM"], ["Monday", "Closed"], ["Tuesday", "11AM–9:30PM"], ["Wednesday", "11AM–9:30PM"]]'}, {'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–9:30PM"], ["Tuesday", "10AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_33', 'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'hours': '[["Thursday", "9AM–10PM"], ["Friday", "9AM–10PM"], ["Saturday", "9AM–10PM"], ["Sunday", "9AM–10PM"], ["Monday", "9AM–10PM"], ["Tuesday", "9AM–10PM"], ["Wednesday", "9AM–10PM"]]'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc', 'hours': '[["Thursday", "9:30AM–10PM"], ["Friday", "9:30AM–10PM"], ["Saturday", "9:30AM–10PM"], ["Sunday", "9:30AM–10PM"], ["Monday", "9:30AM–10PM"], ["Tuesday", "9:30AM–10PM"], ["Wednesday", "9:30AM–10PM"]]'}, {'gmap_id': 'gmap_21', 'name': 'Orient Massage', 'hours': '[["Thursday", "10AM–8PM"], ["Friday", "10AM–8PM"], ["Saturday", "10AM–8PM"], ["Sunday", "10AM–8PM"], ["Monday", "10AM–8PM"], ["Tuesday", "10AM–8PM"], ["Wednesday", "10AM–8PM"]]'}, {'gmap_id': 'gmap_16', 'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'gmap_id': 'gmap_28', 'name': 'Good Massage', 'hours': '[["Thursday", "9:30AM–9:30PM"], ["Friday", "9:30AM–9:30PM"], ["Saturday", "9:30AM–9:30PM"], ["Sunday", "9:30AM–9:30PM"], ["Monday", "9:30AM–9:30PM"], ["Tuesday", "9:30AM–9:30PM"], ["Wednesday", "9:30AM–9:30PM"]]'}, {'gmap_id': 'gmap_30', 'name': 'The Beauty Bar', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "9AM–8PM"], ["Sunday", "Closed"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'hours': '[["Thursday", "3–8PM"], ["Friday", "3–9PM"], ["Saturday", "12–9PM"], ["Sunday", "12–8PM"], ["Monday", "Closed"], ["Tuesday", "3–8PM"], ["Wednesday", "3–8PM"]]'}, {'gmap_id': 'gmap_63', 'name': 'Regus - California, Irvine - Oracle Tower', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_65', 'name': 'Excel Hair & Nails', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "10AM–5PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}, {'gmap_id': 'gmap_51', 'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_36', 'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]'}, {'gmap_id': 'gmap_12', 'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]'}, {'gmap_id': 'gmap_7', 'name': "Rossy's Beauty Salon", 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "9AM–3PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_8', 'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]'}, {'gmap_id': 'gmap_9', 'name': 'Mariscos el poblano', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "8AM–3:30PM"], ["Saturday", "8AM–3:30PM"], ["Sunday", "8AM–3:30PM"], ["Monday", "9AM–3:30AM"], ["Tuesday", "8AM–3:30PM"], ["Wednesday", "8AM–3:30PM"]]'}, {'gmap_id': 'gmap_5', 'name': 'Dr. Syverain Skincare Clinic', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "Closed"], ["Sunday", "8AM–1PM"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]'}, {'gmap_id': 'gmap_34', 'name': "Ruby's Boutique", 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–5PM"], ["Sunday", "11AM–4PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'gmap_id': 'gmap_11', 'name': 'Paradise tattoo', 'hours': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]'}, {'gmap_id': 'gmap_61', 'name': 'Off The Hoof', 'hours': '[["Thursday", "11AM–10PM"], ["Friday", "11AM–10PM"], ["Saturday", "11AM–10PM"], ["Sunday", "11AM–9PM"], ["Monday", "11AM–9PM"], ["Tuesday", "11AM–9PM"], ["Wednesday", "11AM–9PM"]]'}, {'gmap_id': 'gmap_47', 'name': 'Laptop Masters', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'gmap_id': 'gmap_55', 'name': 'Mobile Moreno Valley Dispensary', 'hours': '[["Thursday", "Open 24 hours"], ["Friday", "Open 24 hours"], ["Saturday", "Open 24 hours"], ["Sunday", "Open 24 hours"], ["Monday", "Open 24 hours"], ["Tuesday", "Open 24 hours"], ["Wednesday", "Open 24 hours"]]'}, {'gmap_id': 'gmap_68', 'name': 'Advanced Auto Upholstery', 'hours': '[["Thursday", "8AM–7PM"], ["Friday", "8AM–7PM"], ["Saturday", "8AM–5PM"], ["Sunday", "Closed"], ["Monday", "8AM–7PM"], ["Tuesday", "8AM–7PM"], ["Wednesday", "8AM–7PM"]]'}, {'gmap_id': 'gmap_67', 'name': 'LuXe Organic Nails Boutique', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "9AM–6PM"], ["Sunday", "10AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "Closed"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_64', 'name': 'St John Knits International Inc', 'hours': '[["Thursday", "10AM–6PM"], ["Friday", "10AM–6PM"], ["Saturday", "10AM–6PM"], ["Sunday", "12:30–6PM"], ["Monday", "10AM–6PM"], ["Tuesday", "10AM–6PM"], ["Wednesday", "10AM–6PM"]]'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'hours': '[["Thursday", "11AM–8PM"], ["Friday", "11AM–7PM"], ["Saturday", "10AM–6PM"], ["Sunday", "10AM–2PM"], ["Monday", "Closed"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]'}, {'gmap_id': 'gmap_60', 'name': 'The Dream Junction', 'hours': '[["Thursday", "9AM–7PM"], ["Friday", "9AM–7PM"], ["Saturday", "9AM–7PM"], ["Sunday", "9AM–7PM"], ["Monday", "9AM–7PM"], ["Tuesday", "9AM–7PM"], ["Wednesday", "9AM–7PM"]]'}], 'gmap_ids': ['gmap_41', 'gmap_74', 'gmap_22', 'gmap_33', 'gmap_24', 'gmap_20', 'gmap_32', 'gmap_21', 'gmap_16', 'gmap_28', 'gmap_30', 'gmap_53', 'gmap_63', 'gmap_65', 'gmap_51', 'gmap_36', 'gmap_12', 'gmap_7', 'gmap_8', 'gmap_9', 'gmap_5', 'gmap_34', 'gmap_11', 'gmap_61', 'gmap_47', 'gmap_55', 'gmap_68', 'gmap_67', 'gmap_64', 'gmap_40', 'gmap_60'], 'count': 31}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json'}

exec(code, env_args)
