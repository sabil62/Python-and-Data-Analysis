class questions:
    def __init__(self, question_phrase, answer):
        self.question_phrase = question_phrase
        self.answer = answer


question_pack = [questions('capital of china?\na Beijing\nb Shanghai \n c hongkong', 'a'),
                 questions('boeing is a? \na car \n b Aeroplane \n c tractor', 'b')]

print(len(question_pack))  #not needed using it just for fun


def play_game(questions_pack_here):
    score = 0
    for questionsss in questions_pack_here:
        print(questionsss.question_phrase)  # this asks questions
        answer = input('enter ans:')
        if answer == questionsss.answer:
            score = score + 1
    print('you score ' + str(score) + ' out of ' + str(len(question_pack)))


play_game(question_pack)
