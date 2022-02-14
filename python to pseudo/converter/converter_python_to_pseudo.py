# Using readlines()
file1 = open('ulaz.py', 'r')
file2 = open('pseudo.txt', 'w')
Lines = file1.readlines()

#varijable
KojiNavodnici = ''
izlaznaRijec = ''
count = 0
odZnakaJednakosti = ''
imeTrenutneVarijable = ''
Pozicija1 = 0
Pozicija2 = 0
Pozicija3 = 0
Pozicija4 = 0
Pozicija5 = 0
Pozicija6 = 0
trenutniZnak = 0
BrojZareza = 0
WhilePetljaUvjet = ''
zadnjiSpace = 0
prednjiSpace = 0
prvaVarijabla = ''
drugaVarijabla = ''

#defovi
def Ulaz():
    zadnjiSpace = 0
    trenutniZnak = 0
    prednjiSpace = 0
    for Pozicija1 in range(len(line)):
        if line[Pozicija1] == "=":
            odZnakaJednakosti = line[Pozicija1:Pozicija1+15]
            for i in range(Pozicija1-1, 0, -1):
                if line[i] == " ":
                    zadnjiSpace = i
                    break
            imeTrenutneVarijable = line[zadnjiSpace-1:Pozicija1-1]
            if "input" in odZnakaJednakosti:
                if '()' in odZnakaJednakosti:
                    file2.write("ulaz(" + imeTrenutneVarijable + ")\n")
                else:
                    KojiNavodnici = "'"
                    for Pozicija3 in range(2):
                        for Pozicija2 in range(Pozicija1, Pozicija1+14, 1):
                            if line[Pozicija2] == KojiNavodnici:
                                Pozicija3 = Pozicija2+1
                                while line[Pozicija3] != KojiNavodnici:
                                    Pozicija3 += 1
                                c = line[Pozicija2:Pozicija3+1]
                                file2.write('izlaz(' + str(c) + ')\n')
                                file2.write("ulaz(" + imeTrenutneVarijable + ")\n")
                        KojiNavodnici = '"'

            elif line[Pozicija1 - 1] == '+' or line[Pozicija1 - 1] == '/' or line[Pozicija1 - 1] == '*' or line[Pozicija1 - 1] == '-' or line[Pozicija1 - 1] == '%':
                znak = line[Pozicija1 - 1]
                if line[Pozicija1 - 2] == "/" or line[Pozicija1 - 2] == "*":
                    znak = line[Pozicija1 - 1]
                    if line[Pozicija1 - 3] == ' ':
                        for Pozicija5 in range(Pozicija1 - 4, 0, -1):
                            if line[Pozicija5] == " " or Pozicija5 == 0:
                                prednjiSpace = Pozicija5
                                break
                        prvaVarijabla = line[prednjiSpace:Pozicija1 - 3]
                    else:
                        for Pozicija5 in range(Pozicija1 - 3, 0, -1):
                            if line[Pozicija5] == " " or Pozicija5 == 0:
                                prednjiSpace = Pozicija5
                                break
                        prvaVarijabla = line[prednjiSpace:Pozicija1 - 2]
#############################################################################
                    if line[Pozicija1 + 1] == ' ':
                        for Pozicija6 in range(Pozicija1 + 2, len(line)):
                            if line[Pozicija6] == " " or Pozicija6 == len(line) - 1:
                                print(Pozicija6)
                                zadnjiSpace = Pozicija6
                                break
                        drugaVarijabla = line[Pozicija1 + 2:Pozicija6]
                    else:
                        for Pozicija6 in range(Pozicija1 + 2, len(line)):
                            if line[Pozicija6] == " " or Pozicija6 == len(line) - 1:
                                print(Pozicija6)
                                zadnjiSpace = Pozicija6
                                break
                        drugaVarijabla = line[Pozicija1 + 1:Pozicija6]
#############################################################################
                    if znak == "*":
                        file2.write(prvaVarijabla + " = " + prvaVarijabla + " ^ " + drugaVarijabla + "\n")
                    elif znak == "/":
                        file2.write(prvaVarijabla + " = " + prvaVarijabla + " div " + drugaVarijabla + "\n")
#############################################################################
                else:
                    znak = line[Pozicija1 - 1]
                    
                    if line[Pozicija1 - 2] == ' ':
                        for Pozicija5 in range(Pozicija1 - 3, 0, -1):
                            if line[Pozicija5] == " " or Pozicija5 == 0:
                                prednjiSpace = Pozicija5
                                break
                        prvaVarijabla = line[prednjiSpace:Pozicija1 - 2]
                    else:
                        for Pozicija5 in range(Pozicija1 - 2, 0, -1):
                            if line[Pozicija5] == " " or Pozicija5 == 0:
                                prednjiSpace = Pozicija5
                                break
                        prvaVarijabla = line[prednjiSpace:Pozicija1 - 1]
