
from pprint import pprint
import re
import csv

with open("phonebook_raw.csv",encoding = "UTF-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  
pattern = r'(\+7|8)[-?\s*]?\(?(\d{3})\)?[-\s*]?(\d{3})[-\s*]?(\d{2})[-\s*]?(\d{2})[-\s*]?\(?(доб.)?\)?[\s*]?(\d+)?\)?'
substitution = r'8(\2)\3-\4-\5\6\7'
for person in contacts_list:
    phone_list = re.findall(pattern, person[5])
    person[5] = re.sub(pattern, substitution, person[5])

    
def full_name(contacts_list):
    for person in contacts_list:
        name = (person[0] + ' ' + person[1] + ' ' + person[2]).strip()
        splitted_name = name.split()
        person[0] = splitted_name[0] 
        person[1] = splitted_name[1]
        if len(splitted_name) == 3:
            person[2] = splitted_name[2]
    return(contacts_list)

def delete_doubled_persons(contacts_list):
    num=1
    cont_list = contacts_list[1:]
    for person in contacts_list[1:]:
        for per in cont_list[num:]:
            if person[0] == per[0] and person[1]==per[1]:
                if person[2] == '':
                    person[2] = per[2]
                if person[3] == '':
                    person[3] = per[3]
                if person[4] == '':
                    person[4] = per[4]
                if person[5] == '':
                    person[5] = per[5]
                if person[6] == '':
                    person[6] = per[6]
                contacts_list.remove(per)
        num +=1
    return(contacts_list)
              
        
full_name(contacts_list)
delete_doubled_persons(contacts_list)

with open("phonebook.csv", "w", encoding = 'utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)