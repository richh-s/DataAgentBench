code = """import json
import pandas as pd
import re

# Load data
with open(locals()['var_function-call-3331083869601689377'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-11133696600522148060'], 'r') as f:
    tracks_data = json.load(f)

df_sales = pd.DataFrame(sales_data)
df_tracks = pd.DataFrame(tracks_data)

# Convert types
df_sales['track_id'] = df_sales['track_id'].astype(str)
df_sales['total_revenue'] = pd.to_numeric(df_sales['total_revenue'])
df_tracks['track_id'] = df_tracks['track_id'].astype(str)

# Merge
df = pd.merge(df_sales, df_tracks, on='track_id', how='left')

def clean_str(s):
    if s is None:
        return ""
    return str(s).strip()

df['title'] = df['title'].apply(clean_str)
df['artist'] = df['artist'].apply(clean_str)
df['album'] = df['album'].apply(clean_str)

def resolve_entity(row):
    title = row['title']
    artist = row['artist']
    invalid_artists = ['', 'none', 'unknown', '[unknown]']
    is_artist_valid = artist.lower() not in invalid_artists
    
    if not is_artist_valid:
        if ' - ' in title:
            parts = title.split(' - ', 1)
            artist = parts[0].strip()
            title = parts[1].strip()
            
    title = re.sub(r'^\d+[\.\-\s]+', '', title)
    title = re.sub(r'\s*\(album version\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\(radio edit\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\(.*remix.*\)', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s*\(30 second version\)', '', title, flags=re.IGNORECASE)
    
    if ' - ' in title:
        parts = title.split(' - ', 1)
        if row['album'] and parts[1].lower() in row['album'].lower():
            title = parts[0]
            
    norm_title = re.sub(r'[^\w\s]', '', title).lower().strip()
    norm_artist = re.sub(r'[^\w\s]', '', artist).lower().strip()
    return pd.Series([norm_title, norm_artist])

df[['norm_title', 'norm_artist']] = df.apply(resolve_entity, axis=1)

# Check Emerge
emerge_variants = df[(df['norm_title'] == 'emerge') & (df['norm_artist'] == 'fischerspooner')]
jah_variants = df[(df['norm_title'] == 'jah love') & (df['norm_artist'] == 'lemon d')]

print("__RESULT__:")
print(json.dumps({
    "emerge": emerge_variants[['title', 'artist', 'total_revenue']].to_dict(orient='records'),
    "jah_love": jah_variants[['title', 'artist', 'total_revenue']].to_dict(orient='records')
}))"""

