from collections import namedtuple
import heapq

Star = namedtuple('Star',('distance','inhabitants','name'))

Pluto = Star(10000,500,'Pluto')
Saturn = Star(1000000,200,'Saturn')
Jupiter = Star(1,100000,'Jupiter')
Saturn = Star(200000, 550000,'Saturn')
Mars = Star(10000000000,100000000,'Mars')
Venus = Star(90000,9900000,'Venus')

stars = [Pluto,Saturn,Jupiter,Saturn,Mars,Venus]

def returnKclosestStars(stars,k):
    max_heap = []  # you want to pop the max every time

    for star in stars[:k]:
        heapq.heappush(max_heap, (-star.distance,star))

    for star in stars[k:]:
        heapq.heappushpop(max_heap, (-star.distance,star))

    return [star[1].name for star in heapq.nlargest(k,max_heap)]

def returnKclosestStars2(stars,k):
    max_heap = []  # you want to pop the max every time

    for star in stars:
        heapq.heappush(max_heap,(-star.distance,star))
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [star[1].name for star in heapq.nlargest(k,max_heap)]

print(returnKclosestStars(stars,3))
print(returnKclosestStars2(stars,3))
