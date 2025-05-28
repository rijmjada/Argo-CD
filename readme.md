
### 1. ✅ Requisitos previos
- Tener instalado: `minikube`, `kubectl`, `docker`, `python3`.


### 2. 🚀 Iniciar Minikube

```bash
minikube start --driver=docker
```

### 3. ⚙️ Instalar Argo CD

Ejecutar el script:

```bash
python3 instalar-argocd.py
```

Este script:
- Verifica si existe el namespace `argocd`, y si no, lo crea.
- Aplica el manifiesto oficial de instalación.
- Espera a que todos los pods estén corriendo.
- Realiza un `port-forward` local en `https://localhost:8080`.
- Muestra usuario (`admin`) y contraseña para el acceso.


### 4. 📡 Desplegar app en Argo CD

1. Acceder a [https://localhost:8080](https://localhost:8080).
2. Iniciar sesión con las credenciales mostradas en el script.
3. Crear una nueva aplicación en Argo CD:
   - En Source cargar la url de este repositorio.
   - En Path 'k8s_app_yml'
   - Namespace `default` o el que uses.
   - Activar sincronización automática (opcional).

### 5. 🌐 Acceder a la aplicación

Para acceder a la app Flask:

```bash
minikube service simple-python-app
```

Esto abrirá la app en tu navegador por el puerto asignado.
