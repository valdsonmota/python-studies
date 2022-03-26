#Exercise 5-1 Conditional Tests - Drones
brand = 'dji'
models = ['mavic 3', 'air 2s', 'mini 2', 'mini se', 'fpv', 'phantom 4 pro', 'phantom 4 pro v2.0', 'inspire 2']
for model in models:
    if model.lower() == 'fpv':
        print(brand.upper(), model.upper())
    else:
        print(brand.upper(), model.title())
