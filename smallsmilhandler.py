#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):
	"""
	Clase para manejar etiquetas y devolverlas en  una lista
	"""
	def __init__ (self):
		"""
		Inicializa la lista
		"""
		self.tagsList
		
	def startElement(self, tag, attrs):
		#Tomamos etiquetas/atributos en diccionarios y añadimos a nuestra lista
		if tag == 'root-layout':
			rootAttrs["width"] = attrs.get('width', "")
			rootAttrs["height"] = attrs.get('height', "")
			rootAttrs["background-color"] = attrs.get('background-color', "")
			tagRoot = {'root-layout': rootAttrs} 
			self.tagsList.append(tagRoot)
		elif tag == 'region':
			regionAttrs = {"id": attrs.get('id', ""), "top": attrs.get('top', ""),
							"bottom": attrs.get('bottom', ""), "left":
							attrs.get('left', ""), "right": attrs.get('right', "")}
			tagRegion = {'region': regionAttrs}	
			self.tagsList.appen(tagRegion)		
		elif tag == 'img':
			imgAttrs = {"src": attrs.get('src', ""), "region": 
						attrs.get('region', ""), "begin": 
						attrs.get('begin', ""), "dur": attrs.get('dur', "")}
			tagImg = {'img': imgAttrs}
			self.tagsList.append(tagImg)
		elif tag == 'audio':
			audioAttrs["src"] = attrs.get('src', "")
			audioAttrs["begin"] = attrs.get('begin', "")
			audioAttrs["dur"] = attrs.get('dur', "")
			tagAudio = {'audio': audioAttrs}
			self.tagsList.append(tagAudio)
		elif tag == 'textstream':
			textAttrs["src"] = attrs.get('src', "")
			textAttrs["region"] = attrs.get('region', "")
			tagText = {'textstream': textAttrs}
			self.tagsList.append(tagText)
	
	def get_tags(self):
		return self.tagsList
	
	
	
			
			
			
			
			
			
			
			
			
			
		
		
		
	
	
	
	
