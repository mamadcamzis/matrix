class Matrix:	"""This class implements matrix operations	Attributes:		nline (int): The number of line of the matrix		ncol (int): The number of columns		matrice (array like): Values of matrix	"""	def __init__(self, nline=0, ncol=0):		"""The constructor of matrix		Parameters:			nline (int): number of line			nco			l (int): number of cols		"""		self.rows = nline		self.cols = ncol		self.matrix = []	def set_values(self, values):		"""This method set values to		matrix arguments		Parameters:			values (array like): matrix values		Returns:			The matrix values		"""		nl = len(values)		if isinstance(values[0], list):			nc = len(values[0])			self.cols = nc		self.rows = nl		self.matrix = values		return self.matrix	def __add__(self, other):		"""		Compute matrix additon operation		:param other: other matrix to add		:return: Matrix object		"""		if (self.rows != other.rows) or (self.cols != other.cols):			print("Addition is not allowed, matrix does not have same dim")			raise ArithmeticError		result = Matrix()		values = self.zeros_matrix(self.rows, self.cols)		for i in range(self.rows):				if self.cols > 0:					for j in range(self.cols):						sum_ij = self.matrix[i][j] + other.matrix[i][j]						values[i][j] = sum_ij				else:					sum_i = self.matrix[i] = other.matrix[i]					values[i] = sum_i		result.set_values(values)		return result	def zeros_matrix(self, rows, cols):		"""		create a matrix fill of zeros		:param rows:		:param cols:		:return: array of zeros		"""		A = []		for i in range(rows):			A.append([])			for j in range(cols):				A[-1].append(0.0)		return A		def scalar_mult(self, scalar):		"""Multiply a matrix by  scalar				:param scalar: 		:return: Matrix resultt		"""		prod = self.copy_matrix()		for i in range(self.rows):			for j in range(self.cols):				prod.matrix[i][j] = scalar * self.matrix[i][j]		return prod		def __mul__(self, other):		"""		Matrix multiplication		:param other: Matrix object		:return: Matrix multiplication		"""				if self.cols != other.rows:			print("Matrix multiplication is not allowed")			raise ArithmeticError		result = Matrix()		values = self.zeros_matrix(self.rows, other.cols)		for i in range(self.rows):			for j in range(other.cols):				total = 0				for k in range(self.cols):					total += self.matrix[i][k]*other.matrix[k][j]				values[i][j] = total		result.set_values(values)		return result	def __repr__(self):		"""		print a matrix		:return:		"""		print("Matrix of rows %d and columns %d"%(self.rows, self.cols))		for row in self.matrix:			print([round(x, 3) + 0 for x in row])		return ''	def check_squareness(self):		"""		check if we have a square matrix		:return:		"""		if self.rows != self.cols:			raise ArithmeticError("Not a squared matrix")	def identity_matrix(self):		"""		Creates and returns an identity matrix.			:param n: the square size of the matrix			:returns: a square identity matrix		"""		id_m = self.zeros_matrix(self.rows, self.rows)		for i in range(self.rows):			id_m[i][i] = 1.0		id_matrix = Matrix()		id_matrix.set_values(id_m)		return id_matrix	def copy_matrix(self):		"""		Creates and returns a copy of a matrix.			:return: The copy of the matrix		"""		cm = self.zeros_matrix(self.rows, self.cols)		for i in range(self.rows):			for j in range(self.rows):				cm[i][j] = self.matrix[i][j]		copied_matrix = Matrix()		copied_matrix.set_values(cm)		return copied_matrix	def determinant(self, total=0):		"""		Compute determinant of matrix		:param total:		:return:		"""		# Section 1: Establish n parameter and copy A		n = self.rows		am_matrix = self.copy_matrix().matrix		# Section 2: Row ops on A to get in upper triangle form		for fd in range(n):  # A) fd stands for focus diagonal			for i in range(fd + 1, n):  # B) only use rows below fd row				if am_matrix[fd][fd] == 0:  # C) if diagonal is zero ...					am_matrix[fd][fd] == 1.0e-18  # change to ~zero				# D) cr stands for "current row"				crScaler = am_matrix[i][fd] / am_matrix[fd][fd]				# E) cr - crScaler * fdRow, one element at a time				for j in range(n):					am_matrix[i][j] = am_matrix[i][j] - crScaler *\									am_matrix[fd][j]		# Section 3: Once AM is in upper triangle form ...		product = 1.0		for i in range(n):			# ... product of diagonals is determinant			product *= am_matrix[i][i]		return product	def transpose(self):		"""		Creates and returns a transpose of a matrix.			:return: the transpose of the given matrix		"""		rows = self.rows		cols = self.cols		mt = self.zeros_matrix(cols, rows)		for i in range(rows):			for j in range(cols):				mt[j][i] = self.matrix[i][j]		transposed_matrix = Matrix()		transposed_matrix.set_values(mt)		return transposed_matrix	def check_non_singular(self):		"""		Check if the matrix is not singular		:return:		"""		det = self.determinant()		if det != 0:			return det		else:			raise ArithmeticError("Singular Matrix!")	def check_matrix_equality(self, B, tol=None):		"""		Checks the equality of two matrices.			:param B: The second matrix			:param tol: The decimal place tolerance of the check			:return: The boolean result of the equality check		"""		if (self.rows != B.rows) or (self.cols != B.cols):			return False		for i in range(self.rows):			for j in range(self.cols):				if tol is None:					if self.matrix[i][j] != B.matrix[i][j]:						return False				else:					if round(self.matrix[i][j], tol) != round(B.matrix[i][j],															tol):						return False		return True	def invert_matrix(self, tol=None):		"""		Returns the inverse of the passed in matrix.			:return: The inverse of the matrix A		"""		# Section 1: Make sure A can be inverted.		self.check_squareness()		self.check_non_singular()		# Section 2: Make copies of A & I, AM & IM, to use for row ops		n = self.rows		am_matrix = self.copy_matrix()		id_matrix = self.identity_matrix()		inv_matrix = id_matrix.copy_matrix()		# Section 3: Perform row operations		indices = list(range(n))  # to allow flexible row referencing ***		for fd in range(n):  # fd stands for focus diagonal			fdScaler = 1.0 / am_matrix.matrix[fd][fd]			# FIRST: scale fd row with fd inverse.			for j in range(n):  # Use j to indicate column looping.				am_matrix.matrix[fd][j] *= fdScaler				inv_matrix.matrix[fd][j] *= fdScaler			# SECOND: operate on all rows except fd row as follows:			for i in indices[0:fd] + indices[									 fd + 1:]:  # *** skip row with fd in it.				crScaler = am_matrix.matrix[i][fd]  # cr stands for "current row".				for j in range(n):  # cr - crScaler * fdRow, but one element					# at a time.					am_matrix.matrix[i][j] = am_matrix.matrix[i][j] -\											 crScaler * am_matrix.matrix[fd][j]					inv_matrix.matrix[i][j] = inv_matrix.matrix[i][j] - \											crScaler * inv_matrix.matrix[fd][j]		# Section 4: Make sure that IM is an inverse of A within the specified		# tolerance		#if id_matrix.check_matrix_equality(self * inv_matrix, tol):		#	return inv_matrix		#else:		#	raise ArithmeticError("Matrix inverse out of tolerance.")		return inv_matrix				def main():	A = Matrix()	A.set_values([[5,4,3,2,1],[4,3,2,1,5],[3,2,9,5,4],[2,1,5,4,3],				  [1,2,3,4,5]])	print("Matrix A")	print(A)	print("Tranpose A")	print(A.transpose())	print("Id A")	print(A.identity_matrix())	B = Matrix()	B.set_values([[1, 2, 3], [1, 2, 3]])	print('B matrix')	print(B)	C = B + B	print('C = B + B')	print(C)	print("C * 1")	C1 = C.scalar_mult(1)	print(C1)	idA = A.identity_matrix()	print("Inv Ida")	invid = idA.invert_matrix()	print(invid)	print(idA * idA)	invA = A.invert_matrix()	print('Inverse A')	print(A*invA)if __name__ == '__main__':	main()