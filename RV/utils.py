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

    for i in dataset_1:
        direct_order.append(
            Mantic.mantic.get(answer_keys.get(i), 'Ne zapolneno')
        )

    for i in dataset_2:
        reverse_order.append(
            Mantic.mantic.get(answer_keys.get(i), 'Ne zapolneno')
        )

    return direct_order, reverse_order
