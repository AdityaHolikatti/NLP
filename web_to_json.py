import re
import json
#####3
import io 
word_list = []
f = open('parses.json')
for line in f:
	encoded = json.loads(line)
	strings = encoded[0]['parseText']
	buf = io.StringIO(strings)
	for line in buf.readlines():
		#print line
		if('((' in line):
			tokens = line.split()
			#word_attr = []
			word_attr = ['','','root']
			for token in tokens:
				if '=' in token:
					key = token.split('=')[0]
					value = token.split('=')[1]
					if(key == 'head'):
						#word_attr.append(value)
						word_attr[0] = re.findall(r'"([^"]*)"', value)[0]
					if(key == 'name'):
						#word_attr.append(value)
						word_attr[1] = re.findall(r'"([^"]*)"', value)[0]
					if(key == 'drel'):
						word_attr[2] = re.findall(r'"([^"]*)"', value)[0]
						#word_attr.append(value)
					#print(word_attr)
			word_list.append(word_attr)
		line = f.readline()
	print(word_list)
	subject = ''
	obj = ''
	qty = 'x'
	for each_word in word_list:
		if each_word[2] != 'root' and each_word[2].split(':')[0] == 'k1':
			#print('subject : '+each_word[0])
			subject = subject+ each_word[0]
		if each_word[2] != 'root' and each_word[2].split(':')[0] == 'k2':
			#obj = obj+ each_word[0]
			qty = each_word[0]
		if each_word[2] != 'root' and each_word[2].split(':')[0] == 'pof':
			obj = obj+' '+ each_word[0]
		if each_word[2] != 'root' and each_word[2].split(':')[0] == 'JJP':
			obj = obj+' '+ each_word[0]
			#pos = re.findall(r'"([^"]*)"', line)
			#print(pos[0])
	print('subject : '+subject)
	print('object : '+obj)
	print('qty : '+qty)
		


'''
f = open('parses.json')
word_list = []
for each_line in f:
	encoded = json.loads(each_line)
	line = encoded[0]['parseText']
	print(line)
	print("here")
	
'''




f.close()

'''
######33
################## target 'ne' and  'se'
#f = open('web_op.txt').read()
#inp = json.loads(f)
#print(inp)
line = f.readline()
word_list = []
while(line):
	if('((' in line):
		tokens = line.split()
		#word_attr = []
		word_attr = ['','','root']
		for token in tokens:
			if '=' in token:
				key = token.split('=')[0]
				value = token.split('=')[1]
				if(key == 'head'):
					#word_attr.append(value)
					word_attr[0] = re.findall(r'"([^"]*)"', value)[0]
				if(key == 'name'):
					#word_attr.append(value)
					word_attr[1] = re.findall(r'"([^"]*)"', value)[0]
				if(key == 'drel'):
					word_attr[2] = re.findall(r'"([^"]*)"', value)[0]
					#word_attr.append(value)
				#print(word_attr)
		word_list.append(word_attr)
	line = f.readline()
print(word_list)
subject = ''
obj = ''
qty = 'x'
for each_word in word_list:
	if each_word[2] != 'root' and each_word[2].split(':')[0] == 'k1':
		#print('subject : '+each_word[0])
		subject = subject+ each_word[0]
	if each_word[2] != 'root' and each_word[2].split(':')[0] == 'k2':
		#obj = obj+ each_word[0]
		qty = each_word[0]
	if each_word[2] != 'root' and each_word[2].split(':')[0] == 'pof':
		obj = obj+' '+ each_word[0]
	if each_word[2] != 'root' and each_word[2].split(':')[0] == 'JJP':
		obj = obj+' '+ each_word[0]
		#pos = re.findall(r'"([^"]*)"', line)
		#print(pos[0])
print('subject : '+subject)
print('object : '+obj)
print('qty : '+qty)


class container:
	def __init__(self,subject,obj,quant):
		self.subject = subject
		self.obj = obj
		self.quant = quant

sent1 = container(subject,obj,qty)

'''