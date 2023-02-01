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

file_name = input("Enter the name of the HTML file (without the .html extension): ")
redirect_url = input("Enter the URL you want to redirect to: ")

with open(f"{file_name}.html", "w", encoding="UTF-8") as file:
    file.write(html_template.format(url=redirect_url))

print(f"The file '{file_name}.html' has been created and it redirects to '{redirect_url}'.")
