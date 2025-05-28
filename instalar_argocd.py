import subprocess
import time
import base64

print("1. 🔍 Verificando namespace 'argocd'...")
result = subprocess.run("kubectl get ns argocd", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if result.returncode != 0:
    print(" 🔧 No existe. Creando...")
    if subprocess.run("kubectl create ns argocd", shell=True).returncode != 0:
        print("❌ Error creando namespace.")
        exit(1)
else:
    print("   ✅ Namespace ya existe.")

print("2. 📦 Aplicando manifiesto de instalación...")
if subprocess.run("kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml", shell=True).returncode != 0:
    print("❌ Error aplicando manifiesto.")
    exit(1)

print("3. ⏳ Esperando que inicien los pods...")
while True:
    pods = subprocess.run("kubectl get pods -n argocd --no-headers", shell=True, capture_output=True, text=True)
    lines = pods.stdout.strip().split("\n") if pods.stdout.strip() else []
    total = len(lines)
    running = sum(1 for line in lines if "Running" in line)
    print(f"   🔄 ({running}/{total}) pods en Running...")
    if total > 0 and running == total:
        break
    time.sleep(10)

print("4. 🔐 Obteniendo credenciales de acceso...")
secret = subprocess.run(
    "kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath=\"{.data.password}\"",
    shell=True, capture_output=True, text=True
)
if secret.returncode != 0 or not secret.stdout:
    print("❌ Error obteniendo el password.")
    exit(1)
password = base64.b64decode(secret.stdout).decode("utf-8")

print("5. 🚪 Iniciando port-forward en segundo plano...")
proc = subprocess.Popen(
    "kubectl port-forward svc/argocd-server -n argocd 8080:443",
    shell=True,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL
)
time.sleep(3)

print("\n✨ Argo CD instalado correctamente. Puedes acceder desde:")
print("   🌐 URL: https://localhost:8080")
print("   👤 Usuario: admin")
print(f"   🔑 Password: {password}")

