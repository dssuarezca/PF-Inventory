# Inventory

Análisis exploratorio de datos sobre la empresa manufacturera Inventory

---
## 📚 Tabla de contenidos

- [📌 Objetivo](#-objetivo)
- [📊 Datos Utilizados](#-datos-utilizados)
- [🧰 Herramientas y Tecnologías](#-herramientas-y-tecnologías)
- [📁 Estructura del Repositorio](#-estructura-del-repositorio)
- [📈 Visualizaciones Destacadas](#-visualizaciones-destacadas)
- [🚀 Cómo ejecutar el proyecto](#-cómo-ejecutar-el-proyecto)
- [📊 Visualizacion del Informe en Power BI](#-visualizacion-del-informe-en-power-bi)
- [🧠 Posibles mejoras](#-posibles-mejoras)
- [📥 Fuente de datos](#-fuente-de-datos)
- [📜 Licencia](#-licencia)
- [✒ Autor](#-autor)

---

## 📌 Objetivo

Este proyecto tiene como propósito Determinar los niveles óptimos de inventario de materias primas, productos en proceso (WIP) y productos terminados.
Identificar oportunidades para reducir la falta de existencias y el exceso de inventario.
 
---

## 📊 Datos Utilizados

Los datos provienen de fuentes públicas y confiables, incluyendo:

- [Kaggle]([https://ourworldindata.org/](https://www.kaggle.com/datasets/bhanupratapbiswas/inventory-analysis-case-study/data))

Los datasets se encuentran en la carpeta [`/data`](./data/) 

---

## 🧰 Herramientas y Tecnologías

- Python 3.12.5
- pandas, numpy
- matplotlib, seaborn. scikit-learn
- Jupyter Notebook
- SQL
- Power BI

---

## 📁 Estructura del Repositorio

```
PF-Inventory/
├── eda/
│   └── EDA_compras-ipynb
│   └── EDA_inventario_final.ipynb
│   └── EDA_precio_compra.ipynb
│   └── EDA_purchases.ipynb
│   └── EDA_sales.ipynb
│   └── EDA_ventas.ipynb
│   └── automatizacion.py
│   └── eda y etl.ipynb
│   └── generacion_graficos
├── data/
│   └── 2017PurchasePricesDec/
    └── BegInvFINAL12312016/
    └── EndInvFINAL12312016/
    └── InvoicePurchases12312016/
    └── PurchasesFINAL12312016/
    └── SalesFINAL12312016/
├── informe/ 
│   ├── Imagenes/
│   └── Graficos/
├── powerbi/
│   └── informe_Inventory.pbix
└── README.md

```
powerbi

---

## 📈 Visualizaciones Destacadas

Este proyecto incluye un conjunto de visualizaciones interactivas desarrolladas en Power BI que permiten explorar 

➡️ Puede explorarlas en detalle en el archivo `informe_inventario.pbix` y en el informe completo ubicado en la carpeta [`informe/`](./informe/).


---

## 🚀 Cómo ejecutar el proyecto

Este proyecto se ejecuta en notebooks de Jupyter, por lo que es recomendable contar con un entorno Python configurado con las siguientes librerías:

- pandas
- numpy
- matplotlib
- seaborn

### 1. Clonar el repositorio

```bash
https://github.com/dssuarezca/PF-Inventory.git
```
---

## 📊 Visualizacion del Informe en Power BI

existe una visualización interactiva en Power BI que permitirá explorar de forma dinámica los principales indicadores relacionados con los inventarios de los diferentes proveedores.

🔹 Esta visualización permitirá:

📁 El archivo `.pbix` estara disponible en la carpeta [`powerbi/`](./powerbi)


---
## 🧠 Posibles mejoras
- Implementar una app interactiva con Streamlit o Dash

- Incorporar modelos predictivos (SIR, ARIMA, Prophet)

- Automatizar limpieza de datos con notebooks reutilizables

- Agregar visualizaciones geográficas

---

## ✒ Autores

Daniel Suarez – [GitHub](https://github.com/dssuarezca)  
Walter Frías Mendaro [GitHub](https://github.com/Waldo1939)
Diego Grande Zapata [GitHub](https://github.com/DGrandaZapata)
---




