import os
import subprocess

def run_cmd(cmd):
    print(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def setup_environment():
    print("🚫 A montagem do Google Drive deve ser feita manualmente no notebook com:")
    print("from google.colab import drive\ndrive.mount('/content/drive')\n")

    # Clona seu repositório principal
    run_cmd("git clone https://github.com/ItaloSSantos/HelmetDetection.git")
    
    # Copia o boxmot para a pasta scripts (simulando seu fluxo)
    run_cmd("git clone https://github.com/ItaloSSantos/boxmot.git /content/HelmetDetection/scripts/boxmot")

    # Volta para a pasta raiz do projeto HelmetDetection
    os.chdir("/content/HelmetDetection")

    # Instala as dependências do requirements.txt, se existir
    if os.path.exists("requirements.txt"):
        run_cmd("pip install -r requirements.txt")
    else:
        print("⚠️ Arquivo requirements.txt não encontrado na raiz do projeto /content/HelmetDetection")

    # Comandos específicos do seu setup (exemplo)
    run_cmd("pip uninstall -y torch torchvision torchaudio")
    run_cmd("pip install torch==2.3.0 torchvision==0.18.0 --extra-index-url https://download.pytorch.org/whl/cu121")
    run_cmd("pip install numpy==1.26.4")
    run_cmd("pip install -e ./scripts/boxmot")  # Instalando o boxmot via editable install
    run_cmd("pip install ultralytics")

    try:
        import torch
        print(f"\n✅ PyTorch {torch.__version__} instalado corretamente!")
    except Exception as e:
        print(f"❌ Erro ao verificar PyTorch: {e}")
        print("Reinicie o runtime manualmente no Colab.")

if __name__ == "__main__":
    setup_environment()
