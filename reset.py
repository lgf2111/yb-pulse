import os
import shutil


root_path = os.path.dirname(os.path.abspath(__file__))
flask_path = os.path.join(root_path, 'pulse')
clearing = [os.path.join('static','src','invoice'), 'db.json']
paths = [os.path.join(flask_path, path) for path in clearing]
if os.path.isdir(paths[0]):
    shutil.rmtree(paths[0])
if os.path.isfile(paths[1]) or os.path.islink(paths[1]):
    os.remove(paths[1])

os.mkdir(paths[0])
with open(paths[1], 'w') as f:
    f.write(r'{}')
# for sub_path in clearing:
#     path = os.path.join(flask_path, sub_path)
#     if os.path.isfile(path) or os.path.islink(path):
#         os.remove(path)
#         open(path, 'w').close()
#         print(f"{path} resetted.")
#     elif os.path.isdir(path):
#         shutil.rmtree(path)
#         os.mkdir(path)
#         print(f"{path} resetted.")
#     else:
#         print(f"{path} not found.\nRestoring...")
#         manual = True
        
# if manual:
#     paths = [os.path.join(flask_path, path) for path in clearing]
#     os.system(  f'mkdir {paths[0]};'
#                 f'touch {paths[1]};'
#                 r'echo {} > '+paths[1])
#     print(*[f"{path} restored." for path in clearing], sep="\n")


