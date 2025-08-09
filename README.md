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

## Installation : 

- clone the repository : `$ git clone https://github.com/Vinayakmane47/PPE_detection_YOLO.git`
- create a conda environment : `$ conda create -n myyolo python=3.10 -y`
- Intall and install libraries : `$ pip install -r setup_env.py`
- Upload Image/Video to detect obj
- Run filtros : `Filtro_1` or 'Filtro_bot' or 'Filtro_strong'



## Results : 


<!--![3](https://user-images.githubusercontent.com/103372852/233774758-180186a2-8267-495b-8c04-0d43778299d2.PNG)-->
