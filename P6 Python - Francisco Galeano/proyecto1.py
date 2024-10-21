import flet as ft

def main(page: ft.Page):
    # Definir ancho y alto de la ventana 
    page.window_width = 600  # ancho de la ventana 
    page.window_height = 500  # alto de la ventana
    page.title = "Lista de Compras"
    
    def add_clicked(e):
        if new_task.value:  # Solo agrega si el campo no está vacío
            task = create_task(new_task.value)
            task_list.controls.append(task)
            new_task.value = ""
            new_task.focus()
            page.update()

    def create_task(task_text):
        # Crear una fila que contenga la tarea, el botón de modificar y el botón de eliminar
        checkbox = ft.Checkbox(label=task_text)
        edit_button = ft.ElevatedButton("Modificar", on_click=lambda e: edit_task(checkbox))
        delete_button = ft.ElevatedButton("Eliminar", on_click=lambda e: delete_task(checkbox))

        return ft.Row([checkbox, edit_button, delete_button], alignment="spaceBetween")

    def edit_task(checkbox):
        # Permitir modificar el texto de la tarea
        new_value = ft.TextField(value=checkbox.label, width=300)
        save_button = ft.ElevatedButton("Guardar", on_click=lambda e: save_task(checkbox, new_value))

        # Reemplazar el contenido de la fila con el campo de texto y el botón de guardar
        task_row = checkbox.parent
        task_row.controls.clear()
        task_row.controls.append(new_value)
        task_row.controls.append(save_button)
        page.update()

    def save_task(checkbox, new_value):
        # Guardar el nuevo valor en el checkbox y restaurar los botones de modificar y eliminar
        checkbox.label = new_value.value
        task_row = new_value.parent
        task_row.controls.clear()
        task_row.controls.append(checkbox)
        task_row.controls.append(ft.ElevatedButton("Modificar", on_click=lambda e: edit_task(checkbox)))
        task_row.controls.append(ft.ElevatedButton("Eliminar", on_click=lambda e: delete_task(checkbox)))
        page.update()

    def delete_task(checkbox):
        # Eliminar la tarea de la lista
        task_list.controls.remove(checkbox.parent)
        page.update()

    # Creamos los componentes de la interfaz de usuario
    new_task = ft.TextField(hint_text="¿Qué necesitas comprar?", width=300)
    task_list = ft.Column()

    # Creamos una cabecera con el logo e imagen (texto o imagen)
    header_text = ft.Text("Bienvenidos a la App de Lista de Compras", size=20, weight=ft.FontWeight.BOLD)
    logo = ft.Image(src="C:\\Users\\TOSHIBA\\P6 Python - Francisco Galeano\\logo.png", width=150, height=150) 
    

    # Organizamos cabecera en una columna y centramos
    header = ft.Column([
        logo,
        header_text
    ], alignment="center")  # Alineación centrada

    # Añadimos elementos a la aplicación 
    page.add(
        header,  # Para que muestre el texto primero
        ft.Divider(height=20),  # Agrega un divisor para separar el logo de la sección 
        ft.Row([new_task, ft.ElevatedButton("Agregar", on_click=add_clicked)]),
        task_list
    )

    # Establecer el color de fondo a rojo al inicio
    page.bgcolor = "blue"
    page.update()

ft.app(main)



