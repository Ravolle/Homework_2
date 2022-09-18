class CountVectorizer:
    features = []

    def fit_transform(self, data):
        new_data = []
        for row in data:
            words = row.split(' ')
            low_words = []
            for word in words:
                low_words.append(word.lower())
            new_data.append(low_words)

        data = new_data
        counters = [{} for _ in data]

        for j in range(len(data)):
            for word in data[j]:
                if word not in self.features:
                    self.features.append(word)

                if word in counters[j]:
                    counters[j][word] += 1
                else:
                    counters[j][word] = 1

        result = []
        for j in range(len(data)):
            local_result = []
            for key in self.features:
                if key in counters[j]:
                    local_result.append(counters[j][key])
                else:
                    local_result.append(0)

            result.append(local_result)

        return result

    def get_feature_names(self):
        return self.features


if __name__ == '__main__':
    corpus = []

    n = int(input("Введите число векторов: "))
    for i in range(n):
        corpus.append(input("Введите вектор:"))

    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(matrix)
