code = """import json
import pandas as pd
import re

# Load the large JSON result from the previous query
path = var_call_v2wzdb090GqcLoAmbPUs1Gnk
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Create DataFrame
df = pd.DataFrame(data)

# Ensure description and title are strings
df['description'] = df['description'].fillna('').astype(str)
df['title'] = df['title'].fillna('').astype(str)

# Compute description length
df['desc_len'] = df['description'].str.len()

# Define keyword sets for simple classification
sports_kw = [
    'soccer','football','baseball','basketball','hockey','match','tournament','championship',
    'coach','player','players','scored','score','goal','season','innings','batter','wicket',
    'race','nascar','grand prix','olympic','olympics','par','tee','golf','f1','nfl','nba','mlb',
    'touchdown','penalty','final','cup','league','team','teams','manager','midfielder','striker',
    'defender','goalkeeper','pitcher','inning','rally','set','serve','points','tries'
]
business_kw = [
    'stock','stocks','market','shares','investor','investors','investment','ipo','profit','profits',
    'earnings','dollar','trade','economy','oil','barrel','merger','acquisition','company','companies',
    'bank','interest rate','interest rates','rate cut','central bank','fed','revenue'
]
tech_kw = [
    'scientist','scientists','research','researchers','technology','tech','computer','e-mail','email',
    'nuclear','drug','drugs','ph.d','phd','internet','ibm','google','software','hardware','email','science'
]

# Helper to check keywords
def contains_kw(text, kws):
    txt = text.lower()
    for kw in kws:
        if kw in txt:
            return True
    return False

# Classify
cats = []
for _, row in df.iterrows():
    text = (row['title'] + ' ' + row['description']).lower()
    cat = 'World'  # default
    if contains_kw(text, sports_kw):
        cat = 'Sports'
    elif contains_kw(text, business_kw):
        cat = 'Business'
    elif contains_kw(text, tech_kw):
        cat = 'Science/Technology'
    else:
        cat = 'World'
    cats.append(cat)

df['category'] = cats

# Filter sports
sports_df = df[df['category'] == 'Sports']

if sports_df.empty:
    result = json.dumps("")
else:
    # find article(s) with max description length
    max_len = int(sports_df['desc_len'].max())
    top = sports_df[sports_df['desc_len'] == max_len].iloc[0]
    title = str(top['title']).strip()
    result = json.dumps(title)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_v2wzdb090GqcLoAmbPUs1Gnk': 'file_storage/call_v2wzdb090GqcLoAmbPUs1Gnk.json'}

exec(code, env_args)
