from datetime import datetime
from pydantic import validator


class TaskValidators:
    @staticmethod
    @validator('dueDate')
    #Valida se a data não é no passado
    def validate_due_date(cls, v):
        if v and v < datetime.now():
            raise ValueError("A data de vencimento não pode ser no passado.")
        return v

    @staticmethod
    @validator('title')
    #Valida que o título tenha entre 3 e 100 caracteres.
    def validate_title(cls, v):
        if len(v) < 3:
            raise ValueError("O título deve ter pelo menos 3 caracteres.")
        if len(v) > 100:
            raise ValueError("O título não pode ter mais de 100 caracteres.")
        return v

    @staticmethod
    @validator('description')
    #Valida que a descrição não seja vazia ou muito curta.
    def validate_description(cls, v):
        if len(v.strip()) < 10:
            raise ValueError("A descrição deve ter pelo menos 10 caracteres.")
        return v
