"""
Prezi Creator

Creates PowerPoint presentations with one slide.
"""
import pandas as pd
from pptx import Presentation
from pptx.util import Inches


def create_presentation():
    """Creates an empty presentation"""
    return Presentation()


def add_style(pres):
    """Creates a first slide with the default style"""
    first_slide_layout = pres.slide_layouts[0]
    first_slide = pres.slides.add_slide(first_slide_layout)
    return first_slide


def add_title(slide, title):
    """Adds title to the slide"""
    if slide:
        slide.shapes.title.text = title
    return slide


def add_image(slide, url):
    """Adds an image url to the slide"""
    if slide:
        text_box = slide.placeholders[1]
        text_box.text = "This is the sea"
        slide.shapes.add_picture(url, Inches(4), Inches(5), width=Inches(3))
    return slide