import secrets
import os
from PIL import Image
from pulse import app, DB
from random import Random
import copy


def generate_analysis_report(data):
    if data:
        report = {k:{'percentage':data[k]} for k in data}
        for cat in data:
            if data[cat] <= 30:
                report[cat]['stats'] = 'low'
            elif 30 < data[cat] <= 60:
                report[cat]['stats'] = 'average'
            if 60 < data[cat]:
                report[cat]['stats'] = 'high'
        return report

def save_picture(form_picture, default=''):
    root_path = os.path.join(app.root_path, 'static', 'src')
    if not form_picture:
        if default == 'invoice':
            f_ext = '.jpg'
            form_picture = os.path.join(root_path, 'default', default+f_ext)
    else:
        _, f_ext = os.path.splitext(form_picture.filename)
    random_hex = secrets.token_hex(8)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(root_path, default, picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def create_card():
    visaPrefixList = [
            ['4', '5', '3', '9'],
            ['4', '5', '5', '6'],
            ['4', '9', '1', '6'],
            ['4', '5', '3', '2'],
            ['4', '9', '2', '9'],
            ['4', '0', '2', '4', '0', '0', '7', '1'],
            ['4', '4', '8', '6'],
            ['4', '7', '1', '6'],
            ['4']]

    def completed_number(prefix, length):
        ccnumber = prefix
        while len(ccnumber) < (length - 1):
            digit = str(generator.choice(range(0, 10)))
            ccnumber.append(digit)
        sum = 0
        pos = 0
        reversedCCnumber = []
        reversedCCnumber.extend(ccnumber)
        reversedCCnumber.reverse()
        while pos < length - 1:
            odd = int(reversedCCnumber[pos]) * 2
            if odd > 9:
                odd -= 9
            sum += odd
            if pos != (length - 2):
                sum += int(reversedCCnumber[pos + 1])
            pos += 2
        checkdigit = ((sum / 10 + 1) * 10 - sum) % 10
        ccnumber.append(str(checkdigit))
        return ''.join(ccnumber)
    
    def credit_card_number(rnd, prefixList, length, howMany):
        result = []
        while len(result) < howMany:
            ccnumber = copy.copy(rnd.choice(prefixList))
            result.append(completed_number(ccnumber, length))
        return result
    
    def output(title, numbers):
        {'number': 1234567890123456, 'name': 'Joshua Ng', 'month': 12, 'year': 27}
        result = []
        result.append(title)
        result.append('-' * len(title))
        result.append('\n'.join(numbers))
        result.append('')
        return '\n'.join(result)
    generator = Random()
    generator.seed()        # Seed from current time
    number = f"{credit_card_number(generator, visaPrefixList, 16, 1)[0][:16]}"
    name = 'Joshny Ng'
    month = 12
    year = 27
    db = DB.read()
    db['card'] =   {'number': number,
                    'name': name,
                    'month': month,
                    'year': year}
    DB.write(db)
    return db['card']