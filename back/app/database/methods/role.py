from ..models.role import Role


def db_get_all_roles():
    objs = []
    for role in Role:
        objs.append(f"{role}")
    return objs
