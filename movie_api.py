import pandas as pd
import json
from rank_bm25 import BM25Okapi
import string
import numpy as np

class MovieAPI:
    def __init__(self):
        with open("year_db.json") as f:
            self.year_db = json.load(f)
        with open("person_db.json") as f:
            self.person_db = json.load(f)
        with open("movie_db.json") as f:
            self.movie_db = json.load(f)
        self.person_db_lookup = self._get_direct_lookup_db(self.person_db)
        self.movie_db_lookup = self._get_direct_lookup_db(self.movie_db)
        self.movie_corpus, self.movie_bm25 = self._get_ranking_db(self.movie_db)
        self.person_corpus, self.person_bm25 = self._get_ranking_db(self.person_db)
    
    def _normalize(self, x):
        return " ".join(x.lower().replace("_", " ").translate(str.maketrans('', '', string.punctuation)).split())
    
    def _get_ranking_db(self, db):
        corpus = [i.split() for i in db.keys()]
        bm25 = BM25Okapi(corpus)
        return corpus, bm25
    
    def _get_direct_lookup_db(self, db):
        temp_db = {}
        for key, value in db.items():
            if 'id' in value:
                temp_db[value['id']] = value
        return temp_db
    
    def _search_entity_by_name(self, query, bm25, corpus, map_db):
        n = 10
        query = self._normalize(query)
        scores = bm25.get_scores(query.split())
        top_idx = np.argsort(scores)[::-1][:n]
        top_ne = [" ".join(corpus[i]) for i in top_idx if scores[i] != 0]
        top_e = []
        for ne in top_ne[:n]:
            assert(ne in map_db)
            top_e.append({ne: map_db[ne]})
        return top_e[:n]
    
    def get_person_info(self, person_name):
        # director, actor info
        res = self._search_entity_by_name(person_name, self.person_bm25, self.person_corpus, self.person_db)
        return res
    
    def get_movie_info(self, person_name):
        # director, actor info
        res = self._search_entity_by_name(person_name, self.movie_bm25, self.movie_corpus, self.movie_db)
        return res
    
    def get_year_info(self, year):
        # precise: year function
        if year not in range(1990, 2022):
            raise ValueError("Year must be between 1990 and 2021")
        return self.year_db.get(str(year), None)
    
    def get_movie_info_by_id(self, movie_id):
        # precise locate fuction
        return self.movie_db_lookup.get(movie_id, None)     
    
    def get_person_info_by_id(self, person_id):
        # precise locate fuction
        return self.person_db_lookup.get(person_id, None) 