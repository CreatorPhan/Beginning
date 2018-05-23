def so_chu_so(val):
	scs = 0
	if val != 0 :
		while val != 0:
			scs = scs + 1
			val = val // 10
	else:
		scs = 1
	return scs
def so_2():
	global data
	bienso = 1
	while bienso != 0 :
		x = ngau_nhien()
		y = ngau_nhien()
		bienso = data[x][y]
	data[x][y] = 2
def ngau_nhien():
	import random
	rd = random.random()
	rd = 100 * rd
	rd = rd // 1
	rd = int( rd % 4 )
	return rd
def hien_thi():
	global data
	import os
	os.system('cls')
	for y in [0, 1, 2, 3]:
		for x in [0, 1, 2, 3]:
			chuso = data[x][y]
			scs = so_chu_so(chuso)
			if x == 3:
				print( " "*(6 - scs), chuso)
			else:
				print( " "*(6 - scs), chuso, end = '')

def up():
	global data
	global xyz
	xyz = 0
	for x in [0,1,2,3]:
		iy = 0
		y = 0
		while y < 4:
			if data[x][y] != 0 :
				if y == 3:
					if y != iy :
						data[x][iy] = data[x][y]
						data[x][y] = 0
						xyz = xyz + 1
				else:
					y1 = y +1 
					while y1 < 4:
						if data[x][y1] == 0:
							if y1 == 3 :
								if iy != y :
									data[x][iy] = data[x][y]
									data[x][y] = 0
									y = 3
									xyz = xyz + 1
						else:
							if data[x][y1] == data[x][y] :
								data[x][y] = 0
								data[x][iy] = 2 * data[x][y1]
								data[x][y1] =0
								iy = iy + 1
								y = y1 - 1
								y1 = 3
								xyz = xyz + 1
							else:
								if y == iy :
									iy = iy + 1
								else:
									data[x][iy] = data[x][y]
									data[x][y] = 0
									iy = iy +1
									xyz = xyz + 1
								y = y1 - 1
								y1 = 3
						y1 = y1 + 1
			y = y+1

def left():
	global data
	global xyz
	xyz = 0
	for y in [0,1,2,3]:
		ix = 0
		x = 0
		while x < 4:
			if data[x][y] != 0 :
				if x == 3:
					if x != ix :
						data[ix][y] = data[x][y]
						data[x][y] = 0
						xyz = xyz + 1
				else:
					x1 = x +1 
					while x1 < 4:
						if data[x1][y] == 0:
							if x1 == 3 :
								if ix != x :
									data[ix][y] = data[x][y]
									data[x][y] = 0
									x = 3
									xyz = xyz + 1
						else:
							if data[x1][y] == data[x][y] :
								data[x][y] = 0
								data[ix][y] = 2 * data[x1][y]
								data[x1][y] =0
								ix = ix + 1
								x = x1 - 1
								x1 = 3
								xyz = xyz + 1
							else:
								if x == ix :
									ix = ix + 1
								else:
									data[ix][y] = data[x][y]
									data[x][y] = 0
									ix = ix +1
									xyz = xyz + 1
								x = x1 - 1
								x1 = 3
						x1 = x1 + 1
			x = x + 1
def down():
	global data
	global xyz
	xyz = 0
	for x in [0,1,2,3]:
		iy = 3
		y = 3
		while y >= 0:
			if data[x][y] != 0 :
				if y == 0:
					if y != iy :
						data[x][iy] = data[x][y]
						data[x][y] = 0
						xyz = xyz + 1
				else:
					y1 = y - 1 
					while y1 >= 0:
						if data[x][y1] == 0:
							if y1 == 0 :
								if iy != y :
									data[x][iy] = data[x][y]
									data[x][y] = 0
									y = 0
									xyz = xyz + 1
						else:
							if data[x][y1] == data[x][y] :
								data[x][y] = 0
								data[x][iy] = 2 * data[x][y1]
								data[x][y1] =0
								iy = iy - 1
								y = y1 + 1
								y1 = 0
								xyz = xyz + 1
							else:
								if y == iy :
									iy = iy - 1
								else:
									data[x][iy] = data[x][y]
									data[x][y] = 0
									iy = iy -1
									xyz = xyz + 1
								y = y1 + 1
								y1 = 0
						y1 = y1 - 1
			y = y - 1
def right():
	global data
	global xyz
	xyz = 0
	for y in [0,1,2,3]:
		ix = 3
		x = 3
		while x >= 0 :
			if data[x][y] != 0 :
				if x == 0 :
					if x != ix :
						data[ix][y] = data[x][y]
						data[x][y] = 0
						xyz = xyz + 1
				else:
					x1 = x - 1 
					while x1 >= 0:
						if data[x1][y] == 0:
							if x1 == 0 :
								if ix != x :
									data[ix][y] = data[x][y]
									data[x][y] = 0
									x = 0
									xyz = xyz + 1
						else:
							if data[x1][y] == data[x][y] :
								data[x][y] = 0
								data[ix][y] = 2 * data[x1][y]
								data[x1][y] =0
								ix = ix - 1
								x = x1 + 1
								x1 = 0
								xyz = xyz + 1
							else:
								if x == ix :
									ix = ix - 1
								else:
									data[ix][y] = data[x][y]
									data[x][y] = 0
									ix = ix - 1
									xyz = xyz + 1
								x = x1 + 1
								x1 = 0
						x1 = x1 - 1
			x = x - 1

data = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
import time
t = 1/20
zxc = 1
print("Are you ready")
input()
for xx in range(0,1000) :
	so_2()
	hien_thi()
	time.sleep(t)
	xyz = 0
	while xyz == 0 :
		if ngau_nhien() == 0 :
			up()
		if ngau_nhien() == 1 :
			down()
		if ngau_nhien() == 2 :
			left()
		if ngau_nhien() == 3 :
			right()
	hien_thi()
	time.sleep(t)
print( "Exiting" )
input()