import monkeylearn

from monkeylearn import MonkeyLearn

ml = MonkeyLearn('<<Your API key here>>')
data = ['Very helpful and friendly staff.', 'Bed was extremely comfortable.']
model_id = 'cl_TKb7XmdG' # Revisar el model_id para análisis de sentimientos
result = ml.classifiers.classify(model_id, data)

print(result.body)

