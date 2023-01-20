candies = [2,3,5,1,3]
extraCandies = 3
def kidsWithCandies(candies, extraCandies):
        max_candy = -1
        
        for candy in candies:
            if candy > max_candy:
                max_candy = candy
        results = []
        
        for candy in candies:
            if candy + extraCandies >= max_candy:
                print(candy + extraCandies)
                results.append(True)
            else:
                print(candy+extraCandies)
                results.append(False)
                
        return results

a = kidsWithCandies(candies,extraCandies)
print(a)