# Repository for final project


Crear un entorno por la ventan

```shell
python3 -m venv venv
```

Activar 
```shell
source venv/bin/activate
```

Instalar dependeicas
```shell
pip install flask requests json
```

Probar funciones en pyhton sin paquete

```python
from emotion_detection import emotion_detector
emotion_detector('Me encanta esta nueva tecnología.')
```

Probar funciones en pyhton sin paquete

```python
from EmotionDetection.emotion_detection import emotion_detector
emotion_detector('Me encanta esta nueva tecnología.')
```

Ejecucion pruebas 

```
python3.11  test_emotion_detection.py 
```


Ejecutar flask
```shell
python3 server.py
```

Instalar  lint en python 
```shell
pip install pylint
```

Ejecutar lint en python 
```shell
pylint server.py
```