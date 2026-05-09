import os

products = [
    {'name': 'Cozy Winter Blanket', 'slug': 'cozy-winter-blanket', 'price': '$45', 'description': 'Large crochet blanket with intricate geometric patterns, perfect for cuddling up on cold nights.', 'details': 'This oversized blanket is made with soft, durable yarn and features a timeless stitch pattern that adds depth and warmth to any room.', 'features': ['Generous dimensions for cozy coverage', 'Soft yarn with a gentle hand', 'Textured patterns for visual interest'], 'image': 'assets/product-images/cozy-winter-blanket.jpg'},
    {'name': 'Afghan Throw', 'slug': 'afghan-throw', 'price': '$65', 'description': 'Large throw blanket with mosaic colorwork and fringe borders.', 'details': 'The throw combines rich hues and classic crochet motifs, making it ideal for draping over sofas or beds as a stylish accent.', 'features': ['Mosaic colorwork for a handmade look', 'Light fringe detail along all edges', 'Easy-care yarn blend'], 'image': 'assets/product-images/afghan-throw.jpg'},
    {'name': 'Stylish Beanie Hat', 'slug': 'stylish-beanie-hat', 'price': '$20', 'description': 'Warm and fashionable beanie hat with unique cable knit designs, available in multiple colors.', 'details': 'Perfect for cool-weather layering, this hat combines structure and softness for a fitted, comfortable finish.', 'features': ['Eye-catching cable-style texture', 'Stretchy ribbed brim for secure fit', 'Available in neutral and bright shades'], 'image': 'assets/product-images/stylish-beanie-hat.jpg'},
    {'name': 'Elegant Scarf', 'slug': 'elegant-scarf', 'price': '$25', 'description': 'Lightweight scarf with delicate fringe edges.', 'details': 'Designed to dress up any outfit, this scarf is soft, airy, and finished with fine fringe for graceful movement.', 'features': ['Soft drape and gentle knit', 'Lightweight enough for year-round wear', 'Delicate fringe for polish'], 'image': 'assets/product-images/elegant-scarf.jpg'},
    {'name': 'Fingerless Gloves', 'slug': 'fingerless-gloves', 'price': '$24', 'description': 'Stylish fingerless gloves with thumb holes and cable knit patterns for dexterity.', 'details': 'These gloves keep hands warm while allowing easy use of phones and tools, with a chic knitted detail that pairs well with jackets and sweaters.', 'features': ['Thumb hole support for secure fit', 'Cable-inspired stitch work', 'Ideal for daily indoor-outdoor wear'], 'image': None},
    {'name': 'Decorative Pillow Covers', 'slug': 'decorative-pillow-covers', 'price': '$30', 'description': 'Beautiful pillow covers with textured bobble stitches and modern geometric motifs.', 'details': 'These covers bring handcrafted charm to any sofa or bed, with reversible design options to refresh your decor easily.', 'features': ['Textured bobble and geometric stitching', 'Hidden zipper closure for easy care', 'Fits standard throw pillows'], 'image': 'assets/product-images/pillow-cover.jpg'},
    {'name': 'Wall Hanging', 'slug': 'wall-hanging', 'price': '$35', 'description': 'Unique crochet wall art with 3D elements and natural fiber tassels.', 'details': 'This art piece adds a cozy, boho-inspired focal point to walls and entryways with layered textures and movement.', 'features': ['Handcrafted 3D crochet details', 'Neutral tones with natural tassels', 'Ready to hang with wooden dowel'], 'image': None},
    {'name': 'Plant Hanger', 'slug': 'plant-hanger', 'price': '$28', 'description': 'Crocheted plant hanger available in different sizes.', 'details': 'Designed to lift greenery off the floor and create an airy hanging display, this planter hanger is both functional and decorative.', 'features': ['Strong support for indoor pots', 'Adjustable hanging length', 'Handmade knotwork pattern'], 'image': None},
    {'name': 'Macramé Curtain', 'slug': 'macrame-curtain', 'price': '$60', 'description': 'Bohemian window curtain with intricate knotwork and flowing fringe.', 'details': 'This curtain softens sunlight while creating a touch of artisan style, ideal for small windows and room dividers.', 'features': ['Soft macramé fibers for gentle privacy', 'Decorative fringe edge', 'Custom sizing available'], 'image': None},
    {'name': 'Mandala Wall Art', 'slug': 'mandala-wall-art', 'price': '$42', 'description': 'Circular mandala design with concentric patterns and metallic thread accents.', 'details': 'A statement piece for any wall, this mandala blends bold geometry and shimmer for a calming focal point.', 'features': ['Intricate concentric textures', 'Metallic thread highlights', 'Perfect for gallery walls'], 'image': None},
    {'name': 'Baby Booties Set', 'slug': 'baby-booties-set', 'price': '$15', 'description': 'Adorable crochet booties with soft soles and playful animal motifs for the little ones.', 'details': 'These baby booties are gentle enough for newborn skin while offering a charming hand-made gift option for baby showers and new parents.', 'features': ['Soft sole for comfort', 'Fun animal-inspired decorations', 'Stretchy ankle cuff for easy wear'], 'image': None},
    {'name': 'Crochet Jewelry Necklace', 'slug': 'crochet-jewelry-necklace', 'price': '$40', 'description': 'Handcrafted beaded necklace with intricate crochet flowers and gemstone accents.', 'details': 'A delicate necklace that blends fibers and sparkle, perfect for special occasions and gift giving.', 'features': ['Beaded crochet flowers', 'Gemstone accent beads', 'Adjustable chain length'], 'image': None},
    {'name': 'Amigurumi Unicorn', 'slug': 'amigurumi-unicorn', 'price': '$50', 'description': 'Magical amigurumi doll with iridescent yarn mane and crystal horn details.', 'details': 'Soft and cuddly, this unicorn toy is made for imaginative play and keepsake gifting.', 'features': ['Hand-stitched expression', 'Iridescent yarn mane', 'Safe for gentle play'], 'image': None},
    {'name': 'Baby Diaper Cover', 'slug': 'baby-diaper-cover', 'price': '$18', 'description': 'Soft diaper cover with adjustable waist and cute appliqué designs.', 'details': 'A sweet cover designed to fit over cloth diapers and coordinate with nursery outfits.', 'features': ['Adjustable waistband', 'Soft yarn construction', 'Adorable appliqué details'], 'image': None},
    {'name': 'Kitchen Coasters Set', 'slug': 'kitchen-coasters-set', 'price': '$22', 'description': 'Absorbent coasters made from cotton yarn with botanical patterns.', 'details': 'Protect surfaces in style with a set of handmade coasters that bring a fresh, natural look to your kitchen or coffee table.', 'features': ['Absorbent cotton yarn', 'Set of four with coordinating patterns', 'Machine-washable'], 'image': None},
    {'name': 'Pet Collar', 'slug': 'pet-collar', 'price': '$16', 'description': 'Custom pet collar with reinforced stitching and personalized name tag.', 'details': 'Durable and colorful, this collar combines comfort for pets with a touch of artisanal charm.', 'features': ['Reinforced stitched edges', 'Personalized name tag option', 'Adjustable sizing'], 'image': None},
    {'name': 'Christmas Ornament', 'slug': 'christmas-ornament', 'price': '$12', 'description': 'Handcrafted ornament with beaded details and hanging loop.', 'details': 'A festive holiday accent that adds handmade charm to any tree or seasonal display.', 'features': ['Beaded embellishments', 'Sturdy hanging loop', 'Keepsake gift-ready'], 'image': None},
    {'name': 'Keychain Set', 'slug': 'keychain-set', 'price': '$14', 'description': 'Set of 3 keychains with leather accents and crochet charms.', 'details': 'Small and practical, this set of keychains makes a great add-on gift or stocking stuffer.', 'features': ['Leather accent detailing', 'Three unique crochet charms', 'Easy to attach'], 'image': None},
    {'name': 'Bookmark Collection', 'slug': 'bookmark-collection', 'price': '$10', 'description': 'Set of bookmarks with ribbon ties.', 'details': 'Beautifully made bookmarks that keep your place with style and make lovely gifts for readers.', 'features': ['Set of four designs', 'Ribbon pull tabs', 'Lightweight and durable'], 'image': None},
    {'name': 'Eco Tote Bag', 'slug': 'eco-tote-bag', 'price': '$32', 'description': 'Reusable tote bag with reinforced handles.', 'details': 'A sustainable carry-all made for market trips, library runs, or everyday use with a sturdy, handcrafted finish.', 'features': ['Reinforced handles for strength', 'Spacious enough for daily essentials', 'Designed for reuse'], 'image': None},
]

