import numpy as np
import pdb


class Evaluator():
    def __init__(self, token, op_token):
        self.token = token
        self.op_token = op_token
        self.length = 5

    def evaluate(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, self.length)
        ne_score = self.ne_search(row, col, search_area, self.length)
        east_score = self.east_search(row, col, search_area, self.length)
        se_score = self.se_search(row, col, search_area, self.length)
        south_score = self.south_search(row, col, search_area, self.length)
        sw_score = self.sw_search(row, col, search_area, self.length)
        west_score = self.west_search(row, col, search_area, self.length)
        nw_score = self.nw_search(row, col, search_area, self.length)

        all_scores = [north_score, ne_score, east_score, se_score, south_score, sw_score, west_score, nw_score]
        return sum(all_scores)

    def north_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if row-i < 0:
                break
            elif search_area[row-i][col] == self.token:
                score += 1
        return score

    def ne_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if col+i > search_area.shape[1]-1 or row-i < 0:
                break
            elif search_area[row-i][col+i] == self.token:
                score += 1
        return score

    def east_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if col+i > search_area.shape[1]-1:
                break
            elif search_area[row][col+i] == self.token:
                score += 1
        return score


    def se_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if row+i > search_area.shape[0]-1 or col+i > search_area.shape[1]-1:
                break
            elif search_area[row+i][col+i] == self.token:
                score += 1
        return score

    def south_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if row+i > search_area.shape[0]-1:
                break
            elif search_area[row+i][col] == self.token:
                score += 1
        return score


    def sw_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if col-i < 0 or row+i > search_area.shape[0]-1:
                break
            elif search_area[col-i][row+i] == self.token:
                score += 1
        return score

    def west_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if col-i < 0:
                break
            elif search_area[row][col-i] == self.token:
                score += 1
        return score

    def nw_search(self, row, col, search_area, length):
        score = 0
        for i in range(1, length+1):
            if row-i < 0 or col-i < 0:
                break
            elif search_area[row-i][col-i] == self.token:
                score += 1
        return score




