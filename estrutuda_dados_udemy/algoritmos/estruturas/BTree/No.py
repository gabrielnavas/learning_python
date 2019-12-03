class No:

    def __init__(self, info=0, position=0, n_max=2):
        self.vInfo = []
        self.vPos = []
        self.vLink = []
        self.length = 0

        for i in range(2 * n_max + 1):
            self.vInfo.append(0)
            self.vPos.append(0)
            self.vLink.append(None)
        self.vLink.append(None)

        self.vInfo[0] = info
        self.vPos[0] = position

    def searchPosition(self, info):
        len = self.length
        i=0

        while i < len and info > self.vInfo[i]:
            i += 1

        return i

    def relocate(self, position):
        self.vLink.append(None)
        self.vInfo.append(0)
        self.vPos.append(0)

        i = self.length
        self.vLink[i] = self.vLink[i-1]

        while(i > position):
            self.vInfo[i] = self.vInfo[i-1]
            self.vPos[i] = self.vPos[i-1]
            self.vLink[i] = self.vLink[i-1]
            i -= 1

    def getvInfo(self, position):
        return self.vInfo[position]

    def setvInfo(self, position, info):
        self.vInfo[position] = info

    def getvPos(self, position):
        return self.vPos[position]

    def setvPos(self, position, info):
        self.vPos[position] = info

    def getvLink(self, position):
        return self.vLink[position]

    def setvLink(self, position, no):
        self.vLink[position] = no

    def setTl(self, tl):
        self.length = tl

    def getTl(self):
        return self.length

