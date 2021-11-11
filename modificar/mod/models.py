import cx_Oracle


class Empleado:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    def devolverdato(self, nuevoSalario, numeroEmpleado ):
        cursor = self.connection.cursor()
        try:
            consulta = ("UPDATE EMP SET SALARIO= :p1  WHERE EMP_NO= :p2")

            cursor.execute(consulta, (nuevoSalario, numeroEmpleado))
            if cursor.rowcount > 0:
                mensaje= "Registro insertado satisfactoriamente"
            else:
                mensaje= "Dato no encontrado"


        except self.connection.Error as error:
            print("Error: ", error)

        return mensaje