base_nav = '''    <nav class="site-nav">
      <div class="container nav-inner">
        <a class="brand" href="index.html">
          <div class="logo-title">Heart of the Gem <img src="assets/myheartlogo.png" alt="" class="logo-image"></div>
          <div class="logo-subtitle">the beauty of fiber arts</div>
        </a>
        <div class="nav-links">
          <a href="index.html">Home</a>
          <a href="about.html">About</a>
          <a href="products.html">Products</a>
          <a href="love.html">Love Projects</a>
          <a href="blog.html">Blog</a>
          <a href="signup.html">Sign Up</a>
          <a href="contact.html">Contact</a>
        </div>
      </div>
    </nav>'''

base_footer = '''    <footer class="site-footer">
      <div class="container footer-inner">
        <p>© 2024 Heart of the Gem. All rights reserved.</p>
        <div class="footer-links">
          <a class="social-links" href="http://www.instagram.com/heartofthegem?igsh=NTc4MTIwNjQ2YQ%3D%3D&utm_source=qr" target="_blank"><img class="icon" src="assets/icons/instagram.svg" alt="Instagram">Instagram</a>
          <a class="social-links" href="http://www.tiktok.com/@heart.of.the.gem?_r=1&_t=ZT-96ARomhs2ne" target="_blank"><img class="icon" src="assets/icons/tiktok.svg" alt="TikTok">TikTok</a>
          <a class="social-links" href="https://www.etsy.com" target="_blank"><img class="icon" src="assets/icons/etsy.svg" alt="Etsy">Etsy</a>
        </div>
      </div>
    </footer>'''

