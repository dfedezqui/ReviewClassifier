from transformers import pipeline

def cargar_modelo(ruta: str = "/modelo/trainer_model"):
    print(f"Cargando modelo desde '{ruta}'...")
    clasificador = pipeline(
        "sentiment-analysis",
        model=ruta,
        tokenizer=ruta,
    )
    print("Modelo cargado correctamente.\n")
    return clasificador


def cargar_casos(ruta: str = "dataset/casos_prueba.txt"):
    casos = []
    with open(ruta, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or "#" not in linea:
                continue
            texto, etiqueta = linea.split("#")
            casos.append((texto.strip(), etiqueta.strip()))
    print(f"Cargados {len(casos)} casos de prueba desde '{ruta}'\n")
    return casos


def evaluar(clasificador, casos):
    total     = len(casos)
    correctos = 0
    errores   = []

    print(f"{'#':<5} {'TEXTO':<58} {'ESPERADO':<10} {'OBTENIDO':<10} {'CONF':>6}")
    print("─" * 95)

    for i, (texto, esperado) in enumerate(casos, 1):
        resultado      = clasificador(texto)[0]
        label_raw      = resultado["label"]
        confianza      = resultado["score"]
        obtenido       = "bueno" if label_raw == "LABEL_1" else "malo"
        acierto        = obtenido == esperado

        if acierto:
            correctos += 1
        else:
            errores.append((i, texto, esperado, obtenido, confianza))

        marca   = "✓" if acierto else "✗"
        resumen = texto if len(texto) <= 55 else texto[:52] + "..."
        print(f"{i:<5} {resumen:<58} {esperado:<10} {obtenido:<10} {confianza:>5.1%}  {marca}")

    return correctos, total, errores


def imprimir_resumen(correctos, total, errores):
    porcentaje = (correctos / total) * 100
    print("\n" + "═" * 95)
    print(f"  RESULTADO FINAL")
    print(f"  Aciertos : {correctos} / {total}")
    print(f"  Precisión: {porcentaje:.1f}%")
    print("═" * 95)

    if porcentaje >= 90:
        nivel = "🟢 EXCELENTE"
    elif porcentaje >= 75:
        nivel = "🟡 BUENO"
    elif porcentaje >= 60:
        nivel = "🟠 ACEPTABLE"
    else:
        nivel = "🔴 NECESITA MEJORAS"

    print(f"  Valoración: {nivel}\n")

    if errores:
        print(f"  Casos fallidos ({len(errores)}):")
        print("  " + "─" * 91)
        for num, texto, esperado, obtenido, conf in errores:
            resumen = texto if len(texto) <= 60 else texto[:57] + "..."
            print(f"  #{num:<4} [{esperado} → {obtenido}] ({conf:.1%})  \"{resumen}\"")
    print()


if __name__ == "__main__":
    clasificador = cargar_modelo("./modelo/trainer_model")
    CASOS_DE_PRUEBA = cargar_casos("dataset/casos_prueba.txt")
    correctos, total, err = evaluar(clasificador, CASOS_DE_PRUEBA)
    imprimir_resumen(correctos, total, err)