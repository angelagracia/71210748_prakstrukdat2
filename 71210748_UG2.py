#ANGELA GRACIA CAHYANINGTYAS
#71210748

#fungsi rekursif
import timeit
def deretAjaib(n):
    if (n<=5):
        return n
    else:
        return deretAjaib(n-2)+deretAjaib(n//2)

start = timeit.default_timer()
hasil1 = deretAjaib(50)
end = timeit.default_timer()
print('hasil akhir',hasil1, '=', end-start, 'detik')

#fungsi iteratif
#def deretAjaib(n):
   # for i in range(n>5):
        

#start = time.time()
#hasil2 = deretAjaib(15)
#end = time.time()
#print('hasil akhir',hasil2, '=', end-start, 'detik')
