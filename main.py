#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map
import twitterext
import json

app = Flask(__name__)
GoogleMaps(app)
lista=[]

consulta = raw_input("Introduzca la consulta a realizar: ")
twitter_api = twitterext.oauth_login()

resultados_busqueda = twitter_api.search.tweets(q=consulta, count='1000', geocode='40.4173175,-3.75,1000km')
twitterext.save_json("almacenados",resultados_busqueda)

datos = json.loads(open('almacenados.json').read())

for result in datos["statuses"]:
	if result["geo"]:
		lat=result["geo"]["coordinates"][0]
        longt=result["geo"]["coordinates"][1]
        coord=[lat,longt]
        lista.append(coord)

@app.route("/")
def mapview():
	mymap = Map(
		identifier='view-side',
		lat = 40.45,
		lng = 3.75,
		markers = lista,
		style="height:600px;width:600px;margin:0",
		zoom=4
	)
	return render_template('template2.html', mymap=mymap)

if __name__ == "__main__":
    app.run(debug=True)