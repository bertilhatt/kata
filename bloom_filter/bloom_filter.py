
class Bouquet:
    def __init__(self, hash_num=40, bitmap_size=1024*1024):
        self.hash_num = hash_num
        self.bitmap_size = bitmap_size
        self.bitmap = [set() for _ in range(hash_num)]

    def bloom(self, word):
        _hash_set_ = []
        for i in range(self.hash_num):
            _hash_ = hash(word * i) % self.bitmap_size
            _hash_set_.append(_hash_)
        return _hash_set_

    def fill(self, dictionary):
        for word in dictionary:
            _hash_set_ = self.bloom(word)
            for i, _hash_ in enumerate(_hash_set_):
                self.bitmap[i].add(_hash_)

    def check_presence(self, text):
        flower = self.bloom(text)
        present = True
        for i in range(self.hash_num):
            present &= flower[i] in self.bitmap[i]
        return present

    def saturation(self):
        return [len(self.bitmap[i]) for i in range(self.hash_num)]


if __name__ == '__main__':
    bouquet = Bouquet()
    system_dict_path = '/usr/share/dict/words'
    with open(system_dict_path, 'r') as f:
        system_dict = f.read().split('\n')
    bouquet.fill(system_dict)
    print(bouquet.saturation())
    made_up_strings = ['aisof', 'kltry', 'plllk', 'qwwqw', 'sdrtp', ]
    for string in made_up_strings:
        print(string, bouquet.check_presence(string))
