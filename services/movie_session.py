import datetime

from db.models import MovieSession, CinemaHall, Movie
from django.db.models import QuerySet


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int,
) -> MovieSession:

    return MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id),
    )


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession] | MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None,
) -> None:

    movie_session_filtered = MovieSession.objects.filter(id=session_id)

    if show_time:
        movie_session_filtered.update(show_time=show_time)

    if movie_id:
        movie_session_filtered.update(movie=movie_id)

    if cinema_hall_id:
        movie_session_filtered.update(cinema_hall=cinema_hall_id)


def delete_movie_session_by_id(session_id: int) -> None:
    MovieSession.objects.filter(id=session_id).delete()
