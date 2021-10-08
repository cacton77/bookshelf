import os
import json
import random

def check_shelf(shelf_path):
    shelf_dict = {}
    files = os.listdir(shelf_path)
    books = []
    for file in files:
        if file == "bookshelf":
            continue
        elif file == "desktop.ini":
            continue
        if os.path.isdir(os.path.join(shelf_path, file)):
            sub_shelf_dict = check_shelf(os.path.join(shelf_path, file))
            shelf_dict.update({file: sub_shelf_dict})
        elif os.path.isfile(os.path.join(shelf_path, file)):
            books.append(file)
    shelf_dict.update({"books": books})
    return shelf_dict

def write_index(shelf_path, lib_dict):
    html_str = ""
    for key in lib_dict.keys():
        if type(lib_dict.get(key)) == dict:
            shelf = lib_dict.get(key)
            html_str += "<h2></h2><h2>" + key + "</h2>"
            html_str += write_index(shelf_path + "/" + key, shelf)
        elif type(lib_dict.get(key)) == list:
            books = lib_dict.get(key)
            html_str += "</h2><section class=\"tiles\">"
            for book in books:
                html_str += "<article class=\"style" + str(random.randint(1, 6)) + "\"><span class=\"image\"><img src=\"images/adv_eng_math.png\" alt=\"\" /></span><a href=\"" + shelf_path + "/" + book + "\" target=\"_blank\"><h2>" + book[0:-4] + "</h2><div class=\"content\"><h4>Author</h4></div></a></article>"
            html_str += "</section>"
    return html_str

if __name__ == "__main__":
    main_shelf_path = "C:\\Users\\Colin\\OneDrive\\Books"
    lib_dict = check_shelf(main_shelf_path)
    with open('lib_dict.json', 'w') as json_file:
        json.dump(lib_dict, json_file)
    html_str = "<div id=\"main\"><div class=\"inner\"><header><h1>Bookshelf</h1></header>" + write_index(main_shelf_path, lib_dict) + "</div></div></body></html>"
    with open('index.html', 'r') as f:
        lines = []
        i = 0
        for line in f:
            print(str(i) + ": " + line)
            if line.startswith("<!-- Main -->"):
                line = "<!-- Main -->" + html_str
                lines.append(line)
            else:
                lines.append(line)
            i += 1
    with open('index.html', 'w') as f:
        for line in lines:
            f.write(line)
