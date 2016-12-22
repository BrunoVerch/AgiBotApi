#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout

app = Flask(__name__)

contextos = [
    'creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-épublicoalvo'
    'creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-naoépublicoalvo'
    'creditoconsignado-solicitacaoemprestimo-confirmardadoscliente'
    'creditoconsignado-solicitacaoemprestimo-dto'
]

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    res = processRequest(req)

    res = json.dumps(res, indent=4)

    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    action = req.get('result').get('action')

    if action == 'verificarCpf':
        return verificarCpf(req)
    if action == 'efetuarSimulacao':
        return efetuarSimulacao(req)
    
    return {}

def efetuarSimulacao(req):
    return ''

def verificarCpf(req):
    textoSaida = ''
    contextosDeSaida = []

    cpf = int(req.get('result').get('parameters').get('cpf').get('number'))

    if cpf is 123:
        contextosDeSaida.append({"name":contextos[2], "lifespan":2, "parameters":{}})
        
        contextosDaRequisicao = req.get('result').get('contexts')
        dto = [v for v in contextosDaRequisicao if v.get('name') == contextos[3]]
        dto[0].get('parameters')['fontePagamento'] = 'INSS'

        textoSaida = ' Ah, ent\xc3\xa3o voc\xc3\xaa j\xc3\xa1 \xc3\xa9 cliente!,Agora preciso confirmar alguns dados com voc\xc3\xaa: \n                     O INSS|SIAPE|ETC continua sendo sua fonte pagadora?'        
    else:
        contextosDeSaida.append({"name":contextos[1], "lifespan":3, "parameters":{}})
        contextosDeSaida.append({"name":contextos[0], "lifespan":6, "parameters":{}})
        textoSaida = ' Voc\xc3\xaa ainda n\xc3\xa3o \xc3\xa9 cliente do Banco Agiplan?,Ent\xc3\xa3o seja bem vindo!,\n                     Voc\xc3\xaa \xc3\xa9 funcion\xc3\xa1rio p\xc3\xbablico, aposentado ou pensionista?'

    return {
        'speech': textoSaida,
        'displayText': textoSaida,
        'contextOut': contextosDeSaida,
        # "data": data,
        'source': 'apiai-weather-webhook-sample',
        }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    app.run(debug=False, port=port, host='0.0.0.0')
