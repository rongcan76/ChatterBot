from django.test import TestCase
from django.conf import settings
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


class ChatterBotCorpusTrainingTestCase(TestCase):
    """
    Test case for training with data from the ChatterBot Corpus.

    Note: This class has a mirror tests/training_tests/
    """

    def setUp(self):
        super(ChatterBotCorpusTrainingTestCase, self).setUp()
        self.chatbot = ChatBot(**settings.CHATTERBOT)

        self.trainer = ChatterBotCorpusTrainer(
            self.chatbot,
            show_training_progress=False
        )

    def tearDown(self):
        super(ChatterBotCorpusTrainingTestCase, self).setUp()
        self.chatbot.storage.drop()

    def test_train_with_english_greeting_corpus(self):
        self.trainer.train('chatterbot.corpus.english.greetings')

        results = self.chatbot.storage.filter(text='Hello')

        self.assertGreater(len(results), 1)

    def test_train_with_english_greeting_corpus_tags(self):
        self.trainer.train('chatterbot.corpus.english.greetings')

        results = self.chatbot.storage.filter(text='Hello')

        self.assertGreater(len(results), 1)
        statement = results[0]
        self.assertEqual(['greetings'], statement.get_tags())

    def test_train_with_multiple_corpora(self):
        self.trainer.train(
            'chatterbot.corpus.english.greetings',
            'chatterbot.corpus.english.conversations',
        )
        results = self.chatbot.storage.filter(text='Hello')

        self.assertGreater(len(results), 1)

    def test_train_with_english_corpus(self):
        self.trainer.train('chatterbot.corpus.english')
        results = self.chatbot.storage.filter(text='Hello')

        self.assertGreater(len(results), 1)
