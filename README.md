# Welcome to Instant archive moment Of your Komputer (IamOK)

In the era of digital media, navigating the files of your system manager is the equivalent of digging through old boxes filled with photographs and written letters.

This program is aimed to create a snapshot of that sensation but conserving the lightweightness and anonimity :). That is, the script creates a 'snapshot' of all your folders and files structure and names by creating an empty copy of all your folders and files. This structure is navigable and can be copied and sent to anyone that you like, so that they can explore using their file manager.

Currently, the source code is stored in `tree_manager.py`. 

To execute the source code:

```
python main.py in_dir out_dir mode
```

where `in_dir` selects the directory from which the tree structure is copied, `out_dir` is the directory where the copy is made and `mode` can be:

- `nocopy`: only the name and folder structure is preserved. Default and intended use.
- `docs`: .txt and docs are preserved (filetype package is used for this)
- `docs_images`: .txt, docs are preserved and images are compressed to 64x64 pixels so that the thumbnail can be 

Once the new folder is created in 'out_dir' you can navigate the snapshot or send it to someone as a zip file!

Example:

```
python main.py test/ out_dir/ docs_imagess
```


BUILD RELEASE

Currently, there is also a standalone build in the BUILD folder generated using pyinstall and `tkin_tree.py`
