import numpy
og=numpy.dtype([('name',(numpy.str_, 10)),('class','i1'),('height','f4')])
a=numpy.array([('James', 5, 48.5 ), ('Nail', 6, 52.5 ), ('Paul', 5, 42.1 ), ('Pit', 5, 40.11)],dtype=og)
a=numpy.sort(a,order='class')
a=numpy.sort(a,order='height')
print(a)
