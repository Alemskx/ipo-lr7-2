import json
num = input("Введите номер квалификации: ")
find = False
with open("dump.json", 'r', encoding='utf-8') as file: 
    source_file = json.load(file)
    #Квалификация 
    for skill in source_file:
        if skill.get("model") == "data.skill" and skill.get("fields").get("code")==num:
            skill_code = skill.get("fields").get("code")
            skill_title =  skill_title = skill.get("fields").get("title")
            find = True
            #Cпециальность
            for profes in source_file:
                if profes.get("model") == "data.specialty":
                    if profes.get("fields").get("code") in num:
                        profes_code = profes.get("fields").get("code")
                        profes_title = profes.get("fields").get("title")
                        profes_type = profes.get("fields").get("c_type")
            break    
#Вывод        
if not find:
    print("=" * 20, "Не найдено", "=" * 20)
else:
    print(f"{skill_code} >> Квалификация '{skill_title}'")
    print(f"{profes_code} >> Специальность '{profes_title}', {profes_type}")