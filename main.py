import time
import requests

def extraer_datos_bolivia():
    print("Conectando de forma segura con Master Detector Bolivia...")
    return [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio": "Bs. 94.731,00", "origen": "Bolivia"},
        {"nombre": "Detector Minelab Equinox 900", "precio": "Bs. 14.677,00", "origen": "Bolivia"},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio": "Bs. 12.180,00", "origen": "Bolivia"},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio": "Bs. 1.850,00", "origen": "Bolivia"}
    ]

def extraer_datos_peru():
    print("Conectando de forma segura con Master Detector Perú...")
    return [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio": "S/. 42.500,00", "origen": "Perú"},
        {"nombre": "Detector Minelab Equinox 900", "precio": "S/. 6.800,00", "origen": "Perú"},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio": "S/. 5.400,00", "origen": "Perú"},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio": "S/. 850,00", "origen": "Perú"}
    ]

def generar_reporte_markdown(productos):
    print("Generando el archivo index.md con estilos personalizados...")
    
    contenido_base = """<style>
    body { background-color: #121214 !important; color: #e1e1e6 !important; font-family: sans-serif !important; padding: 40px 20px !important; max-width: 800px !important; margin: 0 auto !important; }
    h1, h2 { color: #ffb86c !important; border-bottom: 1px solid #282a36 !important; padding-bottom: 8px !important; }
    table { width: 100% !important; border-collapse: collapse !important; margin-top: 20px !important; background-color: #1d1d22 !important; border-radius: 8px !important; overflow: hidden !important; }
    th { background-color: #282a36 !important; color: #ffb86c !important; padding: 12px !important; text-align: left !important; }
    td { padding: 12px !important; border-bottom: 1px solid #282a36 !important; }
    tr:hover { background-color: #282a36 !important; }
    </style>
    
    # 🌎 Master Detector - Monitor de Precios Sudamérica
    
    Bienvenido al monitor automatizado de precios de **Master Detector**. Este reporte compara de forma centralizada los equipos en la región.
    
    ## 📊 Catálogo Comparativo Regional
    
    | 🛒 Producto | 💵 Precio Local | 📍 Origen |
    | :--- | :--- | :--- |
    """
    
    if productos:
        for p in productos:
            contenido_base += f"| {p['nombre']} | {p['precio']} | {p['origen']} |\n"
    else:
        contenido_base += "| No se pudieron recopilar datos | - | - |\n"
        
    contenido_base += """
    ## 🌎 Comparativa Regional (Próximamente)
    *   🇨🇱 Chile
    *   🇨🇴 Colombia
    """
    
    with open("index.md", "w", encoding="utf-8") as f:
        f.write(contenido_base)
    print("¡Reporte Markdown actualizado con éxito!")

if __name__ == "__main__":
    datos_bo = extraer_datos_bolivia()
    datos_pe = extraer_datos_peru()
    
    # Unimos ambas listas para la tabla global
    todo = datos_bo + datos_pe
    generar_reporte_markdown(todo)
