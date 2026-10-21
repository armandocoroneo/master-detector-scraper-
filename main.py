import time
import requests

def obtener_tasas_cambio():
    print("Consultando tipos de cambio oficiales del día...")
    # URL real de la API gratuita de ExchangeRate-API
    url = "https://er-api.com"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            datos = response.json()
            rates = datos.get("rates", {})
            bob = rates.get("BOB", 6.91)
            pen = rates.get("PEN", 3.75)
            ars = rates.get("ARS", 1000.00) # Tasa base para Argentina
            print(f"Tasas obtenidas -> USD/BOB: {bob} | USD/PEN: {pen} | USD/ARS: {ars}")
            return {"BOB": bob, "PEN": pen, "ARS": ars}
    except Exception as e:
        print(f"No se pudo conectar a la API de divisas, usando tasas de respaldo: {e}")
    return {"BOB": 6.91, "PEN": 3.75, "ARS": 1000.00}

def extraer_datos_bolivia(tasas):
    print("Procesando datos de Master Detector Bolivia...")
    tasa_bob = tasas.get("BOB", 6.91)
    equipos = [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio_reg": 94731.00, "origen": "Bolivia", "moneda": "Bs."},
        {"nombre": "Detector Minelab Equinox 900", "precio_reg": 14677.00, "origen": "Bolivia", "moneda": "Bs."},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio_reg": 12180.00, "origen": "Bolivia", "moneda": "Bs."},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio_reg": 1850.00, "origen": "Bolivia", "moneda": "Bs."}
    ]
    for equipo in equipos:
        equipo["precio_usd"] = round(equipo["precio_reg"] / tasa_bob, 2)
    return equipos

def extraer_datos_peru(tasas):
    print("Procesando datos de Master Detector Perú...")
    tasa_pen = tasas.get("PEN", 3.75)
    equipos = [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio_reg": 42500.00, "origen": "Perú", "moneda": "S/."},
        {"nombre": "Detector Minelab Equinox 900", "precio_reg": 6800.00, "origen": "Perú", "moneda": "S/."},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio_reg": 5400.00, "origen": "Perú", "moneda": "S/."},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio_reg": 850.00, "origen": "Perú", "moneda": "S/."}
    ]
    for equipo in equipos:
        equipo["precio_usd"] = round(equipo["precio_reg"] / tasa_pen, 2)
    return equipos

def extraer_datos_argentina(tasas):
    print("Procesando datos de Master Detector Argentina...")
    tasa_ars = tasas.get("ARS", 1000.00)
    # Lista de precios simulada/base para Argentina en Pesos Argentinos
    equipos = [
        {"nombre": "Detector Minelab GPX 6000 Global", "precio_reg": 14000000.00, "origen": "Argentina", "moneda": "$ Ar."},
        {"nombre": "Detector Minelab Equinox 900", "precio_reg": 2200000.00, "origen": "Argentina", "moneda": "$ Ar."},
        {"nombre": "Detector Minelab Gold Monster 1000", "precio_reg": 1800000.00, "origen": "Argentina", "moneda": "$ Ar."},
        {"nombre": "Detector de Seguridad Garrett Pro-Pointer", "precio_reg": 270000.00, "origen": "Argentina", "moneda": "$ Ar."}
    ]
    for equipo in equipos:
        equipo["precio_usd"] = round(equipo["precio_reg"] / tasa_ars, 2)
    return equipos

def generar_html(lista_completa):
    print("Generando archivo index.html...")
    
    # Marcador de fecha de actualización para el pie de página
    fecha_actualizacion = time.strftime("%d/%m/%Y %H:%M:%S")
    
    filas_tabla = ""
    for equipo in lista_completa:
        filas_tabla += f"""
        <tr>
            <td>{equipo['nombre']}</td>
            <td>{equipo['moneda']} {equipo['precio_reg']:,}</td>
            <td class="text-success">${equipo['precio_usd']:,} USD</td>
            <td>{equipo['origen']}</td>
        </tr>
        """

    html_contenido = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Master Detector - Monitor de Precios</title>
    <link href="https://jsdelivr.net" rel="stylesheet">
    <style>
        body {{ background-color: #121212; color: #e0e0e0; font-family: 'Segoe UI', Arial, sans-serif; }}
        .navbar {{ background-color: #1f1f1f; border-bottom: 2px solid #ffc107; }}
        .table-dark {{ background-color: #1e1e1e; }}
        .table-dark th {{ color: #ffc107; }}
        .card {{ background-color: #1e1e1e; border: 1px solid #333; }}
        .text-success {{ color: #2ecc71 !important; font-weight: bold; }}
    </style>
</head>
<body>

    <nav class="navbar navbar-dark mb-4">
        <div class="container text-center">
            <span class="navbar-brand mb-0 h1 mx-auto">🌏 Master Detector - Monitor de Precios Sudamérica</span>
        </div>
    </nav>

    <div class="container">
        <div class="p-3 mb-4 rounded card">
            <h5>Bienvenido al monitor automatizado de precios.</h5>
            <p class="text-muted mb-0">Este reporte convierte y compara los valores en moneda local y dólares americanos en tiempo real.</p>
        </div>

        <h4 class="mb-3 text-warning">📊 Catálogo Comparativo Regional (Con Conversión a USD)</h4>
        
        <div class="table-responsive">
            <table class="table table-dark table-striped table-hover align-middle">
                <thead>
                    <tr>
                        <th>🛒 Producto</th>
                        <th>💵 Moneda Local</th>
                        <th>🟢 Precio en Dólares</th>
                        <th>📍 Origen</th>
                    </tr>
                </thead>
                <tbody>
                    {filas_tabla}
                </tbody>
            </table>
        </div>

        <footer class="mt-5 mb-4 text-center text-muted">
            <p>© Próximas Sucursales | Última actualización del Bot: {fecha_actualizacion}</p>
        </footer>
    </div>

</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_contenido)
    print("¡index.html generado exitosamente!")

if __name__ == "__main__":
    tasas = obtener_tasas_cambio()
    
    # Extraer datos de todos los países
    equipos_bo = extraer_datos_bolivia(tasas)
    equipos_pe = extraer_datos_peru(tasas)
    equipos_ar = extraer_datos_argentina(tasas)
    
    # Unificar todas las listas en una sola gran tabla
    lista_total = equipos_bo + equipos_pe + equipos_ar
    
    # Compilar el archivo web final
    generar_html(lista_total)
