import os
import subprocess

def run_cmd(cmd):
    print(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def setup_environment():
    print("🚫 A montagem do Google Drive deve ser feita manualmente no notebook com:")
    print("from google.colab import drive\ndrive.mount('/content/drive')\n")
    # Volta para a pasta raiz do projeto HelmetDetection
    os.chdir("/content/HelmetDetection")
    
    # Clona seu repositório principal
    run_cmd("pip install -q colab-env --upgrade")
    run_cmd("git clone https://github.com/ItaloSSantos/boxmot.git")
    os.chdir("/content/boxmot")
    run_cmd("pip uninstall -y torch torchvision torchaudio")
    run_cmd("pip install torch==2.3.0 torchvision==0.18.0 --extra-index-url https://download.pytorch.org/whl/cu121")
    run_cmd("pip install numpy==1.26.4")
    run_cmd("pip install -e .")
    run_cmd("pip install ultralytics")

    # Verificação
    try:
        import torch
        print(f"\n✅ PyTorch {torch.__version__} instalado corretamente!")
    except Exception as e:
        print(f"❌ Erro ao verificar PyTorch: {e}")
        print("Reinicie o runtime manualmente no Colab.")

if __name__ == "_

    try:
        import torch
        print(f"\n✅ PyTorch {torch.__version__} instalado corretamente!")
    except Exception as e:
        print(f"❌ Erro ao verificar PyTorch: {e}")
        print("Reinicie o runtime manualmente no Colab.")

if __name__ == "__main__":
    setup_environment()


