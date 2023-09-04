import json

# Crear una lista de diccionarios que representen a los usuarios
usuarios = [
    {
        "Usuario": "Hola",
        "Bot": "Hola, De que quieres hablar?"
    },
    {
        "Usuario": "Necesito un psicologo?",
        "Bot": "No necesitas uno\nTE URGEN 3"
    },
    {
        "Usuario": "Musica",
        "Bot": "KuruKuruuuu"
    }
]

# Guardar la lista de usuarios en un archivo JSON
with open("BaseDatos.json", "w") as json_file:
    json.dump(usuarios, json_file, indent=4)  # "indent" agrega formato legible

print("Info guardada.json")