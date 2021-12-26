from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
import requests
import json

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/team", methods=["GET", "POST"])
def team():
    if request.method == "GET":
        player_info = "https://www.balldontlie.io/api/v1/teams"

        response = requests.get(url = player_info).json()

        imgs = ["https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612751/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612741/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612739/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612742/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612743/global/L/logo.svg",
                "https://cdn.worldvectorlogo.com/logos/detroit-pistons-4.svg","https://cdn.nba.com/logos/nba/1610612744/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612745/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612754/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612746/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612747/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612763/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612748/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612749/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612750/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612740/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612752/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612760/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612753/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612755/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612756/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612757/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612758/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612759/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612761/global/L/logo.svg",
                "https://cdn.nba.com/logos/nba/1610612762/global/L/logo.svg","https://cdn.nba.com/logos/nba/1610612764/global/L/logo.svg"]

        teams = []

        for i in range(response['meta']['total_count']):
            player_team = response['data'][i]['abbreviation']
            teams.append(player_team)

        return render_template("teams.html", teams=teams, imgs=imgs)
    else:
        team = request.form.get("teams")
        if not team:
            flash("You must select a team!")
            return redirect("/team")
        if team == "ATL":
            img = "https://cdn.nba.com/logos/nba/1610612737/global/L/logo.svg"
            img2 = "https://cdn.wegow.com/media/venues/state-farm-arena/state-farm-arena-1634221655.8113344.jpg"
            ph = "State Farm Arena"
        elif team == "BOS":
            img = "https://cdn.nba.com/logos/nba/1610612738/global/L/logo.svg"
            img2 = "https://antsize.files.wordpress.com/2014/07/td-garden.jpg"
            ph = "TD Garden"
        elif team == "BKN":
            img = "https://cdn.nba.com/logos/nba/1610612751/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/BarclayCenter-2_%2848034233762%29.jpg/1200px-BarclayCenter-2_%2848034233762%29.jpg"
            ph = "Barclays Center"
        elif team == "CHA":
            img = "https://cdn.nba.com/logos/nba/1610612766/global/L/logo.svg"
            img2 = "https://www.spectrumcentercharlotte.com/assets/img/Spectrum_Center_TradeSt_Slide-b25a4c749a.jpg"
            ph = "Spectrum Center"
        elif team == "CHI":
            img = "https://cdn.nba.com/logos/nba/1610612741/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/4/47/United_Center_060716.jpg"
            ph = "United Center"
        elif team == "CLE":
            img = "https://cdn.nba.com/logos/nba/1610612739/global/L/logo.svg"
            img2 = "https://sporttechie-prod.s3.amazonaws.com/rocket-mortgage-fieldhouse-exterior-1500x1000.png"
            ph = "Rocket Mortgage FieldHouse"
        elif team == "DAL":
            img = "https://cdn.nba.com/logos/nba/1610612742/global/L/logo.svg"
            img2 = "https://visitdallas-sv.imgix.net/c_fit,w_800,h_600/crm/dallas/AAC1_00c413cc-b050-48c3-83143c9df378c04b.jpg?w=800&h=600&fit=fill&crop=edges,faces&q=60&fm=pjpg&dpr=3&auto=compress,format,redeye&trim=auto"
            ph = "American Airlines Center"
        elif team == "DEN":
            img = "https://cdn.nba.com/logos/nba/1610612743/global/L/logo.svg"
            img2 = "https://www.denverpost.com/wp-content/uploads/2019/08/4805989.jpg"
            ph = "Ball Arena"
        elif team == "DET":
            img = "https://cdn.worldvectorlogo.com/logos/detroit-pistons-4.svg"
            img2 = "https://www.giffelswebster.com/wp-content/uploads/2018/09/little-caesars.jpg"
            ph = "Little Caesars Arena"
        elif team == "GSW":
            img = "https://cdn.nba.com/logos/nba/1610612744/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/c/c4/Chase_Center_2019.jpg"
            ph = "Chase Center"
        elif team == "HOU":
            img = "https://cdn.nba.com/logos/nba/1610612745/global/L/logo.svg"
            img2 = "https://populous.com/wp-content/uploads/2018/01/POP_00_0653_00_N56_medium.jpg"
            ph = "Toyota Center"
        elif team == "IND":
            img = "https://cdn.nba.com/logos/nba/1610612754/global/L/logo.svg"
            img2 = "https://www.gannett-cdn.com/presto/2021/09/28/PIND/dd91186f-cb8a-42e3-953d-2763c5304019-2021_0922_Penn_GAINBRIDGE.jpeg?crop=3823,2151,x0,y0&width=3200&height=1801&format=pjpg&auto=webp"
            ph = "Gainbridge Fieldhouse"
        elif team == "LAC":
            img = "https://cdn.nba.com/logos/nba/1610612746/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/e/e3/Staples_Center%2C_LA%2C_CA%2C_jjron_22.03.2012.jpg"
            ph = "Staples Center"
        elif team == "LAL":
            img = "https://cdn.nba.com/logos/nba/1610612747/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/e/e3/Staples_Center%2C_LA%2C_CA%2C_jjron_22.03.2012.jpg"
            ph = "Staples Center"
        elif team == "MEM":
            img = "https://cdn.nba.com/logos/nba/1610612763/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/FedExForum.jpg/1200px-FedExForum.jpg"
            ph = "FedExCenter"
        elif team == "MIA":
            img = "https://cdn.nba.com/logos/nba/1610612748/global/L/logo.svg"
            img2 = "https://assets.simpleviewinc.com/simpleview/image/upload/c_fit,w_1440,h_900/crm/miamifl/AAArena_Miami_Heat_exterior_day_1440x9000-cb3417e25056a36_cb3418eb-5056-a36a-0b180fd96272dd26.jpg"
            ph = "FTX Arena"
        elif team == "MIL":
            img = "https://cdn.nba.com/logos/nba/1610612749/global/L/logo.svg"
            img2 = "https://www.fiservforum.com/assets/img/fiserv-forum-tours-190321-93fb6c42c4.jpg"
            ph= "Fiserv Forum"
        elif team == "MIN":
            img = "https://cdn.nba.com/logos/nba/1610612750/global/L/logo.svg"
            img2 = "https://www.nba.com/timberwolves/sites/timberwolves/files/171016_targetcenter_s_060.jpg"
            ph = "Target Center"
        elif team == "NOP":
            img = "https://cdn.nba.com/logos/nba/1610612740/global/L/logo.svg"
            img2 = "https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,h_1200,q_75,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/neworleans/1_72F6311E-227D-44FE-BBA9CAB1B7B04BD5_21eda2bb-4960-4109-8ac6a6596ec9f8ac.jpg"
            ph = "Smoothie King Center"
        elif team == "NYK":
            img = "https://cdn.nba.com/logos/nba/1610612752/global/L/logo.svg"
            img2 = "https://cdn.pixabay.com/photo/2020/03/31/03/41/nyc-4986116_1280.jpg"
            ph = "Madison Square Garden"
        elif team == "OKC":
            img = "https://cdn.nba.com/logos/nba/1610612760/global/L/logo.svg"
            img2 = "https://image.cnbcfm.com/api/v1/image/106917098-1627334645367-paycomcenter_roof_night-1.jpg?v=1627334826"
            ph = "Paycom Center"
        elif team == "ORL":
            img = "https://cdn.nba.com/logos/nba/1610612753/global/L/logo.svg"
            img2 = "https://i1.wp.com/www.laemorlando.com/wp-content/uploads/2019/02/amway-center-externo.jpg?fit=1200%2C675&ssl=1"
            ph = "Amway Center"
        elif team == "PHI":
            img = "https://cdn.nba.com/logos/nba/1610612755/global/L/logo.svg"
            img2 = "https://images2.minutemediacdn.com/image/fetch/w_2000,h_2000,c_fit/https%3A%2F%2Fbroadstreetbuzz.com%2Fwp-content%2Fuploads%2Fgetty-images%2F2020%2F07%2F1254856609.jpeg"
            ph = "Wells Fargo Center"
        elif team == "PHX":
            img = "https://cdn.nba.com/logos/nba/1610612756/global/L/logo.svg"
            img2 = "https://image.cnbcfm.com/api/v1/image/106912094-1626446661133Phoenix-Suns-Mercury-x-Footprint-jpg?v=1626463246"
            ph = "Footprint Center"
        elif team == "POR":
            img = "https://cdn.nba.com/logos/nba/1610612757/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/RoseGardenArenaS.jpg/1200px-RoseGardenArenaS.jpg"
            ph = "Moda Center"
        elif team == "SAC":
            img = "https://cdn.nba.com/logos/nba/1610612758/global/L/logo.svg"
            img2 = "https://www.golden1center.com/assets/img/IMG_6664-8a16984e98.jpg"
            ph = "Golden 1 Center"
        elif team == "SAS":
            img = "https://cdn.nba.com/logos/nba/1610612759/global/L/logo.svg"
            img2 = "https://304ljw4amcep3ali496xph6b-wpengine.netdna-ssl.com/wp-content/uploads/2019/05/ATT-center-SF-20160330_DIG_2708_MAS-1900-1600x1069.jpg"
            ph = "AT&T Center"
        elif team == "TOR":
            img = "https://cdn.nba.com/logos/nba/1610612761/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/5/57/Scotiabank_Arena_-_2018_%28cropped%29.jpg"
            ph = "Scotiabank Arena"
        elif team == "UTA":
            img = "https://cdn.nba.com/logos/nba/1610612762/global/L/logo.svg"
            img2 = "https://assets.simpleviewinc.com/simpleview/image/fetch/c_limit,h_1200,q_75,w_1200/https://assets.simpleviewinc.com/simpleview/image/upload/crm/saltlake/VSM0-b706a4cf5056a36_b706a7a5-5056-a36a-0648f9c6e260f33b.jpg"
            ph = "Vivint Arena"
        elif team == "WAS":
            img = "https://cdn.nba.com/logos/nba/1610612764/global/L/logo.svg"
            img2 = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Verizon_Center_wide.jpg/1200px-Verizon_Center_wide.jpg"
            ph = "Capital One Arena"

        info = "https://www.balldontlie.io/api/v1/teams"
        response = requests.get(url = info).json()
        data = []
        for i in range(30):
            if response['data'][i]['abbreviation'] == team:
                data.append(response['data'][i])
        print(data)
        return render_template("team.html", team = team, data=data, img=img , img2=img2, ph=ph)

