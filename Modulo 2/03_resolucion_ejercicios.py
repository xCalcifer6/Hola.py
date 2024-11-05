
def un_anagrama(palabra_uno, palabra_dos):
    if palabra_uno.lower() == palabra_dos.lower():
        return False
    return sorted(palabra_uno.lower()) == sorted(palabra_dos.lower())

print(un_anagrama("Iman", "Mani"))


