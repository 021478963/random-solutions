class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        points_set = set()
        closest_found = {}
        
        
        for i in points:
            points_set.add((i[0], i[1]))
            
        sorted_points = sorted(points_set, key=itemgetter(0))
        last = sorted_points.pop(0)
        
        for i in sorted_points:
            if i in closest_found.keys():
                closest = closest_found[i]
            else:
                closest = abs(i[0] - last[0]) + abs(i[1] - last[1])
            
            for m in range(max(0, i[0] - closest), i[0] + closest):
                for n in range(max(0, i[1] - closest), i[1] + closest):
                    if (m, n) in points_set:
                        distance = abs(i[0] - m) + abs(i[1] - n)
                        if distance < closest:
                            print(closest)
                            closest = distance
                            if m > i[0]:
                                closest_found[(m, n)] = distance
            last = i
            # print(closest)
            total += closest
        
        return total



            # for m in range(max(0, i[0] - closest), i[0] + closest):
            #     for n in range(max(0, i[1] - closest), i[1] + closest):
            #         if i == (m, n):
            #             continue
            #         if (m, n) in points_set:
            #             distance = abs(i[0] - m) + abs(i[1] - n)
            #             if distance < closest:
            #                 closest = distance
            #                 if m > i[0]:
            #                     closest_found[(m, n)] = distance