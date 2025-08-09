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

- clone the repository : !git clone https://github.com/ItaloSSantos/HelmetDetection.git
- change the directory : %cd /content/HelmetDetection/scripts
- Run the configuration file: !python setup_env.py
- Upload an Image/Video to detect object
- Run the Filter file: !python /content/HelmetDetection/scripts/Filtro1_

## Results : 


<!--![3](https://user-images.githubusercontent.com/103372852/233774758-180186a2-8267-495b-8c04-0d43778299d2.PNG)-->
