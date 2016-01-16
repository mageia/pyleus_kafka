from pyleus.storm import SimpleBolt


class classifierByUid(SimpleBolt):
    def process_tuple(self, tup):
        print tup.values
        self.emit(tup.values, anchors=[tup])


if __name__ == '__main__':
    classifierByUid().run()

