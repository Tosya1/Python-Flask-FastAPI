from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    context = {'title': 'Главная'}
    _categories = [
        {'name': 'Одежда',
         'image': '/static/img/dress.png',
         'path': "/clothes/",
         },
        {'name': 'Обувь',
         'image': '/static/img/shoes.png',
         'path': "/shoes/",
         }
    ]
    return render_template('main.html', **context, categories=_categories)


@app.route('/clothes/')
def clothes():
    context = {'title': 'Одежда'}
    _clothes = [
        {'name': 'Платье',
         'image': '/static/img/dress.png',
         'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium consequatur modi deleniti hic.',
         'price': 50,
         'path': "/clothes/dress/"
         },
        {'name': 'Куртка',
         'image': '/static/img/jacket.png',
         'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium consequatur modi deleniti hic.',
         'price': 75,
         'path': "/clothes/jacket/"
         },
        {'name': 'Футболка',
         'image': '/static/img/t-shirt.png',
         'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium consequatur modi deleniti hic.',
         'price': 25,
         'path': "/clothes/t-shirt/"
         }
    ]
    return render_template('category.html', **context, category=_clothes)


@app.route('/shoes/')
def shoes():
    context = {'title': 'Обувь'}
    _shoes = [
        {'name': 'Туфли',
         'image': '/static/img/shoes.png',
         'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium consequatur modi deleniti hic.',
         'price': 125,
         'path': "/shoes/shoes/"
         },
        {'name': 'Кроссовки',
         'image': '/static/img/sneakers.png',
         'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium consequatur modi deleniti hic.',
         'price': 75,
         'path': "/shoes/sneakers/"
         },
        {'name': 'Сапоги',
         'image': '/static/img/boots.png',
         'description': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laudantium consequatur modi deleniti hic.',
         'price': 150,
         'path': "/shoes/boots/"
         }
    ]
    return render_template('category.html', **context, category=_shoes)


@app.route('/clothes/dress/')
def dress():
    dress = {
        'name': 'Платье 1',
        'image': '/static/img/dress.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur fugiat eos consectetur amet corrupti ut laborum id? Blanditiis quibusdam vero ex? Ad excepturi quasi numquam a cupiditate blanditiis facilis maxime!',
        'price': 50
    }

    return render_template('card.html', **dress)


@app.route('/clothes/jacket/')
def jacket():
    jacket = {
        'name': 'Куртка 1',
        'image': '/static/img/jacket.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur fugiat eos consectetur amet corrupti ut laborum id? Blanditiis quibusdam vero ex? Ad excepturi quasi numquam a cupiditate blanditiis facilis maxime!',
        'price': 75
    }

    return render_template('card.html', **jacket)


@app.route('/clothes/t-shirt/')
def t_shirt():
    t_shirt = {
        'name': 'Футболка 1',
        'image': '/static/img/t-shirt.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur fugiat eos consectetur amet corrupti ut laborum id? Blanditiis quibusdam vero ex? Ad excepturi quasi numquam a cupiditate blanditiis facilis maxime!',
        'price': 25
    }

    return render_template('card.html', **t_shirt)


@app.route('/shoes/shoes/')
def shoes_card():
    shoes = {
        'name': 'Туфли 1',
        'image': '/static/img/shoes.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur fugiat eos consectetur amet corrupti ut laborum id? Blanditiis quibusdam vero ex? Ad excepturi quasi numquam a cupiditate blanditiis facilis maxime!',
        'price': 125
    }

    return render_template('card.html', **shoes)


@app.route('/shoes/sneakers/')
def sneakers():
    sneakers = {
        'name': 'Кроссовки 1',
        'image': '/static/img/sneakers.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur fugiat eos consectetur amet corrupti ut laborum id? Blanditiis quibusdam vero ex? Ad excepturi quasi numquam a cupiditate blanditiis facilis maxime!',
        'price': 75
    }

    return render_template('card.html', **sneakers)


@app.route('/shoes/boots/')
def boots():
    boots = {
        'name': 'Сапоги 1',
        'image': '/static/img/boots.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Aspernatur fugiat eos consectetur amet corrupti ut laborum id? Blanditiis quibusdam vero ex? Ad excepturi quasi numquam a cupiditate blanditiis facilis maxime!',
        'price': 150
    }

    return render_template('card.html', **boots)


if __name__ == '__main__':
    app.run(debug=True)
