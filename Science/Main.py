##Nathan Hinton
#
#TODO:
#working on splitMolic


#import stuff
print("Importing")
import pickle#for loading the file

#Setup state machine error:
class StateMachineError(Exception):
    pass

#Main class
class Science:
    def __init__(self):
        #Load the file as eleList
        print("Loading File")
        pklFile = 'elementlist.pkl'
        dat = pickle.load(open(pklFile, 'rb'))#open('/NathanShare/School/Science2018-2019/elementlist.pkl', 'rb'))
        #dat = dat.read()
        dat = dat.replace('\n', '|')#Remove the newlines and add the pipes to seperate elements.
        eleList = dat.split('|')
        ###########################################
        print("Defining stuff")
        valance = [2, 10, 18, 36, 54, 86, 118]
        MOLE = 6.02*10**27
        return pklFile, eleList, valance, MOLE

    #Calc Atom stuff

    def updatePkl(self, fname, pklFile):
        newDatFile = open(str(fname), 'r')
        newDat = newDatFile.read()
        newDatFile.close()
        print("Loaded data to newDat.  here is data: %s" %newDat)
        print("Backing up pkl file...")
        origPkl = open(pklFile, 'rb')
        bupPkl = open(pklFile+'.bup', 'wb')
        bupPkl.write(origPkl.read())
        bupPkl.close()
        origPkl.close()
        print("pkl backed up. rewriting data to pkl...")
        origPkl = open(pklFile, 'wb')
        pickle.dump(newDat, origPkl)
        origPkl.close()
        print("Data written!")
        print()
        print("Program restart required for changes to make affect.")
        #print("<<<NOT FINISHED>>>")

    def PD(self, item):
        #print('PD (ProcessData) was ran.')
        lst = []
        #Process string:
        if type(item) == str:
            lst = item.split(' ')
        elif type(item) == list:
            for x in range(len(item)):
                try:
                    lst.append(float(item[x]))
                except ValueError:
                    print("ValueError processed")
                    lst.append(item[x])
        else:
            print()
            print("                !!!WARNING!!!")
            print("Unknown or unrecognized data type. returning empty list")
        return lst

    def CalcAtom(self):
        print("Type 0 or 1")
        i = int(input())
        try:
            if i == 0: #When you have the parts not the name
                z = int(input("Protons: "))# (Number of Protons)
                e = int(input("Electrons: "))# (Number of Electrons)
                n = int(input("Neutrons (None if unknown): "))# (Number of Neutrons)

                if n == 'None':
                    a = "Not able to find!"
                else:
                    a = z+n
                charge = z-e

                #Atom number = Z
                #Atomic mass = A

                print('Element is: \n'+str(eleList[z-1]))
                print('Protons: '+str(z))
                print('electrons: '+str(e))
                print('Neutrons: '+str(n))
                print('Atomic weight: '+str(a))
                print('Charge: '+str(charge))
            elif i == 1: #Other stff
                z = int(input("Protons: "))# (Number of Protons)
                #e = int(input("Electrons: "))# (Number of Electrons)
                #n = int(input("Neutrons: "))# (Number of Neutrons)
                charge = int(input("Charge: "))
                a = int(input("Mass: "))

                #a = z+n
                n = a-z
                #charge = z-e
                e = z-charge

                #Atom number = Z
                #Atomic mass = A

                print('Element is: \n'+str(eleList[z-1]))
                print('Protons: '+str(z))
                print('electrons: '+str(e))
                print('Neutrons: '+str(n))
                print('Atomic weight: '+str(a))
                print('Charge: '+str(charge))
            else:
                print("Error")
        except IndexError:
            print("Index error! This could be from missing data in the pkl file. Try running the update function to make sure that the data matches.  This also could be caused by a bug in the progtam.  If you look in the elementlist.txt file and make sure that the data you are requesting is there and then update the pkl file and the error persists then there is an error in the program.")

    def main(self):
        while True:
            #input portion:
            print("There are several different inputs:")
            print("0 = you have the element and want the info")
            print("1 = stoichometry")
            print("2 = limit reagent problem")
            i = input()
            #logic:
            if i == '0':
                ele = findAtom(input("the chars in lowercase:"))
            elif i == '1':
                stoi()
            elif i == '2':
                limitReagent()
            else:
                print('Input error...')

    def findAtom(self, char):
        for x in range(len(eleList)):
            #print(eleList[x]) #Noise reduction
            ele = PD(eleList[x])
            try:
                if ele[1].lower() == str(char):
                    print(ele)
                    return(ele)
            except IndexError:
                print("IndexError processed.")
                print("Elemment not in the list or the abbr was typed wrong")
                findAtom(input("Try again, element:  "))

    def amu(self, eleAbbr):
        ele = findAtom(eleAbbr)
        ele = PD(ele)
        return ele[3]    

    def stoi(self, ):
        add = True
        amu = 0
        equList = []
        i = str(input('element to be processed:  '))
        while add == True:
            ele = findAtom(i.lower())
            ele = PD(ele)
            amu = ele[3] + amu
            equList.append(ele[1])
            i = input('are you done? ("no"):  ')
            if i == 'no':
                add = False
            #i2 = inp'how many grams do you have of %s:  ' %s = i)
        print('how many grams do you have of %s:  ' %equList)
        i2 = float(input())
        mol = round(round(i2, 3)/round(amu, 2), 3)
        print()
        print(mol)
        return mol, (equList, amu)

    def stoi2(self, moles):
        add = True
        amu = 0
        equList = []
        i = str(input('element to be processed:  '))
        while add == True:
            ele = findAtom(i.lower())
            ele = PD(ele)
            amu = ele[3] + amu
            equList.append(ele[1])
            i = input('are you done? ("no"):  ')
            if i == 'no':
                add = False
            #i2 = inp'how many grams do you have of %s:  ' %s = i)
        #print('how many moles do you have of %s:  ' %equList)
        #i2 = float(input())
        gms = round(round(moles, 3)*round(amu, 2), 3)
        print()
        print(gms)
        return gms, (equList, amu)

    def limitReagent(self):
        print("for use in limiting reagent problems.")
        print("First equation set:")
        mol1, dat1 = stoi()
        print("Second equation set:")
        mol2, dat2 = stoi()
        print("Comparing moles and generating ratio...")
        if mol1 > mol2:
            lmt = mol2
            ratio = mol2/mol1
            print("%s is the limiting reagent." %dat2[0])
            print("Ratio: %s"%ratio)
        elif mol1 < mol2:
            lmt = mol1
            ratio = mol1/mol2
            print("Ratio: %s"%ratio)
            print("%s is the limiting reagent." %dat1[0])
        else:
            print("The elements have the same moles or there is an error in the comparing.")
        print("moles of first: %s elements in first: %s" %(mol1, dat1[0]))
        print("moles of second: %s elements in second: %s" %(mol2, dat2[0]))
        print()
        print("Goal compound:")
        mol3, dat3 = stoi2(lmt)
        #gms = dat3[1]*ratio
        #print(gms)
        print(mol3, dat3)
        
    def SearchAtom(self, char):
        print("Please put all of the chars in LOWERCASE")
        if len(char) < 2:
            for x in range(len(eleList)):
                ele = PL(eleList[x].lower())
                if str(char) == ele[2].lower():
                    print(ele)
        else:
            for x in range(len(eleList)):
                ele = eleList[x]
                if str(char) == ele[1].lower():
                    print(ele)
                #print(x)

    def Seperate(self, lst, item):
        x = eleList[lst]
        try:
            return x[item]
        except IndexError:
            print("Item was to large! You made an index error.  Please make item smaller and try again!")

    def PC(self):#Process compound
