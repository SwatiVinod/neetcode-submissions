from collections import defaultdict
class Twitter:

    def __init__(self):
        self.time = 0
        self.followerMap = defaultdict(set) # user Id -> (followee ids)
        self.tweetmap = defaultdict(list) # userid -> [(time, tweet id)]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append((self.time, tweetId))
        self.time -= 1
        print(self.followerMap)
        print(self.tweetmap)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        result = []

        self.followerMap[userId].add(userId)
        for userId in self.followerMap[userId]:
            if self.tweetmap[userId]:
                index = len(self.tweetmap[userId]) - 1
                neg_time, tweetId = self.tweetmap[userId][index]
                minHeap.append((neg_time, tweetId, userId, index - 1))

        heapq.heapify(minHeap)        
        while len(result) < 10 and minHeap:
            neg_time, tweetId, userId, lastindex = heapq.heappop(minHeap)
            result.append(tweetId)
            if lastindex >=0:
                last_neg_time, last_tweetId = self.tweetmap[userId][lastindex]
                heapq.heappush(minHeap, (last_neg_time, last_tweetId, userId, lastindex-1))
        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followerMap[followerId].add(followeeId)
        print(self.followerMap)
        print(self.tweetmap)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        print(self.followerMap)
        print(self.tweetmap)

        
