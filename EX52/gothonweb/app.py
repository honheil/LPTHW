from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map
import got

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('option.html')

@app.route('/game/1', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        return render_template('you_died.html')


@app.route('/game/1', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            return render_template('you_died.html')

        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('you_died.html')

            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('you_died.html')

@app.route('/game1/start')
def start():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get'))

@app.route('/game/2', methods=['GET']) 
def game_get_2():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        return render_template('you_died.html')


@app.route('/game/2', methods=['POST'])
def game_post_2():
    userinput = request.form.get('userinput_2')
    if 'scene' in session:
        if userinput is None:
            return render_template('you_died.html')

        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                return render_template('you_died.html')

            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        return render_template('you_died.html')

@app.route('/game2/start')
def start_2():
    session['scene'] = map.start.urlname
    return redirect(url_for('game_get_2'))

@app.route('/userdata', methods=['POST'])
def userdata():
    userdata = request.form.get('userdata')
    userlist = ['unknown']; # I tried to apply this like {{userlist}} in html but it doesnt work
    userlist.append( userdata );
    userlist.sort();
    return render_template('userdata.html')

app.secret_key = 'terrencelhh429'

if __name__ == "__main__":
    app.run()
