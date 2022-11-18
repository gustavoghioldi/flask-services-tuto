def response_person_body(p: tuple)->dict:
    return {
            "dni": p[0],
            "firstName": p[2],
            "lastName": p[1],
            "active": True if p[3] == 1 else False
        }