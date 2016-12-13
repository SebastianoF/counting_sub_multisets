import os


root_dir = os.path.abspath(os.path.dirname(__file__))

info = {
        "name": "Counting submultisets",
        "version": "0.0.0",
        "description": "Enumerative combinatoric methods to compute constrained k-resolutions of n.",
        "web_infos" : "http://arxiv.org/abs/1511.06142",
        "repository": {
                       "type": "git",
                       "url": "https://github.com/SebastianoF/counting_sub_multisets.git"
                      },
        "author": "Sebastiano Ferraris",
        "dependencies": {
                         # requirements.txt file automatically generated using pipreqs
                         "python" : "{0}/requirements.txt".format(root_dir)
                         }
        }