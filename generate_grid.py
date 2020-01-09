import numpy as np
from PIL import Image


def save_image(img, fname) :
	img = Image.fromarray(img.astype(np.uint8))
	img.save(fname)

def remove_val(indices, val) :
	if type(val) is list :
		for element in val :
			print(element)
			indices.pop(indices.index(element))
	else :
		indices.pop(indices.index(val))
	return indices

def get_path(grid, start_pos, distance) :
	st = []
	parent = {}
	start_i, start_j = int(start_pos/grid_size), start_pos%grid_size
	st.append((start_i, start_j))
	dist = 0
	while len(st) > 0 and dist < distance:
		temp = []
		while len(st) > 0 :
			pos = st.pop()
			i, j = pos
			if i + 1 < grid_size and grid[i+1][j] == 0 and not (i+1, j) in temp:
				temp.append((i+1, j))
				parent[temp[-1]] = (i, j)
			if j + 1 < grid_size and grid[i][j+1] == 0 and not (i, j+1) in temp:
				temp.append((i, j+1))
				parent[temp[-1]] = (i, j)
		st = temp[::]
		dist += 1
	if dist < distance :
		return -1, []
	else :
		idx = np.random.randint(0, len(temp))
		i, j = temp[idx]
		paths = []
		pos_i, pos_j = i, j
		while not parent[pos_i, pos_j] == (start_i, start_j) :
			paths.append(parent[pos_i, pos_j])
			pos_i, pos_j = parent[pos_i, pos_j]
		return i * grid_size + j, paths


def get_start(indices) :
	pos = np.random.choice(indices, size = 1)[0]
	i, j = int(pos/grid_size), pos%grid_size
	img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = start_color
	grid[i,j] = 1
	return remove_val(indices, pos), pos

def get_obstacles(indices) :
	obstacles = np.random.randint(min_total_obstacles, max_total_obstacles)
	positions = list(np.random.choice(indices, size = obstacles, replace = False))
	for pos in positions :
		i, j = int(pos/grid_size), pos%grid_size
		img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = block_color
		grid[i,j] = 1
	return remove_val(indices, positions)

def get_end(start_pos, distance) :
	pos, paths = get_path(grid, start_pos, distance)
	if pos == -1 :
		return pos
	i, j = int(pos/grid_size), pos%grid_size
	img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = end_color
	for pos in paths :
		i, j = pos
		img[i*step_h:(i+1)*step_h, j*step_w:(j+1)*step_w] = path_color
	return pos

def generate(distance) :
	
	end_pos = -1
	while end_pos == -1 :
		indices = list(np.arange(grid_size*grid_size))
		indices, start_pos = get_start(indices)
		indices = get_obstacles(indices)
		end_pos = get_end(start_pos, distance)


img_size = 28
grid_size = 14
max_total_obstacles = 40
min_total_obstacles = 20

step_h = int(img_size/grid_size)
step_w = int(img_size/grid_size)
grid = np.zeros([grid_size, grid_size])
img = np.ones([img_size, img_size])*255.0
start_color = 100
end_color = 200
block_color = 0
path_color = 150

generate(10)

save_image(img, "grid.png")
