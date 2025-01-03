# Guía para Desarrolladores

## Estructura del Proyecto
```
legal_agent/
├── src/         # Código fuente principal
├── docs/        # Documentación técnica
├── tests/       # Pruebas unitarias
├── context/     # Archivos de contexto para LLMs
└── templates/   # Plantillas de documentos legales
```

## Configuración del Entorno
1. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar variables de entorno en .env

## Estándares de Código
- Usar type hints
- Documentar funciones con docstrings
- Seguir PEP 8
- Escribir pruebas unitarias
- Usar black para formateo

## Contribución
1. Crear nueva rama:
   ```bash
   git checkout -b feature/nombre-feature
   ```
2. Hacer commits atómicos
3. Crear Pull Request
4. Pasar pruebas y revisión de código
