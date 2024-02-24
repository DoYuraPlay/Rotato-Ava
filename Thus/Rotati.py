from PIL import Image
image=Image.open('GF.jpg')
image.show()
print("Куда повернёшь?")
h=input("Ответ:   ")
if h=="90гЛево":
    new_image=Image.open('GF.jpg')
    new_image=image.rotate(90)
    new_image.save("rotated_GF.jpg")
elif h=="90гПраво":
    new_image=Image.open('GF.jpg')
    new_image=image.rotate(270)
    new_image.save("rotate_GF.jpg")
elif h=="180г":
    new_image=Image.open('GF.jpg')
    new_image=image.rotate(180)
    new_image.save("rotat_GF.jpg")
else:
    print("На русском можно?")