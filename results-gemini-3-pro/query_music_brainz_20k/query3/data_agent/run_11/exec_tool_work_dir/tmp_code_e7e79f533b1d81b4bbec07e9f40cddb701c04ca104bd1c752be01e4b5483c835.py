code = """import pandas as pd
import json
import re

sales_file = locals()['var_function-call-16976298203827158307']
tracks_file = locals()['var_function-call-10581686767626383820']

with open(sales_file, 'r') as f:
    sales_data = json.load(f)
with open(tracks_file, 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])

df_tracks = pd.DataFrame(tracks_data)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_title(title):
    if not title or title == 'None': return ""
    s = str(title).lower()
    # Remove leading numbers
    s = re.sub(r'^\d+[\.\-\s]+', '', s)
    # Remove parens and brackets and their content
    s = re.sub(r'\s*[\(\[].*?[\)\]]', '', s)
    # Remove non-alphanumeric (except spaces) to handle "it's" vs "its" or punctuation differences
    # Actually, let's keep it simple first. "it's" and "its" might be different. 
    # But usually punctuation removal helps.
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def clean_artist(artist):
    if not artist or str(artist) in ['None', '[unknown]', '']:
        return None
    s = str(artist).lower()
    # Remove "feat." part
    s = re.sub(r'\s(feat|ft)\.?\s.*', '', s)
    # Remove parens
    s = re.sub(r'\s*[\(\[].*?[\)\]]', '', s)
    s = re.sub(r'[^\w\s]', '', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

df['clean_title'] = df['title'].apply(clean_title)
df['clean_artist'] = df['artist'].apply(clean_artist)

def extract_artist_title(row):
    t = row['clean_title']
    a = row['clean_artist']
    
    if not a and ' - ' in str(row['title']).lower(): # Check original title for separator
        # This logic is tricky if I already cleaned the title. 
        # Let's use the cleaned title but I removed punctuation.
        # " - " became " ". Hard to split.
        pass
    
    # Let's rely on the previous logic but apply cleaning after extraction?
    # No, let's look at the cleaned title.
    # If artist is missing, maybe I can't do much unless I re-parse the original title.
    
    if not a:
        # Try to parse original title
        orig = str(row['title'])
        if ' - ' in orig:
            parts = orig.split(' - ', 1)
            # clean both parts
            a_new = clean_artist(parts[0])
            t_new = clean_title(parts[1])
            return a_new, t_new
            
    return a, t

extracted = df.apply(extract_artist_title, axis=1)
df['final_artist'] = [x[0] for x in extracted]
df['final_title'] = [x[1] for x in extracted]

# Filter out empty titles
df_final = df[df['final_title'] != '']
# Filter out unknown artists if you want strictly identified songs?
# Or group unknown artists together? 
# "Groovey" by "Rich Matteson" is a specific song.
# If artist is unknown, we group by title only? Risk of collision.
# Let's keep artist as 'unknown' but grouping by (unknown, title).

df_final['group_artist'] = df_final['final_artist'].fillna('unknown')
df_final['group_title'] = df_final['final_title']

grouped = df_final.groupby(['group_artist', 'group_title'])['total_revenue'].sum().reset_index()
grouped = grouped.sort_values('total_revenue', ascending=False)

print("__RESULT__:")
print(grouped.head(20).to_json(orient='records'))"""

env_args = {'var_function-call-16976298203827158307': 'file_storage/function-call-16976298203827158307.json', 'var_function-call-10581686767626383820': 'file_storage/function-call-10581686767626383820.json', 'var_function-call-13342668590390360399': [{'group_artist': 'unknown', 'group_title': '', 'total_revenue': 54610.42}, {'group_artist': '', 'group_title': '', 'total_revenue': 19324.28}, {'group_artist': 'rich matteson', 'group_title': 'groovey', 'total_revenue': 5668.5}, {'group_artist': 'luke bryan', 'group_title': 'all my friends say (album version)', 'total_revenue': 5180.93}, {'group_artist': 'pras', 'group_title': 'ghetto supastar (that is what you are)', 'total_revenue': 4933.98}, {'group_artist': 'frankie goes to hollywood', 'group_title': 'the power of love (rob searle club mix)', 'total_revenue': 4909.04}, {'group_artist': 'syb van der ploeg', 'group_title': 'zo gaat het leven aan je voor', 'total_revenue': 4881.42}, {'group_artist': 'fausto papetti', 'group_title': 'lovers', 'total_revenue': 4770.54}, {'group_artist': 'the turtles', 'group_title': 'happy together', 'total_revenue': 4747.05}, {'group_artist': 'lemon d', 'group_title': 'jah love (vip remix)', 'total_revenue': 4645.11}, {'group_artist': 'madbones', 'group_title': 'alona', 'total_revenue': 4615.9}, {'group_artist': 'the heath brothers', 'group_title': 'passion flower', 'total_revenue': 4533.34}, {'group_artist': 'echolyn', 'group_title': 'letters: a short essay', 'total_revenue': 4484.08}, {'group_artist': 'crookers feat. miike snow', 'group_title': 'remedy (numan remix)', 'total_revenue': 4482.8}, {'group_artist': 'lasgo', 'group_title': 'something', 'total_revenue': 4461.79}, {'group_artist': 'vrisak generacije', 'group_title': 'ne veruj', 'total_revenue': 4450.29}, {'group_artist': 'ske', 'group_title': 'vagga', 'total_revenue': 4447.87}, {'group_artist': 'quincy jones', 'group_title': 'call me mr tibbs (main title)', 'total_revenue': 4442.71}, {'group_artist': 'lupe fiasco', 'group_title': 'intruder alert', 'total_revenue': 4401.09}, {'group_artist': 'louis armstrong', 'group_title': 'basin street blues', 'total_revenue': 4399.52}]}

exec(code, env_args)
