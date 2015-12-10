import urllib, re, os

if __name__ == '__main__':
    r = urllib.urlopen('http://10.169.102.190')
    d = r.read()
    m = re.findall(r'>(01-[0-9]{14}-snapshot\.jpg)<', d)
    if m:
        with open('got.txt', 'r') as f:
            l = f.readlines()
        l = [x.strip() for x in l]
        for newurl in m:
            if newurl not in l:
                # download the file
                testfile = urllib.URLopener()
                testfile.retrieve('http://10.169.102.190/' + newurl, newurl)
                #urllib.urlretrieve('http://10.169.102.190/' + newurl, newurl)
                print newurl
                with open('got.txt', 'a') as f:
                    f.write(newurl + '\n')
