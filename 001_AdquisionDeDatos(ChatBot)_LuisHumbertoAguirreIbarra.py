import json

TXT = []
data= []
print("Bot: Hola, de que deseas hablar?\n(presiona [Q] para cerrar)\n")

#Chat bot
while True:
    
    with open("BaseDatos.json", "r") as json_file:
        data = json.load(json_file)
    usuario_a_buscar = input("Usuario: ")
    if usuario_a_buscar.lower() == 'q':
        break
    
    # Buscar el usuario y extraer el valor "Bot"
    bot_usuario = None
    for item in data:
        if item["Usuario"] == usuario_a_buscar:
            bot_usuario = item["Bot"]
            break  # Si se encuentra el usuario, no es necesario continuar la búsqueda
    if bot_usuario is not None:
        print("Bot: "+bot_usuario)
    else:
        bot=input("Bot: Lo siento, mis respuestas son limitadas\n    cual seria la apropiada para: "+usuario_a_buscar+"?\nUsuario: ")
        TXT = {
            "Usuario": usuario_a_buscar,
            "Bot": bot
            }
        data.append(TXT)
        
# Guardar la lista de usuarios en un archivo JSON
        with open("BaseDatos.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        print("Bot: Entiendo, entiendo. Gracias\n algo mas de lo que quieras hablar?")