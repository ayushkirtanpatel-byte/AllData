class JournalManager:

    def _init_(self):
        self.file="journal.txt"

    def add(self):
        self.entry=input("Enter journal entry: ")
        self.file=open("journal.txt","a")
        self.file.write("\n"+self.entry)
        self.file.close()
        print("Entry added successfuly")

    def view(self):
        try:
            self.file=open("journal.txt","r")
            print("Your journal entries are ")
            print("------------------------------")
            self.lines=self.file.readlines()
            for self.l in self.lines:
                print(self.l)
            self.file.close()
        except Exception:
            print("Error:","The journal file does not exists, please add a new entry first")
    
    def delete(self):
        aa=input("Are you sure you want to delete all enteries (yes/no): ")
        try:
            if aa=="yes":
                self.file=open("journal.txt","w")
                self.file.close()
                print("All entries deleted")
            else:
                print("Not deleted")
        except Exception:
            print("No journal entries to delete")

    def search(self):
        try: 
            self.enter=input("Enter a keyword from journal entry to view that specific entry: ")
            self.file=open("journal.txt","r")
            self.line=self.file.readlines()
            for self.l in self.line:
                if self.enter in self.l:
                    print(self.l)
                    break
            else:
                print("No matching entries found")
            self.file.close()

        except Exception:
            print("Error:","The journal file does not exists, please add a new entry first")

        
while 1<2:
    print("""
Personal Journal Manager 👏\n
Please select an option:

1. Add a new entry➕
2. View all entries👀
3. Search for an entry🤔
4. Delete all entries❌
5. Exit📤
""")
    a=int(input("Enter your choice: "))
    if a==5:
        print("Thank you for using Personal Journal Manager. GoodBye 🙋‍♂️")
        break
    if a==1:
        obj=JournalManager()
        obj.add()
    elif a==2:
        obj=JournalManager()
        obj.view()
    elif a==3:
        obj=JournalManager()
        obj.search()
    elif a==4:
        obj=JournalManager()
        obj.delete()