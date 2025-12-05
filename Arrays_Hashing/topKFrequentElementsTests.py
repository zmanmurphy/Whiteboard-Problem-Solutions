from topKFrequentElements import topKFrequent

def test_topKFrequent():
    assert topKFrequent([1,2,3,4,5,5,6,7,1], 2) == [5,1]
    assert topKFrequent([6,8,2,1,3,4,4,5,2,2,2,5,6,7], 1) == [2]