for product in products:
    page_file = f"{product['slug']}.html"
    image_html = ''
    if product['image']:
        image_html = f'<img src="{product["image"]}" alt="{product["name"]}" class="product-image" />\n          '
    content = f'''<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{product['name']} - Heart of the Gem</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
{base_nav}
    <main class="site-main">
      <section class="section-light">
        <div class="container">
          <h1>{product['name']}</h1>
          <p class="section-intro">{product['description']}</p>
          {image_html}
          <div class="writeup-card">
            <h2>About this item</h2>
            <p>{product['details']}</p>
            <p>Price: <strong>{product['price']}</strong></p>
            <ul class="feature-list">
{''.join(f'              <li>{feature}</li>\n' for feature in product['features'])}            </ul>
            <div class="centered-link" style="margin-top:1.5rem;">
              <a href="contact.html" class="button primary">Request this item</a>
              <a href="products.html" class="button secondary">Back to Products</a>
            </div>
          </div>
        </div>
      </section>
    </main>
{base_footer}
  </body>
</html>'''
    with open(page_file, 'w', encoding='utf8') as f:
        f.write(content)

root_path = 'products.html'
with open(root_path, 'r', encoding='utf8') as f:
    root_html = f.read()
for product in products:
    root_html = root_html.replace(f'<h3>{product['name']}</h3>', f'<h3><a href="{product['slug']}.html">{product['name']}</a></h3>')
with open(root_path, 'w', encoding='utf8') as f:
    f.write(root_html)

product_detail = '''{% extends 'base.html' %}
{% block content %}
<section class="section-light">
  <div class="container">
    <h1>{{ product.name }}</h1>
    <p class="section-intro">{{ product.description }}</p>
    {% if product.image %}
    <img src="{{ product.image }}" alt="{{ product.name }}" class="product-image" />
    {% endif %}
    <div class="writeup-card">
      <h2>Details</h2>
      <p>{{ product.details }}</p>
      <p><strong>Price: {{ product.price }}</strong></p>
      <ul class="feature-list">
        {% for feature in product.features %}
        <li>{{ feature }}</li>
        {% endfor %}
      </ul>
      <div class="centered-link" style="margin-top:1.5rem;">
        <a href="{{ url_for('contact') }}" class="button primary">Request this item</a>
        <a href="{{ url_for('products_page') }}" class="button secondary">Back to Products</a>
      </div>
    </div>
  </div>
</section>
{% endblock %}
'''
with open(os.path.join('templates', 'product_detail.html'), 'w', encoding='utf8') as f:
    f.write(product_detail)
