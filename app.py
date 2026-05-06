from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secure-key'

products = [
    {
        'name': 'Cozy Winter Blanket',
        'price': '$45',
        'description': 'Large crochet blanket perfect for cuddling up on cold nights.',
        'icon': '🧶'
    },
    {
        'name': 'Stylish Beanie Hat',
        'price': '$20',
        'description': 'Warm and fashionable beanie hat available in multiple colors.',
        'icon': '🧢'
    },
    {
        'name': 'Elegant Scarf',
        'price': '$25',
        'description': 'Lightweight scarf with intricate crochet patterns.',
        'icon': '🧣'
    },
    {
        'name': 'Decorative Pillow Covers',
        'price': '$30',
        'description': 'Beautiful pillow covers to add charm to your home decor.',
        'icon': '🛋️'
    },
    {
        'name': 'Baby Booties Set',
        'price': '$15',
        'description': 'Adorable crochet booties for the little ones.',
        'icon': '👟'
    },
    {
        'name': 'Wall Hanging',
        'price': '$35',
        'description': 'Unique crochet wall art to decorate your space.',
        'icon': '🖼️'
    }
]

blog_posts = [
    {
        'title': 'Getting Started with Crochet: Essential Tools',
        'excerpt': 'Learn about the basic tools and materials you need to begin your crochet journey.',
        'date': '2024-01-15',
        'read_time': '5 min read'
    },
    {
        'title': 'Choosing the Right Yarn for Your Project',
        'excerpt': 'A guide to different yarn types and when to use them for various crochet projects.',
        'date': '2024-01-10',
        'read_time': '7 min read'
    },
    {
        'title': 'Crochet Patterns for Beginners',
        'excerpt': 'Simple patterns to help new crocheters build confidence and skills.',
        'date': '2024-01-05',
        'read_time': '10 min read'
    },
    {
        'title': 'Sustainable Crochet: Eco-Friendly Practices',
        'excerpt': 'Tips for making your crochet hobby more environmentally friendly.',
        'date': '2023-12-28',
        'read_time': '6 min read'
    }
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products_page():
    return render_template('products.html', products=products)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
