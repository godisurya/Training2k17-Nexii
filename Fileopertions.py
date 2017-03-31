class FileOwners:

    @staticmethod
    def group_by_owners(files):
        d1 = {}
        for i,j in files.items():
            if j not in d1:
                d1[j] = [i]
            else:
                d1[j].append(i)
        
        return d1

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))
