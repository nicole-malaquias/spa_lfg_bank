import random
import time
from lfg_bank.celery_config import app
from .models import Proposal

@app.task
def funcao_com_atraso(proposal_id):
    try:
        obj = Proposal.objects.get(id=proposal_id)
        resultado = random.choice([True, False])
    
        if resultado:
            print("A função retornará imediatamente com resultado True.")
        else:
            print("A função levará até 10 segundos e retornará False.")
            time.sleep(random.uniform(0, 10))  # Introduza um atraso de até 10 segundos
        obj.aproved = resultado
        obj.save()
        return resultado
    except Proposal.DoesNotExist:
        print(f"Objeto Proposal com ID {proposal_id} não encontrado.")
        return False

