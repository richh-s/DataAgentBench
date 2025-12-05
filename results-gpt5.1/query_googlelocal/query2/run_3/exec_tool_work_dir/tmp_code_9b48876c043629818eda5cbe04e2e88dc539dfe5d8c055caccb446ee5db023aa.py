code = """import json, pandas as pd

# load full reviews data from file
with open(var_call_F57c3lPVIxajpGr1E1CVLopR, 'r') as f:
    reviews = json.load(f)

df_reviews = pd.DataFrame(reviews)
df_reviews['rating'] = df_reviews['rating'].astype(float)

# business names and ids
biz = pd.DataFrame(var_call_Q4BlU7WtftYdqXsrQMtwNG3i)

# compute average rating per gmap_id
avg_r = df_reviews.groupby('gmap_id', as_index=False)['rating'].mean()

# join with business to get names
merged = avg_r.merge(biz, on='gmap_id', how='left')

# keep only massage businesses (name contains 'massage', case-insensitive)
mask = merged['name'].str.contains('massage', case=False, na=False)
res = merged[mask]

# filter avg rating >= 4.0
res = res[res['rating'] >= 4.0]

# sort by rating desc
res = res.sort_values('rating', ascending=False)

# prepare output: list of {name, average_rating}
output = [
    {
        'business_name': row['name'],
        'average_rating': round(float(row['rating']), 2)
    }
    for _, row in res.iterrows()
]

result = json.dumps(output)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_EapMZyyCejRClbhCJoLmVTsF': [], 'var_call_F57c3lPVIxajpGr1E1CVLopR': 'file_storage/call_F57c3lPVIxajpGr1E1CVLopR.json', 'var_call_2l3icQm6q5IoFNBffu6xSjVn': [{'gmap_id': 'gmap_44'}, {'gmap_id': 'gmap_41'}, {'gmap_id': 'gmap_43'}, {'gmap_id': 'gmap_38'}, {'gmap_id': 'gmap_45'}, {'gmap_id': 'gmap_74'}, {'gmap_id': 'gmap_17'}, {'gmap_id': 'gmap_22'}, {'gmap_id': 'gmap_29'}, {'gmap_id': 'gmap_25'}, {'gmap_id': 'gmap_19'}, {'gmap_id': 'gmap_33'}, {'gmap_id': 'gmap_24'}, {'gmap_id': 'gmap_20'}, {'gmap_id': 'gmap_32'}, {'gmap_id': 'gmap_21'}, {'gmap_id': 'gmap_48'}, {'gmap_id': 'gmap_50'}, {'gmap_id': 'gmap_18'}, {'gmap_id': 'gmap_16'}, {'gmap_id': 'gmap_26'}, {'gmap_id': 'gmap_28'}, {'gmap_id': 'gmap_23'}, {'gmap_id': 'gmap_31'}, {'gmap_id': 'gmap_27'}, {'gmap_id': 'gmap_2'}, {'gmap_id': 'gmap_30'}, {'gmap_id': 'gmap_53'}, {'gmap_id': 'gmap_72'}, {'gmap_id': 'gmap_63'}, {'gmap_id': 'gmap_52'}, {'gmap_id': 'gmap_65'}, {'gmap_id': 'gmap_37'}, {'gmap_id': 'gmap_51'}, {'gmap_id': 'gmap_39'}, {'gmap_id': 'gmap_36'}, {'gmap_id': 'gmap_59'}, {'gmap_id': 'gmap_57'}, {'gmap_id': 'gmap_13'}, {'gmap_id': 'gmap_15'}, {'gmap_id': 'gmap_12'}, {'gmap_id': 'gmap_14'}, {'gmap_id': 'gmap_3'}, {'gmap_id': 'gmap_35'}, {'gmap_id': 'gmap_4'}, {'gmap_id': 'gmap_6'}, {'gmap_id': 'gmap_7'}, {'gmap_id': 'gmap_8'}, {'gmap_id': 'gmap_10'}, {'gmap_id': 'gmap_9'}, {'gmap_id': 'gmap_77'}, {'gmap_id': 'gmap_42'}, {'gmap_id': 'gmap_78'}, {'gmap_id': 'gmap_70'}, {'gmap_id': 'gmap_5'}, {'gmap_id': 'gmap_34'}, {'gmap_id': 'gmap_11'}, {'gmap_id': 'gmap_0'}, {'gmap_id': 'gmap_1'}, {'gmap_id': 'gmap_62'}, {'gmap_id': 'gmap_61'}, {'gmap_id': 'gmap_58'}, {'gmap_id': 'gmap_56'}, {'gmap_id': 'gmap_66'}, {'gmap_id': 'gmap_46'}, {'gmap_id': 'gmap_47'}, {'gmap_id': 'gmap_75'}, {'gmap_id': 'gmap_76'}, {'gmap_id': 'gmap_73'}, {'gmap_id': 'gmap_55'}, {'gmap_id': 'gmap_54'}, {'gmap_id': 'gmap_68'}, {'gmap_id': 'gmap_71'}, {'gmap_id': 'gmap_67'}, {'gmap_id': 'gmap_69'}, {'gmap_id': 'gmap_64'}, {'gmap_id': 'gmap_49'}, {'gmap_id': 'gmap_40'}, {'gmap_id': 'gmap_60'}], 'var_call_Q4BlU7WtftYdqXsrQMtwNG3i': [{'name': 'City Textile', 'gmap_id': 'gmap_44'}, {'name': 'San Soo Dang', 'gmap_id': 'gmap_41'}, {'name': 'Nova Fabrics', 'gmap_id': 'gmap_43'}, {'name': 'Nobel Textile Co', 'gmap_id': 'gmap_38'}, {'name': 'Matrix International Textiles', 'gmap_id': 'gmap_45'}, {'name': 'Vons Chicken', 'gmap_id': 'gmap_74'}, {'name': 'Black Tie Ski Rental Delivery of Mammoth', 'gmap_id': 'gmap_17'}, {'name': 'Angel-A Massage', 'gmap_id': 'gmap_22'}, {'name': 'Dunn-Edwards Paints', 'gmap_id': 'gmap_29'}, {'name': 'Elite Massage', 'gmap_id': 'gmap_25'}, {'name': 'PODS Sacramento Hub', 'gmap_id': 'gmap_19'}, {'name': 'Happy Spa & Massage (Formerly Hawaii Massage & Spa)', 'gmap_id': 'gmap_33'}, {'name': 'SUSY massage', 'gmap_id': 'gmap_24'}, {'name': 'Aurora Massage', 'gmap_id': 'gmap_20'}, {'name': 'J B Oriental Inc', 'gmap_id': 'gmap_32'}, {'name': 'Orient Massage', 'gmap_id': 'gmap_21'}, {'name': 'State Street/7th Street', 'gmap_id': 'gmap_48'}, {'name': 'HDR', 'gmap_id': 'gmap_50'}, {'name': 'Porvene Doors', 'gmap_id': 'gmap_18'}, {'name': 'Hanford Auto Supply', 'gmap_id': 'gmap_16'}, {'name': "Jeff's Auto Repair", 'gmap_id': 'gmap_26'}, {'name': 'Good Massage', 'gmap_id': 'gmap_28'}, {'name': 'Tax Deferred Solutions (TDS Group, INC)', 'gmap_id': 'gmap_23'}, {'name': 'Origin Church', 'gmap_id': 'gmap_31'}, {'name': 'Colfax Elementary School', 'gmap_id': 'gmap_27'}, {'name': 'Life Pointe Church', 'gmap_id': 'gmap_2'}, {'name': 'The Beauty Bar', 'gmap_id': 'gmap_30'}, {'name': 'The Boochyard @ Local Roots', 'gmap_id': 'gmap_53'}, {'name': "Zuby's Brake Tires & Wheels", 'gmap_id': 'gmap_72'}, {'name': 'Regus - California, Irvine - Oracle Tower', 'gmap_id': 'gmap_63'}, {'name': 'Fitness Machine Technicians', 'gmap_id': 'gmap_52'}, {'name': 'J & T Plumbing Pros', 'gmap_id': 'gmap_56'}, {'name': 'Excel Hair & Nails', 'gmap_id': 'gmap_65'}, {'name': 'Birdi Systems, Inc.', 'gmap_id': 'gmap_37'}, {'name': 'Taba Rug Gallery', 'gmap_id': 'gmap_51'}, {'name': 'Beads and More', 'gmap_id': 'gmap_39'}, {'name': 'Beauty Divine Artistry', 'gmap_id': 'gmap_36'}, {'name': 'IBEW 441', 'gmap_id': 'gmap_59'}, {'name': "Ely's Beauty Salon", 'gmap_id': 'gmap_57'}, {'name': 'United Methodist Church', 'gmap_id': 'gmap_13'}, {'name': 'Dirk Vermeulen - State Farm Insurance Agent', 'gmap_id': 'gmap_15'}, {'name': 'White Barn Candle Co', 'gmap_id': 'gmap_12'}, {'name': "Teter's Oakdale Jewelry", 'gmap_id': 'gmap_14'}, {'name': 'Timmons Auto & Truck Repair', 'gmap_id': 'gmap_3'}, {'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'gmap_id': 'gmap_35'}, {'name': 'Lafayette Entrance 1', 'gmap_id': 'gmap_4'}, {'name': 'ATSI', 'gmap_id': 'gmap_6'}, {'name': "Rossy's Beauty Salon", 'gmap_id': 'gmap_7'}, {'name': 'TACOS LA CABANA', 'gmap_id': 'gmap_8'}, {'name': 'Jjironwork', 'gmap_id': 'gmap_10'}, {'name': 'Mariscos el poblano', 'gmap_id': 'gmap_9'}, {'name': 'Climate Control', 'gmap_id': 'gmap_77'}, {'name': 'Ace Jewelry & Loan', 'gmap_id': 'gmap_42'}, {'name': 'Avani Staffing Solutions', 'gmap_id': 'gmap_78'}, {'name': 'CrossFit to the Core', 'gmap_id': 'gmap_70'}, {'name': 'Dr. Syverain Skincare Clinic', 'gmap_id': 'gmap_5'}, {'name': "Ruby's Boutique", 'gmap_id': 'gmap_34'}, {'name': 'Paradise tattoo', 'gmap_id': 'gmap_11'}, {'name': 'Full Circle Trading Post', 'gmap_id': 'gmap_0'}, {'name': 'Northern Builders Supply', 'gmap_id': 'gmap_1'}, {'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin', 'gmap_id': 'gmap_62'}, {'name': 'Off The Hoof', 'gmap_id': 'gmap_61'}, {'name': 'Weatherline Reroofing & Repairs', 'gmap_id': 'gmap_58'}, {'name': 'HIGHPOINTE', 'gmap_id': 'gmap_66'}, {'name': 'B2Sign, Inc.', 'gmap_id': 'gmap_46'}, {'name': 'Laptop Masters', 'gmap_id': 'gmap_47'}, {'name': 'HAVEN™ Dispensary', 'gmap_id': 'gmap_75'}, {'name': 'IronStep', 'gmap_id': 'gmap_76'}, {'name': 'CYD Works Electric', 'gmap_id': 'gmap_73'}, {'name': 'Mobile Moreno Valley Dispensary', 'gmap_id': 'gmap_55'}, {'name': 'Wildomar Campground', 'gmap_id': 'gmap_54'}, {'name': 'Advanced Auto Upholstery', 'gmap_id': 'gmap_68'}, {'name': 'AMMCOR Management Company, Inc.', 'gmap_id': 'gmap_71'}, {'name': 'LuXe Organic Nails Boutique', 'gmap_id': 'gmap_67'}, {'name': 'Taitz Orly DDS', 'gmap_id': 'gmap_69'}, {'name': 'St John Knits International Inc', 'gmap_id': 'gmap_64'}, {'name': 'NEX Barbershop', 'gmap_id': 'gmap_49'}, {'name': 'Widows Peak Salon', 'gmap_id': 'gmap_40'}, {'name': 'The Dream Junction', 'gmap_id': 'gmap_60'}], 'var_call_AH7ZuAgVoBupB7hbXXQ1Zc4L': ['review'], 'var_call_tLq58p1UUmDuX2z2gthl0rYj': ['business_description']}

exec(code, env_args)
