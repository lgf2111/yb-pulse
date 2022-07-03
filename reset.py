import os
import shutil


root_path = os.path.dirname(os.path.abspath(__file__))
flask_path = os.path.join(root_path, 'pulse')
clearing = [os.path.join('static','src','invoice'), 'db.json']
manual = False
for sub_path in clearing:
    path = os.path.join(flask_path, sub_path)
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
        open(path, 'w').close()
        print(f"{path} resetted.")
    elif os.path.isdir(path):
        shutil.rmtree(path)
        os.mkdir(path)
        print(f"{path} resetted.")
    else:
        print(f"{path} not found.\nRestoring...")
        manual = True
        
if manual:
    paths = [os.path.join(flask_path, path) for path in clearing]
    os.system(  f'mkdir {paths[0]};'
                f'touch {paths[1]};'
                r'echo {} > '+paths[1])
    print(*[f"{path} restored." for path in clearing], sep="\n")


