#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "verificarCpf":
        return {}
    # baseurl = "https://query.yahooapis.com/v1/public/yql?"
    # yql_query = makeYqlQuery(req)
    # if yql_query is None:
    #     return {}
    # yql_url = baseurl + urllib.urlencode({'q': yql_query}) + "&format=json"
    # result = urllib.urlopen(yql_url).read()
    # data = json.loads(result)
    # res = makeWebhookResult(data)

    cpf = int(req.get("result").get("parameters").get("cpf").get("number"))
    texto = "jufs"
    contexts = []
    if cpf is 123:
        texto = "Você ainda não é cliente do Banco Agiplan? Então seja bem vindo! Você é funcionário público, aposentado ou pensionista?"
        contexts.append({ "name": "creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-épublicoalvo", "lifespan": 2 })
        contexts.append({ "name": "creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-nãoépublicoalvo", "lifespan": 2 })
    else:
        texto = "Sua fonte pagadora continua sendo o INSS?"
        contexts.append({ "name": "creditoconsignado-solicitacaoemprestimo-confirmardadoscliente", "lifespan": 2 })

    return {
        "speech": texto,
        "displayText": texto,
        # "data": data,
        "contextOut": contexts,
        "source": "apiai-weather-webhook-sample"
    }


def makeYqlQuery(req):
    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("cpf")
    if city is None:
        return None

    return "select * from weather.forecast where woeid in (select woeid from geo.places(1) where text='" + city + "')"


def makeWebhookResult(data):
    query = data.get('query')
    if query is None:
        return {}

    result = query.get('results')
    if result is None:
        return {}

    channel = result.get('channel')
    if channel is None:
        return {}

    item = channel.get('item')
    location = channel.get('location')
    units = channel.get('units')
    if (location is None) or (item is None) or (units is None):
        return {}

    condition = item.get('condition')
    if condition is None:
        return {}

    # print(json.dumps(item, indent=4))

    speech = "Today in " + location.get('city') + ": " + condition.get('text') + \
             ", the temperature is " + condition.get('temp') + " " + units.get('temperature')

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