env_args = {'var_function-call-3331083869601689377': 'file_storage/function-call-3331083869601689377.json', 'var_function-call-11133696600522148060': 'file_storage/function-call-11133696600522148060.json', 'var_function-call-2938307876171220754': [{'norm_title': '', 'norm_artist': 'unknown', 'total_revenue': 65286.36}, {'norm_title': 'none', 'norm_artist': 'unknown', 'total_revenue': 14647.52}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4379.75}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'total_revenue': 4311.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 4102.45}], 'var_function-call-9944138461387281347': [{'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 4379.75}, {'norm_title': 'all my friends say album version', 'norm_artist': 'luke bryan', 'total_revenue': 4311.59}, {'norm_title': 'the fire still burns', 'norm_artist': 'russ ballard', 'total_revenue': 4102.45}, {'norm_title': 'here i am nevins dirtyrock club mix reedit', 'norm_artist': 'sertab erener', 'total_revenue': 3863.69}, {'norm_title': 'happy together', 'norm_artist': 'the turtles', 'total_revenue': 3773.49}, {'norm_title': 'vostok', 'norm_artist': 'craig padilla', 'total_revenue': 3767.95}, {'norm_title': 'christmas in my heart', 'norm_artist': 'candi staton', 'total_revenue': 3744.97}, {'norm_title': 'september in the rain', 'norm_artist': 'the ralph sharon trio', 'total_revenue': 3732.72}, {'norm_title': 'the power of love rob searle club mix', 'norm_artist': 'frankie goes to hollywood', 'total_revenue': 3697.5299999999997}, {'norm_title': 'suddenly bt radio edit', 'norm_artist': 'bt', 'total_revenue': 3696.46}], 'var_function-call-16044646853984478263': {'groovey_variants': [{'title': 'Psycho & Horror: Vertigo Groove (30 second version) - Suspense Atmo', 'artist': 'Oliver F. Koelling', 'total_revenue': 1547.19}, {'title': 'Psycho & Horror: Vertigo Groove (30 second version)', 'artist': 'Oliver F. Koelling', 'total_revenue': 936.89}, {'title': 'Echoes From the Deep (stinger)(Atmospheric Grooves)', 'artist': 'Devine-King', 'total_revenue': 820.04}, {'title': 'Get Down (feat. Kenny Dope, DJ Sneak, Terry Hunter & Tara McDonald) (Mousse T club mix) - Bargrooves: Bar Anthems', 'artist': 'Todd Terry All Stars', 'total_revenue': 763.49}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 1036.29}, {'title': 'Final Cut (30 second version) - Moods and Grooves, Volume 11', 'artist': 'Gary Philips', 'total_revenue': 472.53}, {'title': 'The Pickle Groove (Ewan Dobson II)', 'artist': 'Ewan Dobson', 'total_revenue': 1321.61}, {'title': 'All the Time in the World (Grooves, Volume Thirteen)', 'artist': 'Subdudes', 'total_revenue': 1306.38}, {'title': 'Solid Groove - Flookin’', 'artist': 'None', 'total_revenue': 67.93}, {'title': "Dizzy Gillespie - Groovin' High", 'artist': 'None', 'total_revenue': 1772.9599999999998}, {'title': "Turn Your Head (The Plague That Makes Your Booty Move... It's the Infectious Grooves)", 'artist': 'Infectious Grooves', 'total_revenue': 386.65}, {'title': "Spiller - Groovejet (If This Ain't Love) (Ernest St. Laurent 'Rosetrack' remix)", 'artist': 'None', 'total_revenue': 1345.47}, {'title': "Nothing to Offer (Not Just a Dub) (GT's House: Supercharged by Groove Terminator)", 'artist': 'Robbie Rivera', 'total_revenue': 1264.22}, {'title': 'A Little Jingle Jam - In the Christmas Groove', 'artist': 'Derek Close', 'total_revenue': 1242.13}, {'title': 'Blind Date (MAD Grooves)', 'artist': 'Green Jellÿ', 'total_revenue': 1021.68}, {'title': 'Ponto Sem Retorno (Groove Junkies 1995-2005)', 'artist': 'Cool Hipnoise', 'total_revenue': 891.85}, {'title': 'Groove Juice Special - The Groove Juice Special', 'artist': 'Slim & Slam', 'total_revenue': 29.19}, {'title': 'Psycho & Horror: Vertigo Groove (30 second version) (Suspense Atmo)', 'artist': 'Oliver F. Koelling', 'total_revenue': 245.25}, {'title': 'Prohibition Groove - Investigation Grooves', 'artist': 'Christof Dejean', 'total_revenue': 1680.75}, {'title': 'Magic Carpet 1/2 (Voice Over Grooves)', 'artist': 'Phil Beazley', 'total_revenue': 1612.5500000000002}, {'title': 'Christof Dejean - Prohibition Groove', 'artist': 'None', 'total_revenue': 349.11}, {'title': "It Don't Have To Be Funky (To Be A Groove) (Nice 'n' Naasty)", 'artist': 'Salsoul Orchestra', 'total_revenue': 590.49}, {'title': 'Caned - Fish Grooves, Volume 1: Advanced Beats From The Deep', 'artist': 'Dynamite', 'total_revenue': 360.09}, {'title': 'Prohibition Groove', 'artist': 'Christof Dejean', 'total_revenue': 2005.89}, {'title': '043-Prohibition Groove', 'artist': 'Christof Dejean', 'total_revenue': 769.01}, {'title': '006-Groovey', 'artist': 'Rich Matteson', 'total_revenue': 251.16}, {'title': 'STAY… (HYPER GROOVE PARTY)', 'artist': 'Folder 5', 'total_revenue': 773.61}, {'title': 'Final Cut (30 second version) (Moods and Grooves, Volume 11)', 'artist': 'Gary Philips', 'total_revenue': 477.73}, {'title': "Groovin' High (Complete Edition, Volume 7-8: 1946)", 'artist': 'Dizzy Gillespie', 'total_revenue': 1140.22}, {'title': "Albert's Groove", 'artist': "Dave D'Angelico", 'total_revenue': 2177.7200000000003}, {'title': "The Outfield - Heaven's Little Angel (groove mix)", 'artist': 'None', 'total_revenue': 581.53}, {'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'total_revenue': 505.61}, {'title': "I Can't Wait Anymore (easy order mix) (groove remixes)", 'artist': '露崎春女', 'total_revenue': 360.79}, {'title': 'Slim & Slam - Groove Juice Special', 'artist': 'None', 'total_revenue': 290.05}, {'title': 'Miss Clawdy (30 second version) - Groovemasters: Funky Mix', 'artist': 'Nigel Mullaney & Jonathan Jowett', 'total_revenue': 238.96}, {'title': 'A Groovy Kind of Love (Gold & Platinum, Volume 6)', 'artist': 'Phil Collins', 'total_revenue': 1107.87}, {'title': 'Rich Matteson - Groovey', 'artist': 'None', 'total_revenue': 1288.75}, {'title': "Charlie Parker - Groovin' High", 'artist': 'None', 'total_revenue': 218.88}, {'title': 'Groove Is in the Girls (Deee-Lite vs. The Prodigy)', 'artist': "Dunproofin'", 'total_revenue': 617.4399999999999}, {'title': 'Groove Addicts - Construction Kit: One Shots: Whole Note OS 07 G#', 'artist': 'None', 'total_revenue': 632.5799999999999}, {'title': "Groovejet (If This Ain't Love) (Video Hits 96-06)", 'artist': 'Spiller', 'total_revenue': 538.82}, {'title': 'Oliver F. Koelling - Psycho & Horror: Vertigo Groove (30 second version)', 'artist': 'None', 'total_revenue': 1301.88}, {'title': "Groovin' High - Bird of Paradise", 'artist': 'Charlie Parker', 'total_revenue': 1055.27}, {'title': 'Prohibition Groove (Investigation Grooves)', 'artist': 'Christof Dejean', 'total_revenue': 532.98}, {'title': "019-Groovejet (If This Ain't Love)", 'artist': 'Sp iller', 'total_revenue': 192.14}, {'title': 'Hello - New York Groove', 'artist': 'None', 'total_revenue': 1562.71}, {'title': 'New York Groove - 101 Hits 70s', 'artist': 'Hello', 'total_revenue': 1383.38}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 949.82}, {'title': "Groovejet (If This Ain't Love)", 'artist': 'Spiller', 'total_revenue': 525.35}, {'title': "It Don't Have To Be Funky (To Be A Groove)", 'artist': 'The Salsoul Orchesttra', 'total_revenue': 1116.85}, {'title': "We're Into This Groove", 'artist': 'By All Means', 'total_revenue': 509.29}, {'title': 'Infectious Grooves - Turn Your Head', 'artist': 'None', 'total_revenue': 1743.09}, {'title': 'The Pickle Groove', 'artist': 'Ewan Dobson', 'total_revenue': 687.18}, {'title': 'Groove My Mind - Best of Me', 'artist': 'Thriller U', 'total_revenue': 1026.28}, {'title': "We're Into This Groove (By All Means)", 'artist': 'By All Means', 'total_revenue': 1260.94}, {'title': "The Salsoul Orchestra - It Don't Have To Be Funky (To Be A Groove)", 'artist': 'None', 'total_revenue': 654.0}, {'title': 'Just a Touch of Love (Jazzy instrumental version) - The Definitive Groove Collection', 'artist': 'Slave', 'total_revenue': 1558.65}, {'title': '069-Psycho & Horror: Vertigo Groove (30 second version)', 'artist': 'Oliver F. Koelling', 'total_revenue': 1206.76}, {'title': "Groovin' High - Complete iEdition, Volume 7-8: 1946", 'artist': 'Dizzy Gillespie', 'total_revenue': 747.79}, {'title': 'FX and Scratches - Bust a Groove', 'artist': 'Paul Oakenfold', 'total_revenue': 104.76}, {'title': "Turn Your Head - The Plague That Makes Your Booty Move... It's the Infectious Grooves", 'artist': 'Infectious Grooves', 'total_revenue': 290.95000000000005}, {'title': 'Ponto em Retorno - Groove Junkies 1995-2005', 'artist': 'Cool Hipnoise', 'total_revenue': 767.3599999999999}, {'title': 'Groovey', 'artist': 'Rich Matteson', 'total_revenue': 2142.48}, {'title': 'StreetH ype (Groove City)', 'artist': 'Bruce Maginnis', 'total_revenue': 1055.51}, {'title': 'Groove 5 - Xtreme Sports', 'artist': 'Michael Bartel', 'total_revenue': 1188.09}, {'title': 'Here I Go Again (I Get My Groove - Crossover Soul From the Deep South)', 'artist': 'Jean Plum', 'total_revenue': 858.5499999999998}, {'title': "You Don't Know Me (Roots & Grooves)", 'artist': 'Maceo Parker', 'total_revenue': 1054.99}, {'title': 'Original Jive - Bargrooves: Members Only', 'artist': 'Natural Rhythm', 'total_revenue': 541.9799999999999}], 'friends_variants': [{'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'total_revenue': 1501.6699999999998}, {'title': '002-All My Friends Say (album version)', 'artist': 'Luke Bryan', 'total_revenue': 1070.38}, {'title': 'All My Friends Say (album version)', 'artist': 'Luke Bryan', 'total_revenue': 1739.54}, {'title': 'Luke Bryan - All My Friends Say (album version)', 'artist': 'None', 'total_revenue': 869.34}]}, 'var_function-call-8495888752070622274': [{'norm_title': '', 'norm_artist': 'none', 'total_revenue': 39995.87}, {'norm_title': '', 'norm_artist': '', 'total_revenue': 24063.73}, {'norm_title': 'none', 'norm_artist': 'none', 'total_revenue': 14647.52}, {'norm_title': 'emerge', 'norm_artist': 'fischerspooner', 'total_revenue': 6665.27}, {'norm_title': 'groovey', 'norm_artist': 'rich matteson', 'total_revenue': 5668.5}, {'norm_title': 'all my friends say', 'norm_artist': 'luke bryan', 'total_revenue': 5180.93}, {'norm_title': 'jah love', 'norm_artist': 'lemon d', 'total_revenue': 5168.45}, {'norm_title': 'ghetto supastar that is what you are', 'norm_artist': 'pras', 'total_revenue': 4933.98}, {'norm_title': 'the power of love rob searle club mix', 'norm_artist': 'frankie goes to hollywood', 'total_revenue': 4909.04}, {'norm_title': 'zo gaat het leven aan je voor', 'norm_artist': 'syb van der ploeg', 'total_revenue': 4881.42}]}

exec(code, env_args)
