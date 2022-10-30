### Import Models

```python
from artists.models import Artist
from albums.models import Album
from users.models import User
```

### 1. create some artists

```python
user1 = User.objects.create_user(username='user1', password='password')
user1.save()
artist1 = Artist(stage_name="Coldplay", social_media_link="https://www.instagram.com/coldplay/?hl=en", user=user1)
artist1.save()

user2 = User.objects.create_user(username='user2', password='password')
user2.save()
artist2 = Artist(stage_name="Kanye West", social_media_link="https://www.instagram.com/kanyewest/?hl=en", user=user2)
artist2.save()

user3 = User.objects.create_user(username='user3', password='password')
user3.save()
artist3 = Artist(stage_name="Eminem", social_media_link="https://www.instagram.com/eminem/?hl=en", user=user3)
artist3.save()

user4 = User.objects.create_user(username='user4', password='password')
user4.save()
artist4 = Artist(stage_name="Ahmed Nasser", social_media_link="https://www.instagram.com/kanyewest/?hl=en", user=user4)
artist4.save()
```

### 2. list down all artists

```python
Artist.objects.all()
```

### 3. list down all artists sorted by name

```python
Artist.objects.order_by('stage_name')
```

### 4. list down all artists whose name starts with `a`

```python
Artist.objects.filter(stage_name__startswith='C');
```

### 5. in 2 different ways, create some albums and assign them to any artists (hint: use `objects` manager and use the related object reference)

```python
from datetime import datetime
from tzlocal import get_localzone

tz = get_localzone()

release_datetime1 = datetime(2023, 5, 15, 8, 15, 12, 0, tzinfo=tz)
album1 = artist1.album_set.create(name='album 1', release_datetime=release_datetime1, cost=25.00)

release_datetime2 = datetime(2024, 2, 13, 5, 35, 22, 0, tzinfo=tz)
album2 = Album(name='album 2', release_datetime=release_datetime2, cost=28.99, artist=artist2)
album2.save()

release_datetime3 = datetime(2010, 2, 13, 5, 35, 22, 0, tzinfo=tz)
album3 = Album(name='album 3', release_datetime=release_datetime3, cost=30.69, artist=artist3)
album3.save()
```

### 6. get the latest released album

```python
Album.objects.order_by('release_datetime')
```

### 7. get all albums released before today

```python
Album.objects.filter(release_datetime__lt=datetime.datetime.today())
```

### 8. get all albums released today or before but not after today

```python
Album.objects.filter(release_datetime__lte=datetime.datetime.today())
```

### 9. count the total number of albums (hint: count in an optimized manner)

```python
Album.objects.all().count()
```

### 10. in 2 different ways, for each artist, list down all of his/her albums (hint: use `objects` manager and use the related object reference)

```python
for artist in Artist.objects.all():
    artist.album_set.all()

for artist in Artist.objects.all():
    Album.objects.filter(artist=artist)
```

### 11. list down all albums ordered by cost then by name (cost has the higher priority)

```python
Album.objects.order_by('cost', 'name')
```
