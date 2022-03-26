#Exercise 5-1 Conditional Tests - Drones
brand = 'dji'
models = ['mavic 3', 'air 2s', 'mini 2', 'mini se', 'fpv', 'phantom 4 pro', 'phantom 4 pro v2.0', 'inspire 2']
new_model = 'mini 3'
if new_model.lower() not in models:
    print('\n' + brand.upper(), new_model.title(), 'NOT registered in the list of models.\n')
else:
    print('\n' + brand.upper(), new_model, 'already registered in the list of models.\n')
