import subprocess
file = 'Datatype_B'
a = subprocess.call('gcc ' + file + '.c -o ' + file + ' -lm', shell=True)
text = './' + file + ' > out1'
b = subprocess.call(text, shell=True)
print(a)
print(b)
