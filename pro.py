def generate_page(title, text, color):
    
    html = f"""
    <html>
    <head>
    <title>{title}</title>
    </head>

    <body style="background-color:{color};">
    <h1>{title}</h1>
    <p>{text}</p>
    </body>

    </html>
    """

    return html