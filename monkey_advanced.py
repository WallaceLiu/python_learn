class XiaoMing(object):
    def favorite(self):
        print "apple"


class God(object):
    @classmethod
    def new_xiaoming_favorite(cls):
        print "banana"

    @classmethod
    def monkey_patch(cls):
        XiaoMing.favorite = cls.new_xiaoming_favorite


God.monkey_patch()

xiaoming = XiaoMing()
xiaoming.favorite()
