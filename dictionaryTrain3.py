# Dictionary train 3

class ThirdTrain:
    thirdDictionary = {
        "key1": {
            "key1a": "value1a"
        },
        "key2":
            {"key2a": {"key2aa": "value1aa"},
             "key2b": {"key2ab": {"subkey1ab": "subValue1ab"}}
             }
    }
    # print(thirdDictionary["key2"]["key2b"]["key2ab"]["subkey1ab"])

    thirdDictionaryB = {}
    thirdDictionaryB["first"] = {"firstInnerKey": "firstInnerValue"}
    thirdDictionaryB["second"] = {"secondInnerKey": {}}
    thirdDictionaryB["second"]["secondInnerKey"]["secondDeeperKey"] = 3

    print(thirdDictionaryB)
    print(thirdDictionaryB["second"]["secondInnerKey"]["secondDeeperKey"])
