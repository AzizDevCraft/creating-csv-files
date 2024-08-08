from faker import Faker 
import csv 

fake_data = Faker ("fr_FR") # fake french data 
headers = ["passport_id", "name", "gender", "phone_number"] #examples of headers
list_of_rows = []

def create_csv (file_name, rows) : 
    with open (f"{file_name}.csv", "w") as f : 
        file = csv.DictWriter (f, fieldnames=headers)
        file.writeheader ()
        for row in range (int(rows)) : 
            dict_data = {}
            dict_data["passport_id"] = fake_data.passport_number ()
            dict_data["name"] = fake_data.name ()
            dict_data["gender"] = fake_data.passport_gender ()
            dict_data["phone_number"] = fake_data.phone_number ()
            list_of_rows.append (dict_data)
        file.writerows(list_of_rows)
        
if __name__ == "__main__" : 
    file_name = input("donner le nom du fichier: ")
    rows = input ("donner le nombre des lignes :")
    create_csv (file_name, rows)
    