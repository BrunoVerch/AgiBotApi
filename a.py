import json

req = {
"id": "4c074725-ac86-4eb1-a75d-cfea6b7dbbfe",
"timestamp": "2016-12-21T20:21:05.762Z",
"result": {
"source": "agent",
"resolvedQuery": "767",
"action": "verificarCpf",
"actionIncomplete": False,
"parameters": {
    "cpf": {
    "number": 767
    }
},
"contexts": [
    {
    "name": "creditoconsignado-solicitacaoemprestimo-confirmardadoscliente",
    "parameters": {
        "cpf.original": "767",
        "cpf": {
        "number": 767,
        "number.original": "767"
        }
    },
    "lifespan": 5
    },
    {
    "name": "creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-épublicoalvo",
    "parameters": {
        "cpf.original": "767",
        "cpf": {
        "number": 767,
        "number.original": "767"
        }
    },
    "lifespan": 5
    },
    {
    "name": "creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-naoépublicoalvo",
    "parameters": {
        "cpf.original": "767",
        "cpf": {
        "number": 767,
        "number.original": "767"
        }
    },
    "lifespan": 5
    },
    {
    "name": "creditoconsignado-solicitacaoemprestimo",
    "parameters": {
        "cpf.original": "767",
        "cpf": {
        "number": 767,
        "number.original": "767"
        }
    },
    "lifespan": 4
    },
    {
    "name": "creditoconsignado-solicitacaoemprestimo-dto",
    "parameters": {
        "cpf.original": "767",
        "cpf": {
        "number": 767,
        "number.original": "767"
        }
    },
    "lifespan": 5
    }
],
"metadata": {
    "intentId": "00cbad05-b5d8-4778-b6f6-2f6a6d30a061",
    "webhookUsed": "true",
    "webhookForSlotFillingUsed": "false",
    "intentName": "creditoconsignado.solicitacaoemprestimo"
},
"fulfillment": {
    "speech": "",
    "messages": [
    {
        "type": 0,
        "speech": ""
    }
    ]
},
"score": 1
},
"status": {
"code": 206,
"errorType": "partial_content",
"errorDetails": "Webhook call failed. Error message: org.springframework.web.client.HttpServerErrorException: 500 INTERNAL SERVER ERROR ErrorId: 1341380d-2ef2-4f61-b0f1-f56113eecb4d"
},
"sessionId": "99ff8f91-9de9-4d7a-aa57-1b5e4a0c1cc3"
}
print(req.get("contexts"))
speech = 'aa'
ctx = 'creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-épublicoalvo'
ctx1 = 'creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-naoépublicoalvo'
ctx2 = 'creditoconsignado-solicitacaoemprestimo-confirmardadoscliente'

cpf = int(req.get('result').get('parameters').get('cpf'
            ).get('number'))
print(cpf)

arr = req.get('result').get('contexts')
if cpf is 123:
    speech = \
        ' Ah, ent\xc3\xa3o voc\xc3\xaa j\xc3\xa1 \xc3\xa9 cliente!,Agora preciso confirmar alguns dados com voc\xc3\xaa: \n                     O INSS|SIAPE|ETC continua sendo sua fonte pagadora?'
    arr = [v for v in arr if v.get('name') != ctx and v.get(name) != ctx1 ]
else:
    speech = \
        ' Voc\xc3\xaa ainda n\xc3\xa3o \xc3\xa9 cliente do Banco Agiplan?,Ent\xc3\xa3o seja bem vindo!,\n                     Voc\xc3\xaa \xc3\xa9 funcion\xc3\xa1rio p\xc3\xbablico, aposentado ou pensionista?'
    arr = [v for v in arr if v.get('name') != ctx2 ]