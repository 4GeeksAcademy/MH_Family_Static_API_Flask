from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generateId(self):
        return randint(0, 999)

    def add_member(self, member):
        member['id'] = self._generateId()  # Generar un nuevo ID
        self._members.append(member)  # Agregar el miembro a la lista
        return member  # Retornar el miembro agregado

    def delete_member(self, id):
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)  # Eliminar el miembro
                return True  # Retornar True si se eliminó
        return False  # Retornar False si no se encontró

    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member  # Retornar el miembro encontrado
        return None  # Retornar None si no se encontró

    def get_all_members(self):
        return self._members  # Retorna la lista de miembros