code = """import json
from collections import Counter

# Load metadata
with open(locals()['var_function-call-5900547977647289407'], 'r') as f:
    metadata_list = json.load(f)

# Load articles content
with open(locals()['var_function-call-12526826201360126982'], 'r') as f:
    content_list = json.load(f)

content_map = {}
for item in content_list:
    content_map[str(item['article_id'])] = (item.get('title', '') + " " + item.get('description', '')).lower()

keywords = {
    "World": [
        "afghanistan", "africa", "arab", "baghdad", "beijing", "bomb", "border", "britain", 
        "brussels", "chancellor", "china", "crisis", "diplomat", "egypt", "embassy", "eu", 
        "europe", "explosion", "foreign", "france", "gaza", "germany", "government", "greece", 
        "guerrilla", "hostage", "india", "insurgent", "international", "iran", "iraq", "israel", 
        "japan", "jerusalem", "kabul", "kerry", "kiev", "korea", "leader", "libya", "london", 
        "merkel", "migrant", "military", "minister", "missile", "moscow", "nato", "navy", 
        "nuclear", "obama", "official", "pakistan", "palestine", "parliament", "peace", 
        "politics", "premier", "president", "prime minister", "protest", "putin", "rebel", 
        "refugee", "russia", "sanction", "soldier", "suicide", "syria", "taliban", "tehran", 
        "terror", "treaty", "troop", "turkey", "ukraine", "un", "united nations", "war", "weapon", 
        "yemen"
    ],
    "Sports": [
        "baseball", "basketball", "champion", "championship", "coach", "cup", "defeat", "football", 
        "game", "gold", "golf", "hockey", "league", "medal", "mlb", "nascar", "nba", "nfl", 
        "nhl", "olympic", "player", "race", "score", "season", "soccer", "sport", "stadium", 
        "team", "tennis", "tournament", "victory", "win", "world cup"
    ],
    "Business": [
        "bank", "bond", "business", "buy", "ceo", "company", "corp", "deal", "dollar", "dow", 
        "earnings", "economy", "euro", "export", "federal", "finance", "firm", "fund", "growth", 
        "import", "inc", "industry", "invest", "ipo", "job", "loss", "market", "merger", "money", 
        "nasdaq", "oil", "price", "profit", "quarter", "rate", "report", "revenue", "sale", 
        "share", "stock", "trade", "wall street"
    ],
    "Sci/Tech": [
        "android", "apple", "app", "astronomy", "biology", "browser", "cancer", "cell", "computer", 
        "device", "disease", "drug", "facebook", "galaxy", "gene", "google", "health", "internet", 
        "mars", "microsoft", "mission", "mobile", "moon", "nasa", "network", "online", "phone", 
        "planet", "research", "robot", "satellite", "science", "scientist", "server", "software", 
        "space", "study", "tech", "technology", "virus", "web", "windows", "wireless"
    ]
}

region_counts = Counter()
debug_samples = []

for meta in metadata_list:
    aid = str(meta['article_id'])
    if aid in content_map:
        text = content_map[aid]
        scores = {cat: 0 for cat in keywords}
        
        for cat, words in keywords.items():
            for word in words:
                if word in text:
                    scores[cat] += 1
        
        # Classification Logic
        category = 'Other'
        s_world = scores['World']
        s_sports = scores['Sports']
        s_business = scores['Business']
        s_tech = scores['Sci/Tech']
        
        # Priority: If specific categories match, prefer them over World if scores are close
        # But if World score is high (e.g. war, president, syria), it should win.
        
        # Let's verify matches:
        # If Sports has ANY score? "Russia wins" -> World(1), Sports(1). Sports wins.
        # "President at Baseball game" -> World(1), Sports(1). Sports wins? Probably okay.
        
        if s_sports >= s_world and s_sports > 0:
            category = 'Sports'
        elif s_business >= s_world and s_business > 0:
            category = 'Business'
        elif s_tech >= s_world and s_tech > 0:
            category = 'Sci/Tech'
        elif s_world > 0:
            category = 'World'
            
        if category == 'World':
            region_counts[meta['region']] += 1
            if len(debug_samples) < 5:
                debug_samples.append({"id": aid, "text": text[:100], "scores": scores, "region": meta['region']})

print("__RESULT__:")
print(json.dumps({
    "region_counts": dict(region_counts), 
    "debug_samples": debug_samples
}))"""

env_args = {'var_function-call-5900547977647289407': 'file_storage/function-call-5900547977647289407.json', 'var_function-call-8253439238580865499': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52]}, 'var_function-call-11413350339637926914': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6748392322076207893': {'counts': {}, 'debug': []}, 'var_function-call-11835655730956261158': {'common': 0}, 'var_function-call-12334258275261728907': {'common_int': 0}, 'var_function-call-762477354594242145': {'meta_count': 6696, 'content_count': 5, 'meta_min': 13, 'meta_max': 127570, 'content_min': 0, 'content_max': 4, 'meta_sample': [13, 18, 26, 51, 52], 'content_sample': [0, 1, 2, 3, 4], 'content_sample_raw': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_function-call-17256143422197129974': [{'_id': '694510d0f346764387e32f39', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}], 'var_function-call-15580149888157125641': [{'_id': '694510d0f346764387e32f39', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '694510d0f346764387e32f3a', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '694510d0f346764387e32f3b', 'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'_id': '694510d0f346764387e32f3c', 'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'_id': '694510d0f346764387e32f3d', 'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}], 'var_function-call-12526826201360126982': 'file_storage/function-call-12526826201360126982.json', 'var_function-call-985103073594669786': {'region_counts': {'South America': 715, 'Asia': 677, 'North America': 700, 'Europe': 719, 'Africa': 695}, 'missing_content': 0, 'debug_samples': [{'id': '51', 'text': "delightful dell the company's results show that it's not grim all over tech world. just all of it th", 'scores': {'World': 1, 'Sports': 0, 'Business': 1, 'Sci/Tech': 1}, 'region': 'South America'}, {'id': '67', 'text': 'it myth 5: most it projects fail do most it projects fail? some point to the number of giant consult', 'scores': {'World': 1, 'Sports': 0, 'Business': 1, 'Sci/Tech': 0}, 'region': 'Asia'}, {'id': '97', 'text': "what's in a name? well, matt is sexier than paul (reuters) reuters - as shakespeare said, a rose by ", 'scores': {'World': 1, 'Sports': 0, 'Business': 0, 'Sci/Tech': 0}, 'region': 'North America'}, {'id': '141', 'text': 'indictments using dna on rise nationally (ap) ap - authorities once had no choice but to drop rape c', 'scores': {'World': 2, 'Sports': 0, 'Business': 2, 'Sci/Tech': 0}, 'region': 'Asia'}, {'id': '179', 'text': "reverse psychology \\\\i really hope sun doesn't open source java at javaone this year.  it would be a", 'scores': {'World': 1, 'Sports': 0, 'Business': 1, 'Sci/Tech': 1}, 'region': 'Europe'}]}}

exec(code, env_args)
