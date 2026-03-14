import tkinter as tk
from tkinter import messagebox

root = None

with open("rp.txt", "a+") as rp:
    content = rp.read()
    if not content:
        rp.write("0")
researchpoints = int(rp.read().strip())
bgval = tk.StringVar(value="gray7")
bg2val = tk.StringVar(value="gray12")
fgval = tk.StringVar(value="white")
upvar = tk.StringVar()

with open("milestones.txt", "a+") as rm:
    rm.seek(0)
    data = rm.read().strip()
print(data)

mainframe = tk.Frame(root, bg=bgval.get(), width=1200, height=800)
mainframe.grid_propagate(False)
mainframe.grid()

def rpchanger():
    rpchangerwin = tk.Toplevel(root, bg=bgval.get())
    rpchangerwin.title("Research Point Changer")
    entry = tk.Entry(rpchangerwin, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"))
    entry.pack(side="top", fill="x", expand=True)
    def add():
        global researchpoints
        value = int(entry.get())
        researchpoints += value
        rplabel.config(text=f"Research Points: {researchpoints}")
    addbtn = tk.Button(rpchangerwin, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), command=add, text="Add")
    addbtn.pack(side="top", fill="x", expand=True)
    def subtract():
        global researchpoints
        value = int(entry.get())
        researchpoints -= value
        rplabel.config(text=f"Research Points: {researchpoints}")
        if researchpoints <= -1:
            value = int(entry.get())
            researchpoints += value
            rplabel.config(text=f"Research Points: {researchpoints}")
            messagebox.showerror(
                title="Research Points",
                message="You dont have enough research points"
            )
    subtractbtn = tk.Button(rpchangerwin, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 15, "bold"), text="Subtract", command=subtract)
    subtractbtn.pack(side="top", fill="x", expand=True)
def upwin():
    win = tk.Toplevel(root)
    win.title("Unlocked Parts")
    uplabel = tk.Label(win, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text=f"Unlocked Parts: {upvar.get()}")
    uplabel.pack(fill="both", expand=True)

