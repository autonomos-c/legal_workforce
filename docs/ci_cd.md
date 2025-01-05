# CI/CD Pipeline

## Configuración de GitHub Actions

El sistema usa GitHub Actions para:
1. Verificar calidad del código
2. Ejecutar tests básicos
3. Construir documentación

### Workflow Principal (ci.yml)

El workflow se ejecuta en:
- Push a main o local-dev
- Pull Requests a main

### Jobs

1. Test:
   - Linting con black y flake8
   - Tests básicos (no requieren API keys)
   - Excluye tests que requieren configuración externa

2. Docs:
   - Construye la documentación con mkdocs
   - Verifica formato estricto

## Tests

### Tests Básicos
- Ejecutados en CI
- No requieren configuración especial
- Verifican funcionalidad core

### Tests de Integración
- Requieren API keys
- Se ejecutan localmente
- Verifican integración con servicios externos

## Notas Importantes

1. Los tests que requieren API keys (Groq, Brave) están excluidos del CI:
   - test_groq_integration
   - test_environment

2. Para ejecutar todos los tests localmente:
   ```bash
   # Con API keys configuradas
   pytest tests/ -v

   # Solo tests básicos
   pytest tests/ -v -k "not test_groq_integration and not test_environment"
   ```

3. Estado Inicial del CI:
   - Los checks de linting son informativos (no fallan el build)
   - Los tests básicos son informativos (no fallan el build)
   - Esta configuración es temporal durante el setup inicial

4. Configuración Futura:
   - El linting será obligatorio
   - Los tests básicos deberán pasar
   - Se agregarán más verificaciones

## Solución de Problemas

1. Si los tests fallan en CI:
   - Verificar que no se agregaron tests que requieren API keys
   - Comprobar el formateo del código
   - Revisar los logs de GitHub Actions

2. Si la documentación falla:
   - Verificar sintaxis de markdown
   - Comprobar enlaces internos
   - Revisar formato de mkdocs.yml
