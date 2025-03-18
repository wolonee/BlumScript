from pymongo import MongoClient, DESCENDING

class Table_scr:

    def __init__(self, dbase):
        cluster = MongoClient(dbase, connectTimeoutMS=120000)
        db = cluster["admin"]
        self.collection = db["Collection_BlumScript_2"]


    def Count_Data(self):
        count_users = self.collection.count_documents({})
        # who_have_WebName = self.collection.count_documents({"User.Web.WebName": {"$exists": True, "$ne": None}})
        # Data = [count_users, who_have_Valentine]
        return count_users


    def AddUser(self, UserId_getnode):
        try:
            highest_id_doc = self.collection.find_one(sort=[("_id", DESCENDING)])
            
            if highest_id_doc:
                highest_id = highest_id_doc['_id']
            else:
                highest_id = 0

            new_user = {
                '_id': highest_id + 1,
                "User": {
                    "ID": UserId_getnode,
                    "UnicKey": False,
                    "PATHs_to_Telegram": None
                }
            }

            self.collection.insert_one(new_user)
        except Exception as error:
            print("Error AddUser", error)


    def AddFreeKey_toUser(self, Comp_id, UnicKey):
        try:         
            result = self.collection.find_one({'User.ID': Comp_id})
            self.collection.update_one(result, {"$set": {f"User.UnicKey": UnicKey}})
        except Exception as error:
            print("Error AddFreeKey_toUser", error)


    def AddFreeKey(self, AddFreeKey):
        try:
            self.collection.update_one(
                {"name": "example"},
                {"$push": {"FreeKeys": AddFreeKey}}
            )
        except Exception as error:
            print("Error AddFreeKey", error)


    def GetFreeKey(self):
        try:
            result = self.collection.find_one({"name": "example"})
            return result["FreeKeys"]
        except Exception as error:
            print("Error GetFreeKey", error)


    def DeleteFreeKey(self, NameKey):
        try:         
            self.collection.update_one(
                {"name": "example"},
                {"$pull": {"FreeKeys": NameKey}}
            )
        except Exception as error:
            print("Error DeleteFreeKey", error)


    def CheckRegistr(self, UserId_getnode):
        try:
            result = self.collection.find_one({'User.ID': UserId_getnode})
            return bool(result)
        except Exception as error:
            print("Error CheckRegistr", error)

    def CheckUnicKey(self, UserId_getnode):
        try:
            result = self.collection.find_one({'User.ID': UserId_getnode})
            # print(bool(result["User"]["UnicKey"]))
            return bool(result["User"]["UnicKey"])
        except Exception as error:
            print("Error CheckUnicKey", error)


    # def SavePaths(self, UserId_getnode, list_with_paths):
    #     try:         
    #         result = self.collection.find_one({'User.ID': UserId_getnode})
    #         for path in list_with_paths:
    #             true_path = path.replace("\\", "/")
    #             self.collection.update_one(result, {"$set": {f"User.PATHs_to_Telegram": true_path}})
    #     except Exception as error:
    #         print("Error SavePaths", error)

    
    # def GetSavePaths(self, UserId_getnode):
    #     try:
    #         result = self.collection.find_one({'User.ID': UserId_getnode})
    #         print(result["User"]["PATHs_to_Telegram"])
    #         return result["User"]["PATHs_to_Telegram"]
    #     except Exception as error:
    #         print("Error CheckSavePaths", error)


    # def GetUsersAll(self):
    #     try:
    #         user_ids = []
    #         users = self.collection.find({}, {"User.ID": 1})
    #         for user in users:
    #             user_ids.append(user["User"]["ID"])
    #         return user_ids
    #     except Exception as error:
    #         print("Error GetUsersAll", error)


db = Table_scr("mongodb://expin1226707:.aRTTIG12267@91.107.123.97:37757/admin")
# db.SavePaths()
# # Подключение к MongoDB
# client = MongoClient("mongodb://expin1226707:.aRTTIG12267@91.107.123.97:37757/admin")

# # Выполнение запроса serverStatus для получения информации о сервере
# server_status = client.admin.command("serverStatus")

# # Вывод информации о подключениях
# print("Максимальное количество подключений:", server_status)

# # Закрытие соединения с MongoDB
# client.close()

db.AddFreeKey("c4940c4f-8896-43ce-823c-575199851ed3")
# new_user = {
#     '_id': 1,
#     "name": "example",
#     "FreeKeys": ["b174ee50-59f7-429a-aff0-5f2b23c58c48"]
# }

# db.collection.insert_one(new_user)

# db.AddFreeKey("bhertbjtej")
# a = db.GetFreeKey()
# print(a)
# for i in a:
#     print(i)
