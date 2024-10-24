from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def Get_Main_Page() -> dict:
    return {'message': "Главная страница"}


@app.get("/user/admin")
async def Get_Admin_Page() -> dict:
    return {'message': f"Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def Get_User_Number(user_id: str) -> dict:
    return {'message': f"Вы вошли как пользователь № {user_id}"}


#  полноценные WEB-запросы:
@app.get("/user")
async def Get_User_info(username: str, age: int) -> dict:
    return {'massage': "Информация о пользователе.", 'Имя': username, 'Возраст': age}
