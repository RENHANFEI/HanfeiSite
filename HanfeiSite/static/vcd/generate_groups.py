from random import choice, random, shuffle, sample

class GroupGenerator(object):
    def __init__(self):

        super(GroupGenerator, self).__init__()

        self.__group_num = 200

        self.__images = list(range(32))
        self.__models = ['equal', 'sinc']
        self.__apertures = [3, 5]    # pinhole size
        self.__degrees = [300, 320]
        self.__test_num = 12
        self.__adapt_num = 4

    def generate(self):

        groups = []

        for i in range(self.__group_num):
            pairs = []
            for image_idx in sample(self.__images, self.__test_num):
                for model in self.__models:
                    for aperture in self.__apertures:
                        for degree in self.__degrees:
                            param1 = (str(image_idx), model, str(aperture), str(degree))
                            param2 = (str(image_idx), choice(self.__models), 
                                str(choice(self.__apertures)), str(degree))
                            # avoid evaluation between two same images
                            while param2 == param1:
                                param2 = (str(image_idx), choice(self.__models), 
                                str(choice(self.__apertures)), str(degree))
                            # shuffle two images
                            param1, param2 = (param1, param2) if random() < 0.5 \
                                else (param2, param1)
                            filename1 = '_'.join(param1) + '.png'
                            filename2 = '_'.join(param2) + '.png'

                            pairs.append((filename1, filename2))

            adaptation = sample(pairs, self.__adapt_num)
            pairs.extend(adaptation)
            pairs = list(reversed(pairs))

            groups.append(pairs)

        print(groups)


if __name__ == '__main__':
    gen = GroupGenerator()
    gen.generate()