from database.db import get_connection
from .entities.wheater import Wheater

class WheaterModel():
    @classmethod #para instaciar directamente
    def get_wheaters(self):
        try:
            connection = get_connection()
            wheaters=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, ciudad, hora, clima FROM valores")
                resultset=cursor.fetchall()

                for row in resultset:
                    wheater = Wheater(row[0],row[1],row[2],row[3])
                    wheaters.append(wheater.to_JSON())
            connection.close()
            return wheaters

        except Exception as ex:
            raise Exception(ex)