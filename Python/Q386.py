for x in range(2,201):
	for i in range (2,x):
		for j in range(i,x):
			for z in range(j,x):
				if i*i*i+j*j*j+z*z*z == x*x*x:
					print(x,i,j,z)