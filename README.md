# FastAPI Trino Demo

API REST de demostración construida con **FastAPI** para visualizar datos y medir tiempos de respuesta sobre un stack de Data Lakehouse moderno usando **Trino**, **Apache Iceberg**, **Hive Metastore** y **Apache Ozone**.

## 🎯 Objetivo

Esta aplicación sirve como interfaz de prueba para consultar datos almacenados en el stack desplegado en [trino-iceberg-hive-ozone](https://github.com/mpita/trino-iceberg-hive-ozone). Permite:

- Explorar datos de **clientes**, **productos** y **ventas** mediante endpoints REST
- Medir tiempos de respuesta de queries sobre tablas Iceberg
- Probar la integración FastAPI + SQLModel + Trino
- Documentación automática con OpenAPI/Swagger

## 🏗️ Arquitectura del Stack

```
┌─────────────────────────────────────────────────────────────────┐
│                        FastAPI Application                       │
│                    (Esta aplicación - Puerto 8000)               │
└─────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────┐
│                         Trino (v478)                             │
│              Motor de consultas SQL distribuido                  │
│                    (Puerto 8080 - Compute Layer)                 │
└─────────────────────────────────────────────────────────────────┘
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                              ▼
┌───────────────────────────┐      ┌───────────────────────────────┐
│   Hive Metastore (v4.0)   │      │      Apache Iceberg           │
│   Catálogo de metadatos   │      │   Formato de tabla ACID       │
│      (Puerto 9083)        │      │   con time-travel             │
└───────────────────────────┘      └───────────────────────────────┘
            │                                      │
            ▼                                      ▼
┌───────────────────────────┐      ┌───────────────────────────────┐
│    PostgreSQL (v13)       │      │    Apache Ozone (v2.0.0)      │
│  Backend del Metastore    │      │  Almacenamiento distribuido   │
│                           │      │  compatible con S3/HDFS       │
└───────────────────────────┘      └───────────────────────────────┘
```

## 🛠️ Stack Tecnológico

### Backend (Esta aplicación)
| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| **Python** | 3.13+ | Lenguaje de programación |
| **FastAPI** | 0.124+ | Framework web async de alto rendimiento |
| **SQLModel** | 0.0.27+ | ORM que combina SQLAlchemy + Pydantic |
| **Pydantic** | 2.x | Validación de datos y serialización |
| **Trino Python Client** | 0.336+ | Conector Python para Trino |
| **uv** | - | Gestor de paquetes y entornos Python |

### Data Lakehouse ([trino-iceberg-hive-ozone](https://github.com/mpita/trino-iceberg-hive-ozone))
| Componente | Versión | Rol |
|------------|---------|-----|
| **Apache Ozone** | 2.0.0 | Storage Layer - Almacén de objetos distribuido |
| **Hive Metastore** | 4.0.0 | Catalog - Metadatos de tablas y esquemas |
| **Apache Iceberg** | - | Table Format - ACID, schema evolution, time-travel |
| **Trino** | 478 | Compute Layer - Motor SQL distribuido |
| **PostgreSQL** | 13 | Backend de persistencia para Hive |

## 📁 Estructura del Proyecto

```
fastapi-trino/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Punto de entrada de FastAPI
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py             # Router principal
│   │   ├── deps.py             # Dependencias (sesión DB)
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── customers.py    # Endpoints de clientes
│   │       ├── products.py     # Endpoints de productos
│   │       └── sales.py        # Endpoints de ventas
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuración con Pydantic Settings
│   │   └── db.py               # Conexión a Trino
│   └── models/
│       ├── __init__.py
│       ├── customers.py        # Modelo Customer
│       ├── products.py         # Modelo Product
│       ├── sales.py            # Modelo Sale
│       └── schemas.py          # Schemas de respuesta (Pydantic)
├── pyproject.toml              # Configuración del proyecto
└── README.md
```

## 🚀 Instalación y Ejecución

### Prerrequisitos

1. **Python 3.13+** instalado
2. **uv** instalado ([instrucciones](https://docs.astral.sh/uv/getting-started/installation/))
3. **Stack de datos ejecutándose** - Clona y levanta [trino-iceberg-hive-ozone](https://github.com/mpita/trino-iceberg-hive-ozone):
   ```bash
   git clone https://github.com/mpita/trino-iceberg-hive-ozone.git
   cd trino-iceberg-hive-ozone
   docker-compose up -d --build
   ```

### Configuración

1. **Clonar este repositorio:**
   ```bash
   git clone https://github.com/mpita/fastapi-trino-demo.git
   cd fastapi-trino-demo
   ```

2. **Crear archivo `.env`** (opcional, valores por defecto funcionan con el stack local):
   ```env
   TRINO_SERVER=localhost
   TRINO_PORT=8080
   TRINO_CATALOG=iceberg
   TRINO_SCHEMA=default
   TRINO_USER=admin
   ```

3. **Instalar dependencias:**
   ```bash
   uv sync
   ```

### Ejecución

**Modo desarrollo (con hot-reload):**
```bash
uv run fastapi dev
```

**Modo producción:**
```bash
uv run fastapi run
```

La API estará disponible en: **http://localhost:8000**

## 📖 Documentación de la API

Una vez ejecutándose, accede a:

| URL | Descripción |
|-----|-------------|
| http://localhost:8000/docs | Swagger UI - Documentación interactiva |
| http://localhost:8000/redoc | ReDoc - Documentación alternativa |
| http://localhost:8000/api/v1/openapi.json | Especificación OpenAPI |

## 🔌 Endpoints Disponibles

### Customers (Clientes)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/v1/customers/` | Listar clientes (paginado) |
| `GET` | `/api/v1/customers/{id}` | Obtener cliente por ID |

### Products (Productos)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/v1/products/` | Listar productos (paginado) |
| `GET` | `/api/v1/products/{id}` | Obtener producto por ID |

### Sales (Ventas)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/api/v1/sales/` | Listar ventas (paginado) |
| `GET` | `/api/v1/sales/{id}` | Detalle de venta con cliente y producto |

## ⚙️ Variables de Entorno

| Variable | Default | Descripción |
|----------|---------|-------------|
| `TRINO_SERVER` | `localhost` | Host del servidor Trino |
| `TRINO_PORT` | `8080` | Puerto de Trino |
| `TRINO_CATALOG` | `iceberg` | Catálogo a usar |
| `TRINO_SCHEMA` | `default` | Schema por defecto |
| `TRINO_USER` | `admin` | Usuario de Trino |
| `TRINO_PASSWORD` | `None` | Contraseña (opcional) |
| `ENVIRONMENT` | `local` | Entorno (local/staging/production) |

## 📊 Datos de Prueba

Los datos son generados por el script `load_fake_data.py` del repo [trino-iceberg-hive-ozone](https://github.com/mpita/trino-iceberg-hive-ozone):

- **~20,000 clientes** con datos demográficos
- **~5,000 productos** con categorías y precios
- **~50,000 ventas** relacionando clientes y productos

Para cargar los datos:
```bash
cd trino-iceberg-hive-ozone
uv run python load_fake_data.py
```

## 🔗 Enlaces Relacionados

- **Stack de datos**: [trino-iceberg-hive-ozone](https://github.com/mpita/trino-iceberg-hive-ozone)
- **Trino UI**: http://localhost:8080 (monitorización de queries)
- **Ozone UI**: http://localhost:9874 (explorador de archivos)

## 📝 Licencia

MIT License

## 👤 Autor

**Manuel Pita**
