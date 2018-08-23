# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 10:37:23 2018

@author: amanosalva
"""

import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    
    res = makeResponse(req)
    
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResponse(req):

    result = req.get("result")
    metadata = result.get("metadata")
    intentName = metadata.get("intentName")
    
    if intentName == "no.secuencial.no.parametrica.pg1-options":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "¡Ya diste el primer paso :D!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "¡Ya diste el primer paso ;)!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech,
                "messages": [
				{
					"type": 0,
					"speech": speech,
                    "platform": "facebook"
				}
			]
            }

    if intentName == "no.secuencial.no.parametrica.pg2-options":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "Puedes realizar \n *depósitos ilimitados, 2 operaciones sin costo* (retiros de dinero y transferencias entre cuentas) en la misma localidad donde se contrató tu cuenta."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "Puedes realizar depósitos ilimitados *sin costo* y hasta 1 operación mensual sin costo por retiros de dinero y transferencias entre cuentas (en la misma localidad donde se contrató la cuenta)."
            return {
                "speech": speech,
                "displayText": speech,
                "messages": [
				{
					"type": 0,
					"speech": speech,
                    "platform": "facebook"
				}
			]
            }

    if intentName == "no.secuencial.no.parametrica.pg3-options":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "¡Ya diste el primer paso :D!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "¡Ya diste el primer paso ;)!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech,
                "messages": [
				{
					"type": 0,
					"speech": speech,
                    "platform": "facebook"
				}
			]
            }

    if intentName == "no.secuencial.no.parametrica.pg4-options":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "¡Ya diste el primer paso :D!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "¡Ya diste el primer paso ;)!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech,
                "messages": [
				{
					"type": 0,
					"speech": speech,
                    "platform": "facebook"
				}
			]
            }

    if intentName == "no.secuencial.no.parametrica.pg5-options":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "¡Ya diste el primer paso :D!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "¡Ya diste el primer paso ;)!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech,
                "messages": [
				{
					"type": 0,
					"speech": speech,
                    "platform": "facebook"
				}
			]
            }

    if intentName == "no.secuencial.no.parametrica.pg6-options":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "¡Ya diste el primer paso :D!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "¡Ya diste el primer paso ;)!, ahora solo debes acercarte a nuestras oficinas para obtener la *Tarjeta de Débito* que te permitirá acceder a todos nuestros canales de atención: _Banca por Internet_, _Banca Móvil_, _Banca por Teléfono_, entre otros. Con tu Tarjeta de Débito podrás realizar operaciones, como *pagar tus servicios*, *realizar transferencias* y mucho más."
            return {
                "speech": speech,
                "displayText": speech,
                "messages": [
				{
					"type": 0,
					"speech": speech,
                    "platform": "facebook"
				}
			]
            }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')

















