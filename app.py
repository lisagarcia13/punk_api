
from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict 


db = PostgresqlDatabase('punk', user='postgres', password='', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Beer(BaseModel):
    name = CharField()
    tagline = CharField()
    description = CharField()
    abv = IntegerField()

db.connect()
db.drop_tables([Beer])
db.create_tables([Beer])

buzz = Beer(name = 'Buzz', tagline ='A Real Bitter Experience.', description = 'A light, crisp and bitter IPA brewed with English and American hops. A small batch brewed only once.', abv = 4.5)
blonde = Beer(name = 'Trashy Blonde', tagline ="You Know You Shouldn't", description = 'A titillating, neurotic, peroxide punk of a Pale Ale. The seductive lure of the sassy passion fruit hop proves too much to resist.', abv = 4.1)
berliner = Beer(name = 'Berliner Weisse With Yuzu - B-Sides', tagline ='Japanese Citrus Berliner Weisse.', description = 'Japanese citrus fruit intensifies the sour nature of this German classic.', abv = 4.2)
lager = Beer(name = 'Pilsen Lager', tagline ='Unleash the Yeast Series', description = 'Our Unleash the Yeast series was an epic experiment into the differences in aroma and flavour provided by switching up your yeast.', abv = 6.3)
avery = Beer(name = 'Avery Brown Dredge', tagline ='Bloggers Imperial Pilsner.', description = 'An Imperial Pilsner in collaboration with beer writers. Tradition. Homage. Revolution.', abv = 7.2)

buzz.save()
blonde.save()
berliner.save()
lager.save()
avery.save()

app = Flask(__name__)
@app.route('/beers', methods=['GET'])
@app.route('/beers/<id>', methods=['GET'])
def beer(id=None):
  if id:
    beer = Beer.get(Beer.id == id)
    beer = model_to_dict(beer)
    return jsonify(beer)
  else:
    beers = []
    for beer in Beer.select():
      beers.append(model_to_dict(beer))
    return jsonify(beers)


app.run(port=9000, debug=True)