#############################################################################
                    if line[Pozicija1 + 1] == ' ':
                        for Pozicija6 in range(Pozicija1 + 2, len(line)):
                            if line[Pozicija6] == " " or Pozicija6 == len(line) - 1:
                                print(Pozicija6)
                                zadnjiSpace = Pozicija6
                                break
                        drugaVarijabla = line[Pozicija1 + 2:Pozicija6]
                    else:
                        for Pozicija6 in range(Pozicija1 + 2, len(line)):
                            if line[Pozicija6] == " " or Pozicija6 == len(line) - 1:
                                print(Pozicija6)
                                zadnjiSpace = Pozicija6
                                break
                        drugaVarijabla = line[Pozicija1 + 1:Pozicija6]

                    if znak == "%":
                        file2.write(prvaVarijabla + " = " + prvaVarijabla + " mod " + drugaVarijabla + "\n")
                    else:
                        file2.write(prvaVarijabla + " = " + prvaVarijabla + " " + znak + " " + drugaVarijabla + "\n")
            else:
                if ":" not in line:
                    linija = line
                    pozicijaPos = linija.find("%")
                    pozicijaSl = linija.find("//")
                    if pozicijaPos != -1:
                        linija = "".join([linija[0:pozicijaPos], "mod", linija[pozicijaPos+1:len(linija)]])
                        file2.write(linija)
                    elif pozicijaSl != -1:
                        linija = "".join([linija[:pozicijaSl], "div", linija[pozicijaSl+2::]])
                        file2.write(linija)
                    else:
                        while line[trenutniZnak] == " ":
                            trenutniZnak += 1
                        for Pozicija4 in range(trenutniZnak, len(line)):
                            file2.write(line[Pozicija4])
#############################################################################
            
            
def Izlaz():
    izlaznaRijec = ""
    if "print" in line:
        for Pozicija1 in range(len(line)):
            if line[Pozicija1] == "p" and line[Pozicija1+1] == "r" and line[Pozicija1+2] == "i":
                for Pozicija2 in range(Pozicija1, len(line)):
                    if line[Pozicija2] == "(":
                        for Pozicija3 in range(Pozicija2+1, len(line)):
                            if line[Pozicija3] == ")":
                                break
                            izlaznaRijec += line[Pozicija3]  
                        file2.write("izlaz(" + izlaznaRijec + ")\n")

def Tab():
    trenutniZnak = 0
    while line[trenutniZnak] == " ":
        trenutniZnak += 1
        file2.write(" ")

def RedPrazan():
    if line == "\n":
        file2.write("\n")

def If():
    if "if" in line:
        linija = line
        pozicijaPos = linija.find("%")
        pozicijaSl = linija.find("//")
        if pozicijaPos != -1:
            linija = "".join([linija[0:pozicijaPos], "mod", linija[pozicijaPos+1:len(linija)]])
        elif pozicijaSl != -1:
            linija = "".join([linija[:pozicijaSl], "div", linija[pozicijaSl+2::]])

        file2.write("ako je ")
        for Pozicija1 in range(len(line)):
            if line[Pozicija1] == "i" and line[Pozicija1+1] == "f":
                pozicijaJedJed = linija.find("=")
                linija = "".join([linija[:pozicijaJedJed], linija[pozicijaJedJed+1::]])
                for Pozicija2 in range(Pozicija1 + 3, len(linija)):
                    if linija[Pozicija2] == ":":
                        break
                    else:
                        file2.write(linija[Pozicija2])
        file2.write(" onda\n")
                
def Else():
    if "else" in line:
        file2.write("inače\n")

def While():
    WhilePetljaUvjet = ''
    if "while" in line:
        for Pozicija1 in range(len(line)):
            if line[Pozicija1] == 'w' and line[Pozicija1 + 1] == 'h' and line[Pozicija1 + 2] == 'i' and line[Pozicija1 + 3] == 'l' and line[Pozicija1 + 4] == 'e':
                Pozicija2 = Pozicija1 + 6
                for Pozicija2 in range(Pozicija1 + 6, len(line), 1):
                    if line[Pozicija2] != ':':
                        WhilePetljaUvjet += line[Pozicija2]
                    else:
                        break
                file2.write('dok je ' + WhilePetljaUvjet + ' činiti\n')

def For():
    BrojZareza = 0
    pozicijaR = 0
    pozicijaI = 0
    pozivijaOdKud = 0
    pozivijaDoKud = 0
    PozicijaZareza = 0
    PozicijaZareza1 = 0
    PozicijaZareza2 = 0
    if "for" in line:
        for Pozicija1 in range(len(line)):
            if line[Pozicija1] == "f" and line[Pozicija1 + 1] == "o" and line[Pozicija1 + 2] == "r":
                pozicijaR = Pozicija1 + 4
            if line[Pozicija1] == "i" and line[Pozicija1 + 1] == "n":
                pozicijaI = Pozicija1
            if line[Pozicija1] == "(":
                pozicijaOdKud = Pozicija1 + 1
            if line[Pozicija1] == ")":
                pozicijaDoKud = Pozicija1
            if line[Pozicija1] == ",":
                BrojZareza += 1
                
        if BrojZareza == 0:
            file2.write("za " + line[pozicijaR:pozicijaI] + "= 0 do " + line[pozicijaOdKud:pozicijaDoKud] + " činiti\n")

        if BrojZareza == 1:
            for Pozicija2 in range(len(line)):
                if line[Pozicija2] == ",":
                    PozicijaZareza = Pozicija2
                    break
            file2.write("za " + line[pozicijaR:pozicijaI] + "= " + line[pozicijaOdKud:PozicijaZareza] + " do" + line[PozicijaZareza+1:pozicijaDoKud] + " činiti\n")

        if BrojZareza == 2:
            for Pozicija2 in range(len(line)):
                if line[Pozicija2] == ",":
                    PozicijaZareza1 = Pozicija2
                    break
            for Pozicija3 in range(Pozicija2, len(line)):
                if line[Pozicija3] == ",":
                    PozicijaZareza2 = Pozicija3

#builder
for line in Lines:
    print(line.strip())

    RedPrazan()
    Tab()
    If()
    Else()
    For()
    While()
    Ulaz()             
    Izlaz()
    
file2.close()
