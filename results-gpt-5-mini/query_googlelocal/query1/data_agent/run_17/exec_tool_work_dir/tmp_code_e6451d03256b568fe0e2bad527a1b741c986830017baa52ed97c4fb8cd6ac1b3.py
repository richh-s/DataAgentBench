code = """import pandas as pd
import json
# Load results from previous queries
df_bus = pd.DataFrame(var_call_GvneVGGtHLXXqc4C4HWFzRfg)
df_rev = pd.DataFrame(var_call_yjR6W3A4pERLnucYwb781AXP)
# Convert numeric fields
df_rev['avg_rating'] = df_rev['avg_rating'].astype(float)
df_rev['review_count'] = df_rev['review_count'].astype(int)
df_bus['num_of_reviews'] = pd.to_numeric(df_bus['num_of_reviews'], errors='coerce').fillna(0).astype(int)
# Merge on gmap_id
merged = pd.merge(df_bus, df_rev, on='gmap_id', how='inner')
# Sort by avg_rating desc and take top 5
top5 = merged.sort_values(by='avg_rating', ascending=False).head(5)
# Build result list
result_list = []
for _, row in top5.iterrows():
    result_list.append({
        'gmap_id': row['gmap_id'],
        'name': row['name'],
        'description': row.get('description', None),
        'avg_rating': float(row['avg_rating']),
        'review_count': int(row['review_count']),
        'num_of_reviews': int(row['num_of_reviews'])
    })
# Print result following required format
print("__RESULT__:")
print(json.dumps(result_list))"""

env_args = {'var_call_LZzrhCSn6byGUt4b0kEZsRe3': ['review'], 'var_call_K6tvdDXH2oxoQaxdJ6TMO5QB': ['business_description'], 'var_call_GvneVGGtHLXXqc4C4HWFzRfg': [{'gmap_id': 'gmap_44', 'name': 'City Textile', 'description': ' Located in Los Angeles, CA 90023, this company specializes in the international trade of high-quality fabrics and materials.', 'num_of_reviews': '6', 'MISC': 'None'}, {'gmap_id': 'gmap_41', 'name': 'San Soo Dang', 'description': ' This vibrant eatery in Los Angeles, CA 90005 offers a delightful array of traditional dishes and barbecue specialties inspired by the rich flavors of Korean cuisine.', 'num_of_reviews': '18', 'MISC': '{"Service options": ["Takeout", "Dine-in", "Delivery"], "Accessibility": ["Wheelchair accessible entrance"], "Offerings": ["Comfort food"], "Amenities": ["Good for kids"], "Atmosphere": ["Casual"]}'}, {'gmap_id': 'gmap_43', 'name': 'Nova Fabrics', 'description': ' Discover a vibrant selection of textiles and materials for all your crafting and sewing needs in Los Angeles, CA 90021.', 'num_of_reviews': '6', 'MISC': '{"Service options": ["In-store shopping"], "Payments": ["Checks", "Debit cards", "Credit cards"]}'}, {'gmap_id': 'gmap_38', 'name': 'Nobel Textile Co', 'description': ' This vibrant shop in Los Angeles, CA 90021 offers a diverse selection of textiles and sewing supplies for all your creative projects.', 'num_of_reviews': '7', 'MISC': '{"Service options": ["In-store pickup"]}'}, {'gmap_id': 'gmap_39', 'name': 'Beads and More', 'description': ' This vibrant boutique in Los Angeles, CA 90014 specializes in a diverse selection of decorative crafting elements, ideal for jewelry-making enthusiasts and DIY crafters alike.', 'num_of_reviews': '18', 'MISC': '{"Service options": ["In-store shopping"], "Accessibility": ["Wheelchair accessible entrance"], "Planning": ["Quick visit"]}'}, {'gmap_id': 'gmap_42', 'name': 'Ace Jewelry & Loan', 'description': ' Located in Los Angeles, CA 90014, this elegant boutique offers a stunning collection of handcrafted adornments and exquisite timepieces for every occasion.', 'num_of_reviews': '7', 'MISC': '{"Service options": ["In-store shopping"], "Accessibility": ["Wheelchair accessible entrance"], "Planning": ["Quick visit"]}'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.', 'num_of_reviews': '35', 'MISC': '{"Accessibility": ["Wheelchair accessible entrance"], "Amenities": ["Wi-Fi"], "Planning": ["Appointments recommended"], "Payments": ["Debit cards", "NFC mobile payments", "Credit cards"]}'}], 'var_call_yjR6W3A4pERLnucYwb781AXP': [{'gmap_id': 'gmap_38', 'avg_rating': '4.285714285714286', 'review_count': '7'}, {'gmap_id': 'gmap_39', 'avg_rating': '3.2222222222222223', 'review_count': '18'}, {'gmap_id': 'gmap_40', 'avg_rating': '4.857142857142857', 'review_count': '35'}, {'gmap_id': 'gmap_41', 'avg_rating': '4.277777777777778', 'review_count': '18'}, {'gmap_id': 'gmap_42', 'avg_rating': '3.2857142857142856', 'review_count': '7'}, {'gmap_id': 'gmap_43', 'avg_rating': '3.3333333333333335', 'review_count': '6'}, {'gmap_id': 'gmap_44', 'avg_rating': '4.5', 'review_count': '6'}]}

exec(code, env_args)
