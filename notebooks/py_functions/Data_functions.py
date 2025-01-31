import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def getData(path):
	"""
	This function takes the path to an obj file, reads it and then returns two pandas data frames. the first is for verticies the second is for faces (refering to the verticies)
	
	path: str
			the path to the file you want to read as a string.
	"""
	# open and read chosen file, split the file by lines and store them in a list
	with open(path, 'r') as f:
		file = f.read()
		file = file.splitlines()
	# add all non commented lines to a new list (containing all verticies and faces)
	vfs = []
	for q in file:
		if not '#' in q:
			vfs.append(q)
	verts = []
	faces = []
	# remove unwanted wightspace
	for i in range(vfs.count('')):
		vfs.remove('')
	
	for i in range(len(vfs)):
		vfs[i] = vfs[i].split(' ')
		for j in range(vfs[i].count('')):
			vfs[i].remove('')
	# split the data into seperate lists
		if vfs[i][0] == 'v':
			verts.append(vfs[i][1:])

		elif vfs[i][0] == 'f':
			faces.append(vfs[i][1:])
	# convert lists into data frames
	verts = np.array(verts, dtype= float)
	faces = np.array(faces, dtype= float)
	
	df_f = pd.DataFrame(faces, columns= ['x','y','z'])
	df_v = pd.DataFrame(verts, columns= ['x','y','z'])
	# this line can be used to normalize the verticies data into a unit cube, it has been commented out to prevent interference in surface area calculations
	#df_v= (df_v-(df_v.max(0)+df_v.min(0))/2)/max(df_v.max(0)-df_v.min(0))
	
	return df_v, df_f
	
# geometric center function


def obj_center(path_to_file):
    '''
    Parameters:
        df_vert: a three-dimensional dataframe of the object verticies (x,y,z)
            - must have numeric entries
        
    Returns:
        center_point: a list containing the x, y, and z coordinates of the geometric center
    '''
    df_v, df_f = getData(path_to_file)
    
    av_x = np.sum(df_v['x'])/len(df_v['x'])
    av_y = np.sum(df_v['y'])/len(df_v['y'])
    av_z = np.sum(df_v['z'])/len(df_v['z'])

    center_point = [av_x,av_y,av_z]
    return center_point

