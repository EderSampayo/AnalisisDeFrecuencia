# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




#Programa Análisis de Frecuencia

Alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
frecuAlta = ['e','a','o','l', 's', 'n', 'd', 'r', 'u']

from collections import Counter

texto = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
letras = Counter(texto)
print("cantidad de letras = ", len(letras))
print(len(Alfabeto))
print(letras)

texto = texto.replace('X', 'e')
texto = texto.replace('E', 'a')
texto = texto.replace('T', 'l')
texto = texto.replace('A', 'd')
texto = texto.replace('N', 's')
texto = texto.replace('Z', 'u')
texto = texto.replace('S', 'q')
texto = texto.replace('K', 'r')
texto = texto.replace('C', 'i')
texto = texto.replace('H', 't')
texto = texto.replace('U', 'g')
texto = texto.replace('D', 'p')
texto = texto.replace('R', 'c')
texto = texto.replace('I', 'o')
texto = texto.replace('O', 'f')
texto = texto.replace('P', 'm')
texto = texto.replace('Q', 'b')
texto = texto.replace('V', 'y')
texto = texto.replace('G', 'j')
texto = texto.replace('H', 'j')
texto = texto.replace('F', 'x')
texto = texto.replace('M', 'h')
texto = texto.replace('J', 'n')
texto = texto.replace('L', 'z')

print(texto)