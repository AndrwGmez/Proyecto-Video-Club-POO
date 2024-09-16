class Socio():


	def __init__(self, codigo, nombre, telefono, domicilio):
		self.codigo = codigo
		self.nombre = nombre
		self.telefono = telefono
		self.domicilio = domicilio


	def mostrar_socio(self):
		print("Codigo : %s" % (self.codigo))
		print("Nombre : %s" % (self.nombre))
		print("Telefono : %s" % (self.telefono))
		print("Domicilio : %s" % (self.domicilio))	