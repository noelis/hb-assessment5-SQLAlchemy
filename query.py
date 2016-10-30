"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.

brand_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.

mod = Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()

# Get all models that are older than 1960.

mods = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.

brands_1920 = db.session.query(Brand).filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".

mod = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.

brand_active = Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.

brand_d_f = Brand.query.filter(Brand.discontinued.isnot(None), Brand.founded < 1950).all()

# Get all models whose brand_name is not Chevrolet.

not_chevrolet = Brand.query.filter(Brand.name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info_year =  db.session.query(Model.name, Model.brand_name, Brand.headquarters).join(Brand).filter(Model.year==year).all()

    # I don't understand why we need to add a join to this query, since we already 
    # established the relationship? I tried it with/without the .join and got very 
    # different answers, the .join() provided the right answer. Do we use a join 
    #  here since we are querying with db.session instead of by class name?

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    test = Model.query.options(db.joinedload('brands')).all()

    #  I don't think this is the right query for this since it prints out the year 
    # and I can't get it to group by brand name :( 


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

The query "Brand.query.filter_by(name='Ford')" does nothing by itself. It would
need a .all() or something similar to actually return something. 


If you add .one() to it, it returns a single object from the Brands table that has
the brand name 'Ford'. It makes sense to use .one() instead of .all() since we know
that there is only one car brand with the name Ford. If there was more than brand 
name with that same name, then it makes sense to use .all() instead which returns a 
list of objects that match the query.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

An association table is what I like to call a 'Frankentable'! It has no unique 
fields in the table, meaning that the data it stores already exists as a column
in another table. We use these tables if we need to hold a bunch of information 
together for easy access. It has a many to one relationship with other tables.

For example: If you have a database for books, and have a Books, Genres and 
BookGenre tables; the BookGenre table is an association table that holds the 
BookGenre_id, book_id (which already exists in the Books table) and a genre_id 
(which already exists in the Genres table). It holds no meaningful/unique information,
like a Middle table would.

# -------------------------------------------------------------------
# Part 3


def search_brands_by_name(mystr):
    " Takes a string & returns all brand names that contain or are equal to that string."

    mystr = '%' + mystr + '%'
    mystr_brand = Brand.query.filter(Brand.name.like(mystr)).all()


def get_models_between(start_year, end_year):
    " Given a range of years, return a list of models released during those years."

    years = range(start_year, end_year)
    models_between_years = Model.query.filter(Model.year.in_(years)).all()
