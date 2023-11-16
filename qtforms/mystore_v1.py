from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QLabel, QSpinBox, QTextEdit, QCheckBox, \
    QDateEdit
import sys


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.user = False
        self.initUI()
        self.login_data = [self.leb, self.rb1, self.rb2, self.btn]

    def initUI(self):
        self.setGeometry(300, 150, 1170, 750)
        self.setWindowTitle('Логин')

        self.leb = QLabel('Выберете пользователя:', self)
        # self.leb.resize(180, 50)
        self.leb.move(500, 200)

        self.rb1 = QRadioButton('Продавец', self)
        self.rb1.resize(150, 50)
        self.rb1.move(500, 250)
        self.rb1.clicked.connect(self.rbtn1)

        self.rb2 = QRadioButton('Покупатель', self)
        self.rb2.resize(150, 50)
        self.rb2.move(500, 300)
        self.rb2.clicked.connect(self.rbtn2)

        self.btn = QPushButton('Продолжить', self)
        self.btn.resize(110, 40)
        self.btn.move(500, 550)
        self.btn.clicked.connect(self.contin)

    def set_catalog(self, catalog):
        self.catalog = catalog

    def set_creator(self, creator):
        self.creator = creator

    def rbtn1(self):
        self.user = 'Продавец'

    def rbtn2(self):
        self.user = 'Покупатель'

    def contin(self):
        if self.user == 'Продавец':
            self.creator.show()
            self.hide()
            rect = self.geometry()
            self.creator.setGeometry(rect)
        elif self.user == 'Покупатель':
            self.catalog.show()
            self.hide()
            rest = self.geometry()
            self.catalog.setGeometry(rest)


class ProductCreator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.data = []
        self.creator_data = [self.back, self.name, self.inf, self.crldate, self.cdate, self.cteg, self.crprice,
                             self.createdn]

    def initUI(self):
        self.setWindowTitle('Создание нового товара')

        self.back = QPushButton('<-- Назад', self)
        self.back.resize(150, 46)
        self.back.move(40, 20)
        self.back.clicked.connect(self.back_click)

        self.name = QTextEdit('Название товара', self)  # название товара
        self.name.resize(250, 30)
        self.name.move(150, 150)

        self.inf = QTextEdit('Информация по товару', self)  # поле для ввода краткой информации по товару
        self.inf.resize(300, 400)
        self.inf.move(150, 200)

        self.crldate = QLabel('Дата изготовления:', self)  # надпись "Дата изготовления"
        self.crldate.adjustSize()
        self.crldate.move(550, 300)

        self.cdate = QDateEdit(self)
        self.cdate.adjustSize()
        self.cdate.move(700, 300)

        self.cteg = QTextEdit('Теги', self)
        self.cteg.resize(200, 80)
        self.cteg.move(550, 350)

        self.crprice = QTextEdit('Цена', self)
        self.crprice.resize(200, 40)
        self.crprice.move(550, 450)

        self.createdn = QPushButton('Создать', self)
        self.createdn.resize(200, 40)
        self.createdn.move(800, 650)
        self.createdn.clicked.connect(self.product_creator)

    def return_data(self):
        return self.data

    def set_creator(self, creator):
        self.creator = creator

    def set_login(self, login):
        self.login = login

    def back_click(self):
        self.login.show()
        self.hide()
        rect = self.geometry()
        self.login.setGeometry(rect)

    def product_creator(self):
        self.data.append([self.name.toPlainText(), self.inf.toPlainText(), self.cteg.toPlainText(),
                          self.crprice.toPlainText()])
        # for elem in self.return_data():
        #     print(f'название - {elem[0]};\nинформация - {elem[1]};\nтеги - {elem[2]};\nцена - {elem[3]}\n\n')


class Catalog(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.catalog_data = [self.back, self.lsearch, self.search, self.categ, self.food, self.technique]
# self.label, self.namprod, self.description, self.teg, self.ldate, self.date, self.price, self.basket, self.num,
    # self.bsearch

    def initUI(self):
        self.setWindowTitle('Каталог')

        self.back = QPushButton('<-- Назад', self)
        self.back.resize(150, 46)
        self.back.move(40, 20)
        self.back.clicked.connect(self.back_click)

        self.lsearch = QLabel('Поиск по тегу', self)
        self.lsearch.resize(142, 28)
        self.lsearch.move(220, 40)

        self.search = QTextEdit('Поиск', self)  # Поиск; строка для ввода
        self.search.resize(722, 42)
        self.search.move(40, 100)

        self.bsearch = QPushButton('Искать', self)
        self.bsearch.resize(150, 46)
        self.bsearch.move(335, 30)
        self.bsearch.clicked.connect(self.search_clict)

        self.cartbutton = QPushButton('Перейти в корзину', self)
        self.cartbutton.resize(250, 46)
        self.cartbutton.move(500, 30)
        self.cartbutton.clicked.connect(self.go_to_cart)

        self.categ = QLabel('Категории:', self)
        self.categ.resize(114, 28)
        self.categ.move(780, 20)

        self.food = QCheckBox('Пищевые продукты', self)
        self.food.resize(238, 36)
        self.food.move(820, 60)
        # self.food.clicked.connect(self.categories_food)

        self.technique = QCheckBox('Бытовая техника', self)
        self.technique.resize(212, 36)
        self.technique.move(820, 100)

    def set_login(self, login):
        self.login = login

    def set_basket(self, basket):
        self.basket = basket

    def set_creator(self, creator):
        self.creator = creator

    def back_click(self):
        self.login.show()
        self.hide()
        rect = self.geometry()
        self.login.setGeometry(rect)

    def search_clict(self):
        print(self.

    def go_to_cart(self):
        self.basket.show()
        self.hide()
        rest = self.geometry()
        self.basket.setGeometry(rest)


class Basket(QWidget):

    def __init__(self):
        super().__init__()
        self.data = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Корзина')

        self.back = QPushButton('<-- Назад', self)
        self.back.resize(150, 46)
        self.back.move(40, 20)
        self.back.clicked.connect(self.back_click)

        self.buybatton = QPushButton('Купить', self)
        self.buybatton.resize(150, 46)
        self.buybatton.move(900, 650)

        self.lebel = QLabel('В корзине лежит:', self)
        self.lebel.adjustSize()
        self.lebel.move(400, 100)

        self.price = QLabel('Стоимость заказа', self)
        self.price.adjustSize()
        self.price.move(550, 650)

        if not self.data:
            self.empty = QLabel('Пока здесь ничего нет', self)
            self.empty.adjustSize()
            self.empty.move(400, 200)

    def set_catalog(self, catalog):
        self.catalog = catalog

    def back_click(self):
        self.catalog.show()
        self.hide()
        rest = self.geometry()
        self.catalog.setGeometry(rest)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    creator = ProductCreator()
    catalog = Catalog()
    basket = Basket()

    login.set_creator(creator)
    login.set_catalog(catalog)
    creator.set_login(login)
    catalog.set_login(login)
    catalog.set_basket(basket)
    catalog.set_creator(creator)
    basket.set_catalog(catalog)

    login.show()
    sys.exit(app.exec())
