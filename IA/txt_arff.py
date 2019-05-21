<<<<<<< HEAD
def identify_items_of_column(data, index):
    unique_attribute_items = []
    for line in data:
        if line[index] not in unique_attribute_items:
            unique_attribute_items.append(line[index])
    return '{' + ','.join(sorted(unique_attribute_items)) + '}'


def convert(filename):
    text_file = open(filename).read().splitlines()

    arff_name = filename[:-4]  # remove '.txt'
    arff_file = open(arff_name + '.arff', 'w')
    arff_file.write('@relation ' + arff_name + '\n\n')

    file_lines = [line.split(' ') for line in text_file]

    # Attributes
    for i in range(len(file_lines[0])):
        if isinstance(file_lines[1][i], str):  # Nominal Attribute
            items = identify_items_of_column(file_lines[1:], i)
            arff_file.write(
                '@attribute ' + str(file_lines[0][i]) + ' nominal ' + items + '\n')

        else:  # Numeric Attribute
            arff_file.write(
                '@attribute ' + str(file_lines[0][i]) + ' numeric\n')

    # Data
    arff_file.write('\n@data\n')
    for row in file_lines:
        arff_file.write(','.join(row) + '\n')

    arff_file.close()

# João Victor da Silva Dias Canavarro
# Colunas Adicionadas: Eat_Meat(nominal) e ID(numeric).
convert('mammals.txt')
=======
def convert(filename):
    with open(filename) as text_file:
    	arff_content = []
    	for row in text_file:
    		arff_content.append(row)
    	
    	arff_name = filename + 'arff'
    	arff_file = open(arff_name, 'w')

    	arff_file.write('@relation ' + arff_name + '\n\n')

    	for i in range(len(arff_content[0])):

    		
convert('mammals.txt')
>>>>>>> 74278d2a833534b84e8385b746c45178b4fd68b3
