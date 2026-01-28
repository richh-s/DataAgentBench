code = """import pandas as pd

# Load data
businesses = var_functions.query_db_5
reviews = var_functions.query_db_6

# Check data
print('Businesses:', len(businesses))
print('Reviews:', len(reviews))

# Create DataFrames
df_biz = pd.DataFrame(businesses)
df_rev = pd.DataFrame(reviews)

# Convert ratings to numeric
df_rev['rating'] = pd.to_numeric(df_rev['rating'])

# Calculate average ratings per business
avg_ratings = df_rev.groupby('gmap_id')['rating'].mean()

# Filter for ratings >= 4.0
high_rated = avg_ratings[avg_ratings >= 4.0].reset_index()

# Merge with business names
result = pd.merge(high_rated, df_biz[['gmap_id', 'name']], on='gmap_id', how='left')

# Sort and round
result = result.sort_values(['rating', 'name'], ascending=[False, True])
result['rating'] = result['rating'].round(2)

# Generate output
output = []
for _, row in result.iterrows():
    business_name = str(row['name'])
    rating_val = str(row['rating'])
    output.append(business_name + ': ' + rating_val)

result_text = '\n'.join(output)
print('__RESULT__:')
print(result_text)"""

env_args = {'var_functions.list_db:0': ['business_description'], 'var_functions.list_db:2': ['review'], 'var_functions.query_db:5': [{'name': 'Angel-A Massage', 'gmap_id': 'gmap_22', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25', 'description': ' Located in Fair Oaks, CA 95628, this wellness studio offers expert bodywork services designed to promote relaxation and alleviate tension.'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33', 'description': ' Experience rejuvenating bodywork and relaxation techniques at this wellness studio in Roseville, CA 95678.'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21', 'description': ' This wellness studio in Sacramento, CA 95841 offers rejuvenating bodywork services designed to relieve tension and promote relaxation.'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28', 'description': ' Indulge in rejuvenating treatments and holistic wellness services designed to refresh your mind and body in Penryn, CA 95663.'}, {'name': 'Regus - California, Irvine - Oracle Tower', 'gmap_id': 'gmap_63', 'description': ' This company in Irvine, CA 92614 specializes in providing flexible workspace solutions tailored to meet the needs of professionals and businesses.'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51', 'description': 'Longtime boutique featuring high-quality Persian & Oriental rugs, plus repair & cleaning services. Discover a curated selection of exquisite floor coverings and textiles that enhance any space, conveniently located in La Jolla, CA 92037.'}, {'name': 'IBEW 441', 'gmap_id': 'gmap_59', 'description': ' Located in Orange, CA 92868, this professional hub offers a variety of workspace solutions and essential services for entrepreneurs and companies seeking a productive environment.'}, {'name': 'Lafayette Entrance 1', 'gmap_id': 'gmap_4', 'description': ' This serene green space in Orinda, CA 94563 offers picturesque walking trails, lush picnic areas, and a tranquil environment for outdoor recreation and relaxation.'}, {'name': 'HIGHPOINTE', 'gmap_id': 'gmap_66', 'description': ' This professional workspace in Mission Viejo, CA 92691 offers flexible office solutions and meeting facilities designed to support your business needs.'}], 'var_functions.query_db:6': [{'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '4'}, {'gmap_id': 'gmap_22', 'rating': '5'}, {'gmap_id': 'gmap_22', 'rating': '3'}, {'gmap_id': 'gmap_25', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '2'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '1'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_33', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '4'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '5'}, {'gmap_id': 'gmap_24', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '2'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '4'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '1'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '3'}, {'gmap_id': 'gmap_20', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '1'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_21', 'rating': '4'}, {'gmap_id': 'gmap_21', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '4'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}, {'gmap_id': 'gmap_28', 'rating': '1'}, {'gmap_id': 'gmap_28', 'rating': '5'}]}

exec(code, env_args)
