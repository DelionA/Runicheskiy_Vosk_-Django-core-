from .order_answer import *
from .mantic import *

def generate_order_answer(form_cleaned_data):
    answer_keys = dict()
    direct_order = list()
    reverse_order = list()
    for i in form_cleaned_data:
        for j in form_cleaned_data:
            if i < j:
                answer_keys[i+j] = form_cleaned_data[i] + form_cleaned_data[j]
            elif i > j:
                answer_keys[i+j]= form_cleaned_data[i] + form_cleaned_data[j]

    return answer_keys
