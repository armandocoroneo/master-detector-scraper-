import time
import requests

def extraer_datos_bolivia():
    # Código para conectar y extraer los datos de la sucursal de Bolivia
    url = "https://masterdetector.com.bo"
    # ...
    return [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio": "Bs. 94.731,00", "origen": "Bolivia"},
        {"nombre": "Detector Minelab Equinox 900", "precio": "Bs. 14.677,00", "origen": "Bolivia"},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio": "Bs. 12.180,00", "origen": "Bolivia"},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio": "Bs. 1.850,00", "origen": "Bolivia"}
    ]

def generar_reporte_markdown(productos):
    # Función para generar el archivo index.md con estilos CSS personalizados y la tabla de productos
    # Puedes encontrar el código completo del script con los estilos integrados en la referencia.
    pass

if __name__ == "__main__":
    datos = extraer_datos_bolivia()
    generar_reporte_markdown(datos)
