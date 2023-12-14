    #davaleba1
import json

def get_user_info():
    user_info = {}
    user_info['name'] = input("Tqveni saxeli: ")
    user_info['age'] = int(input("Tqveni asaki: "))
    user_info['email'] = input("Tqveni email: ")
    user_info['address'] = input("Tqveni misamarti: ")
    return user_info

def save_to_json(data, filename='user_info.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print(f'informacia shenaxulia {filename} failshi.')

def main():
    user_info = get_user_info()

    save_to_json(user_info)

if __name__ == "__main__":
    main()







    #davaleba2
import json

def load_from_json(filename='user_info.json'):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
        print(f'Data aghebulia {filename}.')
        return data
    except FileNotFoundError:
        print(f'Error: Faili "{filename}" ar moidzebna.')
        return None

def edit_user_info(data):
    if data:
        #vvaraudob rom email sheeshleba xalxs
        new_email = input("Sheiyvanet tqveni Emaili: ")
        data['email'] = new_email
        print("informacia ganaxlebulia.")
    return data

def save_to_json(data, filename='user_info.json'):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print(f'Data shenaxulia {filename} failshi.')

def main():
    user_info = load_from_json()

    edited_info = edit_user_info(user_info)

    if edited_info:
        save_to_json(edited_info)

if __name__ == "__main__":
    main()



