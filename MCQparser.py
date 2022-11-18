import re
import pandas as pd

file = open('MCQ.txt',encoding = 'utf-8')

raw_text = file.read()
text = raw_text
#text = raw_text.replace('\n','' ).replace('\t', '' )

questions = re.findall('[0-9]+?-(.+?\?)', text)
answer_a = re.findall('A\.(.+?)\n',text)
answer_b = re.findall('B\.(.+?)\n',text)
answer_c = re.findall('C\.(.+?)\n',text)
answer_d = re.findall('D\.(.+?)\n',text)

df = pd.DataFrame(zip(questions, answer_a, answer_b, answer_c, answer_d), 
                 columns = ['question', 'A', 'B', 'C', 'D'])

df.index = df.index + 1

df.to_csv('parsed_MCQ.csv', index = True, encoding='utf-8-sig') 