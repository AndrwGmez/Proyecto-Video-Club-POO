from os import system
from adicionar_socio import Socio
from video_club import Videoclub
from pelicula import Pelicula


class Menu: 
 

	def __init__(self):
		self.videoclub = Videoclub()


	def adicionar_socio(self):
		system("cls")
		print("*****************************")
		print("*****************************")
		print("     Adicionar Socio        ")
		print("*****************************")
		print("*****************************")
		print()

		codigo = input("Digite el codigo del socio : ")
		nombre = input("Ingrese el nombre del socio : " )
		telefono = input("Ingrese el telefono del socio : " )
		domicilio = input("Ingrese el domicilio del socio : " )
		socio = Socio(codigo, nombre, telefono, domicilio)

		if self.videoclub.adicionar_socio(socio):

			print()
			print("**************************")
			print("  INFO - El socio fue agregado exitosamente   ")
			print("**************************")
			print()
			input()

		else:

			print()
			print("**************************")
			print("   INFO - El socio NO fue agregado   ")
			print("**************************")
			print()
			input()


	def listar_socio(self):
		system("cls")
		print("********************************")
		print("********************************")
		print("        LISTAR SOCIO            ")
		print("********************************")
		print("********************************")
		self.videoclub.listar_socio()
		input()


	def eliminar_socio(self):
		system("cls")
		print("********************************")
		print("********************************")
		print("        ELIMINAR SOCIO          ")
		print("********************************")
		print("********************************")
		print()
		codigo = input("Ingrese el codigo del socio que desea eliminar : ")

		if self.videoclub.eliminar_socio(codigo):

			print()
			print("********************************")
			print("  INFO - El socio fue eliminado exitosamente     ")
			print("********************************")
			input()

		else:
			print()
			print("********************************")
			print("  INFO - El socio NO fue eliminado exitosamente, no existe")
			print("********************************")
			input()

	
	def adicionar_pelicula(self):
		system("cls")
		print("********************************")
		print("********************************")
		print("   ADICIONAR PELICULA     ")
		print("********************************")
		print("********************************")
		print()

		codigo = input("Ingrese el codigo de la pelicula : ")
		titulo = input("Ingrese el titulo de la pelicula : ")
		genero = input("Ingrese el genero de la pelicula : ")
		pelicula = Pelicula(codigo,titulo,genero)

		if self.videoclub.adicionar_pelicula(pelicula):
			print()
			print("**************************")
			print("   INFO - La pelicula fue agregada   ")
			print("**************************")
			input()

		else: 
			print()
			print("********************************")
			print("  INFO - La pelicula NO fue agregada ")
			print("********************************")
			input()

	
	def  listar_pelicula(self):
		system("cls")
		print("********************************")
		print("********************************")
		print("        LISTAR PELICULA         ")
		print("********************************")
		print("********************************")
		self.videoclub.listar_pelicula()
		input()


	def eliminar_pelicula(self):
		system("cls")
		print("********************************")
		print("********************************")
		print("        ELIMINAR PELICULA          ")
		print("********************************")
		print("********************************")
		print()
		codigo = input("Ingrese el codigo de la pelicula que desea eliminar : ")

		if self.videoclub.eliminar_pelicula(codigo):
			print()
			print("********************************")
			print("  INFO - La pelicula fue eliminado exitosamente     ")
			print("********************************")
			input()

		else:
			print()
			print("********************************")
			print("  INFO - La pelicula NO fue eliminado exitosamente, no existe")
			print("********************************")
			input()


	def alquilar_pelicula(self):
		system("cls")
		print()
		print("********************************")
		print("********************************")		
		print("        ALQUILAR PELICULA       ")
		print("********************************")
		print("********************************")
		print()

		codigo_pelicula = input("Ingrese el codigo de la pelicula : ")
		codigo_socio = input("Ingrese el codigo del socio : ")

		if self.videoclub.alquilar_pelicula(codigo_socio, codigo_pelicula):
			print()
			print("*************************")
			print("   INFO - La pelicula fue alquilada exitosamente")
			print("*************************")
			input()

		else:
			print()
			print("********************************")
			print("  INFO - La pelicula NO fue alquila exitosamente")
			print("********************************")
			input()


	def devolver_pelicula(self):
		system("cls")
		print("********************************")
		print("********************************")
		print("       DEVOLVER PELICULA ")
		print("********************************")
		print("********************************")
		print()

		codigo_pelicula = input("Ingrese el codigo de la pelicula : ")
		codigo_socio = input("Ingrese el codigo del socio : ")


		if self.videoclub.devolver_pelicula(codigo_pelicula, codigo_socio):
			print()
			print("********************************")
			print("  INFO - La pelicula ha sido devuelta")
			print("********************************")
			print()
			input()

		else:
			print()
			print("********************************")
			print("  INFO - La pelicula NO ha sido devuelta, error de ingreso")
			print("********************************")
			print()
			input()


	def mostrar_menu_principal(self):
		while True:

			system("cls")
			print()
			print("**************************")
			print("**************************")
			print("        Video Club   ")
			print("**************************")
			print("**************************")

			print()
			print("*-.*-.*-.*-*.*-.**-.*-.*-.*-*.*-.*")
			print("  Bienvenido Al Menu Principal")
			print("*-.*-.*-.*-*.*-.**-.*-.*-.*-*.*-.*")
			print()

			print("   1 = Crear Socio   ")
			print("*************************")
			print("   2 = Listar socio   ")
			print("*************************")
			print("   3 = Eliminar Socio   ")
			print("*************************")

			print()
			print("*************************")
			print("*************************")
			print("*************************")
			print("*************************")
			print()

			print("   4 = Crear Pelicula   ")
			print("*************************")
			print("   5 = Listar Pelicula   ")
			print("*************************")
			print("   6 = Eliminar Pelicula   ")
			print("*************************")
			
			print()
			print("*************************")
			print("*************************")
			print("*************************")
			print("*************************")
			print()
			
			print("   7 = Alquilar Pelicula   ")
			print("*************************")
			print("   8 = Devolver Pelicula   ")
			print("*************************")
			print("   10 = Salir Del Sistema   ")
			print()


			try:

				print("*-.*-.*-.*-*.*-.**-.*-.*-.*-*.*-.*")
				print()
				op = int(input("Digite la accion a utilizar : "))
				print()
				print("Hasta Luego")


				if op == 1:
					self.adicionar_socio()


				elif op == 2:
					self.listar_socio()


				elif op == 3:
					self.eliminar_socio()


				elif op == 4:
					self.adicionar_pelicula()



				elif op == 5:
					self.listar_pelicula()



				elif op == 6:
					self.eliminar_pelicula()



				elif op == 7:
					self.alquilar_pelicula()


				elif op == 8:
					self.devolver_pelicula()


				elif op == 10:
					break 


				else:
					print()
					print("********************************")
					print("********************************")
					print("        Error De Ingreso ")
					print("********************************")
					print("********************************")
					input()

			except ValueError:
				print()
				print("*******************************")
				print("Error - Solo valores numericos")
				print("********************************")
				input()



if __name__ == '__main__': 
	menu = Menu()
	menu.mostrar_menu_principal()

