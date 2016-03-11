from munin.models import Model, User, Token
from peewee import DateTimeField, FloatField, ForeignKeyField
import datetime


class Location(Model):
    latitude = FloatField()
    longitude = FloatField()
    timestamp = DateTimeField()
    user = ForeignKeyField(User, related_name='locations')
    token = ForeignKeyField(Token, related_name='data')

    @staticmethod
    def add(token_id, latitude, longitude, timestamp):
        try:
            token = Token.get(Token.id == token_id)

            timestamp = datetime.datetime.strptime(timestamp,
                                                   '%Y-%m-%dT%H:%M:%S.%fZ')

            latitude = float(latitude)
            longitude = float(longitude)

            location = Location.create(user=token.user, token=token,
                                       latitude=latitude, longitude=longitude,
                                       timestamp=timestamp)

            return location
        except User.DoesNotExist:
            pass

        return None
