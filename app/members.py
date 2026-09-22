from .data import members


def add_member(name, email):
    member = {"id": len(members) + 1, "name": name, "email": email}
    members.append(member)
    return member


def get_members():
    return members


def find_member(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None
