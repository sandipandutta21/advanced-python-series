from datetime import datetime
from uuid import UUID


class Tweets:
    """ Class to store tweets of users """

    def __init__(self, tweet_body: str, tweet_time: datetime, tweet_id: UUID, tweet_lang: str,
                 tweet_place: str, tweet_retweet_count: int, tweet_hashtags: list,
                 tweet_user_id: str, tweet_user_name: str) -> None:
        self.__tweet_body = tweet_body
        self.__tweet_time = tweet_time
        self.__tweet_id = tweet_id
        self.__tweet_lang = tweet_lang
        self.__tweet_place = tweet_place
        self.__tweet_retweet_count = tweet_retweet_count
        self.__tweet_hashtags = tweet_hashtags
        self.__tweet_user_id = tweet_user_id
        self.__tweet_user_name = tweet_user_name

    def __str__(self) -> str:
        """ Because I need to see things to debug """
        return "Tweet: " + self.__tweet_body + " " + str(self.__tweet_time) + " " + str(self.__tweet_id) \
               + " " + self.__tweet_lang + " " + self.__tweet_place + " " + str(self.__tweet_retweet_count) \
               + " " + str(self.__tweet_hashtags) + " " + self.__tweet_user_id + " " + self.__tweet_user_name

    def __eq__(self, other) -> bool:
        """ Because I need to compare things """
        if other.__class__ == self.__class__:
            return (self.__tweet_body, self.__tweet_time, self.__tweet_id, self.__tweet_lang, self.__tweet_place,
                    self.__tweet_retweet_count, self.__tweet_hashtags, self.__tweet_user_id, self.__tweet_user_name) \
                   == (
                   other.__tweet_body, other.__tweet_time, other.__tweet_id, other.__tweet_lang, other.__tweet_place,
                   other.__tweet_retweet_count, other.__tweet_hashtags, other.__tweet_user_id, other.__tweet_user_name)
        else:
            return NotImplemented

    def __hash__(self):
        """ Because God knows why but someone might try to put these in a dict """

        return hash(self.__tweet_body) ^ hash(self.__tweet_time) ^ hash(self.__tweet_id) \
               ^ hash(self.__tweet_lang) ^ hash(self.__tweet_place) ^ hash(self.__tweet_retweet_count) \
               ^ hash(self.__tweet_hashtags) ^ hash(self.__tweet_user_id) ^ hash(self.__tweet_user_name)

    # Because hashabale means I need to make this ready only i.e. immutable
    @property
    def tweet_body(self) -> str:
        return self.__tweet_body

    @property
    def tweet_time(self) -> datetime:
        return self.__tweet_time

    @property
    def tweet_id(self) -> UUID:
        return self.__tweet_id

    @property
    def tweet_lang(self) -> str:
        return self.__tweet_lang

    @property
    def tweet_place(self) -> str:
        return self.__tweet_place

    @property
    def tweet_retweet_count(self) -> int:
        return self.__tweet_retweet_count

    @property
    def tweet_hashtags(self) -> list:
        return self.__tweet_hashtags

    @property
    def tweet_user_id(self) -> str:
        return self.__tweet_user_id

    @property
    def tweet_user_name(self) -> str:
        return self.__tweet_user_name

