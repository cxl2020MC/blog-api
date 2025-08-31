

def return_data(data: dict | list | None = None, msg: str = "Success", code: int = 200) -> dict:
    """
    Return data with message and status code
    """
    return {
        "code": code,
        "msg": msg,
        "data": data,
    }

def id_replace(data: dict) -> dict:
    data["_id"] = str(data["_id"])
    return data

def id_list_replace(data: list) -> list:
    for i in range(len(data)):
        id_replace(data[i])
    return data
