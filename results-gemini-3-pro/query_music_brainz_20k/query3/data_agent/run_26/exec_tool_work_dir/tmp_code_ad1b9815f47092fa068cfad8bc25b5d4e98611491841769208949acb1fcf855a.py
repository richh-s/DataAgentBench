code = """import pandas as pd
import json
import re

# Load data
sales_path = locals()['var_function-call-11167553081244031459']
tracks_path = locals()['var_function-call-13338430571201753838']

with open(sales_path, 'r') as f:
    sales_data = json.load(f)
df_sales = pd.DataFrame(sales_data)
df_sales['revenue_usd'] = pd.to_numeric(df_sales['total_revenue'])

with open(tracks_path, 'r') as f:
    tracks_data = json.load(f)
df_tracks = pd.DataFrame(tracks_data)

df_merged = pd.merge(df_sales, df_tracks, on='track_id', how='inner')

def clean_field(s):
    if s is None: return ""
    s = str(s).strip()
    if s.lower() in ['none', '[unknown]', 'unk.', '']:
        return ""
    return s

def normalize_title_artist(row):
    raw_title = clean_field(row['title'])
    raw_artist = clean_field(row['artist'])
    
    # 1. Remove leading track numbers (e.g. "003-")
    title = re.sub(r'^\d+-\s*', '', raw_title)
    
    artist = raw_artist
    
    # 2. Extract artist from title if artist is missing
    if artist == "" and " - " in title:
        parts = title.split(" - ", 1)
        artist = parts[0].strip()
        title = parts[1].strip()
        
    # 3. Aggressive normalization for "Song" concept
    # Remove text in parentheses/brackets (e.g. "(Album Version)", "[Remix]")
    # Only if it's at the end or seems like metadata.
    # Be careful not to remove essential title parts (e.g. "(I Can't Get No) Satisfaction")
    # But usually "(...)" contains version info.
    # Let's start by removing (...) and [...]
    
    base_title = re.sub(r'\s*\(.*?\)', '', title)
    base_title = re.sub(r'\s*\[.*?\]', '', base_title)
    base_title = base_title.strip()
    
    # If base_title became empty (e.g. track was just "(Intro)"), revert or keep as is.
    if not base_title:
        base_title = title.strip()

    return artist.lower(), base_title.lower()

df_merged['base_artist'], df_merged['base_title'] = zip(*df_merged.apply(normalize_title_artist, axis=1))

# Filter out empty
df_clean = df_merged[df_merged['base_title'] != ""]

# Group
df_grouped = df_clean.groupby(['base_artist', 'base_title'])['revenue_usd'].sum().reset_index()

# Sort
top_songs = df_grouped.sort_values('revenue_usd', ascending=False).head(20)

print("__RESULT__:")
print(top_songs.to_json(orient='records'))"""

