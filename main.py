import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres:postgres@localhost:5432/orm_dz'
engine= sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

publisher1 = Publisher(name= 'Пушкин')
session.add(publisher1)
session.commit()

book1 = Book(title= 'Капитанская дочка', publisher = publisher1)
book2 = Book(title= 'Руслан и Людмила', publisher = publisher1)
book3 = Book(title= 'Евгений Онегин', publisher = publisher1)

session.add_all([book1, book2, book3])
session.commit()

shop1 = Shop(name= 'Буквоед')
shop2 = Shop(name= 'Лабиринт')
shop3 = Shop(name= 'Книжный дом')

session.add_all([shop1, shop2, shop3])
session.commit()

stock1 = Stock(book= book1, shop= shop1, count= 100)
stock2 = Stock(book= book2, shop= shop1, count= 150)
stock3 = Stock(book= book1, shop= shop2, count= 170)
stock4 = Stock(book= book3, shop= shop3, count= 180)

session.add_all([stock1, stock2, stock3, stock4])
session.commit()

sale1= Sale(price= 600, date_sale = '09-11-2022', stock= stock1, count= 20)
sale2= Sale(price= 500, date_sale = '08-11-2022', stock= stock2, count= 15)
sale3= Sale(price= 580, date_sale = '05-11-2022', stock= stock3, count= 10)
sale4= Sale(price= 490, date_sale = '02-11-2022', stock= stock4, count= 16)
sale5= Sale(price= 600, date_sale = '26-10-2022', stock= stock1, count= 18)

session.add_all([sale1, sale2, sale3, sale4, sale5])
session.commit()

def find_publshier_name():
    name_publisher = input("Введите фамилию Автора: ")
    for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == name_publisher):
        print(c)

def find_publisher_id():
    id_publisher = input("Введите id автора: ")
    for c in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.id== id_publisher ):
        print(c)




session.close()


if __name__ == "__main__":

    find_publshier_name()
    find_publisher_id()
