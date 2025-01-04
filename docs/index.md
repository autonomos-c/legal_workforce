# Legal Agent Documentation

Bienvenido a la documentación oficial del Legal Agent.

## Introducción

Legal Agent es una herramienta para asistencia legal utilizando modelos de lenguaje avanzados.

## Características principales

- Integración con Groq API
- Manejo de contexto legal
- Sistema de memoria persistente
- Configuración automatizada con devcontainer
- Soporte para GitHub Codespaces

## Primeros pasos

1. Clonar el repositorio:
```bash
git clone https://github.com/autonomos-c/c_assistant.git
```

2. Abrir en VSCode:
   - VSCode detectará automáticamente la configuración del devcontainer
   - Click en "Reopen in Container" cuando aparezca la notificación

O usar GitHub Codespaces:
1. Ir al repositorio en GitHub
2. Click en "Code" > "Open with Codespaces"
3. Seleccionar la configuración (4 cores, 16GB RAM recomendado)

## Desarrollo

- La configuración del entorno es automática a través del devcontainer
- Los MCP servers mantienen el contexto del desarrollo
- CI/CD automatizado con GitHub Actions

## Documentación

- [Developer Guide](developer_guide.md) - Guía detallada para desarrolladores
- [Groq Integration](api/groq_integration.md) - Documentación de la integración con Groq
