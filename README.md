# 🧠 ReviewClassifier

> Proyecto de análisis de sentimientos con modelo de Machine Learning propio y una interfaz web servida con Flask.

---

## 📁 Estructura del Proyecto

```
TR1_SENTIMENT_ANALYSIS/
│
├── dataset/
│   ├── review.txt           # 📚 Datos para entrenar el modelo
│   └── casos_prueba.txt     # 🧪 Casos usados para el test/evaluación
│
├── modelo/
│   ├── resultados/          # Resultados generados tras el entrenamiento
│   └── trainer_model/       # Modelo entrenado y guardado
│
├── static/
│   ├── script.js            # Lógica frontend
│   └── style.css            # Estilos de la interfaz
│
├── templates/
│   └── index.html           # Página principal de la app web
│
├── app.py                   # 🚀 Servidor Flask — punto de entrada de la app
├── train.py                 # 🏋️ Entrena y genera el modelo
├── test.py                  # ✅ Testea el modelo y muestra el % de aciertos
├── requirements.txt         # 📦 Dependencias del proyecto
└── README.md
```

---

## 📄 Descripción de Archivos Clave

| Archivo | Descripción |
|---|---|
| `dataset/review.txt` | Contiene los datos con los que se **entrena** el modelo de sentimientos |
| `dataset/casos_prueba.txt` | Casos de ejemplo usados para **testear** el modelo y medir su rendimiento |
| `train.py` | Script que **genera y guarda el modelo** a partir de los datos de entrenamiento |
| `test.py` | Script que **evalúa el modelo** y devuelve el **porcentaje de aciertos** |
| `app.py` | Lanza el servidor **Flask** para probar el modelo desde el navegador |

---

## ⚙️ Puesta en marcha — Paso a paso

### 1. Instalar las dependencias

Asegúrate de tener Python instalado. Luego, desde la raíz del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```

---

### 2. Entrenar el modelo

Este paso genera el modelo a partir de los datos en `review.txt`. El resultado se guardará en la carpeta `modelo/`:

```bash
python train.py
```

> ⏳ Dependiendo del tamaño del dataset, este proceso puede tardar unos minutos.

---

### 3. Testear el modelo

Una vez entrenado, puedes evaluar su precisión con los casos de prueba definidos en `casos_prueba.txt`:

```bash
python test.py
```

Verás en consola el **porcentaje de aciertos** del modelo.

---

### 4. Lanzar la aplicación web

Finalmente, activa el servidor Flask para interactuar con el modelo desde el navegador:

```bash
python app.py
```

Abre tu navegador y accede a:

```
http://127.0.0.1:5000
```

---

## 🧪 Flujo completo

```
requirements.txt
      ↓
  pip install
      ↓
  train.py  ──→  genera modelo en /modelo/trainer_model/
      ↓
  test.py   ──→  muestra % de aciertos
      ↓
  app.py    ──→  lanza Flask en localhost:5000
```

---

## 📋 Requisitos

- Python 3.8+
- pip
- Las librerías especificadas en `requirements.txt`

---
