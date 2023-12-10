import cgi

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Une page web avec python !</title>
    </head>
    <body>
        <h1>Bienvenue</h1>
        <p>Ouiiiiiiiii</p>
    </body>
</html>"""

print(html)