@app.route("/players", methods=["GET", "POST"])
def players():
    if request.method == "POST":
        if not request.form.get("first").strip() or not request.form.get("surname").strip():
            flash("You must insert all the data!")
            return redirect("/players")
        first = request.form.get("first").lower().strip()
        surname = request.form.get("surname").lower().strip()
        try:
            info = "https://www.balldontlie.io/api/v1/players?search=" + first
            response = requests.get(url = info).json()
        except ValueError:
            flash("Error!")
            return redirect("/players")
        data = []
        for i in range(1, response["meta"]["total_pages"] + 1):
            response_2 = requests.get(url = "https://www.balldontlie.io/api/v1/players?search=" + first + "&page=" + str(i)).json()
            print(i)
            if response_2["meta"]["per_page"] < response_2["meta"]["total_count"]:
                for k in range(response_2["meta"]["per_page"]):
                    try:
                        if response_2["data"][k]["first_name"].lower() == first and response_2["data"][k]["last_name"].lower() == surname:
                            data.append(response_2["data"][k])
                        if len(data) > 0:
                            break
                    except IndexError:
                        break
            else:
                for k in range(response_2["meta"]["total_count"]):
                    if response_2["data"][k]["first_name"].lower() == first and response_2["data"][k]["last_name"].lower() == surname:
                        data.append(response_2["data"][k])
                    if len(data) > 0:
                        break
        if data == []:
            flash("Non existing player!")
            return redirect("/players")
        name = data[0]['first_name']
        last = data[0]['last_name']
        team = data[0]['team']['abbreviation']
        return render_template("info_players.html", data=data, name=name, last=last, team=team)
    else:
        return render_template("players.html")

