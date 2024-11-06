# Importar funciones de Flask para renderizar plantillas HTML y acceder a los datos de la solicitud
from flask import render_template, request 
# Importar la biblioteca qrcode para generar códigos QR
import qrcode  
# Importar la clase BytesIO de la biblioteca io para trabajar con datos binarios en memoria
from io import BytesIO
# Importar la biblioteca base64 para codificar y decodificar datos en formato base64
import base64 
# Importar la clase ModelDB del módulo models.model
from models.model import ModelDB  

BASE_URL = "http://localhost:5000/"

class Controller:
    def __init__(self):
        # Se crea una instancia del modelo de base de datos
        self.notas_modelo = ModelDB()
        self.notas_modelo.conectar_base_datos()

    def index(self):
        if request.method == 'POST':
            texto = request.form['texto']  # Obtener el texto ingresado por el usuario en el formulario

            codigo = self.notas_modelo.guardar_nota(texto)  # Guardar la nota en la base de datos y obtener un código único

            enlace = BASE_URL + 'nota/' + codigo  # Construir el enlace completo a la nota utilizando el código

            qr = qrcode.QRCode()  # Crear una instancia de la clase QRCode para generar el código QR
            qr.add_data(enlace)  # Agregar el enlace al código QR
            qr.make(fit=True)  # Generar el código QR

            qr_img = BytesIO()  # Crear un objeto BytesIO para guardar la imagen del código QR
            qr.make_image().save(qr_img, 'PNG')  # Guardar la imagen del código QR en el objeto BytesIO
            qr_img.seek(0)  # Posicionar el puntero de lectura al inicio del objeto BytesIO

            qr_img_base64 = base64.b64encode(qr_img.getvalue()).decode('utf-8')  # Codificar la imagen del código QR en formato base64

            return render_template('enlace.html', enlace=enlace, qr_img_base64=qr_img_base64)  # Renderizar la plantilla 'enlace.html' y pasar el enlace y la imagen del código QR

        return render_template('crearnota.html')  # Si no se realiza una petición POST, renderizar la plantilla 'crearnota.html'

    def nota(self, codigo):
        texto = self.notas_modelo.leer_nota(codigo)  # Leer el texto de la nota correspondiente al código proporcionado
        if texto:
            self.notas_modelo.borrar_nota(codigo)  # Si se encuentra el texto de la nota, borrar la nota de la base de datos
            return render_template('leernota.html', texto=texto)  # Renderizar la plantilla 'leernota.html' y pasar el texto de la nota
        else:
            return render_template('nota.html', mensaje="La nota no existe o ya ha sido borrada.")  # Si no se encuentra la nota, renderizar la plantilla 'nota.html' con un mensaje de error

    def lista_notas(self):
        notas = self.notas_modelo.obtener_todas_notas()  # Obtener todas las notas de la base de datos
        if notas:
            notas_con_enlaces = []
            for nota in notas:
                codigo = nota['codigo']
                enlace = BASE_URL + 'nota/' + codigo  # Construir el enlace completo a cada nota utilizando el código correspondiente
                notas_con_enlaces.append({'nota': nota, 'enlace': enlace})

            return render_template('listanotas.html', notas=notas_con_enlaces)  # Renderizar la plantilla 'listanotas.html' y pasar la lista de notas con enlaces
        else:
            return render_template('listanotas.html', mensaje="No hay notas disponibles.")  # Si no hay notas en la base de datos, renderizar la plantilla 'listanotas.html' con un mensaje de error

    def pagina_no_encontrada(self,error):
     return render_template('404.html', error=error), 404 # Renderizar la plantilla '404.html' si la página no es encontrada