from __future__ import print_function

axis_powers = {0:1, 1:1, 2:-1, 3:-1}  # set the pos/neg multipliers on the coordinate grid

def run_instructions():
	xloc = 0
	yloc = 0

	axis = 0  # value 0 = up, 1 = right, 2 = down, 3 = left
	
	inst = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
	
	instructions = inst.split(", ")
	
	for instruction in instructions:
		axis, xloc, yloc = new_instruction(instruction, axis, xloc, yloc)
		print("Instruction {} Processed. Now at {}, {}".format(instruction, xloc, yloc))
		

def change_axis(current_axis, direction):
	if direction == "L":
		current_axis -= 1
	elif direction == "R":
		current_axis += 1
		
	# handle rollovers
	if current_axis < 0:
		current_axis = 3
	elif current_axis > 3:
		current_axis = 0

	return current_axis

	
def new_instruction(input, axis, x_start, y_start):
	
	direction = input[0]
	distance = int(input[1:])
	
	axis = change_axis(axis, direction)
	
	if axis in (0,2):
		y_loc = y_start + (distance*axis_powers[axis])  # distance times the pos/neg multiplier for our direction, added to the initial
		x_loc = x_start
	elif axis in (1,3):
		x_loc = x_start + (distance*axis_powers[axis])
		y_loc = y_start
		
	return axis, x_loc, y_loc
	
	