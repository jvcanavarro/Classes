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
