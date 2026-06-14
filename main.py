from controller import Steamer_Controller
from models import Streamer, Colors
from authy import Auth

auth = Auth()
auth.create_table_users()

controller = Steamer_Controller()
controller.create_table()

while True:
    print(f"{Colors.CYAN}\n**** SISTEMA DE STREAMERS ****\n{Colors.RESET}")
    print(f"{Colors.YELLOW}1. Iniciar sesión{Colors.RESET}")
    print(f"{Colors.YELLOW}2. Registrarse{Colors.RESET}")
    print(f"{Colors.YELLOW}3. Salir{Colors.RESET}")

    opcion_auth = input(f"{Colors.YELLOW}\nSeleccione una opción: {Colors.RESET}")

    if opcion_auth == "1":
        usuario = input(f"{Colors.YELLOW}Usuario: {Colors.RESET}")
        contrasena = input(f"{Colors.YELLOW}Contraseña: {Colors.RESET}")
        
        if auth.login(usuario, contrasena):

            print(f"{Colors.GREEN}ACESO CONCEDIDO\n{usuario}{Colors.RESET}")

            while True:

                print(f"{Colors.CYAN}\n**** BIENVENIDO ****\n{Colors.RESET}")
                print("Que opcion desea realizar\n")
                print(f"{Colors.YELLOW}1. Crear Streamer{Colors.RESET}")
                print(f"{Colors.YELLOW}2. Visualizar los Streamers{Colors.RESET}")
                print(f"{Colors.YELLOW}3. Actualizar Steamer{Colors.RESET}")
                print(f"{Colors.YELLOW}4. Eliminar Streamer{Colors.RESET}")
                print(f"{Colors.YELLOW}5. Salir\n{Colors.RESET}")

                opcion = input(f"{Colors.YELLOW}Seleccione una opción: {Colors.RESET}")
                print("\n")

                if opcion == "1":
                    try:
                        Nombre_streamer = input(f"{Colors.YELLOW}Ingresa el nombre del streamer: {Colors.RESET}")
                        existe = controller.SearchStreamers(Nombre_streamer)

                        if existe:
                            print(f"{Colors.RED}Este streamer ya existe{Colors.RESET}")
                        else:
                            Followers_streamer = int(input(f"{Colors.YELLOW}Ingresa el numero de followers: {Colors.RESET}"))
                            subs_streamer = int(input(f"{Colors.YELLOW}Ingresa el numero de Subcriptores: {Colors.RESET}"))
                            streamer = Streamer(Nombre_streamer, Followers_streamer, subs_streamer)
                            controller.InsertStreamers(streamer)
                            print(f"{Colors.GREEN}Streamer Creado{Colors.RESET}")

                    except ValueError:
                        print(f"{Colors.RED}Los followers y subs deben ser números{Colors.RESET}")

                elif opcion == "2":
                    print(f"{Colors.CYAN}\n***** BUSQUEDA DE STREAMERS *****{Colors.RESET}")
                    print(f"{Colors.YELLOW}\n1. Buscar por nombre del streamer{Colors.RESET}")
                    print(f"{Colors.YELLOW}2. Visualizar todos los streamers{Colors.RESET}")
                    print(f"{Colors.CYAN}\n*********************************\n{Colors.RESET}")

                    opcion_busqueda = input(f"{Colors.YELLOW}Ingresa la opcion: {Colors.RESET}")

                    if opcion_busqueda == "1":
                        nombre_busq = input(f"{Colors.YELLOW}Ingresa el nombre: {Colors.RESET}")
                        resultado = controller.SearchStreamers(nombre_busq)
                        if resultado:
                            print(resultado)
                        else:
                            print(f"{Colors.RED}No se encontró ningún streamer{Colors.RESET}")

                    elif opcion_busqueda == "2":
                        controller.ReadStreamers()

                    else:
                        print(f"{Colors.RED}Ingrese una opcion correcta{Colors.RESET}")

                elif opcion == "3":
                    print(f"{Colors.CYAN}\n*** ACTUALIZACION DE DATOS ***\n{Colors.RESET}")
                    print(f"{Colors.YELLOW}1. Actualizar Followers{Colors.RESET}")
                    print(f"{Colors.YELLOW}2. Actualizar Subs\n{Colors.RESET}")

                    opcion_act = input(f"{Colors.YELLOW}Ingresa la opcion: {Colors.RESET}")

                    if opcion_act == "1":
                        try:
                            Actualizar_name = input(f"{Colors.YELLOW}Ingresa el nombre del streamer: {Colors.RESET}")
                            Actualzar_foll = int(input(f"{Colors.YELLOW}Ingresa la nueva cantidad de followers: {Colors.RESET}"))
                            controller.update_followers(Actualizar_name, Actualzar_foll)
                            print(f"{Colors.GREEN}Modificacion Exitosa{Colors.RESET}")
                        except ValueError:
                            print(f"{Colors.RED}Los followers deben ser numeros{Colors.RESET}")

                    elif opcion_act == "2":
                        try:
                            Actualizar_name = input(f"{Colors.YELLOW}Ingresa el nombre del streamer: {Colors.RESET}")
                            Actualzar_subs = int(input(f"{Colors.YELLOW}Ingresa la nueva cantidad de subs: {Colors.RESET}"))
                            controller.update_subs(Actualizar_name, Actualzar_subs)
                            print(f"{Colors.GREEN}Modificacion Exitosa{Colors.RESET}")
                        except ValueError:
                            print(f"{Colors.RED}Los subs deben ser numeros{Colors.RESET}")

                    else:
                        print(f"{Colors.RED}Ingrese una opcion correcta{Colors.RESET}")

                elif opcion == "4":
                    eliminar_name = input(f"{Colors.YELLOW}Ingresa el nombre del streamer que desea eliminar: {Colors.RESET}")
                    resultado = controller.SearchStreamers(eliminar_name)

                    if resultado:
                        controller.Deleted_Streamer(eliminar_name)
                        print(f"{Colors.GREEN}Eliminado con éxito{Colors.RESET}")
                    else:
                        print(f"{Colors.RED}El streamer no existe{Colors.RESET}")

                elif opcion == "5":
                    print(f"{Colors.GREEN}Hasta luego\n{Colors.RESET}")
                    break

                else:
                    print(f"{Colors.RED}Opción inválida, Ingrese una opcion valida{Colors.RESET}")
            
        else:
            print(f"{Colors.RED}Usuario o contraseña incorrectos{Colors.RESET}")
          

    elif opcion_auth == "2":
        usuario = input(f"{Colors.YELLOW}Nuevo usuario: {Colors.RESET}")
        contrasena = input(f"{Colors.YELLOW}Nueva contraseña: {Colors.RESET}")
        auth.registrar(usuario, contrasena)
        print(f"{Colors.GREEN}Usuario registrado exitosamente{Colors.RESET}")

    elif opcion_auth == "3":
        break
    else:
        print(f"{Colors.RED}\nOpción inválida, ingrese 1 o 2{Colors.RESET}")