env_args = {'var_function-call-11167553081244031459': 'file_storage/function-call-11167553081244031459.json', 'var_function-call-13338430571201753838': 'file_storage/function-call-13338430571201753838.json', 'var_function-call-8108861843005645843': {'clean_artist': '', 'clean_title': 'none', 'revenue': 14647.52, 'sample_title': 'None', 'sample_artist': 'None'}, 'var_function-call-14991713949932644944': [{'clean_artist': '', 'clean_title': '', 'revenue_usd': 14647.52}, {'clean_artist': '', 'clean_title': '003-', 'revenue_usd': 6841.18}, {'clean_artist': 'rich matteson', 'clean_title': 'groovey', 'revenue_usd': 5417.34}, {'clean_artist': '', 'clean_title': '005-', 'revenue_usd': 5222.0}, {'clean_artist': '', 'clean_title': '009-', 'revenue_usd': 5045.7}, {'clean_artist': '', 'clean_title': '004-', 'revenue_usd': 4868.47}, {'clean_artist': '', 'clean_title': '010-', 'revenue_usd': 4734.36}, {'clean_artist': '', 'clean_title': '002-', 'revenue_usd': 4119.89}, {'clean_artist': 'luke bryan', 'clean_title': 'all my friends say (album version)', 'revenue_usd': 4110.55}, {'clean_artist': 'kerstin gier', 'clean_title': 'kapitel 01', 'revenue_usd': 4091.12}, {'clean_artist': 'damian marley', 'clean_title': 'beautiful (instrumental)', 'revenue_usd': 4004.42}, {'clean_artist': 'matthew barber', 'clean_title': 'the story of your life', 'revenue_usd': 3962.97}, {'clean_artist': '', 'clean_title': '006-', 'revenue_usd': 3946.78}, {'clean_artist': 'sir william gilbert & sir arthur sullivan', 'clean_title': 'a wand\'ring minstrel i, from "the mikado"', 'revenue_usd': 3877.43}, {'clean_artist': 'russ ballard', 'clean_title': 'the fire still burns', 'revenue_usd': 3807.4}, {'clean_artist': 'craig padilla', 'clean_title': 'vostok', 'revenue_usd': 3767.95}, {'clean_artist': 'byzantine', 'clean_title': 'oblivion beckons', 'revenue_usd': 3759.01}, {'clean_artist': '', 'clean_title': '001-', 'revenue_usd': 3742.44}, {'clean_artist': 'kenny rogers', 'clean_title': 'so in love with you', 'revenue_usd': 3642.04}, {'clean_artist': '', 'clean_title': '012-', 'revenue_usd': 3635.13}], 'var_function-call-16756566466648992653': [{'track_id': '313', 'title': '005-Mechanical Advantage', 'artist': 'Deepspace 5', 'revenue_usd': 685.04}, {'track_id': '865', 'title': '005-Il peut pleuvoir', 'artist': 'Jacques Brel', 'revenue_usd': 1566.6}, {'track_id': '1137', 'title': '003-Public Enemy #1', 'artist': 'Motley Crue', 'revenue_usd': 839.28}, {'track_id': '1341', 'title': '003-Concerto for Piano and Orchestra No. 9 in E-flat major, K. 271: III. Rondo. Presto', 'artist': 'Wolfgang Amadeus Mozart', 'revenue_usd': 1075.29}, {'track_id': '1774', 'title': '005-Feedback (Slash remix)', 'artist': 'DJ Flex', 'revenue_usd': 1154.75}, {'track_id': '2070', 'title': '003-Louisiana Sunset', 'artist': 'Passport', 'revenue_usd': 779.95}, {'track_id': '2133', 'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'revenue_usd': 1501.67}, {'track_id': '2780', 'title': '005-Just Stay', 'artist': 'Little Scout', 'revenue_usd': 1934.23}, {'track_id': '2872', 'title': '003-The Succession Crisis in England', 'artist': 'Professor Jennifer Paxton', 'revenue_usd': 1421.23}, {'track_id': '3101', 'title': '003-Smooth Down', 'artist': 'Kas Product', 'revenue_usd': 329.83}, {'track_id': '3663', 'title': '005-How Can You Mend a Broken Heart', 'artist': 'Al Green', 'revenue_usd': 121.2}, {'track_id': '3854', 'title': '005-When the Summer Is Gone', 'artist': 'Jerry Williams', 'revenue_usd': 194.01}, {'track_id': '4146', 'title': '003-Tripping', 'artist': 'Robbie Williams', 'revenue_usd': 693.47}, {'track_id': '5327', 'title': 'Tahdon tanssia kanssasi - Uneni kaunein: Parhaat 2005-2011', 'artist': 'Tomi Metsäketo & Johanna Kurkela', 'revenue_usd': 1302.98}, {'track_id': '5461', 'title': '003-I Wanna Die', 'artist': 'Mauri', 'revenue_usd': 2032.79}, {'track_id': '5491', 'title': "003-Wanderer's Song", 'artist': 'The New Seekers', 'revenue_usd': 1720.91}, {'track_id': '5713', 'title': '003-Broken Promises', 'artist': 'None', 'revenue_usd': 1684.19}, {'track_id': '5903', 'title': '003-Everlasting Sun', 'artist': 'Sundayrunners', 'revenue_usd': 1340.26}, {'track_id': '6270', 'title': '005-Guernsey', 'artist': 'Slovak Radio Symphony Orchestra, Peter Breiner', 'revenue_usd': 472.09}, {'track_id': '6442', 'title': '005-Set the Controls for the Heart of the Sun', 'artist': 'Trance to the Sun', 'revenue_usd': 1597.67}], 'var_function-call-3675759696654998743': [{'clean_artist': 'rich matteson', 'clean_title': 'groovey', 'revenue_usd': 5668.5}, {'clean_artist': 'luke bryan', 'clean_title': 'all my friends say (album version)', 'revenue_usd': 5180.93}, {'clean_artist': 'pras', 'clean_title': 'ghetto supastar (that is what you are)', 'revenue_usd': 4933.98}, {'clean_artist': 'frankie goes to hollywood', 'clean_title': 'the power of love (rob searle club mix)', 'revenue_usd': 4909.04}, {'clean_artist': 'syb van der ploeg', 'clean_title': 'zo gaat het leven aan je voor', 'revenue_usd': 4881.42}, {'clean_artist': 'fausto papetti', 'clean_title': 'lovers', 'revenue_usd': 4770.54}, {'clean_artist': 'the turtles', 'clean_title': 'happy together', 'revenue_usd': 4747.05}, {'clean_artist': 'lemon d', 'clean_title': 'jah love (vip remix)', 'revenue_usd': 4645.11}, {'clean_artist': 'madbones', 'clean_title': 'alona', 'revenue_usd': 4615.9}, {'clean_artist': 'the heath brothers', 'clean_title': 'passion flower', 'revenue_usd': 4533.34}, {'clean_artist': 'echolyn', 'clean_title': 'letters: a short essay', 'revenue_usd': 4484.08}, {'clean_artist': 'crookers feat. miike snow', 'clean_title': 'remedy (numan remix)', 'revenue_usd': 4482.8}, {'clean_artist': 'lasgo', 'clean_title': 'something', 'revenue_usd': 4461.79}, {'clean_artist': 'vrisak generacije', 'clean_title': 'ne veruj', 'revenue_usd': 4450.29}, {'clean_artist': 'ske', 'clean_title': 'vagga', 'revenue_usd': 4447.87}, {'clean_artist': 'quincy jones', 'clean_title': 'call me mr tibbs (main title)', 'revenue_usd': 4442.71}, {'clean_artist': 'lupe fiasco', 'clean_title': 'intruder alert', 'revenue_usd': 4401.09}, {'clean_artist': 'louis armstrong', 'clean_title': 'basin street blues', 'revenue_usd': 4399.52}, {'clean_artist': 'hotstylz', 'clean_title': 'lookin boy (feat. yung joc)', 'revenue_usd': 4361.8}, {'clean_artist': 'ponga', 'clean_title': 'hidden propolsion unit (element 115 mix)', 'revenue_usd': 4282.75}]}

exec(code, env_args)
