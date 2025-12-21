code = """import json, pandas as pd

# Identify the canonical Brucqe/Brucqe-like Maginnis 'Street Hype' tracks from previous result
candidates = json.loads(json.dumps(var_call_hSWTeLMtz5lZxtqbh44YZHYw))

cand_df = pd.DataFrame(candidates)

# Filter to rows clearly about Street Hype and Maginnis/Brucqe
mask = cand_df['title'].str.contains('Street Hype', case=False, na=False) & (
    cand_df['artist'].str.contains('Maginnis', case=False, na=False)
)

street_hype_df = cand_df[mask]

track_ids = set(street_hype_df['track_id'].tolist())

# Also include obvious variants: where title contains 'Street Hype' and title/artist contain Bruce/Brucqe
mask2 = cand_df['title'].str.contains('Street Hype', case=False, na=False) & (
    cand_df['title'].str.contains('Bruce', case=False, na=False) |
    cand_df['title'].str.contains('Brucqe', case=False, na=False) |
    cand_df['artist'].str.contains('Bruce', case=False, na=False) |
    cand_df['artist'].str.contains('Brucqe', case=False, na=False)
)

street_hype_df2 = cand_df[mask2]
for tid in street_hype_df2['track_id'].tolist():
    track_ids.add(tid)

# Also include the clearly typo'd one: 'Bruce Maginnis - Sttreet Hype'
mask3 = cand_df['title'].str.contains('Sttreet Hype', case=False, na=False)
street_hype_df3 = cand_df[mask3]
for tid in street_hype_df3['track_id'].tolist():
    track_ids.add(tid)

track_ids = [int(t) for t in track_ids]

# Load sales
with open(var_call_uy6lO5uMG2mcBNQ2QSZAltLI, 'r') as f:
    sales = json.load(f)

sales_df = pd.DataFrame(sales)
sales_df['track_id'] = sales_df['track_id'].astype(int)
sales_df['revenue_usd'] = sales_df['revenue_usd'].astype(float)

bruce_sales = sales_df[sales_df['track_id'].isin(track_ids)]
agg = bruce_sales.groupby('store', as_index=False)['revenue_usd'].sum().sort_values('revenue_usd', ascending=False)

result = {}
if not agg.empty:
    top = agg.iloc[0]
    result = {"store": top['store'], "revenue_usd": float(top['revenue_usd'])}

print("__RESULT__:")
print(json.dumps({"track_ids": track_ids, "top_store": result}))"""

