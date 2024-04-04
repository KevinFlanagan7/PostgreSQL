from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
# db = create_engine("postgresql:///chinook")
db = create_engine("postgresql://postgres:password@localhost/chinook")

meta = MetaData(db)

# create variable for "Artist" table
artist_table = Table(
    "artist", meta,
    Column("artist_id", Integer, primary_key=True),
    Column("name", String)
)

# create variable for "Album" table
album_table = Table(
    "album", meta,
    Column("album_id", Integer, primary_key=True),
    Column("title", String),
    Column("artist_id", Integer, ForeignKey("artist_table.artist_id"))
)

# create variable for "Track" table
# track_table = Table(
#    "Track", meta,
#    Column("TrackId", Integer, primary_key=True),
#    Column("Name", String),
#    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
#    Column("MediaTypeId", Integer, primary_key=False),
#    Column("GenreId", Integer, primary_key=False),
#    Column("Composer", String),
#    Column("Milliseconds", Integer),
#    Column("Bytes", Integer),
#    Column("UnitPrice", Float)
# )

# making the connection
with db.connect() as connection:

    # First 4 queries work as database file is not compatible with windows PostgreSQL installed!!

    # Query 1 - select all records from the "Artist" table
    # select_query = artist_table.select()

    # Query 2 - select only the "Name" column from the "Artist" table
    # select_query = artist_table.select().with_only_columns([artist_table.c.name])

    # Query 3 - select only 'Queen' from the "Artist" table
    # select_query = artist_table.select().where(artist_table.c.name == "Queen")

    # Query 4 - select only by 'ArtistId' #51 from the "Artist" table
    select_query = artist_table.select().where(artist_table.c.artist_id == 51)

    # Query 5 - select only the albums with 'ArtistId' #51 on the "Album" table
    # select_query = album_table.select().where(album_table.c.artist_id == 51)

    # Query 6 - select all tracks where the composer is 'Queen' from the "Track" table
    # select_query = track_table.select().where(track_table.c.Composer == "Queen")

    results = connection.execute(select_query)
    for result in results:
        print(result)