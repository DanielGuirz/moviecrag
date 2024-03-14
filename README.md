# Description

The mock Movie API to be used in KDD Cup 2024: Comprehensive RAG Benchmark. It provides access to a large movie corpus.

# Self - Setup Instruction

1. Install all packages in requirements.txt
2. Move the 3 cached databases: **movie_db.json**, **person_db.json** and **year_db.json** into the current directory.
3. Create a .py file or a notebook file under the same directory. To import the api:
   ```python
    from movie_api import MovieAPI
   ```

# Example Usage

See **example_usage.py** for details

# Detailed Documentation

```python
class MovieAPI()
```

Knowledge Graph API for movie domain

Mock KG API for movie domain. Supports getting information of movies and of persons including cast and crew.

<a id="..movie_api.MovieAPI.__init__"></a>

#### \_\_init\_\_

```python
def __init__(top_n: int = 10) -> None
```

Initialize API and load data. Loads 3 dbs from json

**Arguments**:

- `top_n` - max number of entities to return in entity search

<a id="..movie_api.MovieAPI.get_person_info"></a>

#### get\_person\_info

```python
def get_person_info(person_name: str) -> List[Dict[str, Any]]
```

Gets person info in database through BM25.

Gets person info through BM25 Search. The returned entities MAY contain the following fields:
- name (string): name of person
- id (int): unique id of person
- acted_movies (list[int]): list of movie ids in which person acted
- directed_movies (list[int]): list of movie ids in which person directed
- birthday (string): string of person's birthday, in the format of "YYYY-MM-DD"
- oscar_awards: list of oscar awards (dict), win or nominated, in which the person was the entity. The format for oscar award entity are:
'year_ceremony' (int): year of the oscar ceremony,
'ceremony' (int): which ceremony. for example, ceremony = 50 means the 50th oscar ceremony,
'category' (string): category of this oscar award,
'name' (string): name of the nominee,
'film' (string): name of the film,
'winner' (bool): whether the person won the award

**Arguments**:

- `person_name` - string to be searched


**Returns**:

  list of top n matching entities. Entities are ranked by BM25 score.

<a id="..movie_api.MovieAPI.get_movie_info"></a>

#### get\_movie\_info

```python
def get_movie_info(person_name: str) -> List[Dict[str, Any]]
```

Gets movie info in database through BM25.

Gets movie info through BM25 Search. The returned entities MAY contain the following fields:
- title (string): title of movie
- id (int): unique id of movie
- release_date (string): string of movie's release date, in the format of "YYYY-MM-DD"
- original_title (string): original title of movie, if in another language other than english
- original_language (string): original language of movie. Example: 'en', 'fr'
- budget (int): budget of movie, in USD
- revenue (int): revenue of movie, in USD
- rating (float): rating of movie, in range [0, 10]
- genres (list[dict]): list of genres of movie. Sample genre object is {'id': 123, 'name': 'action'}
- oscar_awards: list of oscar awards (dict), win or nominated, in which the movie was the entity. The format for oscar award entity are:
'year_ceremony' (int): year of the oscar ceremony,
'ceremony' (int): which ceremony. for example, ceremony = 50 means the 50th oscar ceremony,
'category' (string): category of this oscar award,
'name' (string): name of the nominee,
'film' (string): name of the film,
'winner' (bool): whether the person won the award
- cast (list [dict]): list of cast members of the movie and their roles. The format of the cast member entity is:
'name' (string): name of the cast member,
'id' (int): unique id of the cast member,
'character' (string): character played by the cast member in the movie,
'gender' (string): the reported gender of the cast member. Use 2 for actor and 1 for actress,
'order' (int): order of the cast member in the movie. For example, the actress with the lowest order is the main actress,
- crew' (list [dict]): list of crew members of the movie and their roles. The format of the crew member entity is:
'name' (string): name of the crew member,
'id' (int): unique id of the crew member,
'job' (string): job of the crew member,

**Arguments**:

- `movie_name` - string to be searched


**Returns**:

  list of top n matching entities. Entities are ranked by BM25 score.

<a id="..movie_api.MovieAPI.get_year_info"></a>

#### get\_year\_info

```python
def get_year_info(year: str) -> Dict[str, Any]
```

Gets info of a specific year

Gets year info. The returned entity MAY contain the following fields:
- movie_list: list of movie ids in the year. This field can be very long to a few thousand films
- oscar_awards: list of oscar awards (dict), held in that particular year. The format for oscar award entity are:
'year_ceremony' (int): year of the oscar ceremony,
'ceremony' (int): which ceremony. for example, ceremony = 50 means the 50th oscar ceremony,
'category' (string): category of this oscar award,
'name' (string): name of the nominee,
'film' (string): name of the film,
'winner' (bool): whether the person won the award

**Arguments**:

- `year` - string of year. Note that we only support years between 1990 and 2021


**Returns**:

  an entity representing year information

<a id="..movie_api.MovieAPI.get_movie_info_by_id"></a>

#### get\_movie\_info\_by\_id

```python
def get_movie_info_by_id(movie_id: int) -> Dict[str, Any]
```

Helper fast lookup function to get movie info directly by id

Return a movie entity with same format as the entity in get_movie_info.

**Arguments**:

- `movie_id` - unique id of movie


**Returns**:

  an entity representing movie information

<a id="..movie_api.MovieAPI.get_person_info_by_id"></a>

#### get\_person\_info\_by\_id

```python
def get_person_info_by_id(person_id: int) -> Dict[str, Any]
```

Helper fast lookup function to get person info directly by id

Return a person entity with same format as the entity in get_person_info.

**Arguments**:

- `person_id` - unique id of person


**Returns**:

  an entity representing person information
