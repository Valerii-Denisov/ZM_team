import peewee
import datetime

db = peewee.SqliteDatabase('Profile.db')


class BaseClass(peewee.Model):
    class Meta:
        database = db


class CookieProfile(BaseClass):
    created_date = peewee.DateTimeField(
        default=datetime.datetime.now,
        null=False,
    )
    cookie_value = peewee.TextField(null=True)
    last_launch_date = peewee.DateTimeField(null=True)
    count_launch = peewee.IntegerField(null=True)


def upload_date(database):
    database.create_tables([CookieProfile])
    # for i in range(0, 15):
    #     string = CookieProfile()
    #     string.save()
    database.close()


upload_date(db)



