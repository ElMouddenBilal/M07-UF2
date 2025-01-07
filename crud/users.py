from db_connect.connection import db_session
from model.sql_model import User

# Crear un nuevo usuario
def create_user(name: str, surname: str) -> int:
    try:
        new_user = User(name=name, surname=surname)
        db_session.add(new_user)
        db_session.commit()
        return new_user.id
    except Exception as e:
        raise Exception(f"Error creating user: {str(e)}")

# Obtener todos los usuarios
def read_users() -> list:
    try:
        return db_session.query(User).all()
    except Exception as e:
        raise Exception(f"Error fetching users: {str(e)}")

# Actualizar un usuario
def update_user(user_id: int, name: str, surname: str) -> str:
    try:
        user = db_session.query(User).filter_by(id=user_id).one_or_none()
        if user:
            user.name = name
            user.surname = surname
            db_session.commit()
            return "User updated successfully"
        else:
            return f"User with id {user_id} not found"
    except Exception as e:
        raise Exception(f"Error updating user: {str(e)}")

# Eliminar un usuario
def delete_user(user_id: int) -> str:
    try:
        user = db_session.query(User).filter_by(id=user_id).one_or_none()
        if user:
            db_session.delete(user)
            db_session.commit()
            return "User deleted successfully"
        else:
            return f"User with id {user_id} not found"
    except Exception as e:
        raise Exception(f"Error deleting user: {str(e)}")
