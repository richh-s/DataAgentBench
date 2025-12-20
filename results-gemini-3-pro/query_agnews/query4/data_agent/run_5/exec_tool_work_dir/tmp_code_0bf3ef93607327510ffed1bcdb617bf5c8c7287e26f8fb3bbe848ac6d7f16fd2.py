code = """import json
import collections
import re

# Load metadata
with open(locals()['var_function-call-1474084106243643964'], 'r') as f:
    metadata_list = json.load(f)

metadata = {str(row['article_id']): row['region'] for row in metadata_list}

# Load articles
with open(locals()['var_function-call-307996040387554200'], 'r') as f:
    articles = json.load(f)

# Keywords
categories = {
    "Sports": ["sport", "sports", "football", "soccer", "baseball", "basketball", "hockey", "tennis", "golf", "rugby", "cricket", "league", "team", "game", "match", "cup", "tournament", "championship", "olympic", "olympics", "nfl", "nba", "mlb", "nhl", "fifa", "uefa", "athlete", "player", "coach", "score", "win", "won", "lose", "lost", "defeat", "victory", "medal", "stadium"],
    "Business": ["business", "economy", "economic", "market", "stock", "stocks", "trade", "trading", "financial", "finance", "bank", "banking", "money", "dollar", "currency", "euro", "yen", "yuan", "invest", "investment", "investor", "company", "corp", "corporation", "inc", "firm", "profit", "revenue", "earnings", "sales", "deal", "merger", "acquisition", "ipo", "oil", "price", "prices", "cost", "rate", "rates", "inflation", "tax", "fed", "federal reserve", "ceo", "manager", "executive", "dow", "nasdaq", "wall street", "fund", "funds", "pension", "airline", "airways", "retail", "retailer", "store", "shop", "loss", "losses", "quarter", "quarterly", "growth", "grow", "job", "jobs", "hiring", "unemployment", "labor", "union", "workforce"],
    "Sci/Tech": ["science", "technology", "tech", "computer", "software", "hardware", "internet", "web", "online", "digital", "mobile", "phone", "smartphone", "app", "google", "apple", "microsoft", "ibm", "intel", "facebook", "amazon", "nasa", "space", "astronomy", "galaxy", "planet", "mars", "moon", "robot", "ai", "artificial intelligence", "cyber", "virus", "hacker", "biology", "physics", "chemistry", "study", "research", "scientist", "cancer", "drug", "medical", "health", "disease"],
    "World": ["world", "international", "politics", "political", "government", "president", "minister", "prime", "parliament", "congress", "senate", "election", "vote", "poll", "democracy", "diplomat", "diplomacy", "treaty", "summit", "un", "united nations", "eu", "european union", "nato", "war", "military", "army", "navy", "air force", "troops", "soldier", "rebel", "insurgent", "guerrilla", "terrorist", "terrorism", "attack", "bomb", "blast", "explosion", "kill", "killed", "death", "dead", "injure", "wound", "casualty", "conflict", "crisis", "refugee", "migrant", "immigration", "border", "police", "court", "law", "justice", "prison", "jail", "protest", "riot", "demonstration", "strike", "disaster", "earthquake", "tsunami", "hurricane", "typhoon", "storm", "flood", "drought", "famine", "iraq", "iran", "syria", "afghanistan", "pakistan", "israel", "palestine", "gaza", "ukraine", "russia", "china", "north korea", "sudan", "congo", "nigeria", "somalia", "libya", "yemen", "korea", "ebola", "zika", "climate", "warming", "agreement", "paris"]
}

africa_world = []
sa_world = []

for art in articles:
    aid = str(art['article_id'])
    if aid in metadata:
        region = metadata[aid]
        title = art.get('title', '') or ''
        desc = art.get('description', '') or ''
        text = (title + " " + desc).lower()
        
        tokens = re.findall(r'\w+', text)
        scores = {cat: 0 for cat in categories}
        for token in tokens:
            for cat, keywords in categories.items():
                if token in keywords:
                    scores[cat] += 1
        
        if any(scores.values()):
            max_score = max(scores.values())
            candidates = [c for c, s in scores.items() if s == max_score]
            if "Sports" in candidates: best_cat = "Sports"
            elif "Business" in candidates: best_cat = "Business"
            elif "Sci/Tech" in candidates: best_cat = "Sci/Tech"
            elif "World" in candidates: best_cat = "World"
            else: best_cat = candidates[0]
            
            if best_cat == "World":
                if region == "Africa":
                    africa_world.append(title)
                elif region == "South America":
                    sa_world.append(title)

result = {
    "Africa World Examples (10)": africa_world[:10],
    "South America World Examples (10)": sa_world[:10]
}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1474084106243643964': 'file_storage/function-call-1474084106243643964.json', 'var_function-call-9489092853522118579': 'file_storage/function-call-9489092853522118579.json', 'var_function-call-17105952885415197022': [{'_id': '6944ed7c4e8b2b9e56808f77', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944ed7c4e8b2b9e56808f78', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944ed7c4e8b2b9e56808f79', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944ed7c4e8b2b9e56808f7a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944ed7c4e8b2b9e56808f7b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17682266178667585365': 6696, 'var_function-call-6775491050414127677': 'file_storage/function-call-6775491050414127677.json', 'var_function-call-4705261762392207793': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-7653748084012222185': 'file_storage/function-call-7653748084012222185.json', 'var_function-call-307996040387554200': 'file_storage/function-call-307996040387554200.json', 'var_function-call-10776620088862522512': {'region_counts': {'South America': 405, 'Europe': 384, 'Asia': 382, 'North America': 405, 'Africa': 401}, 'max_region': 'South America', 'max_val': 405, 'total_world_articles': 1977}, 'var_function-call-8616967207663749962': {'region_counts': {'Europe': 319, 'Asia': 313, 'North America': 329, 'Africa': 338, 'South America': 337}, 'max_region': 'Africa', 'max_val': 338, 'total_world_articles': 1636}, 'var_function-call-1828487101150339793': {'Africa World Examples': ["'Mock executions' for UK hostage", 'China Typhoon Death Toll Rises; 40 Missing (AP)', 'For the record', 'US Air to Seek 5-Year Extension for Pension Fund Payments', 'Downer to begin nuclear talks'], 'South America World Examples': ['Karzai likely to visit Pakistan next week', 'Poll: Kerry Continues to Hold Edge in Pa. (AP)', 'S.Korea #39;s Ruling Party Head Resigns on Father #39;s Past', 'THE HOUR: When Time Isn #39;t on Israel #39;s Side', "Iraq's Sistani Leaves London Hospital After Operation"], 'Africa Business Examples': ['Stocks Sharply Higher on Dip in Oil Prices', 'Fall Season Looks Solid for Retailers, but Holidays Could Be Another Story', "N Korea food prices 'rocket'", "Dillard's Posts Narrower 2nd-Quarter Loss (Reuters)", 'Sprint begins \\$3 billion march to 3G']}, 'var_function-call-123681174138458031': {'region_counts': {'Europe': 310, 'Asia': 307, 'North America': 323, 'Africa': 330, 'South America': 331}, 'max_region': 'South America', 'max_val': 331, 'total': 1601}, 'var_function-call-72417473031094308': {'Europe': 1357, 'South America': 1332, 'Africa': 1345, 'Asia': 1333, 'North America': 1329}, 'var_function-call-15290285311598642316': {'region_counts': {'South America': 340, 'Europe': 315, 'Asia': 314, 'North America': 328, 'Africa': 337}, 'max_region': 'South America', 'max_val': 340, 'total': 1634}}

exec(code, env_args)
