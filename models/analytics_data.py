import datetime


class AnalyticsData:
    """
    CREATE TABLE `gra_analytics` (
      `count` int NOT NULL AUTO_INCREMENT,
      `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
      `ip` varchar(20) DEFAULT NULL,
      `url` varchar(100) DEFAULT NULL,
      `count_page` int DEFAULT NULL,
      `userID` int DEFAULT NULL,
      `adblock` int DEFAULT NULL,
      `tokenid` varchar(36) DEFAULT NULL,
      `screen_size` int DEFAULT NULL,
      `exercise_input` text,
      PRIMARY KEY (`count`,`date`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2610683 DEFAULT CHARSET=latin1;
    """

    def __init__(self, count: int = 0, current_date: datetime.datetime = "", ip: str = "", url: str = "", count_page: int = 0, user_id: int = 0, adblock: int = 0, token_id: str = "", screen_size: int = 0, exercise_input: str = ""):
        self._count: int = count
        self._my_date: datetime.datetime = current_date
        self._ip: str = ip
        self._url: str = url
        self._count_page: int = count_page
        self._user_id: int = user_id
        self._adblock: int = adblock
        self._token_id: str = token_id
        self._screen_size: int = screen_size
        self._exercise_input: str = exercise_input

    def get_date(self) -> datetime.datetime:
        return self._my_date

    def get_ip(self) -> str:
        return self._ip

    def get_url(self) -> str:
        return self._url

    def get_count_page(self) -> int:
        return self._count_page

    def get_user_id(self) -> int:
        return self._user_id

    def get_adblock(self) -> int:
        return self._adblock

    def get_token_id(self) -> str:
        return self._token_id

    def get_screen_size(self) -> int:
        return self._screen_size

    def get_exercise_input(self) -> str:
        return self._exercise_input
