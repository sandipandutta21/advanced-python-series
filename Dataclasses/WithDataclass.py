from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4
@dataclass(frozen=True, order=True)
class Tweets:
    """ Class to store tweets of users """

    tweet_body: str = None
    tweet_time: datetime = datetime.utcnow()
    tweet_id: UUID = uuid4()
    tweet_lang: str = 'en-IN'
    tweet_place: str = 'IN'
    tweet_retweet_count: int = 0
    tweet_hashtags: list[str] = field(default_factory=list)
    tweet_user_id: str = None
    tweet_user_name: str = None


@dataclass(init=False, repr=False, eq=False, unsafe_hash=False)
class Tweets():
    tweet_retweet_count: int = field(repr=False, compare=False,                    
                                 default=0)


@dataclass
class ResponseOnTweet:
    
    tweet_total_response_count: int = field(init=False)
    tweet_retweet_count: int = 0
    tweet_comment_count: int = 0 
    tweet_like_count: int = 0
    def __post_init__(self):
        self.tweet_total_response_count = self.tweet_retweet_count + self.tweet_comment_count + self.tweet_like_count


