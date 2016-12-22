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
    "number": 1233
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
        "number": 123,
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
        "number": 123,
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

contextos = [
    'creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-épublicoalvo',
    'creditoconsignado-solicitacaoemprestimo-solicitarperfilcliente-naoépublicoalvo',
    'creditoconsignado-solicitacaoemprestimo-confirmardadoscliente',
    'creditoconsignado-solicitacaoemprestimo-dto',
]


contextosDaRequisicao = req.get('result').get('contexts')
dto = [v for v in contextosDaRequisicao if v.get('name') == contextos[3]]
dto[0].get('parameters')['perfilCliente'] = 'aposentado'
dto[0].get('parameters')['fontePagamento'] = 'INSS'

print(dto[0].get('parameters')['perfilCliente'])