env_args = {'var_call_TIRlkB33DS7YH7NLNy59DNGJ': 'file_storage/call_TIRlkB33DS7YH7NLNy59DNGJ.json', 'var_call_uy6lO5uMG2mcBNQ2QSZAltLI': 'file_storage/call_uy6lO5uMG2mcBNQ2QSZAltLI.json', 'var_call_JhMX87QwpoEetM2u3P7zkpan': {}, 'var_call_hSWTeLMtz5lZxtqbh44YZHYw': [{'track_id': '7', 'title': 'Bruce Maginnis - Sttreet Hype', 'artist': 'None', 'album': 'Groove City', 'year': '05'}, {'track_id': '128', 'title': 'Basin Street Blues (The Quintessence: New York – Chicago 1925-1940)', 'artist': 'Louis Armstrong', 'album': 'The Quintessence: New York – Chicago 1925-1940', 'year': '1994'}, {'track_id': '857', 'title': 'Marlborough Street Blues', 'artist': 'Ian & Sylvia', 'album': 'Early Morning Rain', 'year': '1965'}, {'track_id': '864', 'title': 'Basin Street Blues', 'artist': 'Louis Armstrong', 'album': 'The Quintessence: New York – Chicago 1925-1940', 'year': '1 994'}, {'track_id': '959', 'title': 'Swing Street - Every Turn of the World', 'artist': 'Christopher Cross', 'album': 'None', 'year': 'None'}, {'track_id': '1062', 'title': 'În stânga țin icoana, cu dreapta îmi fac cruce (Colinde pentru suflete românești)', 'artist': 'Polina Manoilă', 'album': 'Colinde pentru suflete românești', 'year': '2004'}, {'track_id': '1322', 'title': 'U2 - Where the Streets Have No Name', 'artist': 'None', 'album': '1993-08-28: Zoo Europa: Royal Dublin Society Arena, Dublin, Ireland (disc 2)', 'year': 'None'}, {'track_id': '1417', 'title': '020-Street Dancer', 'artist': 'Avicii', 'album': 'The Dome, Volume 57 (201)1', 'year': 'None'}, {'track_id': '1768', 'title': "How's Your Mama? (Phil's Theme): 52nd Street Theme / Salt Peanuts / Harlem Nocturne - Celebration!", 'artist': 'Phil Woods & The Festival Orchestra', 'album': 'None', 'year': 'None'}, {'track_id': '2795', 'title': '002-Hyper Chondriac Music', 'artist': 'Muse', 'album': 'Bliss (disc 2) (2001)', 'year': 'None'}, {'track_id': '2997', 'title': 'Lenny Bruce - Shot of Love', 'artist': 'Bob Dylan', 'album': 'None', 'year': "'81"}, {'track_id': '3283', 'title': 'Until the Night Is Through (Dance Dance Dance) (Back Street Symphony)', 'artist': 'Thunder', 'album': 'Back Street Symphony', 'year': '2009'}, {'track_id': '3639', 'title': 'Back to the Street - Dear Friends 2', 'artist': 'SPEED', 'album': 'None', 'year': "'00"}, {'track_id': '3656', 'title': 'My Way (Nightstreet)', 'artist': 'Roxus', 'album': 'Nightstreet', 'year': 'None'}, {'track_id': '3658', 'title': '034-Street Vibe', 'artist': 'Rich Samalin & Christopher E. Hajian', 'album': 'Law and Order (unknown)', 'year': 'None'}, {'track_id': '3707', 'title': '007-Swing Street', 'artist': 'Christopher Cross', 'album': 'Every Turn of the World (unknown)', 'year': 'None'}, {'track_id': '3825', 'title': 'Street Funk (full mix)', 'artist': 'Steve Dymond& Barrie Gledden', 'album': '1970s, Funk', 'year': '2005'}, {'track_id': '3913', 'title': "Christopher O'Riley - Street Spirit (Fade Out)", 'artist': 'None', 'album': "Hold Me to This: Christopher O'Riley Plays Radiohead", 'year': '05'}, {'track_id': '4095', 'title': 'Streets of London (The Greatest Hits of Roger Whittaker)', 'artist': 'Roger Whittaker', 'album': 'The Greatest Hits of Roger Whittaker', 'year': 'None'}, {'track_id': '4122', 'title': 'Street Hype', 'artist': 'Brucqe Maginnis', 'album': 'Groove City', 'year': '2005'}, {'track_id': '4575', 'title': 'U2 - Where the Streets Have No Name', 'artist': 'None', 'album': 'Earthquake in Rome', 'year': 'None'}, {'track_id': '4628', 'title': 'Street Hype - Groove City', 'artist': 'Bruce Maginnis', 'album': 'None', 'year': "'05"}, {'track_id': '4814', 'title': 'Pogo - Need for Speed ProStreet', 'artist': 'Digitalism', 'album': 'None', 'year': "'07"}, {'track_id': '5125', 'title': '019-Hyper Hyper (Faster, Harder, Scooter)', 'artist': 'Scooter', 'album': 'Techno Trance (1995)', 'year': 'None'}, {'track_id': '5483', 'title': 'Broad Factor (Street edit)', 'artist': 'Quasimoto', 'album': 'Broad Factor', 'year': '2004'}, {'track_id': '6486', 'title': 'Bruce Springsteen - Adam Raised a Cain (Guitar) (2005-11-09)', 'artist': 'None', 'album': 'Love, Tears & Mystery', 'year': 'None'}, {'track_id': '6492', 'title': 'Thousand-Mile-Stare - Love for the Streets', 'artist': 'Caessars Palace', 'album': 'None', 'year': "'02"}, {'track_id': '6501', 'title': 'Hyper Chondriac Music', 'artist': 'Muse', 'album': 'Bliss (disc 2)', 'year': '2001'}, {'track_id': '7078', 'title': 'În stânga țin icoana, cu dreaptaa îmi fac cruce - Colinde penttru suflete românești', 'artist': 'Polina Manoilă', 'album': 'None', 'year': "'04"}, {'track_id': '7606', 'title': "Manhattan Medley: Manhattan - Lullaby of Broadway - 42nd Street (It Don't Mean a Thing)", 'artist': 'String Fever, Marin Alsop', 'album': "It Don't Mean a Thing", 'year': 'None'}, {'track_id': '7616', 'title': 'Lenny Bruce', 'artist': 'Bob Dylan', 'album': 'Shot of Love', 'year': '1981'}, {'track_id': '7836', 'title': 'Until the Night Is Through (Dance Dance Dance) - Back Street Symphony', 'artist': 'Thunedr', 'album': 'None', 'year': "'09"}, {'track_id': '7938', 'title': 'Locked Out (Hypertrace)', 'artist': 'Scanner', 'album': 'Hypertrace', 'year': '1998'}, {'track_id': '7963', 'title': '004-Ching-A-Ling (Step U2 the Streets O.S.T. version)', 'artist': 'Miss y Ellivtt', 'album': 'Feel the Streets: The Real Masters of Hip Hop (unknown)', 'year': 'None'}, {'track_id': '8215', 'title': "緋月の狂想曲 (pop'n music 19 TUNE STREET original soundtrack)", 'artist': '倉持武志', 'album': "pop'n music 19 TUNE STREET original soundtrack", 'year': '2011'}, {'track_id': '8727', 'title': 'Infinity Ends - Hypercube', 'artist': 'Zyce & Fox', 'album': 'None', 'year': "'08"}, {'track_id': '8743', 'title': 'Street Vibe - Law and Order', 'artist': 'Rich Samalin & Christopher E. Hajian', 'album': 'None', 'year': 'None'}, {'track_id': '8749', 'title': "009-How's Your Mama? (Phil's Theme): 52nd Street Theme / Salt Peanuts / Harlem Nocturne", 'artist': 'Phil Woods & The Festival Orchestar', 'album': 'Celebration! (unknown)', 'year': 'None'}, {'track_id': '8823', 'title': 'Empty Streets B', 'artist': 'Christopher E. Hajian & William Franklin Lee', 'album': 'Drama Plus, Volume 4', 'year': 'None'}, {'track_id': '9946', 'title': '005-In stanga tin icoana, cu dreapta imi fac cruce', 'artist': 'Polina Manoila', 'album': 'Colinde pentru suflete romanesti (2004)', 'year': 'None'}, {'track_id': '10145', 'title': 'Lenny Bruce (Shot of Love)', 'artist': 'Bob Dylan', 'album': 'Shot of Love', 'year': '1981'}, {'track_id': '10472', 'title': 'Respect’s a Two Way Street - Time to Pay Up #5', 'artist': 'Trying', 'album': 'None', 'year': 'None'}, {'track_id': '10476', 'title': 'Bruce Cockburn - The Embers of Eden', 'artist': 'None', 'album': 'Breakfast in New Orleans, Dinner in Timbuktu', 'year': '99'}, {'track_id': '10627', 'title': 'Next Hype (Ashburner remix) (Ministry of Sound: The Sound of Dubstep 2)', 'artist': 'Tempa T', 'album': 'Ministry of Sound: The Sound of Dubstep 2', 'year': '2010'}, {'track_id': '10688', 'title': 'Louis Armstrong - Basin Street Blues', 'artist': 'None', 'album': 'The Quintessence: New York – Chicago 1925-1940', 'year': '94'}, {'track_id': '10968', 'title': 'Chilling Through the Lives (Hypermodern Jazz 2000.5)', 'artist': 'Alec Empire', 'album': 'Hypermodern Jazz 2000.5', 'year': '1996'}, {'track_id': '11079', 'title': 'Hyperrealism, Part 1: (re-edit)', 'artist': 'Steve Stoll', 'album': 'Pure - Best of Techno, Volume 6', 'year': '1995'}, {'track_id': '11227', 'title': 'Street Mix - The Underdog: El Subestimado', 'artist': 'Chyno Nyno', 'album': 'None', 'year': "'05"}, {'track_id': '11345', 'title': '002-Sunny Side of the Street', 'artist': 'Jon Mosey', 'album': 'Both Sides of the Street (1998)', 'year': 'None'}, {'track_id': '12452', 'title': "Street Spirit (Fade Out) (Hold Me to This: Christopher O'Riley Plays Radiohead)", 'artist': "Christopher O'Riley", 'album': "Hold Me to This: Christopher O'Riley Plays Radiohead", 'year': '2005'}]}

exec(code, env_args)
