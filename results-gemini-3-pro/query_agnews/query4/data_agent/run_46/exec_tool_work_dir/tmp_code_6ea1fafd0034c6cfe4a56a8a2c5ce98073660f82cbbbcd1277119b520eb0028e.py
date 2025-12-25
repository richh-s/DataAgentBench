code = """import json
import pandas as pd

# Load previous data
with open(locals()['var_function-call-16230520417025150586'], 'r') as f:
    metadata_list = json.load(f)
metadata = pd.DataFrame(metadata_list)
metadata['article_id'] = metadata['article_id'].astype(int)

with open(locals()['var_function-call-15625371316220222437'], 'r') as f:
    articles_list = json.load(f)
articles = pd.DataFrame(articles_list)
articles['article_id'] = articles['article_id'].astype(int)

df = pd.merge(metadata, articles, on='article_id', how='inner')

countries = [
    'afghanistan', 'albania', 'algeria', 'angola', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan', 
    'bahrain', 'bangladesh', 'belarus', 'belgium', 'bolivia', 'bosnia', 'brazil', 'britain', 'bulgaria', 'burma', 
    'cambodia', 'canada', 'chile', 'china', 'colombia', 'congo', 'croatia', 'cuba', 'cyprus', 'czech', 'denmark', 
    'ecuador', 'egypt', 'estonia', 'ethiopia', 'finland', 'france', 'georgia', 'germany', 'ghana', 'greece', 
    'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'jamaica', 'japan', 
    'jordan', 'kazakhstan', 'kenya', 'korea', 'kuwait', 'latvia', 'lebanon', 'libya', 'lithuania', 'malaysia', 
    'mexico', 'morocco', 'myanmar', 'nepal', 'netherlands', 'zealand', 'nicaragua', 'nigeria', 'norway', 'oman', 
    'pakistan', 'palestin', 'panama', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 
    'russia', 'rwanda', 'saudi', 'serbia', 'singapore', 'slovakia', 'slovenia', 'somalia', 'spain', 'lanka', 
    'sudan', 'sweden', 'switzerland', 'syria', 'taiwan', 'tajikistan', 'tanzania', 'thailand', 'tunisia', 
    'turkey', 'uganda', 'ukraine', 'kingdom', 'united states', 'usa', 'uruguay', 'uzbekistan', 'venezuela', 
    'vietnam', 'yemen', 'zambia', 'zimbabwe', 'vatican', 'eu', 'un', 'nato'
]

keywords = {
    'Business': ['market', 'stock', 'price', 'share', 'earnings', 'profit', 'loss', 'quarter', 'company', 'corp', 'inc', 'firm', 'bank', 'economy', 'economic', 'trade', 'investment', 'investor', 'wall st', 'bond', 'currency', 'dollar', 'euro', 'yen', 'oil', 'gas', 'energy', 'bid', 'deal', 'merger', 'acquisition', 'sales', 'retail', 'fed', 'federal reserve', 'rate', 'inflation', 'ceo', 'cfo', 'bankruptcy', 'debt', 'dividend', 'nasdaq', 'dow', 'index', 'acquire', 'buyout'],
    'Sci/Tech': ['technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'net', 'mobile', 'wireless', 'phone', 'cellphone', 'chip', 'processor', 'digital', 'electronic', 'device', 'gadget', 'robot', 'space', 'nasa', 'astronomy', 'biology', 'physics', 'study', 'research', 'scientist', 'google', 'microsoft', 'apple', 'ibm', 'intel', 'linux', 'windows', 'server', 'satellite', 'virus', 'spam', 'hacker', 'browser', 'search engine', 'video game', 'videogame', 'sony', 'nintendo', 'facebook', 'amazon'],
    'Sports': ['sport', 'game', 'match', 'team', 'club', 'player', 'coach', 'manager', 'athlete', 'score', 'goal', 'point', 'win', 'lose', 'draw', 'defeat', 'victory', 'champion', 'medal', 'olympic', 'tournament', 'cup', 'league', 'season', 'football', 'basketball', 'baseball', 'soccer', 'tennis', 'golf', 'hockey', 'cricket', 'rugby', 'boxing', 'racing', 'f1', 'nfl', 'nba', 'mlb', 'nhl', 'stadium', 'wrestl', 'doping'],
    'World': ['world', 'international', 'nation', 'state', 'government', 'ministry', 'official', 'president', 'premier', 'minister', 'leader', 'politician', 'parliament', 'senate', 'congress', 'election', 'vote', 'poll', 'campaign', 'party', 'war', 'peace', 'conflict', 'military', 'army', 'navy', 'troop', 'soldier', 'rebel', 'guerrilla', 'terror', 'attack', 'bomb', 'blast', 'explosion', 'kill', 'death', 'dead', 'injure', 'wound', 'crash', 'disaster', 'quake', 'flood', 'storm', 'police', 'crime', 'court', 'trial', 'judge', 'prison', 'jail', 'treaty', 'accord', 'summit', 'diplomacy', 'foreign', 'nuclear', 'sanctions', 'hostage', 'refugee', 'human rights', 'protest', 'demonstration', 'strike', 'riot', 'coup', 'africa', 'asia', 'europe', 'south america', 'north america'] + countries
}

def classify(row):
    title = row['title'].lower()
    desc = row['description'].lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in title:
                scores[cat] += 2
            if kw in desc:
                scores[cat] += 1
    if sum(scores.values()) == 0:
        return "Unknown"
    return max(scores, key=scores.get)

df['category'] = df.apply(classify, axis=1)

world_df = df[df['category'] == 'World']
result = world_df.groupby('region').size().reset_index(name='count')
result = result.sort_values('count', ascending=False)
print("__RESULT__:")
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-16230520417025150586': 'file_storage/function-call-16230520417025150586.json', 'var_function-call-3657157287295125768': 'file_storage/function-call-3657157287295125768.json', 'var_function-call-11380327074732110447': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-7239028984248077893': [{'COUNT(*)': '127600'}], 'var_function-call-4952987129056377997': {'count': 6695.0, 'mean': 19.0525765497, 'std': 18.3984364514, 'min': 1.0, '25%': 6.0, '50%': 14.0, '75%': 26.0, 'max': 181.0}, 'var_function-call-16156824569502898974': 'file_storage/function-call-16156824569502898974.json', 'var_function-call-15625371316220222437': 'file_storage/function-call-15625371316220222437.json', 'var_function-call-3602621004185108934': [{'region': 'North America', 'count': 479}, {'region': 'Europe', 'count': 477}, {'region': 'South America', 'count': 465}, {'region': 'Asia', 'count': 461}, {'region': 'Africa', 'count': 455}], 'var_function-call-16615874053357706300': [{'region': 'Africa', 'count': 543}, {'region': 'Europe', 'count': 537}, {'region': 'South America', 'count': 530}, {'region': 'North America', 'count': 529}, {'region': 'Asia', 'count': 502}], 'var_function-call-13277016520187411835': {'counts': [{'region': 'Europe', 'count': 588}, {'region': 'Africa', 'count': 573}, {'region': 'South America', 'count': 572}, {'region': 'North America', 'count': 570}, {'region': 'Asia', 'count': 533}], 'unknown': 116}}

exec(code, env_args)
