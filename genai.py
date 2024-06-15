# -*- coding: utf-8 -*-
"""Untitled46.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jh89eukfJgSBSXv33TZZ5h4nqeTt9W4w
"""

!pip install google-ai-generativelanguage

import pathlib
import textwrap
import google.generativeai as genai
from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown

def rs(text):
   text = text.replace('*',' *')
   return Markdown(textwrap.indent(text,'> ',predicate=lambda _:True))

import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCZNAhvSw3DfiSvkDOhyzh8ktoIcuzKTuk"

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

model = genai.GenerativeModel('gemini-pro')

model



r= model.generate_content("tell about indian cricket?")

rs(r.text)

akash = model.generate_content("find the value of pie?")

rs(akash.text)

akash1 = model.generate_content("do you know Knowledge Institute of Technology,at salem in india ?")

rs(akash1.text)

akash1.prompt_feedback

import PIL
img = PIL.Image.open("download.jpeg")
img

model1 = genai.GenerativeModel('gemini-pro-vision')

r1 = model1.generate_content(img)
rs(r1.text)

