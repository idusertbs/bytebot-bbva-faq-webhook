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
            speech = "Puedes realizar *depósitos ilimitados, 2 operaciones sin costo* (retiros de dinero y transferencias entre cuentas) en la misma localidad donde se contrató tu cuenta."
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
            speech = "En cajeros del BBVA Continental puedes retirar ilimitadamente sin costo a nivel nacional.\nAdemás, puedes retirar en todos los cajeros de la red VISA en la misma ciudad donde se abrió la cuenta según el ingreso neto mensual:\n\n- *1 retiro:* Hasta S/1,799.\n- *2 retiros:* Desde S/1,800 hasta S/3,499.\n- *4 retiros:* Desde S/3,500 hasta S/6,999.\n- *10 retiros:* Desde S/7,000 a más.\n\nPara disfrutar del beneficio la Cuenta Sueldo debe estar asociada a una tarjeta de crédito o débito del BBVA Continental y aplica después de recibir un mes de abono de sueldo."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "*Ilimitados*: retiro de dinero a través de todos los cajeros BBVA a nivel nacional y transferencias entre cuentas (realizados en la misma localidad donde se contrató la cuenta) y consultas de saldos y movimientos."
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
            speech = "Sí, puedes utilizarla en la amplia red de establecimientos afiliados a Visa"
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "Sí, puedes utilizarla en la amplia red de establecimientos afiliados a Visa."
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
            speech = "Sí, cuando lo necesites."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "*Sí*. Solo en caso de haber participado de la campaña en vigencia canjeando un premio por apertura, se realizará una retención por el importe y tiempo indicado en las condiciones de la misma."
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
            speech = "No, sin embargo se pueden emitirse si así lo solicitas."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "No, sin embargo se pueden emitirse si así lo solicitas."
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

    if intentName == "no.secuencial.parametrica.pg1":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "Es una cuenta en la que puedes realizar operaciones en Soles y en Dólares al tipo de cambio del día. No mantiene los saldos separados por tipo de moneda. Tu saldo se guarda en la moneda que eliges al abrir la cuenta."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "Es una cuenta en la que puedes realizar operaciones en Soles y en Dólares a un tipo de cambio especial. No mantiene los saldos separados por tipo de moneda. Tu saldo se guarda en la moneda que eliges al abrir la cuenta."
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
    if intentName == "no.secuencial.parametrica.pg2":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "Nada, siempre y cuando tu Cuenta Sueldo reciba abonos de Pago de Haberes de manera consecutiva."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "El mantenimiento de cuenta mensual es variable, de acuerdo al saldo medio de tu cuenta:\n\n- Hasta S/ 900 o $ 300: S/ 8.00 o $ 3.00, respectivamente.\n- Mayor a S/ 900 o $ 300: *SIN COSTO*."
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
    if intentName == "no.secuencial.parametrica.pg3":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "Sí, los saldos están cubiertos por Fondo de Seguro Depósito hasta por S/98,894.00 (periodo junio – agosto 2018 N° B-2242-2018, sujeto a modificación trimestral por la SBS)."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "Sí, los saldos están cubiertos por Fondo de Seguro Depósito hasta por S/98,894.00 (periodo junio – agosto 2018 N° B-2242-2018, sujeto a modificación trimestral por la SBS)."
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
    if intentName == "no.secuencial.parametrica.pg4":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "No necesitas de un depósito mínimo para abrir tu Cuenta Sueldo."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "El depósito mínimo de apertura es S/ 300 o US$100."
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
    if intentName == "no.secuencial.parametrica.pg5":
        parameters = result.get("parameters")
        tiposdeproducto = parameters.get("tiposdeproducto")

        if tiposdeproducto == "Cuenta.Sueldo":
            speech = "Sí, siempre."
            return {
                "speech": speech,
                "displayText": speech
            }
        else:
            speech = "Sí, siempre."
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

















