import secrets
import os
from PIL import Image
from pulse import app

def generate_analysis_report(data):
    report = {k:{'percentage':data[k]} for k in data}
    for cat in data:
        if data[cat] <= 30:
            report[cat]['stats'] = 'low'
        elif 30 < data[cat] <= 60:
            report[cat]['stats'] = 'average'
        if 60 < data[cat]:
            report[cat]['stats'] = 'high'
    return report

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/src/invoice', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn