from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpRequest

def menu  (requist: HttpRequest) -> HttpResponse:
    content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nodirbek Abloqulov | Developer Portfolio</title>

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Poppins', sans-serif;
        }

        body {
            background: linear-gradient(135deg, #1b1b2f, #162447, #1f4068);
            color: #e6e6e6;
            min-height: 100vh;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1.5rem 3rem;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
        }

        header h1 {
            font-size: 1.8rem;
            font-weight: 700;
        }

        .nav-links a {
            color: #e6e6e6;
            text-decoration: none;
            margin-left: 1.5rem;
            font-size: 1rem;
            font-weight: 400;
            transition: transform 0.3s ease, color 0.3s ease;
        }

        .nav-links a:hover {
            color: #00d1ff;
            transform: translateY(-3px);
        }

        .hero {
            text-align: center;
            padding: 8rem 2rem;
        }

        .hero h2 {
            font-size: 3.2rem;
            font-weight: 700;
            margin-bottom: 1rem;
            color: #ffffff;
        }

        .hero p {
            font-size: 1.2rem;
            font-weight: 300;
            max-width: 600px;
            margin: 0 auto 2.5rem auto;
            color: #dcdcdc;
        }

        .hero a {
            padding: 0.9rem 2.3rem;
            background-color: #00adb5;
            color: white;
            border-radius: 50px;
            text-decoration: none;
            font-size: 1rem;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .hero a:hover {
            background-color: #008c95;
            transform: scale(1.05);
        }

        footer {
            text-align: center;
            padding: 1.5rem;
            margin-top: 4rem;
            background: rgba(0, 0, 0, 0.3);
            backdrop-filter: blur(10px);
            font-size: 0.85rem;
            letter-spacing: 0.5px;
        }
    </style>
</head>
<body>

<header>
    <h1>Nodirbek</h1>
    <nav class="nav-links">
        <a href="#home">Home</a>
        <a href="#projects">Projects</a>
        <a href="#about">About Me</a>
        <a href="#contact">Contact</a>
    </nav>
</header>

<section class="hero" id="home">
    <h2>Hello, I’m Nodirbek 👋</h2>
    <p>I’m a passionate Python backend developer specializing in FastAPI, Django, and modern web technologies. Welcome to my digital space!</p>
    <a href="#projects">Explore Projects</a>
</section>

<footer>
    © 2025 Crafted with ❤️ by Nodirbek Abloqulov.
</footer>

</body>
</html>"""

    return HttpResponse(content=content)


def home (requist: HttpRequest) -> HttpResponse:
    params = requist.GET

    a = int(params.get('a',0))
    b = int(params.get('b',0))

    result = a + b

    return HttpResponse(f"<h1> Result : {result}  </h1> ")


def about  (requist: HttpRequest) -> HttpResponse:

    content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me | Nodirbek</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: #1b1b2f;
            color: #e6e6e6;
            text-align: center;
            padding: 4rem 2rem;
        }
        a {
            color: #00adb5;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <h2>About Me</h2>
    <p>Men — <strong>Nodirbek Abloqulov</strong>, backend dasturchiman. Python va FastAPI bilan web ilovalar yarataman.</p>
    <a href="/">Homega qaytish</a>
</body>
</html>"""
    return HttpResponse(content=content)

def contact  (requist: HttpRequest) -> HttpResponse:

    content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Me | Nodirbek</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #1b1b2f, #162447, #1f4068);
            color: #e6e6e6;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 2rem;
            margin: 0;
        }
        .contact-box {
            background: rgba(255, 255, 255, 0.08);
            padding: 2.5rem;
            border-radius: 12px;
            text-align: center;
            max-width: 450px;
            width: 100%;
            backdrop-filter: blur(12px);
        }
        h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        p {
            font-size: 1.1rem;
            margin-bottom: 1.5rem;
        }
        a {
            color: #00adb5;
            text-decoration: none;
            font-size: 1.1rem;
            font-weight: 500;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>

<div class="contact-box">
    <h2>Contact Me</h2>
    <p>Quyidagi raqam orqali men bilan bog‘lanishingiz mumkin:</p>
    <p><a href="tel:+998913333628">📞 +998 91 333 36 28</a></p>
    <p>Yoki email orqali:</p>
    <p><a href="mailto:ablokulovdev23@gmail.com">📧 ablokulovdev23@gmail.com</a></p>
    <br>
    <a href="/">← Back to Home</a>
</div>

</body>
</html>"""
    return HttpResponse(content=content)


def g  (requist: HttpRequest,
        name: str ) -> HttpResponse:
    return HttpResponse(f"<h1> Salom  {name.title()} </h1> ")

def get_product(requist: HttpRequest,
            product_id: int
            ) -> HttpResponse:
    
    con = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ product.name }} | Nodirbek Store</title>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap">
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background: #0f172a;
            color: #e2e8f0;
            margin: 0;
            padding: 2rem;
        }
        .product {
            max-width: 900px;
            margin: 0 auto;
            display: flex;
            gap: 2rem;
            background: #1e293b;
            padding: 2rem;
            border-radius: 12px;
        }
        .product img {
            width: 350px;
            border-radius: 10px;
        }
        .product-details h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
        }
        .product-details p {
            margin: 0.5rem 0;
        }
        .product-details a {
            display: inline-block;
            margin-top: 1.5rem;
            padding: 0.7rem 1.5rem;
            background: #38bdf8;
            color: #0f172a;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            transition: 0.3s;
        }
        .product-details a:hover {
            background: #0ea5e9;
        }
    </style>
</head>
<body>

<div class="product">
    <img src="{{ product.image_url }}" alt="{{ product.name }}">
    <div class="product-details">
        <h2>{{ product.name }}</h2>
        <p><strong>Narxi:</strong> {{ product.price }} so‘m</p>
        <p><strong>Izoh:</strong> {{ product.description }}</p>
        <a href="/">← Back to Products</a>
    </div>
</div>

</body>
</html>"""
    return HttpResponse(
        content=con
        )

