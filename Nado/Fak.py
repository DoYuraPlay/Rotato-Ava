from PIL import Image
print("то ты выберишь: Медведь или Мужик?")
oto=input("Я выбираю:  ")
if oto=="Медведь":
    image = Image.open('Chito.jpg')
    print("Ширина:",image.width)
    print("Высота:",image.height)
    print("Название:",image.filename)
    image.show()
    print("Сделать эту картинку Аватаркой?")
    h=input()
    if h=="Да":
        new_image=image.resize((150,150,), Image.LANCZOS)
        new_image.save("icon_Chito.jpg")
        image.close()
        new_image.close()
        print("Сделано")
    elif h=="Нет":
        print("Хорошо)")
elif oto=="Мужик":
    image = Image.open('Mugic.png')
    print("Ширина:",image.width)
    print("Высота:",image.height)
    print("Название:",image.filename)
    image.show()
    print("Сделать эту картинку Аватаркой?")
    k=input()
    if k=="Да":
        new_image=image.resize((150,150,), Image.LANCZOS)
        new_image.save("icon_Mugic.png")
        image.close()
        new_image.close()
        print("Сделано")
    elif k=="Нет":
        print("Хорошо)")