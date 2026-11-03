import os
import filetype
import argparse

from tree_manager import run_mode

if __name__ == '__main__':
   parser = argparse.ArgumentParser(description="Mini files is an open source program that tries to replicate the feeling of navigating a snapshot of the files of another person (or yourself)")
   parser.add_argument('dir', type=str, help='Directory to copy from')
   parser.add_argument('out_dir', type=str, help='Directory to copy to')
   parser.add_argument('mode', type=str, choices={'nocopy', 'docs', 'docs_images'}, help='Running mode')
   args = parser.parse_args()

   mode = args.mode
   this_dir = os.path.dirname(__file__)

   root_dir = args.dir
   out_dir = args.out_dir
   root_dir = os.path.relpath(root_dir)
   out_dir = os.path.relpath(out_dir)

   print('Processing...')

   run_mode(root_dir, out_dir, mode)

   print('Done!')
