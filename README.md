# Helmet Use Detection in Video Sequences with YOLOv11n and Temporal Filtering via Trackers

## Overview
Este projeto realiza a detecção e rastreamento do uso de capacetes de segurança em vídeos, utilizando o modelo **YOLOv11n** treinado em um dataset desenvolvido específicamente para uso e não uso de capacetes de segurança.
 Os ratreadores **BoTSORT e o StrongSORT (BoxMOT)** foram utilizados para rastrear os indivíduos durante as detecções e assim implementar um filtro sequencial no tempo. Além da filtragem com ratreadores também há uma filtragem sem utilizá-los para comparação de eficácia e custo computacional. 

## Tech-Stack  
- OpenCV 
- Ultralytics 
- torch 
- tochvision 
- Python 3.10

## Installation in COLAB environment

- Clone the repository: !git clone https://github.com/ItaloSSantos/HelmetDetection.git  
- Change the directory: %cd /content/HelmetDetection/scripts  
- Run the configuration file: !python setup_env.py
- Restart the session 
- Upload an image or video to detect objects  
- Choose the mode and run the file: !python /content/HelmetDetection/scripts...


## Results : 
![Detecção e Rastreamento](results/ppe_StrongSort.gif)
