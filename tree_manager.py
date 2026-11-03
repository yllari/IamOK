import os
import glob
import shutil
import filetype
from PIL import Image

from pathlib import Path

def copy_fake(src, dest):
    print(src)
    path_dest = Path(os.path.abspath(dest))
    path_dest.touch()
    return None

def copy_only_docs(src, dest):
    print(src)
    kind = filetype.guess(src)

    if kind is None:
        extension = src.split('.')[-1]

        if extension == 'txt':
            shutil.copy2(src, dest)
        else:
            copy_fake(src, dest)
    else:
        file_type, file_ext = kind.mime.split('/')
        if file_type == 'document':
            shutil.copy2(src, dest)
        else:
            copy_fake(src, dest)

def copy_only_docs_images(src, dest):
    print(src)
    kind = filetype.guess(src)

    if kind is None:
        extension = src.split('.')[-1]

        if extension == 'txt':
            shutil.copy2(src, dest)
        else:
            copy_fake(src, dest)
    else:
        if kind.mime.split('/')[0] == 'document':
            shutil.copy2(src, dest)
        elif kind.mime.split('/')[0] == 'image':
            img = Image.open(src)
            ratio = img.size[1]/img.size[0]

            img = img.resize((64,int(ratio*64)))
            img.save(Path(dest).with_suffix('.png'))
        else:
            copy_fake(src, dest)

def run_mode(root_dir, out_dir, mode):

   try:
      if mode == 'nocopy':
           shutil.copytree(root_dir, out_dir, copy_function=copy_fake, dirs_exist_ok=True)
      elif mode == 'docs':
           shutil.copytree(root_dir, out_dir, copy_function=copy_only_docs, dirs_exist_ok=True)
      elif mode == 'docs_images':
           shutil.copytree(root_dir, out_dir, copy_function=copy_only_docs_images, dirs_exist_ok=True)

      return 'Done'
   except:
      return 'Ooops. Something Failed'