topbarframe = tk.Frame(mainframe, bg=bgval.get())
topbarframe.grid(row=0, sticky="nw")
rplabel = tk.Label(topbarframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text=f"Research Points: {researchpoints}")
rplabel.grid(row=0, column=0)
rpbtn = tk.Button(topbarframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Research Point Changer", command=rpchanger)
rpbtn.grid(row=0, column=1)
upbtn = tk.Button(topbarframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Unlocked Parts", command=upwin)
upbtn.grid(row=0, column=2)

def switchpage(frame):
    frame.tkraise()

nodesframe = tk.Frame(mainframe, bg=bg2val.get(), highlightbackground=fgval.get(), highlightthickness=2, width=400, height=670)
nodesframe.grid_propagate(False)
nodesframe.grid(row=2, column=1)
nodename = tk.Label(nodesframe, text="Node Name Here", bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI",30,"bold"))
nodename.grid(row=0, column=0)
nodeunlockedparts = tk.Label(nodesframe, text=f"Unlocked Parts: {upvar.get()}", bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"))
nodeunlockedparts.grid(row=1, column=0)
nodecost = tk.Label(nodesframe, text="Cost: ", bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"))
nodecost.grid(row=2, column=0)
nodeunlockbtn = tk.Button(nodesframe, text="Unlock this node", bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"))
nodeunlockbtn.grid(row=3, column=0)

# Page 1
frame1 = tk.Frame(mainframe, bg=bg2val.get(), highlightbackground=fgval.get(), highlightthickness=2, width=800, height=670)
frame1.grid_propagate(False)
frame1.grid(row=2, column=0)
frame1btn = tk.Button(mainframe, bg=bgval.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Page 1", command=lambda: switchpage(frame1))
frame1btn.grid(row=1, column=0, sticky="nw")

# Saving Logic

if data == "1":
    upvar.set("\n Primitive Conventional Fuel Tank\n Procedural Avionics\n Oriole Engine\n Kestral Engine")
if data == "2":
    upvar.set(upvar.get()+"\n Primitive Conventional Fuel Tank\n Procedural Avionics\n Oriole Engine\n Kestral Engine\n Proto Hawk\n Vertex Engine")
if data == "3":
    upvar.set(upvar.get()+"\n Primitive Conventional Fuel Tank\n Procedural Avionics\n Oriole Engine\n Kestral Engine\n Proto Hawk\n Vertex Engine\nStar-13\nStar-13A\nRCS (Of all kinds)\nStar-13B\nStar-13E\nConventional Fuel Tank\nWoodstar Veierner Engine")

def startnode():
    nodename.config(text="Start Node")
    nodeunlockedparts.config(text="Parts:\n Primitive Conventional Fuel Tank\n Procedural Avionics\n Oriole Engine\n Kestral Engine", font=("Segoe UI", 18, "bold"))
    nodecost.config(text="Cost: 0")
    def unlock():
        nodetext = "\nPrimitive Conventional Fuel Tank\n Procedural Avionics\n Oriole Engine\n Kestral Engine"
        if nodetext.strip() not in upvar.get().strip():
            upvar.set(upvar.get() + nodetext)
            with open("milestones.txt", "r+") as f:
                f.seek(0)
                current = f.read().strip()
                if current != "1":
                    f.seek(0)
                    f.truncate()
                    f.write("1")
            basicrocketrybtn = tk.Button(frame1, bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Basic Rocketry", command=basicrocketry)
            basicrocketrybtn.place(x=150, y=335)
        else:
            messagebox.showinfo(
                title="Node already unlocked",
                message="You already unlocked this node"
            )
            basicrocketrybtn = tk.Button(frame1, bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Basic Rocketry", command=basicrocketry)
            basicrocketrybtn.place(x=150, y=335)
    nodeunlockbtn.config(command=unlock)
    def basicrocketry():
        nodename.config(text="Basic Rocketry")
        nodeunlockedparts.config(text="Parts:\n Proto Hawk\n Vertex Engine")
        nodecost.config(text="Cost: 15")
        def unlock():
            global researchpoints
            researchpoints -= 15
            if researchpoints <= -1:
                messagebox.showerror(
                    title="Not enough research points",
                    message="You do not have enough research points for this"
                )
                researchpoints += 15
            else:
                rplabel.config(text=f"Research Points: {researchpoints}")
                nodetext = "\n Proto Hawk\n Vertex Engine"
                if nodetext.strip() not in upvar.get().strip():
                    upvar.set(upvar.get()+nodetext)
                    with open("milestones.txt", "r+") as f:
                        f.seek(0)
                        current = f.read().strip()
                        if current != 1:
                            f.seek(0)
                            f.truncate()
                            f.write("2")
                    orbitalmaterialsbtn = tk.Button(frame1, bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Orbital Materials", command=orbitalmaterials)
                    orbitalmaterialsbtn.place(x=400, y=335)
                else:
                    researchpoints += 15
                    rplabel.config(text=f"Research Points: {researchpoints}")
                    messagebox.showinfo(
                        title="Node already unlocked",
                        message="You already unlocked this node"
                    )
                    orbitalmaterialsbtn = tk.Button(frame1, bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), text="Orbital Materials", command=orbitalmaterials)
                    orbitalmaterialsbtn.place(x=400, y=335)
        nodeunlockbtn.config(command=unlock)
        def orbitalmaterials():
            nodename.config(text="Orbital Materials")
            nodeunlockedparts.config(text="Parts:\nStar-13\nStar-13A\nRCS (Of all kinds)\nStar-13B\nStar-13E\nConventional Fuel Tank\nWoodstar Veierner Engine")
            nodecost.config(text="Cost: 45")
            def unlock():
                global researchpoints
                researchpoints -= 45
                if researchpoints <= -1:
                    researchpoints += 45
                    messagebox.showerror(
                        title="Not enough research points",
                        message="You do not have enough research points for this"
                    )
                else:
                    rplabel.config(text=f"Research Points: {researchpoints}")
                    nodetext = "\nStar-13\nStar-13A\nRCS (Of all kinds)\nStar-13B\nStar-13E\nConventional Fuel Tank\nWoodstar Veierner Engine"
                    if nodetext.strip() not in upvar.get().strip():
                        with open("milestones.txt", "r+") as f:
                            f.seek(0)
                            current = f.read().strip()
                            if current != "3":
                                f.seek(0)
                                f.truncate()
                                f.write("3")
                        upvar.set(upvar.get()+nodetext)
                    else:
                        researchpoints += 45
                        rplabel.config(text=f"Research Points: {researchpoints}")
                        messagebox.showinfo(
                            title="Node already unlocked",
                            message="You already unlocked this node"
                        )
            nodeunlockbtn.config(command=unlock)
    

startnodebtn = tk.Button(frame1, bg=bg2val.get(), fg=fgval.get(), font=("Segoe UI", 20, "bold"), command=startnode, text="Start")
startnodebtn.place(x=0, y=335)