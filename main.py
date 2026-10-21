import time
import requests

def obtener_tasas_cambio():
    print("Consultando tipos de cambio oficiales del día...")
    url = "https://er-api.com"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            datos = response.json()
            rates = datos.get("rates", {})
            bob = rates.get("BOB", 6.91)
            pen = rates.get("PEN", 3.75)
            return {"BOB": bob, "PEN": pen}
    except Exception as e:
        print(f"No se pudo conectar a la API de divisas, usando tasas de respaldo: {e}")
    return {"BOB": 6.91, "PEN": 3.75}

def extraer_datos_bolivia(tasas):
    print("Procesando datos de Master Detector Bolivia...")
    equipos = [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio_reg": 94731.00},
        {"nombre": "Detector Minelab Equinox 900", "precio_reg": 14677.00},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio_reg": 12180.00},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio_reg": 1850.00}
    ]
    
    productos = []
    for eq in equipos:
        usd = eq["precio_reg"] / tasas["BOB"]
        productos.append({
            "nombre": eq["nombre"],
            "precio_local": f"Bs. {eq['precio_reg']:,.2f}",
            "precio_usd": f"${usd:,.2f} USD",
            "origen": "Bolivia"
        })
    return productos

def extraer_datos_peru(tasas):
    print("Procesando datos de Master Detector Perú...")
    equipos = [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio_reg": 42500.00},
        {"nombre": "Detector Minelab Equinox 900", "precio_reg": 6800.00},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio_reg": 5400.00},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio_reg": 850.00}
    ]
    s
    productos = []
    for eq in equipos:
        usd = eq["precio_reg"] / tasas["PEN"]
        productos.append({
            "nombre": eq["nombre"],
            "precio_local": f"S/. {eq['precio_reg']:,.2f}",
            "precio_usd": f"${usd:,.2f} USD",
            "origen": "Perú"
        })
    return productos

def generar_reporte_html(productos):
    print("Generando el archivo index.html con el convertidor de dólares...")
    
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Master Detector - Monitor de Precios Regional</title>
    <style>
        body {
            background-color: #202124;
            color: #e8eaed;
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 40px 20px;
            display: flex;
            justify-content: center;
        }
        .container {
            max-width: 900px;
            width: 100%;
        }
        h1 { color: #ffffff; margin-bottom: 5px; }
        h2 { color: #fbbc04; margin-top: 30px; padding-bottom: 5px; border-bottom: 1px solid #3c4043; }
        p { color: #bdc1c6; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            background-color: #292a2d;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            border-radius: 6px;
            overflow: hidden;
        }
        th, td { padding: 12px 15px; text-align: left; }
        th { background-color: #35363a; color: #fbbc04; font-weight: bold; }
        td { border-bottom: 1px solid #3c4043; }
        .usd-price { color: #81c995; font-weight: bold; }
        tr:hover { background-color: #35363a; }
        ul { color: #bdc1c6; padding-left: 20px; }
        li { margin-bottom: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌎 Master Detector - Monitor de Precios Sudamérica</h1>
        <p>Bienvenido al monitor automatizado de precios. Este reporte convierte y compara los valores en moneda local y dólares americanos en tiempo real.</p>
        
        <h2>📊 Catálogo Comparativo Regional (Con Conversión a USD)</h2>
        <table>
            <thead>
                <tr>
                    <th>🛒 Producto</th>
                    <th>💵 Moneda Local</th>
                    <th>🟢 Precio en Dólares</th>
                    <th>📍 Origen</th>
                </tr>
            </thead>
            <tbody>
"""
    
    for p in productos:
        html_content += f"                <tr><td>{p['nombre']}</td><td>{p['precio_local']}</td><td class='usd-price'>{p['precio_usd']}</td><td>{p['origen']}</td></tr>\n"
        
    html_content += """            </tbody>
        </table>
        
        <h2>🌎 Próximas Sucursales</h2>
        <ul>
            <li>🇨🇱 <b>Chile</b> (Sede Santiago de Chile)</li>
            <li>🇨🇴 <b>Colombia</b> (Sedes Bogotá y Medellín)</li>
        </ul>
    </div>
</body>
</html>
"""
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("¡Archivo index.html con convertidor generado con éxito!")

if __name__ == "__main__":
    tasas = obtener_tasas_cambio()
    datos_bo = extraer_datos_bolivia(tasas)
    datos_pe = extraer_datos_peru(tasas)
    todo = datos_bo + datos_pe
    generar_reporte_html(todo)
