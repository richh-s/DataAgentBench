code = """import json
import re

def load_data(data_var):
    if isinstance(data_var, str):
        with open(data_var, 'r') as f:
            return json.load(f)
    elif isinstance(data_var, list):
        return data_var
    else:
        return []

# Load SQL result (metadata)
meta_list = load_data(locals()['var_function-call-14838360778106258720'])
# Load Mongo result (articles)
articles_list = load_data(locals()['var_function-call-1196445325152998757'])

# Build metadata dict: article_id -> year
meta_dict = {}
for m in meta_list:
    aid = str(m['article_id'])
    if 'publication_date' in m and m['publication_date']:
        try:
            y = int(m['publication_date'][:4])
            meta_dict[aid] = y
        except:
            pass

# Keywords
cats = {
    'business': ["business", "economy", "market", "stock", "trade", "financial", "finance", "money", "bank", "invest", "company", "industry", "profit", "revenue", "dollar", "euro", "oil", "price", "gold", "wall street", "nasdaq", "dow jones", "share", "growth", "crisis", "inflation", "rate", "fed", "central bank", "jobs", "unemployment", "tax", "ceo", "earnings", "deal", "merger", "acquisition", "bond", "fund", "asset", "credit", "recession", "sales", "retail", "consumer", "spending", "budget", "deficit", "ipo", "currency"],
    'sports': ["sport", "game", "team", "match", "cup", "win", "loss", "score", "olympic", "championship", "league", "player", "coach", "football", "soccer", "baseball", "basketball", "tennis", "golf", "cricket", "racing", "f1", "medal", "athlete", "stadium", "tournament", "club", "nba", "nfl", "fifa", "uefa", "rugby", "boxing", "hockey"],
    'sci_tech': ["technology", "science", "computer", "internet", "software", "web", "space", "nasa", "research", "study", "mobile", "phone", "apple", "google", "microsoft", "chip", "robot", "gadget", "discovery", "experiment", "biology", "physics", "astronomy", "launch", "satellite", "online", "digital", "data", "cyber", "virus", "hacker", "facebook", "amazon", "intel", "linux", "browser"],
    'world': ["world", "war", "peace", "government", "president", "minister", "election", "military", "army", "police", "attack", "bomb", "blast", "protest", "court", "law", "treaty", "united nations", "obama", "bush", "clinton", "putin", "trump", "iraq", "afghanistan", "iran", "korea", "syria", "gaza", "israel", "palestinians", "official", "leader", "party", "vote", "congress", "senate", "parliament", "terrorism", "diplomat", "nuclear", "eu", "european union", "brexit", "prime minister"]
}

count_by_year = {y: 0 for y in range(2010, 2021)}
processed_count = 0
business_count = 0

for art in articles_list:
    aid = str(art['article_id'])
    if aid in meta_dict:
        processed_count += 1
        text = (str(art.get('title', '')) + " " + str(art.get('description', ''))).lower()
        
        scores = {k: 0 for k in cats}
        tokens = re.findall(r'\w+', text)
        
        for token in tokens:
            for cat, kws in cats.items():
                if token in kws:
                    scores[cat] += 1
        
        # Tie-breaking logic: 
        # If business has score, prefer it if it's >= others?
        # Or strict max.
        # "Google IPO" -> Google (Tech), IPO (Business). Tie.
        # Usually IPO is Business news.
        # "Oil prices" -> Oil (Business), Prices (Business).
        # "Oil war" -> Oil (Business), War (World). Tie.
        # Let's verify max logic.
        
        if sum(scores.values()) > 0:
            best_cat = max(scores, key=scores.get)
            
            # Tie breaker: if tie between Business and others, what to do?
            # Standard max() returns the first occurrence of max value.
            # Dict order depends on insertion. 
            # Insertion order: Business, Sports, SciTech, World.
            # So if Business ties with others, Business wins.
            
            if best_cat == 'business':
                y = meta_dict[aid]
                if 2010 <= y <= 2020:
                    count_by_year[y] += 1
                    business_count += 1

avg = sum(count_by_year.values()) / 11.0

print("__RESULT__:")
print(json.dumps({
    "average": avg, 
    "counts": count_by_year, 
    "processed": processed_count,
    "total_business": business_count
}))"""

env_args = {'var_function-call-14838360778106258720': 'file_storage/function-call-14838360778106258720.json', 'var_function-call-10623188398356643492': {'count': 14860, 'sample_ids': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63']}, 'var_function-call-1633174315725084248': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11527900083983285698': {'average': 0.09090909090909091, 'counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}}, 'var_function-call-2425371894314014899': {'meta_count': 14860, 'articles_count': 5, 'intersection_count': 1, 'sample_meta_ids': ['6818', '97290', '36159', '20123', '95019'], 'sample_article_ids': ['2', '4', '0', '1', '3']}, 'var_function-call-522906220509130476': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-1196445325152998757': 'file_storage/function-call-1196445325152998757.json'}

exec(code, env_args)
