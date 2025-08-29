from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_babel import Babel
from config import Config
from models import db, Term
from forms import AddTermForm, CATEGORIAS

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

babel = Babel()

def get_locale():
    lang = request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])  # Default a 'es'
    return lang

babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET', 'POST'])
def index():
    lang = get_locale()
    session['lang'] = lang
    query = request.args.get('q', '')
    letra = request.args.get('letra', '')
    categoria = request.args.get('categoria', '')

    terms_query = Term.query
    if query:
        terms_query = terms_query.filter(Term.termino.ilike(f'%{query}%'))
    if letra:
        terms_query = terms_query.filter(Term.termino.like(f'{letra}%'))
    if categoria:
        terms_query = terms_query.filter(Term.categoria == categoria)
    terms = terms_query.order_by(Term.termino).all()

    return render_template('index.html', terms=terms, lang=lang, locale=lang, categorias=CATEGORIAS)

@app.route('/add_term', methods=['GET', 'POST'])
def add_term():
    lang = session.get('lang', get_locale())
    form = AddTermForm(lang=lang)

    if form.validate_on_submit():
        new_term = Term(
            codigo=form.codigo.data,
            termino=form.termino.data,
            categoria=form.categoria.data,
            term_es=form.term_es.data if lang == 'es' else '',
            term_en=form.term_en.data if lang == 'en' else '',
            term_fr=form.term_fr.data if lang == 'fr' else '',
            ejemplo1_es=form.ejemplo1_es.data if lang == 'es' else None,
            ejemplo1_en=form.ejemplo1_en.data if lang == 'en' else None,
            ejemplo1_fr=form.ejemplo1_fr.data if lang == 'fr' else None,
            ejemplo2_es=form.ejemplo2_es.data if lang == 'es' else None,
            ejemplo2_en=form.ejemplo2_en.data if lang == 'en' else None,
            ejemplo2_fr=form.ejemplo2_fr.data if lang == 'fr' else None,
            fuente=form.fuente.data,
            observacion=form.observacion.data
        )
        db.session.add(new_term)
        db.session.commit()
        return redirect(url_for('index', lang=lang))

    return render_template('add_term.html', form=form, lang=lang, locale=lang)

@app.route('/term/<int:id>')
def term_detail(id):
    lang = get_locale()
    term = Term.query.get_or_404(id)
    return render_template('term_detail.html', term=term, lang=lang, locale=lang, id=id)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)