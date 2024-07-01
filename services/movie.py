from db.models import Movie
from django.db.models import QuerySet


def get_movies(
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> QuerySet[Movie]:
    all_movie = Movie.objects.all()

    if genres_ids and actors_ids:
        return all_movie.filter(genres__in=genres_ids, actors__in=actors_ids)
    if genres_ids:
        return all_movie.filter(genres__in=genres_ids)
    if actors_ids:
        return all_movie.filter(actors__in=actors_ids)
    if (genres_ids and actors_ids) is None:
        return all_movie


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list[int] = None,
        actors_ids: list[int] = None,
) -> Movie:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
    return movie
