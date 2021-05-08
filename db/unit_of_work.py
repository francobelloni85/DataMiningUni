from typing import List

import pymysql
from pymysql.connections import Connection

from models.analytics_data import AnalyticsData


class UnitOfWork:

    def __init__(self):
        self._host = "localhost"
        self._user = "root"
        self._password = "admin"
        self._database = "sql1238724_5"

    def get_all_row(self, limit: int = 100):

        connection: Connection = None
        result: List[AnalyticsData] = []
        try:
            # database connection
            connection: Connection = pymysql.connect(host=self._host, user=self._user, passwd=self._password, database=self._database)
            cursor = connection.cursor()

            # queries for retrieving all rows
            retrieve = "SELECT count, date, ip, url, count_page, userID, adblock,  tokenid, screen_size, exercise_input FROM ese_analytics LIMIT {0}".format(limit)

            # executing the query
            cursor.execute(retrieve)
            rows = cursor.fetchall()
            for row in rows:
                result.append(AnalyticsData(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

        except Exception as ex:
            print(ex)
        finally:
            # committing the connection then closing it.
            if connection is not None:
                connection.commit()
                connection.close()
