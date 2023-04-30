def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "username": item["username"],
        "firstname": item["firstname"],
        "lastname": item["lastname"],
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def userList(item) -> list:
    return [item["username"], item["firstname"], item["lastname"]]

def usersList(ulist) -> list:
    return [userList(item) for item in ulist]