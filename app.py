#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import json
import os

from flask import Flask,request,make_response

app = Flask(__name__)

contextoSaida = 'creditoconsignado-solicitacaoemprestimo-dto'

class Result:
    def __init__(self, action, parameters):
      self.action = action
      self.parameters = parameters

class WebhookRequest(object):
   def __init__(self, result):
      self.result = result

class WebhookResponse:
   def __init__(self, speech, displayText, data, contextOut):
      self.speech = speech
      self.displayText = displayText
      self.data = data
      self.contextOut = contextOut
      self.source = 'apiai-weather-webhook-sample'

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    req = WebhookRequest(json.loads(req.result))

    res = processRequest(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def processRequest(req):
    action = req.result.action
    print('action: '+action)

    if action == 'verificarCpf':
        return verificarCpf(req)
    
    return {}

def verificarCpf(req):
    textoSaida = ''
    contextosDeSaida = []

    cpf = int(req.result.parameters['cpf']['number'])
    print('cpf: ' + cpf)

    if cpf is 123:
        contextosDeSaida.append({"name":contextoSaida, "lifespan":5, "parameters":{ "perfilCliente":"aposentado", "fontePagamento":"INSS" }})
        textoSaida = ' Ah, então você já é cliente! Agora preciso confirmar alguns dados com você: O INSS continua sendo sua fonte pagadora?'        
    else:
        textoSaida = ' Você ainda não é cliente do Banco Agiplan? Então seja bem vindo! Você é funcionário público, aposentado ou pensionista?'

    return WebhookResponse(textoSaida, textoSaida, None, contextosDeSaida)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

app.run(debug = False, port = port, host = '0.0.0.0')