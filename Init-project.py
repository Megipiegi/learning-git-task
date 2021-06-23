shopping_dictionary = {
    'optyk' : ['okulary', 'soczewki', 'etui'],
    'apteka' : ['paracetamol', 'bandaż']
}
for i, j in shopping_dictionary.items():
    print('Idę do', i.title(),',', 'kupuję tu następujące rzeczy', str(j).title())
total_elements=0
for j in shopping_dictionary:
    total_elements += len (shopping_dictionary[j])
print('w sumie kupuję:', total_elements, 'produktów')
