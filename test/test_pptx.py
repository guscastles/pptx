"""
PowerPoint Creator

Generates a PPTX file with name and image from a local dataset (csv file).
"""
import os
from prezi import prezi as pz
from pptx import Presentation


def test_create_prezi():
    prezi = pz.create_presentation()
    slide = pz.add_style(prezi)
    image = 'arabian_sea.jpeg'
    slide = pz.add_image(pz.add_title(slide, "Gus is here!"), image)
    prezi_file_name = 'prezi.pptx'
    pz.save_presentation(prezi, prezi_file_name)
    assert os.path.isfile(prezi_file_name) 