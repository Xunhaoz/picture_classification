# demo

## requirement
```shell
pip install wheel
pip install Flask
pip install matplotlib
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu
```

## run

### docker

```shell
sudo docker image build -t classify .
sudo docker run -p 5000:5000 --name classify_web classify
```

### terminal
```shell
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python app.py
```
