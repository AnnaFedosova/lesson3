with open ('referat.txt', 'r', encoding = "utf-8") as referat:
    content = referat.read()
    content = content.replace ('.','!')
    print(content)
    print(len(content))
    with open ('referat2.txt', 'w', encoding = "utf-8") as referat2:
        referat2 = referat2.write(content)