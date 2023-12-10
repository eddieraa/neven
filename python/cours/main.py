import pickle

if False:#input("1 ou 2 ? ") == "1":
    with open("test.txt", "w") as fic:
        dic = {
            "nom": input("Nom : "),
            "age": "15"
        }
        fic.write(str(dic))

else:
    with open("test.txt", "r") as fic:
        dic = eval(fic.read())



class Test:
    def __init__(self, level):
        self.level = level
    
    def lolxptdrr(self):
        print("Niveau :", self.level)


if True:#input("Test n : ") == "1":
    p1 = Test(2)#int(input("Entrez niveau : ")))
    with open("player.data", "wb") as fic:
        record = pickle.Pickler(fic)
        record.dump(p1)


else:
    with open("player.data", "rb") as fic:
        record = pickle.Unpickler(fic)
        p1 = record.load()
        print(p1.lolxptdrr())


import time
import threading

lock = threading.RLock()

class process(threading.Thread):
    def __inut__(self):
        threading.Thread.__init__(self)

    def run(self):
        i = 0
        while i < 3:
            with lock:
                for lt in "ABC":
                    print(lt)
                    time.sleep(0.1)
            i += 1












import asyncio

async def bar(id, waiting):
    for i in range(5):
        print(f"La tâche {id} prend le dessus")
        await asyncio.sleep(waiting)


async def main():
    await asyncio.gather(
        bar("A", 0.1),
        bar("AB", 0.2),
        bar("B", 0.3),
        bar("BC", 0.4),
        bar("C", 0.5)
    )

asyncio.run(main())