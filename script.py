class transpose:
    def __init__(self, tpose):
        self.reference = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
        self.transpose=""
        self.count=tpose
    
    def getnote(self, note):
        for j,i in enumerate(self.reference):
            if i==note:
                if j+self.count>=len(self.reference):
                    return self.reference[(j+self.count)-len(self.reference)]
                else:
                    return self.reference[j+self.count]

def start(tpose, line):
    note = transpose(tpose)
    line = line.split(" ")
    solution=[]
    for i in line:
        solution.append(note.getnote(i))
    solution= " ".join(solution)
    return solution

def chord_start(tpose, line):
    note = transpose(tpose)
    line = line.split(" ")
    intial = []
    for j,i in enumerate(line):
        if i[1]=="#":
            intial.append(i[0].upper()+"#")
            line[j]=i[2:]
        else:
            intial.append(i[0].upper())
            line[j]=i[1:]

    solution=[]
    for i in intial:
        solution.append(note.getnote(i))
    for i in range(len(line)):
        solution[i]+=line[i]
    solution= " ".join(solution)
    return solution

def major_chord(line):
    solution=[]
    lead=[]
    solution.append(line + "add9")
    lead.append(line)
    notes = transpose(2)
    a=notes.getnote(line)
    solution.append(a + "min11")
    lead.append(a)
    notes = transpose(4)
    a=notes.getnote(line)
    solution.append(a + "min7")
    lead.append(a)
    notes = transpose(5)
    a=notes.getnote(line)
    solution.append(a + "add9")
    lead.append(a)
    notes = transpose(7)
    a=notes.getnote(line)
    solution.append(a + "add9")
    lead.append(a)
    notes = transpose(9)
    a=notes.getnote(line)
    solution.append(a + "min7")
    lead.append(a)
    notes = transpose(11)
    a=notes.getnote(line)
    solution.append(a + "dim")
    lead.append(a)
    notes = transpose(12)
    a=notes.getnote(line)
    solution.append(a + "M")
    lead.append(a)


    solution = "    ".join(solution)
    lead = " ".join(lead)
    return solution + "\n\nThe Lead Notes for the scale are:-\n" + lead

def minor_chord(line):
    solution=[]
    lead=[]
    solution.append(line + "min7")
    lead.append(line)
    notes = transpose(2)
    a=notes.getnote(line)
    solution.append(a + "dim/min7b5")
    lead.append(a)
    notes = transpose(3)
    a=notes.getnote(line)
    solution.append(a + "M7")
    lead.append(a)
    notes = transpose(5)
    a=notes.getnote(line)
    solution.append(a + "min7")
    lead.append(a)
    notes = transpose(7)
    a=notes.getnote(line)
    solution.append(a + "min7")
    lead.append(a)
    notes = transpose(8)
    a=notes.getnote(line)
    solution.append(a + "M7")
    lead.append(a)
    notes = transpose(10)
    a=notes.getnote(line)
    solution.append(a + "7")
    lead.append(a)
    notes = transpose(12)
    a=notes.getnote(line)
    solution.append(a + "min")
    lead.append(a)

    solution = "    ".join(solution)
    lead = " ".join(lead)
    return solution + "\n\nThe Lead Notes for the scale are:-\n" + lead