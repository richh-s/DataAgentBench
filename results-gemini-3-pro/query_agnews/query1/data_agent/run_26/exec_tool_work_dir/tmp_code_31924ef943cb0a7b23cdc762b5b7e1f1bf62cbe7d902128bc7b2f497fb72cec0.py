code = """import json

# Load the file
file_path = locals()['var_function-call-9779383998375679082']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
keywords = {
    "Sports": ["sport", "baseball", "basketball", "football", "soccer", "tennis", "golf", "hockey", "olympic", "medal", "athlete", "championship", "tournament", "league", "team", "coach", "game", "match", "score", "win", "victory", "defeat", "cup", "nfl", "nba", "mlb", "nhl", "fifa", "racing", "f1", "nascar", "rugby", "cricket", "boxing", "wrestling", "swimming", "marathon", "stadium", "espn", "driver", "rider", "squad", "club", "athens", "games"],
    "Business": ["market", "stock", "price", "company", "business", "economy", "trade", "profit", "bank", "dollar", "oil", "invest", "share", "finance", "corporate", "industry", "revenue", "sales", "ceo", "merger", "acquisition", "inflation", "rate", "fed", "reserve", "wall", "street", "dow", "nasdaq", "euro", "yen", "yuan"],
    "Sci/Tech": ["computer", "software", "technology", "internet", "web", "google", "microsoft", "apple", "linux", "virus", "security", "space", "nasa", "phone", "mobile", "digital", "online", "network", "science", "research", "lab", "processor", "chip", "intel", "amd", "server", "browser"],
    "World": ["president", "minister", "prime", "country", "war", "peace", "iraq", "israel", "palestine", "afghanistan", "iran", "un", "united nations", "government", "official", "election", "vote", "military", "army", "police", "blast", "attack", "kill", "die", "bomb", "explosion", "terror", "troops", "nuclear", "senate", "congress", "parliament", "democrat", "republican", "bush", "kerry", "candidate", "campaign", "poll", "voter", "party", "law", "court", "justice"]
}

candidates = []

for article in articles:
    text = (article.get('title', '') + " " + article.get('description', '')).lower()
    
    scores = {cat: 0 for cat in keywords}
    for cat, words in keywords.items():
        for word in words:
            if word in text:
                scores[cat] += 1
    
    # Check if Sports score is non-zero
    if scores["Sports"] > 0:
        candidates.append({
            "article": article,
            "scores": scores,
            "len": len(article.get('description', ''))
        })

# Sort by length
candidates.sort(key=lambda x: x['len'], reverse=True)

# Print top 10 candidates with their scores
top_10 = []
for c in candidates[:10]:
    top_10.append({
        "title": c['article']['title'],
        "len": c['len'],
        "scores": c['scores'],
        "preview": c['article']['description'][:50]
    })

print("__RESULT__:")
print(json.dumps(top_10))"""

env_args = {'var_function-call-6833759783790572362': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-6833759783790573323': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}], 'var_function-call-17617418666776808318': ['articles'], 'var_function-call-17617418666776809305': ['authors', 'article_metadata'], 'var_function-call-824548603619282537': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694476c261590ca75deef376', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694476c261590ca75deef377', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694476c261590ca75deef378', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694476c261590ca75deef379', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-18427185302018865351': [{'_id': '694476c261590ca75deef375', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694476c261590ca75deef376', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694476c261590ca75deef377', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694476c261590ca75deef378', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694476c261590ca75deef379', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4260440268981957139': 'file_storage/function-call-4260440268981957139.json', 'var_function-call-9779383998375679082': 'file_storage/function-call-9779383998375679082.json', 'var_function-call-6585599168967989728': {'title': '2004 US Senate Outlook', 'description_length': 944, 'description_preview': 'With all the hoopla over Bush and Kerry, some of y'}, 'var_function-call-14177394142800639821': [{'title': 'The Rundown', 'len': 841, 'desc': "4 Miami at N.C. State &lt;em&gt;7:45 p.m., ESPN &lt;/em&gt;&lt;br&gt;Think the Wolfpack is kicking itself for that loss two weeks ago at North Carolina? You bet. Had N.C. State (4-2, 3-1 ACC) won that one, this would be for sole possession of first place in the ACC. As it is, this is a chance for the Wolfpack to show it belongs in the upper echelon of the restructured league -- which, for now, is Miami, Florida State, and a cesspool of also-rans. The Wolfpack's defense is the best in the nation against the pass (97.5 yards per game) and overall (203.7). It will have to shut down a rejuvenated Brock Berlin, who threw for 308 yards last week against Louisville, his most in 13 games. Key for N.C. State: Will perpetually banged-up tailback T.A. McLendon -- a game-time decision because of a bad hamstring -- be able to run effectively?"}, {'title': 'Cavaliers, Hokies Play Host', 'len': 773, 'desc': "Akron at No. 12 Virginia &lt;br&gt;   Where:  Scott Stadium, Charlottesville&lt;br&gt;   When:  3 p.m.    Radio:  WTNT-570    Tickets:  Sold out &lt;br&gt;   Another Top QB:  Like North Carolina's Darian Durant last week, Akron quarterback Charlie Frye is the key to his team's slim chances of upsetting the Cavaliers. The 6-foot-4 senior, likened by Virginia Coach Al Groh to recent ACC stars Matt Schaub and Philip Rivers, ranks fourth among active NCAA quarterbacks with 9,048 career passing yards. In losses the past two weeks to Penn State and Middle Tennessee, Frye completed 60 of 80 passes for 622 yards. Weather permitting, he will present a challenge for an inexperienced Virginia secondary that made a few too many errors in deep coverage in its first two games."}, {'title': 'Area College Football Capsules', 'len': 761, 'desc': 'Navy at Tulsa &lt;br&gt;   Where:  Skelly Stadium    When:  7 p.m. &lt;br&gt;   Shooting for 3-0:  Navy is off to its first 2-0 start since 1996. The Midshipmen haven\'t started 3-0 since 1979, when they won their first six games and finished 7-4. Navy has started 3-0 only twice in the past 40 years -- the 1978 team won its first seven games. Tulsa, which improved from 1-11 in 2002 to 8-5 last season, the best turnaround in college football, has lost its first two games, 21-3 at Kansas and 38-21 at Oklahoma State. Going 3-0 "would be a great start, and it would be a great beginning to achieve the goals that they\'ve set for themselves," Navy Coach Paul Johnson said. "It\'s not going to make the season if we win, and it\'s not going to kill it if we lose."'}]}

exec(code, env_args)
