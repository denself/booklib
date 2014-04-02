#!flask/bin/python
from flask_login import make_secure_token

from app.models import Author, Book, User
from app import db

books = {
    "Lord of the Rings": "John Tolkien",
    "Fairy tales": "Hans Christian Andersen",
    "The Divine Comedy": "Dante Alighieri",
    "Pride and Prejudice": "Jane Austen",
    "Le Père Goriot": "Honoré de Balzac",
    "Molloy": "Samuel Beckett",
    "Malone Dies": "Samuel Beckett",
    "The Unnamable": "Samuel Beckett",
    "The Decameron": "Giovanni Boccaccio",
    "Ficciones": "Jorge Luis Borges",
    "Wuthering Heights": "Emily Brontë",
    "The Stranger": "Albert Camus",
    "Poems": "Paul Celan",
    "Journey to the End of the Night": "Louis-Ferdinand Céline",
    "Don Quixote": "Miguel de Cervantes",
    "The Canterbury Tales": "Geoffrey Chaucer",
    "Stories": "Anton Chekhov",
    "Nostromo": "Joseph Conrad",
    "Great Expectations": "Charles Dickens",
    "Jacques the Fatalist": "Denis Diderot",
    "Berlin Alexanderplatz": "Alfred Döblin",
    "Crime and Punishment": "Fyodor Dostoevsky",
    "The Idiot": "Fyodor Dostoevsky",
    "The Possessed": "Fyodor Dostoevsky",
    "The Brothers Karamazov": "Fyodor Dostoevsky",
    "Middlemarch": "George Eliot",
    "Invisible Man": "Ralph Ellison",
    "Medea": "Euripides",
    "Absalom, Absalom!": "William Faulkner",
    "The Sound and the Fury": "William Faulkner",
    "Madame Bovary": "Gustave Flaubert",
    "Sentimental Education": "Gustave Flaubert",
    "Gypsy Ballads": "Federico García Lorca",
    "One Hundred Years of Solitude": "Gabriel García Márquez",
    "Love in the Time of Cholera": "Gabriel García Márquez",
    "Faust": "Johann Wolfgang von Goethe",
    "Dead Souls": "Nikolai Gogol",
    "The Tin Drum": "Günter Grass",
    "The Devil to Pay in the Backlands": "João Guimarães Rosa",
    "Hunger": "Knut Hamsun",
    "The Old Man and the Sea": "Ernest Hemingway",
    "Iliad": "Homer",
    "Odyssey": "Homer",
    "A Doll's House": "Henrik Ibsen",
    "Ulysses": "James Joyce",
    "The Trial": "Franz Kafka",
    "The Castle": "Franz Kafka",
    "Shakuntala": "Kālidāsa",
    "The Sound of the Mountain": "Yasunari Kawabata",
    "Zorba the Greek": "Nikos Kazantzakis",
    "Sons and Lovers": "D. H. Lawrence",
    "Independent People": "Halldór Laxness",
    "The Golden Notebook": "Doris Lessing",
    "Pippi Longstocking": "Astrid Lindgren",
    "A Madman's Diary": "Lu Xun",
    "Children of Gebelawi": "Naguib Mahfouz",
    "Buddenbrooks": "Thomas Mann",
    "The Magic Mountain": "Thomas Mann",
    "Moby-Dick": "Herman Melville",
    "Essays": "Michel de Montaigne",
    "History": "Elsa Morante",
    "Beloved": "Toni Morrison",
    "The Tale of Genji": "Murasaki Shikibu",
    "The Man Without Qualities": "Robert Musil",
    "Lolita": "Vladimir Nabokov",
    "Nineteen Eighty-Four": "George Orwell",
    "Metamorphoses": "Ovid",
    "The Book of Disquiet": "Fernando Pessoa",
    "Tales": "Edgar Allan Poe",
    "In Search of Lost Time": "Marcel Proust",
    "The Life of Gargantua and of Pantagruel": "François Rabelais",
    "Pedro Páramo": "Juan Rulfo",
    "Masnavi": "Rumi",
    "Midnight's Children": "Salman Rushdie",
    "Bostan": "Saadi",
    "Season of Migration to the North": "Tayeb Salih",
    "Blindness": "José Saramago",
    "Hamlet": "William Shakespeare",
    "King Lear": "William Shakespeare",
    "Othello": "William Shakespeare",
    "Oedipus the King": "Sophocles",
    "The Red and the Black": "Stendhal",
    "Tristram Shandy": "Laurence Sterne",
    "Confessions of Zeno": "Italo Svevo",
    "Gulliver's Travels": "Jonathan Swift",
    "War and Peace": "Leo Tolstoy",
    "Anna Karenina": "Leo Tolstoy",
    "The Death of Ivan Ilyich": "Leo Tolstoy",
    "Adventures of Huckleberry Finn": "Mark Twain",
    "Ramayana": "Valmiki",
    "Aeneid": "Virgil",
    "Mahabharata": "Vyasa",
    "Leaves of Grass": "Walt Whitman",
    "Mrs Dalloway": "Virginia Woolf",
    "To the Lighthouse": "Virginia Woolf",
    "Memoirs of Hadrian": "Marguerite Yourcenar",
}


def fill_books(books):
    for author in set([a for a in books.values()]):
        a = Author(name=author)
        db.session.add(a)
        db.session.commit()

    for book_name in books.keys():
        b = Book(name=book_name)
        b.authors = [Author.query.filter_by(name=books[book_name]).first()]
        db.session.add(a)
        db.session.commit()


def create_admin(username, password):
    user = User(username=username, email="admin@email.com", password=password, role=1)
    db.session.add(user)
    db.session.commit()


db.create_all()
fill_books(books)
create_admin("admin", "e2a2975558433d26aab82d614b91beb48de16fac")

