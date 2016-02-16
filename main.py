class text:
    sewtances = None
    def set_t(self, sewtances):
        self.sewtances = sewtances
    def get_t(self):
        return self.sewtances

class word:
    def replace(self, sewtances, chNum, ch2):
        for elem in sewtances:
            str = ""
            l = elem.get_s().split(' ')
            for e in l:
                if( len(e) > chNum):
                    str += (e.replace(e[chNum], ch2)+' ')
                else:
                    str += e
            print(str)

class sewtance:
    str = ""
    def set_s(self, str):
        self.str = str
    def get_s(self):
        return self.str


def main():
    sewtance1 = sewtance()
    sewtance2 = sewtance()
    sewtance3 = sewtance()
    sewtance4 = sewtance()

    sewtance1.set_s("Oepqw oepqwo peoqwp owqe epqw.")
    sewtance2.set_s("Lqwel pwql pleqp wdlpqwl pl.")
    sewtance3.set_s("Alspdl psqlp dlpq ldp.")
    sewtance4.set_s("Sald, lqw wqp dpw kdpw.")

    sewtances = [sewtance1, sewtance2, sewtance3, sewtance4]

    t = text()
    w = word()

    t.set_t(sewtances)

    chNum = input('Номер символа для замены: ')
    chReplace = input('Символ: ')

    w.replace(t.get_t(), int(chNum)-1, chReplace)

main()