@app.route("/games", methods=["GET", "POST"])
def games():
    if request.method == "POST":
        season = request.form.get("season")
        home = request.form.get("visited")
        away = request.form.get("visitor")
        date = request.form.get("date")
        if not home or not away or not season or not date:
            flash("You must insert all the data!")
            return redirect("/games")
        if home == away:
            flash("Home team and Away team cannot be the same!")
            return redirect("/games")
        try:
            info = "https://www.balldontlie.io/api/v1/games?seasons[]=" + season + "&dates[]=" + date
            response = requests.get(url = info).json()
        except ValueError:
            flash("Error!")
            return redirect("/games")
        data = []
        if home and away and season and date:
            for i in range(1, response["meta"]["total_pages"] + 1):
                response_2 = requests.get(url = "https://www.balldontlie.io/api/v1/games?seasons[]=" + season + "&dates[]=" + date + "&page=" + str(i)).json()
                if response_2["meta"]["per_page"] > response_2["meta"]["total_count"]:
                    for k in range(response_2['meta']['total_count']):
                        if response_2['data'][k]['home_team']['abbreviation'] == home and response_2['data'][k]['visitor_team']['abbreviation'] == away:
                            response_2['data'][k]['date'] = response_2['data'][k]['date'].replace('T00:00:00.000Z','')
                            data.append(response_2['data'][k])
                        if len(data) > 0:
                            break
                else:
                    for k in range(response_2['meta']['per_page']):
                        if response_2['data'][k]['home_team']['abbreviation'] == home and response_2['data'][k]['visitor_team']['abbreviation'] == away:
                            response_2['data'][k]['date'] = response_2['data'][k]['date'].replace('T00:00:00.000Z','')
                            data.append(response_2['data'][k])
                        if len(data) > 0:
                            break
        if len(data) == 0:
            flash("Non existing game!")
            return redirect("/games")
        return render_template("info_games.html", data = data)
    else:
        player_info = "https://www.balldontlie.io/api/v1/teams"
        response = requests.get(url = player_info).json()
        teams = []
        for i in range(response['meta']['total_count']):
            player_team = response['data'][i]['abbreviation']
            teams.append(player_team)
        return render_template("games.html", teams=teams)

