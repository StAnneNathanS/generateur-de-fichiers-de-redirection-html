html_template = """
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; URL={url}">
  <title>Redirection à {url} en cours...</title>
</head>
<body>
  Si vous n'êtes pas redirigé automatiquement, suivez ce <a href="{url}">lien</a>.
</body>
</html>
"""

file_name = input("Entrez le nom du fichier HTML (sans l'extension .html): ")
redirect_url = input("Saisissez l'URL vers laquelle vous souhaitez rediriger les données: ")

with open(f"{file_name}.html", "w", encoding="UTF-8") as file:
    file.write(html_template.format(url=redirect_url))

print(f"Le fichier '{file_name}.html' a été créé et il redirige versa été créé et il redirige vers '{redirect_url}'.")
