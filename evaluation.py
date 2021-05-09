import numpy as np
import pdb


class Evaluator():
    def __init__(self, token, op_token):
        self.token = token
        self.op_token = op_token

    def evaluate(self, row, col, search_area):
        state_score = 0
        state_score += self.fiveRow(row, col, search_area)
        state_score += self.liveFour(row, col, search_area)
        state_score += self.fourRow(row, col, search_area)
        state_score += self.liveThree(row, col, search_area)
        state_score += self.threeRow(row, col, search_area)
        state_score += self.liveTwo(row, col, search_area)
        state_score += self.twoRow(row, col, search_area)
        pdb.set_trace()
        return state_score

    def fiveRow(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 5, False)
        ne_score = self.ne_search(row, col, search_area, 5, False)
        east_score = self.east_search(row, col, search_area, 5, False)
        se_score = self.se_search(row, col, search_area, 5, False)
        south_score = self.south_search(row, col, search_area, 5, False)
        sw_score = self.sw_search(row, col, search_area, 5, False)
        west_score = self.west_search(row, col, search_area, 5, False)
        nw_score = self.nw_search(row, col, search_area, 5, False)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*1000

    def liveFour(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 4, True)
        ne_score = self.ne_search(row, col, search_area, 4, True)
        east_score = self.east_search(row, col, search_area, 4, True)
        se_score = self.se_search(row, col, search_area, 4, True)
        south_score = self.south_search(row, col, search_area, 4, True)
        sw_score = self.sw_search(row, col, search_area, 4, True)
        west_score = self.west_search(row, col, search_area, 4, True)
        nw_score = self.nw_search(row, col, search_area, 4, True)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*500

    def fourRow(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 4, False)
        ne_score = self.ne_search(row, col, search_area, 4, False)
        east_score = self.east_search(row, col, search_area, 4, False)
        se_score = self.se_search(row, col, search_area, 4, False)
        south_score = self.south_search(row, col, search_area, 4, False)
        sw_score = self.sw_search(row, col, search_area, 4, False)
        west_score = self.west_search(row, col, search_area, 4, False)
        nw_score = self.nw_search(row, col, search_area, 4, False)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*200

    def liveThree(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 3, True)
        ne_score = self.ne_search(row, col, search_area, 3, True)
        east_score = self.east_search(row, col, search_area, 3, True)
        se_score = self.se_search(row, col, search_area, 3, True)
        south_score = self.south_search(row, col, search_area, 3, True)
        sw_score = self.sw_search(row, col, search_area, 3, True)
        west_score = self.west_search(row, col, search_area, 3, True)
        nw_score = self.nw_search(row, col, search_area, 3, True)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*400

    def threeRow(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 3, False)
        ne_score = self.ne_search(row, col, search_area, 3, False)
        east_score = self.east_search(row, col, search_area, 3, False)
        se_score = self.se_search(row, col, search_area, 3, False)
        south_score = self.south_search(row, col, search_area, 3, False)
        sw_score = self.sw_search(row, col, search_area, 3, False)
        west_score = self.west_search(row, col, search_area, 3, False)
        nw_score = self.nw_search(row, col, search_area, 3, False)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*150

    def liveTwo(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 2, True)
        ne_score = self.ne_search(row, col, search_area, 2, True)
        east_score = self.east_search(row, col, search_area, 2, True)
        se_score = self.se_search(row, col, search_area, 2, True)
        south_score = self.south_search(row, col, search_area, 2, True)
        sw_score = self.sw_search(row, col, search_area, 2, True)
        west_score = self.west_search(row, col, search_area, 2, True)
        nw_score = self.nw_search(row, col, search_area, 2, True)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*200

    def twoRow(self, row, col, search_area):
        north_score = self.north_search(row, col, search_area, 2, False)
        ne_score = self.ne_search(row, col, search_area, 2, False)
        east_score = self.east_search(row, col, search_area, 2, False)
        se_score = self.se_search(row, col, search_area, 2, False)
        south_score = self.south_search(row, col, search_area, 2, False)
        sw_score = self.sw_search(row, col, search_area, 2, False)
        west_score = self.west_search(row, col, search_area, 2, False)
        nw_score = self.nw_search(row, col, search_area, 2, False)

        scores = [north_score, ne_score, east_score, se_score,
                  south_score, sw_score, west_score, nw_score]
        return sum(scores)*100

    def north_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if row-i == -1:
                    break
                elif i == length-1:
                    return 1 if search_area[row-i][col] == self.token and score == length else 0
                elif search_area[row-i][col] == self.token:
                    score += 1
        else:
            for i in range(length):
                if row-i == -1:
                    break
                elif search_area[row-i][col] == self.token:
                    score += 1

        return 1 if score == length else 0

    def ne_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if col+i == search_area.shape[1] or row-i == -1:
                    break
                elif i == length-1:
                    return 1 if search_area[row-i][col+i] == self.token and score == length else 0
                elif search_area[row-i][col+i] == self.token:
                    score += 1
        else:
            for i in range(length):
                if col+i == search_area.shape[1] or row-i == -1:
                    break
                elif search_area[row-i][col+i] == self.token:
                    score += 1

        return 1 if score == 5 else 0

    def east_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if col+i == search_area.shape[1]:
                    break
                elif i == length-1:
                    return 1 if search_area[row][col+i] == self.token and score == length else 0
                elif search_area[row][col+i] == self.token:
                    score += 1
        else:
            for i in range(length):
                if col+i == search_area.shape[1]:
                    break
                elif search_area[row][col+i] == self.token:
                    score += 1

        return 1 if score == 5 else 0

    def se_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if row+i == search_area.shape[0] or col+i == search_area.shape[1]:
                    break
                elif i == length-1:
                    return 1 if search_area[row+i][col+i] == self.token and score == length else 0
                elif search_area[row+i][col+i] == self.token:
                    score += 1
        else:
            for i in range(length):
                if row+i == search_area.shape[0] or col+i == search_area.shape[1]:
                    break
                elif search_area[row+i][col+i] == self.token:
                    score += 1

        return 1 if score == 5 else 0

    def south_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if row+i == search_area.shape[0]:
                    break
                elif i == length-1:
                    return 1 if search_area[row+i][col] == self.token and score == length else 0
                elif search_area[row+i][col] == self.token:
                    score += 1
        else:
            for i in range(length):
                if row+i == search_area.shape[0]:
                    break
                elif search_area[row+i][col] == self.token:
                    score += 1

        return 1 if score == 5 else 0

    def sw_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if col-i == -1 or row+i == search_area.shape[0]:
                    break
                elif i == length-1:
                    return 1 if search_area[row+i][col-i] == self.token and score == length else 0
                elif search_area[row+i][col-i] == self.token:
                    score +=1
        else:
            for i in range(length):
                if col-i == -1 or row+i == search_area.shape[0]:
                    break
                elif search_area[row+i][col-i] == self.token:
                    score += 1

        return 1 if score == 5 else 0

    def west_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if col-i == -1:
                    break
                elif i == length-1:
                    return 1 if search_area[row][col-i] == self.token and score == length else 0
                elif search_area[row][col-i] == self.token:
                    score +=1
        else:
            for i in range(length):
                if col-i == -1:
                    break
                elif search_area[row][col-i] == self.token:
                    score += 1

        return 1 if score == 5 else 0

    def nw_search(self, row, col, search_area, length, live):
        score = 0
        if live:
            for i in range(length+1):
                if row-i == -1 or col-i == -1:
                    break
                elif i == length-1:
                    return 1 if search_area[row-i][col-i] == self.token and score == length else 0
                elif search_area[row-i][col-i] == self.token:
                    score += 1
        else:
            for i in range(length):
                if row-i == -1 or col-i == -1:
                    break
                elif search_area[row-i][col-i] == self.token:
                    score += 1

        return 1 if score == 5 else 0



