import csv,collections,sys

def summarize(path):
    with open(path,newline='') as stream:
        return collections.Counter(row['route'] for row in csv.DictReader(stream))

if __name__=='__main__':
    for route,count in sorted(summarize(sys.argv[1]).items()):
        print(f'{route}: {count} shipments')
