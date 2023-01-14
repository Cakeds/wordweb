from flask import Flask, render_template, request, redirect


app=Flask(__name__)


words=[
    {'id':1, 'english':'Pneumonoultramicroscopicsilicovolcanoconiosis', 'korea':'규성진폐증'},
    {'id':2, 'english':'Floccinaucinihilipilification', 'korea':'경시함'},
    {'id':3, 'english':'hippopotomonstrosesquippedaliophobia', 'korea':'긴 단어에 대한 공포증'},
    {'id':4, 'english':'MethionylglutaminylarginytyrosylglutamylserylleucylphenylalanylalanylglutaminylleucyllysylglutamylarginyllysylglutamylglycylalanylphenylalanyvalylprolylphenylalanylvalythreonylleucylglycylaspartylprolyglycylisoleucylglutamylglutaminylserylleucyllysylisoleucylaspartylthreonylleucylisoleucylglutamylalanylglycylalanylaspartylalanylleucylglutamylleucylglycylglycylisoleucylprolylphenylalanylserylspartylprolylleucelalanylaspartyglycylprolythreonylisoleucylglutamiylasparaginylalanylthreonylleucylarginylalanylphenylalanylalanylglycylvalyltheonylprolylalanylglutaminylcysteinylphenylalanygllutamylmethionylleucyalanylleucylisoleucylarginylglutaminyllysylhistidylprolylthreonylisoleucylpriIylisoleucylglycylleucylleucylmethionyltyrosylalanylasparaginylleucylvalyphenylalanycyoleucylaspartylglutamylphenylalanyltysylalanylgutaminyllcysteinylglutamyllysylvalylglycylavlylaspartylserylvalylleucylvalylalanylaspartylvalyprolylvalylglutaminylglutamyllserylalanyprolyphenylalanylarginylglutaminylalanylalanylleucylargihistidylasparaginylvaylalanylprolylisoleucylphenylalanylisoleucylcysteinylprolylprolylaspartylalanylaspartylaspartylaspartylleucylleucylarginyglutaminylisoleucylalanyylseryltyrosylglycylarginylglycyltyrosylthreonyltyrsylleucylleucylserylarginylalanylglycylvalythreonylglycylalanylglutamylasparaginylarginylanylalanylleucylprolylleucylaspaaginylhistidylleucylvaylalanyllysylleucyllysylglutamyltyrosylasaraginylglycylphenylalanylglycylisoleucylalanylprolylaspartylglutaminylvalyllysylalanylalanylisoleucylaspartylalanylalanyglycylalanylalanyglycylalanylisoleucylserylglycyserylalanylisoleucylbalyllsylisoleucylisoleucylglutamyyylglutaminylhistidylasparaginylisoleucylglutamylprolyglutamyllysylmethionylleucylalanylalanylleucyllysylvalylphenylalabylvalylglutaminlylprolylmethionyllysylalanylalanylthreonylarginylserine', 'korea':'트리토판'},
    {'id':5, 'english':'Apple', 'korea':'핸드폰'}
]
nextid=len(words)+1

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list/')
def list():
    return render_template('list.html', word_list=words)

@app.route('/word/<int:id>/')
def read(id):
    english=""
    korea=""
    for word in words:
        if id == word["id"]:
            english = word['english']
            korea = word['korea']
            break

    return render_template('word.html', id=id, english=english, korea=korea)

@app.route('/new/')
def create():
    return render_template('create.html', word_list=words)

@app.route('/create/', methods=['POST'])
def post_create():
    global nextid
    english = request.form['english']
    korea = request.form['korea']
    newword = {'id': nextid, 'english': english, 'korea': korea}
    words.append(newword)
    nextid += 1
    return redirect('/word/{}/'.format(newword['id'])) 



@app.route('/modify/<int:id>/')
def update():
    english=""
    korea=""
    for word in words:
        if id == word["id"]:
            english = word['english']
            korea = word['korea']
            break
    return render_template('update.html', id=id, english=english, korea=korea)


app.run(debug=True)