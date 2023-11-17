try:
    with open('newfile.txt', 'w') as file:
        file.write("first line")
        
    with open('newfile.txt', 'a') as file:
        file.writelines(["\nfirst line", "\nanother line"])
except FileNotFoundError as e:
    print("ERROR", e)