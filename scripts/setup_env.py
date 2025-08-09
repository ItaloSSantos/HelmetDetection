import os
import subprocess

def run_cmd(cmd):
    print(f"Executando: {cmd}")
    subprocess.run(cmd, shell=True, check=True)

def setup_environment():
    os.chdir("/content/HelmetDetection")
    
    if not os.path.exists("boxmot"):
        run_cmd("git clone https://github.com/ItaloSSantos/boxmot.git")
    else:
        print("Repositório boxmot já clonado.")
    
    run_cmd("pip uninstall -y torch torchvision torchaudio")
    run_cmd("pip install torch==2.2.1 torchvision==0.17.1 --extra-index-url https://download.pytorch.org/whl/cu121")
    run_cmd("pip install numpy==1.26.4")
    
    os.chdir("boxmot")
    run_cmd("pip install ultralytics")
    run_cmd("pip install -e .")
    
    try:
        import torch
        print(f"\n✅ PyTorch {torch.__version__} instalado corretamente!")
    except Exception as e:
        print(f"❌ Erro ao verificar PyTorch: {e}")
        print("Reinicie o runtime manualmente no Colab.")

if __name__ == "__main__":
    setup_environment()


