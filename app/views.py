import json
from app import app, db, lm
from flask import render_template, g, redirect, url_for, request, flash
from flask_login import login_required, make_secure_token, login_user, current_user, logout_user
from app.forms import SignInForm, SignUpForm, NewBookForm
from app.models import User, Author, Book


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template("index.html",
                           title='Home',
                           user=current_user)


@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('books'))
    signinform = SignInForm()
    signupform = SignUpForm()
    if signinform.validate_on_submit():
        user = User.query.filter_by(username=signinform.username.data).first()
        password = make_secure_token(signinform.password.data)
        if user is not None and password == user.password:
            login_user(user)
            return redirect(url_for('books'))
        else:
            flash('Invalid login. Please try again.')
    if signupform.validate_on_submit():
        username = signupform.username.data
        email = signupform.email.data
        password = make_secure_token(signupform.password.data)
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('books'))
    return render_template('auth.html',
                           title='Sign In',
                           signinform=signinform,
                           signupform=signupform, )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route("/books")
@login_required
def books():
    books = Book.query.all()
    return render_template(
        "books.html",
        title='Home',
        user=current_user,
        books=books,
    )


@app.route("/authors")
@login_required
def authors():
    authors = Author.query.all()
    return render_template("authors.html",
                           title='Home',
                           user=current_user,
                           authors=authors, )

@app.route("/AjaxAuthorCreate", methods=['POST'])
@login_required
def AjaxAuthorCreate():
    name = request.values.get("name", "")
    print(name)
    if name and not len(Author.query.filter_by(name=name).all()):
        author = Author(name=name)
        db.session.add(author)
        db.session.commit()
        return json.dumps(dict(id=author.id, name=author.name, is_admin=g.user.is_admin()))
    return json.dumps(dict(error=1))

@app.route("/AjaxAuthorDelete", methods=['POST'])
@login_required
def AjaxAuthorDelete():

    id = request.values.get("id", "")
    Author.query.filter_by(id=id).delete()
    db.session.commit()
    return json.dumps(dict(id=id))

@app.route("/AjaxAuthorEdit", methods=['POST'])
@login_required
def AjaxAuthorEdit():

    id = request.values.get("id", "")[4:]
    newname = request.values.get("name", "")
    a = Author.query.filter_by(id=id).first()
    a.name = newname
    db.session.commit()
    return json.dumps(dict(id=id, name=newname))


@app.route("/addbook", methods=['GET', 'POST'])
@login_required
def addbook():
    form = NewBookForm()
    form.authors.choices = [(author.id, author.name) for author in Author.query.all()]
    if form.validate_on_submit():
        name = form.name.data
        authors = [Author.query.filter_by(id=author).first() for author in form.authors.data]
        book = Book(name=name)
        for author in authors:
            book.authors.append(author)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template("addbook.html",
                           form=form,
                           title='Home',
                           user=current_user,
                           books=books, )

@app.route("/AjaxBookDelete", methods=['POST'])
@login_required
def AjaBookDelete():
    id = request.values.get("id", "")
    Book.query.filter_by(id=id).delete()
    db.session.commit()
    return json.dumps(dict(id=id))

@app.route("/book/<id>/<name>")
@login_required
def book(id=None, name=''):
    if id is None:
        return redirect('/books')
    else:
        book = Book.query.filter_by(id=id).first()
    return render_template("book.html",
                           title='Home',
                           user=current_user,
                           book=book, )

@app.route("/editbook/<id>/<name>", methods=['GET', 'POST'])
@login_required
def editbook(id=None, name=''):
    book = Book.query.filter_by(id=id).first()
    form = NewBookForm()
    form.authors.choices = [(author.id, author.name) for author in Author.query.all()]
    form.name.default = book.name
    form.authors.data=[author.id for author in book.authors]
    print(book.name)
    if form.validate_on_submit():
        name = form.name.data
        authors = [Author.query.filter_by(id=author).first() for author in form.authors.data]
        book.name=name
        book.authors=[]
        for author in authors:
            book.authors.append(author)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('books'))
    return render_template("editBook.html",
                           form=form,
                           title='Edit',
                           user=current_user,
                           books=books, )

@app.route('/tags')
@login_required
def search_tags():
    tag = "%"+request.args.get("search_item")+"%"
    res = {}
    books = Book.query.filter(Book.name.like(tag))
    authors = Author.query.filter(Author.name.like(tag))
    for book in books:
        key = "/book/"+str(book.id)+"/"+book.name
        value = book.name
        res[key] = value
    for author in authors:
        for book in author.books:
            key = "/book/"+str(book.id)+"/"+book.name
            value = book.name+" ("+author.name+")"
            res[key] = value
    return json.dumps(res)

@app.route('/api/authorize')
def apiAuthorize():
    username = request.values.get("username", "")
    password = make_secure_token(request.values.get("password", ""))
    user = user = User.query.filter_by(username=username).first()
    if username == "":
        return json.dumps(dict(error=1))

    elif user.password==password:
        return json.dumps(dict(token=password))
    else:
        return json.dumps(dict(error=1))