################################################################################
        ##In progress/copied works:
        #new molicule prosser where i is input.  Needs testing:
        #a int is niether upper or lower so if a leter is neither than its an int.

        self.i = str(input("Compound: ")

        ##if i[x].isupper():
        ##    state = 'upper'
        ##elif i[x].islower():
        ##    state = 'lower'
        ##elif i[x].isdigit():
        ##    state = 'digit'
        ##else:
        ##    raise StateMachineError


        state = 'init'
        self.element = ''
        self.number = 1
        self.finalData = []
        def commit():
            for l in range(int(self.number)):
                self.finalData.append(self.element)
            self.number = 1
            self.element = ''

        for x in self.i:
            print(state)
            if state == 'init':
                if x.isupper():
                    self.element += x
                    state = 'upper'
                else:
                    raise StateMachineError("@ init expected upper char", state)
            elif state == 'upper':#Done
                if x.isupper():
                    commit()
                    self.element += x
                elif x.islower():
                    self.element += x
                    state = 'lower'
                elif x.isdigit():
                    self.number = x
                    state = 'digit'
                else:
                    raise StateMachineError("@ upper unexpected char", state)
            elif state == 'lower':
                if x.isupper():
                    commit()
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.number += x
                    state = 'digit'
                else:
                    raise StateMachineError("@ lower expected upper or digit", state)
            elif state == 'digit':
                if x.isupper():
                    commit()
                    self.element += x
                    state = 'upper'
                elif x.isdigit():
                    self.number += x
                    state = 'digit'
                else:
                    raise StateMachineError("@ Digit expected upper or digit", state)
            else:
                raise StateMachineError("@StateMachine expected something, I dont know what", state)
        commit()
        return self.finalData


################################################################################

Science = Science
#Science.main(self)
