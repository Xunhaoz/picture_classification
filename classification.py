import os
from flask import Flask, request, render_template
from PIL import Image
from flask import jsonify
from PIL import Image
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.backends.cudnn as cudnn
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
import base64
import re


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = torch.load('gold.pt',  map_location=torch.device('cpu'))
model.eval()

def make_predict(img):

    map_dict = {'0':'手鍊', '1':'手串', '2':'耳環', '3':'項鍊', '4':'擺件', '5':'戒指', '6':'手錶'}

    
    
    tr1 = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    
    
    tra_input = tr1(img)
    final_input = tra_input.unsqueeze(0)
    final_input = final_input.to(device)
    
    output = model(final_input).to(device)
    
    _, y_hat = output.max(1)
    predicted_idx = str(y_hat.item())
    class_name = map_dict[predicted_idx]
    return jsonify({'status': 'success', 'class_name': class_name})


app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = './upload_img'

@app.route("/", methods=["GET", "POST"])
def upload_file():

    if request.method == "POST":
    
        if "data" not in request.values:
            return jsonify({'status': 'fail', 'reason': "there is no picture in files!"})

        upload_file = request.values["data"]
        
        a, b, tail = upload_file.partition('/')
        file_formate, b, base_64_img = tail.partition(';base64,')

        path = os.path.join(app.config["UPLOAD_FOLDER"], 
            re.sub(r'[^\w\s]','',base_64_img[-10:]) + '.' + file_formate)
        with open(path, 'wb') as f:
            f.write(base64.b64decode(base_64_img))

        img = Image.open(path)
        h, w = img.size
        allowed_format = ['png', 'jpg', 'jpeg']
        
        if img.format.lower() not in allowed_format:
            return jsonify({'status': 'fail', 'reason': '照片格式錯誤'})

        if h <224 or w <224:
            return jsonify({'status': 'fail', 'reason': '請上傳解析度較大之照片'})

        rgb_img = img.convert("RGB")
        pre_result = make_predict(rgb_img)

        return pre_result

    return render_template("index.html")



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