@app.route("/stats", methods=["GET","POST"])
def stats():
    if request.method == "POST":
        id = request.form.get("id")
        name = request.form.get("first")
        last = request.form.get("surname")
        if not id or not name or not last:
            flash("You must insert all the data!")
            return redirect("/stats")
        try:
            info = "https://www.balldontlie.io/api/v1/stats?game_ids[]=" + id + "&per_page=30"
            response = requests.get(url = info).json()
        except ValueError:
            flash("Error!")
            return redirect("/stats")
        data = []
        for i in range(response['meta']['total_count']):
            if response['data'][i]['player']['first_name'].lower() == name.lower().strip() and response['data'][i]['player']['last_name'].lower() == last.lower().strip():
                data.append(response['data'][i])
                name = response['data'][i]['player']['first_name']
                last = response['data'][i]['player']['last_name']
        if len(data) == 0:
            flash("Invalid Stats!")
            return redirect("/stats")
        return render_template("info_stats.html", data = data, name = name, last = last)
    else:
        return render_template("stats.html")

@app.route("/games1", methods=["GET", "POST"])
def games1():
    if request.method == "POST":
        team = request.form.get("team")
        season = request.form.get("season")
        if not team or not season:
            flash("You must insert all the data!")
            return redirect("/games1")
        response_id = requests.get(url = "https://www.balldontlie.io/api/v1/teams").json()
        for i in range(response_id["meta"]["total_count"]):
            if response_id["data"][i]["abbreviation"] == team:
                id = response_id["data"][i]["id"]
        data = []
        response = requests.get(url = "https://www.balldontlie.io/api/v1/games?seasons[]=" + season + "&team_ids[]=" + str(id) + "&per_page=100").json()
        for i in range(response['meta']['total_count']):
            response['data'][i]['date'] = response['data'][i]['date'].replace('T00:00:00.000Z','')
            data.append(response['data'][i])
        if len(data) == 0:
            flash("Invalid Form!")
            return redirect("/games1")
        return render_template("info_games1.html", data=data)
    else:
        player_info = "https://www.balldontlie.io/api/v1/teams"
        response = requests.get(url = player_info).json()
        teams = []
        for i in range(response['meta']['total_count']):
            player_team = response['data'][i]['abbreviation']
            teams.append(player_team)
        return render_template("games1.html", teams=teams)

@app.route("/games2", methods=["GET", "POST"])
def games2():
    if request.method == "POST":
        date = request.form.get("date")
        if not date:
            flash("You must insert all the data!")
            return redirect("/games2")
        try:
            response = requests.get(url = "https://www.balldontlie.io/api/v1/games?dates[]=" + date).json()
        except ValueError:
            flash("Error!")
            return redirect("/games2")
        data = []
        for i in range(response['meta']['total_count']):
            response['data'][i]['date'] = response['data'][i]['date'].replace('T00:00:00.000Z','')
            data.append(response['data'][i])
        if len(data) == 0:
            flash("There are no games on that date!")
            return render_template("games2.html")
        return render_template("info_games2.html", data=data)
    else:
        return render_template("games2.html")

@app.route("/season_stats", methods=["GET","POST"])
def season_stats():
    if request.method == "POST":
        if not request.form.get("season") or not request.form.get("id"):
            flash("You must insert all the data!")
            return redirect("/season_stats")
        try:
            response = requests.get(url = "https://www.balldontlie.io/api/v1/season_averages?season=" + request.form.get('season') + "&player_ids[]=" + request.form.get('id')).json()
            data = []
        except ValueError:
            flash("Error!")
            return redirect("/season_stats")
        if len(response['data']) == 0:
            flash("Non-existing stats")
            return render_template("season_stats.html")
        data.append(response['data'][0])
        response_2 = requests.get(url = "https://www.balldontlie.io/api/v1/players/" + request.form.get('id')).json()
        name = response_2['first_name']
        last = response_2['last_name']
        team = response_2['team']['abbreviation']
        return render_template("season_showed.html", data=data, name=name, last=last, team=team)
    else:
        return render_template("season_stats.html")
