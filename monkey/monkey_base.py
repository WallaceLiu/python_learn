class XiaoMing(object):
    def favorite(self):
        print("apple")


def new_favorite():
    print("banana")


xiaoming = XiaoMing()
xiaoming.favorite()

xiaoming.favorite = new_favorite
xiaoming.favorite()
