import time
import requests
from bs4 import BeautifulSoup

def extraer_datos_bolivia():
    url = "https://masterdetector.com.bo/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    print("Conectando con Master Detector Bolivia...")
    try:
        # Petición segura a la web
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code != 200:
            print(f"Error al acceder a la página: Código {response.status_code}")
            return []
        
        soup = BeautifulSoup(response.text, "lxml")
        productos_extraidos = []
        
        # Buscamos los bloques de productos destacados en el HTML
        tarjetas = soup.find_all("div", class_="product-grid-item") or soup.find_all("div", class_="product")
        
        # Si la estructura es genérica, buscamos por elementos de producto comunes
        if not tarjetas:
            tarjetas = soup.find_all("div", class_=["col-sm-4", "product-layout", "product-thumb"])

        for tarjeta in tarjetas:
            titulo_el = tarjeta.find(["h3", "h4", "div"], class_=["name", "product-title", "title"])
            precio_el = tarjeta.find(["span", "div", "p"], class_=["price", "amount", "price-new"])
            
            if titulo_el:
                nombre = titulo_el.get_text(strip=True)
                # Extraemos el precio o le ponemos 'Consultar' si no figura
                precio = precio_el.get_text(strip=True) if precio_el else "Consultar Bs."
                
                # Evitamos duplicados en la lista
                if nombre and not any(p['nombre'] == nombre for p in productos_extraidos):
                    productos_extraidos.append({
                        "nombre": nombre,
                        "precio": precio,
                        "origen": "Bolivia"
                    })
                    
        # Simulación de espera humana para navegación segura
        time.sleep(2)
        return productos_extraidos

    except Exception as e:
        print(f"Ocurrió un error durante el scraping: {e}")
        return []

def generar_reporte_markdown(productos):
    print("Generando el archivo index.md para GitHub Pages...")
    
    contenido_base = """# 🌎 Master Detector - Monitor de Precios Sudamérica

Bienvenido al monitor automatizado de precios de **Master Detector**. Este reporte se genera recolectando información de las distintas sucursales de la región.

## 🇧🇴 Sucursal Bolivia (Última Actualización)
Aquí se muestran los equipos destacados de la sede central y sucursales bolivianas.

| 🛒 Producto | 💵 Precio / Estado | 📍 Origen |
| :--- | :--- | :--- |
"""
    
    # Si encontramos productos, armamos las filas de la tabla
    if productos:
        for p in productos:
            contenido_base += f"| {p['nombre']} | {p['precio']} | {p['origen']} |\n"
    else:
        contenido_base += "| No se pudieron recopilar datos en esta ejecución | - | - |\n"
        
    contenido_base += """
## 🌎 Comparativa Regional (Próximamente)
*   🇵🇪 Perú
*   🇨🇱 Chile
*   🇨🇴 Colombia

---
*Herramienta de código abierto desarrollada en Python y desplegada en GitHub Pages.*
"""
    
    # Sobrescribimos el archivo index.md con los nuevos datos
    with open("index.md", "w", encoding="utf-8") as f:
        f.write(contenido_base)
    print("¡Reporte Markdown actualizado con éxito!")

if __name__ == "__main__":
    datos = extraer_datos_bolivia()
    generar_reporte_markdown(datos)

