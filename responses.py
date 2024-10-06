from random import choice, random





def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "You didn't say anything"
    elif "hello" in lowered:
        return "hello"
    elif "gm" in lowered:
        return "Good Morning!"
    else:
        return "I dont understand what that means"
    
